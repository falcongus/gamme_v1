"""
Just a game

Simple program to show basic sprite usage.

Artwork from

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_animation
"""
import arcade
import random
import os
import boty
from boty import Enemy

SPRITE_SCALING = 1
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move with a Sprite Animation Example"

COIN_SCALE = 1
COIN_COUNT = 1000
ENEMY_COUNT=2

VIEWPORT_MARGIN=40


MOVEMENT_SPEED = 10
LEVELx=1000
LEVELy=1000
class Coin(arcade.Sprite):
    def __init__(self):
        super().__init__("coin.png",COIN_SCALE)
class Mos(arcade.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__("sword.png")
        # Take the parameters of the init function above, and create instance variables out of them.
        self.center_x = position_x
        self.center_y = position_y





class heroy(arcade.Sprite):
    hero_textures=[]
    def __init__(self, texture_list):
        super().__init__("ichigoanim/ichigo_stand0.png")


        # Start at the first frame
        self.current_texture = 0
        self.textures = texture_list
        self.plbegintexture = 0
        self.plendtexture = 0
        self.k = self.center_x
        self.lpose = ""
        self.p = 0
        self.pl = 1
        self.hp = 100
        self.damage=10
        self.atak=False
        self.a=0

        self.damage=10
        self.b=random.randint(1,10)
        if self.b==9:
            self.damage=self.damage*2
        # Update to the next frame of the animation. If we are at the end
        # of our frames, then delete this sprite.
        self.b = 0
        self.flash = False
        self.move_x = 0
        self.move_y = 0
        self.ata_m = ""
        self.mana = 20
        self.shit = 1

    def update(self):
        if self.hp <= 0:
            self.kill()
        if self.lpose=="rs":
            self.plbegintexture=0
            self.plendtexture=3
        if self.lpose=="ls":
            self.plbegintexture=4
            self.plendtexture=7
        if self.lpose=="rw":
            self.plbegintexture=8
            self.plendtexture=15

        if self.lpose=="lw":
            self.plbegintexture=16
            self.plendtexture=23
        if self.lpose=="ra":
            self.plbegintexture=24
            self.plendtexture=30
            self.ata_m="right"
        if self.lpose=="la":
            self.plbegintexture=31
            self.plendtexture=37
            self.ata_m="left"
        if self.lpose=="lf":
            self.plbegintexture=38
            self.plendtexture=38
        if self.lpose=="rf":
            self.plbegintexture=39
            self.plendtexture=39

        self.p+=1
        if self.lpose=="rs" or self.lpose=="ls":
            if self.p>=3:
                self.current_texture += 1
                if self.current_texture < len(self.textures):
                    if self.current_texture>=self.plbegintexture and self.current_texture<=self.plendtexture:
                        self.set_texture(self.current_texture)

                    else:
                        self.current_texture=self.plbegintexture
                else:
                    self.current_texture=0
                if self.current_texture >= self.plendtexture:
                    self.current_texture = self.plbegintexture
                self.p=0
        if self.lpose=="rw" or self.lpose=="lw" and self.pl==0 :
            if self.center_x-self.k<=-20 or self.center_x-self.k>=20:
                self.current_texture += 1
                if self.current_texture < len(self.textures):
                    if self.current_texture >= self.plbegintexture and self.current_texture <= self.plendtexture:
                        self.set_texture(self.current_texture)

                    else:
                        self.current_texture = self.plbegintexture
                else:
                    self.current_texture = 0
                if self.current_texture >= self.plendtexture:

                    self.current_texture = self.plbegintexture

                self.k=self.center_x
        if (self.lpose=="lf" or self.lpose=="rf") and self.flash==True:
            if self.lpose=="lf":
                self.current_texture=39
            else:
                self.current_texture=38

            self.set_texture(self.current_texture)


        if (self.lpose=="la" or self.lpose=="ra") and self.atak==True:
            self.current_texture += 1
            self.a+=1
            if self.current_texture < len(self.textures):
                if self.current_texture >= self.plbegintexture and self.current_texture <= self.plendtexture:
                    self.set_texture(self.current_texture)

                else:
                    self.current_texture = self.plbegintexture
            else:
                self.current_texture = 0
            if self.current_texture>=self.plendtexture:
                self.current_texture=self.plbegintexture
                self.a=0
                self.atak = False


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = None
        self.coin_list = None
        self.enemy_list=None
        self.l=0
        # Set up the player
        self.money = 0
        self.player = None
        self.mos=None
        self.player_stand=None
        self.wall_list=None
        self.physics_engine=None
        self.physics_engine2=None
        self.engine_list1=[]
        self.view_bottom=0
        self.view_left=0
        self.atak=False
        self.e=0
        self.GRAVITY=-5
        self.last_move="right"
        self.movespeed=MOVEMENT_SPEED
        self.onground=False
        self.isjump=False
        self.xx=10
        self.yy=20
        self.player_texture_list=[]
        self.last_x=0
        self.last_y=0
        self.ataak=False
        self.set_mouse_visible(False)
        self.set_mouse_position(100,100)

        self.level=[
        "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-      -----------                                      --      -----------                                      --      -----------                                      --      -----------                                           -----------                                      --      -----------                                       -      -----------                                       -      -----------                                           -----------                                       -      -----------                                       -      -----------                                       -      -----------                                           -----------                                       -      -----------                                       -      -----------                                       -      -----------                                   -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                      -------          --                                      -------           --                                      -------           --                                      -------                                             -------          --                                      -------           --                                      -------           --                                      -------                                             -------           -                                      -------           --                                      -------           --                                      -------                                             -------           -                                      -------           --                                      -------           --                                      -------     -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                      --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                         -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                         -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------       -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-           --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                          -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-      -----------                                      --      -----------                                       --     -----------                                      --      -----------                                           -----------                                      --      -----------                                       -      -----------                                       -      -----------                                           -----------                                       -      -----------                                       -      -----------                                       -      -----------                                           -----------                                       -      -----------                                       -      -----------                                       -      -----------                                   -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                      -------           --                                     -------           --                                      -------           --                                      -------                                             -------          --                                      -------           --                                      -------           --                                      -------                                             -------           -                                      -------           --                                      -------           --                                      -------                                             -------           -                                      -------           --                                      -------           --                                      -------     -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                      --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                         -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                         -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------       -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-           --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                          -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-      -----------                                      --      -----------                                      --      -----------                                      --      -----------                                           -----------                                      --      -----------                                       -      -----------                                       -      -----------                                           -----------                                       -      -----------                                       -      -----------                                       -      -----------                                           -----------                                       -      -----------                                       -      -----------                                       -      -----------                                   -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                      -------           --                                     -------           --                                      -------           --                                      -------                                             -------          --                                      -------           --                                      -------           --                                      -------                                             -------           -                                      -------           --                                      -------           --                                      -------                                             -------           -                                      -------           --                                      -------           --                                      -------     -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                      --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                                                 --------                                                --------                                                --------                                                --------                         -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                 --                      -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------                                                  -------                                                 -------                                                 -------                                                 -------       -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-           --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                                       --                                                      --                                                      --                                                      --                                          -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -",
        "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    ]


    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.enemy_list=arcade.SpriteList()
        self.LEVELw=44800
        self.LEVELh=2750
        self.gameover=False
        # Set up the player
        self.money = 0
        self.flc=0
        self.plbegintexture=0
        self.plendtexture=0
        self.lpose="rs"

        character_scale = 0.85


        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand0.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand1.png",
                                                                    scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand2.png",
                                                                    scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand3.png",
                                                                    scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand0.png",
                                                                   scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand1.png",
                                                                   scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand2.png",
                                                                   scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand3.png",
                                                                   scale=character_scale, mirrored=True))


        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg0.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg1.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg2.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg3.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg4.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg5.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg6.png",
                                                                   scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg7.png",
                                                                   scale=character_scale))


        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg0.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg1.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg2.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg3.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg4.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg5.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg6.png",
                                                                  scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg7.png",
                                                                  scale=character_scale, mirrored=True))

        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak0.png",
                                                            scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak1.png",
                                                            scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak2.png",
                                                            scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak3.png",
                                                            scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak4.png",
                                                            scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak5.png",
                                                            scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak6.png",
                                                            scale=character_scale))

        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak0.png",
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak1.png",
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak2.png",
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak3.png",
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak4.png",
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak5.png",
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak6.png",
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_flash.png",scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_flash.png",scale=character_scale,mirrored=True))


        self.player=heroy(self.player_texture_list)
        self.player.center_x=100
        self.player.center_y=500
        self.mos=Mos(100,100)
        self.mos.angle=45

        # -- Set up several columns of walls
        x=0
        y=0
        for row in self.level:
            for col in row:
                if col == "-":
                # Randomly skip a box so the player can find a way through
                #if random.randrange(5) > 0:
                    wall = arcade.Sprite("LazyList/tanks_crateWood.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y

                    self.wall_list.append(wall)
                x+=50
            y+=50
            x=0

        for i in range(COIN_COUNT):
            coin = Coin()
            coin.center_x = random.randint(100,44500)
            coin.center_y = random.randint(100,2750)




            self.coin_list.append(coin)
        self.engine_list=[]
        for i in range(ENEMY_COUNT):
            enemy=Enemy(1)

            enemy.center_x=random.randint(500,4000)
            enemy.center_y=random.randint(100,2500)
            enemy.boundary_right = enemy.center_x + 600 * 1
            enemy.boundary_left = enemy.center_x - 600 * 1

            enemy.change_x=5

            self.physics_engine1=arcade.PhysicsEnginePlatformer(enemy,self.wall_list,gravity_constant=-self.GRAVITY)

            self.enemy_list.append(enemy)
            self.engine_list.append(self.physics_engine1)

        self.physics_engine=arcade.PhysicsEnginePlatformer(self.player,self.wall_list,gravity_constant=-self.GRAVITY)

        #self.physics_engine=arcade.PhysicsEnginePlatformer(enemy,self.wall_list,gravity_constant=-self.GRAVITY)
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)


        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.coin_list.draw()
        self.wall_list.draw()

        self.enemy_list.draw()

        self.player.draw()
        self.mos.draw()

        # Put the text on the screen.
        output = f"Gold: {self.money}"
        arcade.draw_text(output, self.xx,self.yy, arcade.color.WHITE, 14)
        output1=f"HP: {self.player.hp}"
        arcade.draw_text(output1,self.player.center_x-40,self.player.center_y+30,arcade.color.RED_ORANGE,15)
        for enemy in self.enemy_list:
            enemy.output=f"hp: {enemy.hp}"

            arcade.draw_text(enemy.output, enemy.center_x-20, enemy.center_y + 30, arcade.color.RED_ORANGE, 10)


    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.mos.center_x = self.view_left+x
        self.mos.center_y = self.view_bottom+y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.player.lpose=="rf":
                self.player.lpose ="rs"
            if self.player.lpose=="lf":
                self.player.lpose="ls"
            self.player.flash=True


        if button==arcade.MOUSE_BUTTON_LEFT:
            if self.player.center_x>self.mos.center_x:
                self.player.lpose="la"
                self.player.ata_m="left"
            if self.player.center_x<self.mos.center_x:
                self.player.lpose="ra"
                self.player.ata_m="right"

            self.player.atak=True
        if button == arcade.MOUSE_BUTTON_RIGHT:
            if self.player.center_x<self.mos.center_x:
                self.player.lpose ="rf"
            if self.player.center_x>self.mos.center_x:
                self.player.lpose="lf"
            self.player.move_x=self.mos.center_x
            self.player.move_y=self.mos.center_y
            self.flc=1
            self.player.flash=True





    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT and self.player.atak==False and self.player.ata_m=="right":
            self.player.lpose="rs"
        if button==arcade.MOUSE_BUTTON_LEFT and self.player.atak==False and self.player.ata_m=="left":
            self.player.lpose="ls"




    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
       # if key == arcade.key.UP:
        #   self.player.change_y = self.movespeed
        #elif key == arcade.key.DOWN:
        #    self.player.change_y = -self.movespeed
        if key == arcade.key.A:
            self.player.change_x = -self.movespeed
            self.last_move = "left"
            self.player.lpose = "lw"
            self.player.pl = 0
        elif key == arcade.key.D and self.player.center_x<=self.LEVELw-100:
            self.player.change_x = self.movespeed
            self.last_move = "right"
            self.player.lpose = "rw"
            self.player.pl = 0
        elif key == arcade.key.P:
            self.atak = True
        elif key == arcade.key.LSHIFT and self.player.center_x < self.LEVELw - 1000 and self.player.center_y < self.LEVELh - 250 and self.player.center_y > 50 and self.player.center_x > 500:
            self.movespeed = 50
        elif key == arcade.key.SPACE:
           # if self.onground == True:
            #    self.isjump = True
             #   self.jumpcount = 70
            if self.physics_engine.can_jump():
                self.player.change_y = 80

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player.change_x = 0
        elif key==arcade.key.P:
            self.atak=False
        elif key==arcade.key.LSHIFT or not(self.player.center_x<self.LEVELw-1000 and self.player.center_y<self.LEVELh-250 and self.player.center_y>250 and self.player.center_x>500 ):
            self.movespeed=25

    def update(self, delta_time):
        """ Movement and game logic """

        if not(self.gameover):
            self.l+=1
            if self.flc>=1:
                self.flc+=1
                if self.flc==3:
                    self.player.center_x = self.player.move_x
                    self.player.center_y = self.player.move_y
                    if self.player.flash:
                        if self.player.lpose == "rf":
                            self.player.lpose = "rs"
                        if self.player.lpose == "lf":
                            self.player.lpose = "ls"
                        self.player.flash = False
                        self.flc=0
            self.e=len(self.enemy_list)
            if self.e<ENEMY_COUNT:
                for self.e in range(ENEMY_COUNT):
                    enemy = Enemy(1)

                    enemy.center_x = random.randint(500, 4000)
                    enemy.center_y = random.randint(100, 2500)
                    enemy.boundary_right = enemy.center_x + 600 * 1
                    enemy.boundary_left = enemy.center_x - 600 * 1

                    enemy.change_x = 5

                    self.physics_engine1 = arcade.PhysicsEnginePlatformer(enemy, self.wall_list,
                                                                          gravity_constant=-self.GRAVITY)

                    self.enemy_list.append(enemy)
                    self.engine_list.append(self.physics_engine1)

            changed=False
            self.onground=False
            hp=self.player.hp
            if self.player.center_x+100>self.LEVELw-100:
                self.movespeed=10
                self.player.center_x=self.LEVELw-200
            self.last_x = self.player.center_x
            self.last_y = self.player.center_y

            self.physics_engine.update()
            for i in self.engine_list:
                i.update()


            self.coin_list.update()
            self.coin_list.update_animation()

            for enemy in self.enemy_list:
                enemy.update(hp)
                enemy.atak=False
                enemy.getdamage=False
            # If the enemy hit a wall, reverse
                if len(arcade.check_for_collision_with_list(enemy, self.wall_list)) > 0:
                    enemy.change_x *= -1
                    if enemy.lpose=="rw":
                        enemy.lpose="lw"
                    if enemy.lpose=="lw":
                        enemy.lpose="rw"
            # If the enemy hit the left boundary, reverse
                elif enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
                    enemy.change_x *= -1
                    enemy.lpose="rw"
            # If the enemy hit the right boundary, reverse
                elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
                    enemy.change_x *= -1
                    enemy.lpose="lw"
                elif arcade.check_for_collision(self.player,enemy):
                    enemy.atak = True
                    enemy.change_x =0
                    self.player.hp-=enemy.attak//self.player.shit
                    if self.player.hp<=0:
                        self.gameover=True
                    if self.player.atak==True and self.player.lpose=="la" and enemy.center_x<self.player.center_x:
                        enemy.atak==False
                        enemy.getdamage=True
                        if self.player.a>=5:
                            enemy.hp-=self.player.damage
                            self.player.a=0
                        if enemy.hp<=0:
                            self.money+=10
                            enemy.kill()
                    if self.player.atak == True and self.player.lpose == "ra" and enemy.center_x > self.player.center_x:
                        enemy.atak == False
                        enemy.getdamage = True
                        if self.player.a>=5:
                            enemy.hp-=self.player.damage
                            self.player.a=0
                        if enemy.hp <= 0:
                            self.money += 10
                            enemy.kill()


                elif enemy.atak==False and enemy.change_x==0:
                    enemy.change_x=enemy.l_x

            if self.player.center_x == self.last_x and self.player.center_y == self.last_y and self.l >= 10:
                if self.last_move == "left":
                    self.player.lpose = "ls"
                else:
                    self.player.lpose = "rs"
                self.l = 0

            self.player.update()
        # Generate a list of all sprites that collided with the player.
            hit_list = arcade.check_for_collision_with_list(self.player , self.coin_list)
            hit_list1=arcade.check_for_collision_with_list(self.player,self.wall_list)
        #wall collision

     #   for wall in self.wall_list:
    #        if (self.player.center_x+10+100>wall.center_x and self.player.center_x+10+100<wall.center_x+50) and ((self.player.center_y+70>wall.center_y and self.player.center_y+70<wall.center_y+50) or (self.player.center_y>wall.center_y and self.player.center_y<wall.center_y+50)):
   #             self.player.set_position(wall.center_x-100,self.player.center_y)
  #          if (self.player.center_x-20>wall.center_x and self.player.center_x-20<wall.center_x+50) and ((self.player.center_y+70>wall.center_y and self.player.center_y+70<wall.center_y+50) or (self.player.center_y>wall.center_y and self.player.center_y<wall.center_y+50)):
 #               self.player.set_position(wall.center_x + 70, self.player.center_y)
#
     #       if ((self.player.center_x+100>wall.center_x and self.player.center_x+100<wall.center_x+50) or (self.player.center_x>wall.center_x and self.player.center_x<wall.center_x+50)) and  (self.player.center_y-20>wall.center_y and self.player.center_y-20<wall.center_y+50):
    #            self.player.set_position(self.player.center_x,wall.center_y+70)
   #             self.onground= True
  #          if ((self.player.center_x+100>wall.center_x and self.player.center_x+100<wall.center_x+50) or (self.player.center_x>wall.center_x and self.player.center_x<wall.center_x+50)) and  (self.player.center_y+10+70>wall.center_y and self.player.center_y+10+70<wall.center_y+50):
 #               self.player.set_position(self.player.center_x,wall.center_y-80)
#                self.onground=True
            #wall c


        #self.player.center_y+=self.GRAVITY
        #if self.isjump:
        #    if self.jumpcount>=-70:
       #         if self.jumpcount<0:
      #              self.player.center_y-=(self.jumpcount**2)/2
     #           else:
    #                self.player.center_y+=(self.jumpcount**2)/2
   #             self.jumpcount-=1
  #          else:
 #               self.isjump=False
#                self.jumpcount=70
            #wall collision

            #for wall in self.wall_list:
           #     if (self.player.center_x + 10 + 100 > wall.center_x and self.player.center_x + 10 + 100 < wall.center_x + 50) and ((self.player.center_y + 70 > wall.center_y and self.player.center_y + 70 < wall.center_y + 50) or (self.player.center_y > wall.center_y and self.player.center_y < wall.center_y + 50)):
          #          self.player.set_position(wall.center_x - 100, self.player.center_y)
         #       if (self.player.center_x - 20 > wall.center_x and self.player.center_x - 20 < wall.center_x + 50) and ((self.player.center_y + 70 > wall.center_y and self.player.center_y + 70 < wall.center_y + 50) or (self.player.center_y > wall.center_y and self.player.center_y < wall.center_y + 50)):
        #            self.player.set_position(wall.center_x + 70, self.player.center_y)
       #         if ((self.player.center_x + 100 > wall.center_x and self.player.center_x + 100 < wall.center_x + 50) or (self.player.center_x > wall.center_x and self.player.center_x < wall.center_x + 50)) and (self.player.center_y - 20 > wall.center_y and self.player.center_y - 20 < wall.center_y + 50):
      #              self.player.set_position(self.player.center_x, wall.center_y + 70)
     #               self.onground = True
    #                self.isjump=False
   #             if ((self.player.center_x + 100 > wall.center_x and self.player.center_x + 100 < wall.center_x + 50) or (self.player.center_x > wall.center_x and self.player.center_x < wall.center_x + 50)) and (self.player.center_y + 10 + 70 > wall.center_y and self.player.center_y + 10 + 70 < wall.center_y + 50):
  #                  self.player.set_position(self.player.center_x, wall.center_y - 80)
 #                   self.onground = True
#                    self.jumpcount=0
                    #self.isjump=False

                #wall colision


        # Loop through each colliding sprite, remove it, and add to the score.
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.money += 1

       # if self.atak==True:
        #    if self.last_move=="left":
         #       self.player_list.update_texture(self.player_stand.textures[2])

        # Scroll left
            left_bndry = self.view_left + VIEWPORT_MARGIN
            if self.player.left < left_bndry:
                self.view_left -= left_bndry - self.player.left
                self.mos.center_x-=left_bndry-self.player.left
                self.xx=self.view_left
                changed = True

        # Scroll right
            right_bndry = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
            if self.player.right > right_bndry:
                self.view_left += self.player.right - right_bndry
                self.mos.center_x+=self.player.right-right_bndry
                self.xx=self.view_left
                changed = True

        # Scroll up
            top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
            if self.player.top > top_bndry:
                self.view_bottom += self.player.top - top_bndry
                self.mos.center_y+=self.player.top-top_bndry
                self.yy=self.view_bottom
                changed = True

        # Scroll down
            bottom_bndry = self.view_bottom + VIEWPORT_MARGIN
            if self.player.bottom < bottom_bndry:
                self.view_bottom -= bottom_bndry - self.player.bottom
                self.mos.center_y-=bottom_bndry-self.player.bottom

                self.yy=self.view_bottom
                changed = True

            if changed:


                arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()