"""
Just a game

Die or Battle
"""
import arcade
import random
import os
from multiprocessing import Process
import threading
import time
import sys
import boty
from boty import Enemy
from knopka import Knopka

SPRITE_SCALING = 1
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Die or Battle"

COIN_SCALE = 1
COIN_COUNT = 100
ENEMY_COUNT=20

VIEWPORT_MARGIN=40


MOVEMENT_SPEED = 10
LEVELx=1000
LEVELy=1000
BOUNX=100
class volna(arcade.Sprite):
    def __init__(self,napr,bankai):
        if not(bankai):
            if napr=="left":
                super().__init__("ichigoanim/ichigo_aatak_volna1.png")
            else:
                super().__init__("ichigoanim/ichigo_aatak_volna.png")
        if bankai:
            if napr=="left":
                super().__init__("ichigoanim/ichigo_b_volna1.png")
            else:
                super().__init__("ichigoanim/ichigo_b_volna.png")
        self.j=0
        self.napr=napr
        self.move=0

    def update(self):
        if self.j==0:
            if self.napr=="left":
                self.lb=self.center_x-600
                self.move=-20
            else:
                self.lb=self.center_x+600
                self.move=20
            self.j=1
        self.center_x+=self.move
class Menu(arcade.Sprite):
    def __init__(self):
        super().__init__("ichigoanim/MENU.png")
class Map(arcade.Sprite):
    def __init__(self,sc,lvl,text_lists):
        super().__init__("other/karta{}.png".format(lvl),scale=sc)
        self.textures=text_lists
    def new_lvl(self,lvl):
        self.set_texture(lvl)

class Coin(arcade.Sprite):
    def __init__(self):
        super().__init__("coin.png",COIN_SCALE)
class Mos(arcade.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__("sword.png")
        # Take the parameters of the init function above, and create instance variables out of them.
        self.center_x = position_x
        self.center_y = position_y




class Orihime(arcade.Sprite):
    def __init__(self,textures):
        super().__init__("other/orihime.png")
        self.textures=textures
        self.i=0
    def update(self):
        self.set_texture(self.i)
        self.i+=1
        if self.i>=2:
            self.i=0
class Bankai(arcade.Sprite):
    def __init__(self,texture_list):
        super().__init__("ichigoanim/ichigo_stand0.png")
        self.textures=texture_list
        self.plbegintexture=1
        self.plendtexture=108
    def update(self,bankaipl):

        self.current_texture+=1
        if self.current_texture<len(self.textures):
            if self.current_texture>=self.plbegintexture and self.current_texture<=self.plendtexture:
                self.set_texture(self.current_texture)
                if self.current_texture==self.plendtexture-1:
                    bankaipl = True



            else:
                self.current_texture=self.plbegintexture



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
        self.xp=0
        self.bankai=False
        self.damage=10
        self.ddamage=10
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
        self.max_mana=100
        self.mana = 100
        self.shit = 1
        self.ar=False
        self.ojk=False
        self.new_lvl=100
        self.max_hp=100
        self.sec=0
        self.lp=0
        self.t=False
        self.lvl=0
        self.op=0

    def update(self):
        if self.lp==0 and self.bankai:
            self.damage*=10
            self.lp=1
        if self.lp==1 and not(self.bankai):
            self.damage//=10
            self.lp=0
        self.sec+=1
        if self.hp>0 and self.hp<self.max_hp and self.sec>20:
            self.hp+=self.lvl//2
            if self.mana>=0 and self.mana<self.max_mana:
                self.mana+=self.lvl//2
            self.sec=0
        if self.xp>=self.new_lvl:
            self.lvl+=1
            self.max_hp+=self.max_hp//4
            self.max_mana+=self.max_mana//8
            self.damage+=self.damage//4

            self.new_lvl*=2
            self.hp=self.max_hp
            self.mana=self.max_mana
        if self.hp <= 0:
            self.kill()
        if self.lpose=="rs":
            if not self.bankai:
                self.plbegintexture=0
                self.plendtexture=3
            else:
                self.plbegintexture=45
                self.plendtexture=48

        if self.lpose=="bankaibegin":
            self.plbegintexture=91
            self.plendtexture=199
        if self.lpose=="bankaibegin1":
            self.plbegintexture=200
            self.plendtexture=308
        if self.lpose=="ls":
            if not self.bankai:
                self.plbegintexture=4
                self.plendtexture=7
            else:
                self.plbegintexture=49
                self.plendtexture=52
        if self.lpose=="rw":
            if not self.bankai:
                self.plbegintexture=8
                self.plendtexture=15
            else:
                self.plbegintexture=53
                self.plendtexture=60

        if self.lpose=="lw":
            if not self.bankai:
                self.plbegintexture=16
                self.plendtexture=23
            else:
                self.plbegintexture=61
                self.plendtexture=68
        if self.lpose=="ra":
            if not self.bankai:
                self.plbegintexture=24
                self.plendtexture=30
                self.ata_m="right"
            else:
                self.plbegintexture=69
                self.plendtexture=74
                self.ata_m="right"
        if self.lpose=="la":
            if not self.bankai:
                self.plbegintexture=31
                self.plendtexture=37
                self.ata_m="left"
            else:
                self.plbegintexture=75
                self.plendtexture=80
                self.ata_m="left"
        if self.lpose=="lf":
            if not self.bankai:
                self.plbegintexture=38
                self.plendtexture=38
            else:
                self.plbegintexture=81
                self.plendtexture=81
        if self.lpose=="rf":
            if not self.bankai:
                self.plbegintexture=39
                self.plendtexture=39
            else:
                self.plbegintexture=82
                self.plendtexture=82
        if self.lpose=="raa":
            if not self.bankai:
                self.plbegintexture=40
                self.plendtexture=43
            else:
                self.plbegintexture=83
                self.plendtexture=86
        if self.lpose=="laa":
            if not self.bankai:
                self.plbegintexture=44
                self.plendtexture=47
            else:
                self.plbegintexture=87
                self.plendtexture=89

        self.p+=1
        if self.lpose=="bankaibegin" or self.lpose=="bankaibegin1":
            self.current_texture += 1
            if self.current_texture < len(self.textures):
                if self.current_texture >= self.plbegintexture and self.current_texture <= self.plendtexture:
                    self.set_texture(self.current_texture)

                    if self.current_texture==self.plendtexture-3:
                        self.bankai=True
                        self.timebegin=time.time()
                        self.lpose="rs"
                else:
                    self.current_texture = self.plbegintexture
            else:
                self.current_texture = 0
            if self.current_texture >= self.plendtexture:
                self.current_texture = self.plbegintexture



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
                if not self.bankai:
                    self.current_texture=39

                else:
                    self.current_texture=84
            else:
                if not self.bankai:
                    self.current_texture=38
                else:
                    self.current_texture=85

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
        if (self.lpose=="laa" or self.lpose=="raa") :
            self.current_texture += 1
            self.a+=1
            if self.current_texture < len(self.textures):
                if self.current_texture >= self.plbegintexture and self.current_texture <= self.plendtexture:
                    self.set_texture(self.current_texture)

                else:
                    self.ojk=True
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
        self.lvl=1
        self.level = [
            "------------------------------------------------------------------------------------",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                      -----             --                        -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-      -----------                                      --      -----------        -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                      -------           --                        -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-        ---------                                      --        ---------        -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                        -----           --                        -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                      --------                                                    -",
            "-                                                                                  -",
            "-                 --                      -------                                  -",
            "-                                                                             ------",
            "-           --                                                      --             -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-                                                                                  -",
            "-----------------------------------------------------------------------------      -",
            "-----------------------------------------------------------------------------      -",
            "-----------------------------------------------------------------------------      -",
            "-----------------------------------------------------------------------------      -",

        ]
    def setup(self):
        self.ichigo_nothit=arcade.load_sound("ichigonothit.wav")
        self.ichigo_hit=arcade.load_sound("ichigohit.wav")
        self.ichigo_flash=arcade.load_sound("flash.wav")
        self.ichio_hit_coin=arcade.load_sound("moneyget.wav")
        self.ichigo_bankai=arcade.load_sound("bankai.wav")
        self.lvl5=arcade.load_sound("lvl5.wav")
        self.ichigo_died=arcade.load_sound("died.wav")
        self.ofg=[]
        self.ofg.append(0)
        self.ofg.append(0)
        self.ofg.append(0)
        self.ofg.append(0)
        self.ofg.append(0)
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.enemy_list=arcade.SpriteList()
        self.LEVELw=0
        self.LEVELh=0
        self.volna_c=0
        self.d=0
        for i in range(len(self.level[0])):
            self.LEVELw+=50
        for i in range(len(self.level)):
            self.LEVELh+=50

        sc=1
        self.text_lis=[]
        self.lplplj=1

        self.text_lis.append(arcade.load_texture("other/karta1.png"))
        self.text_lis.append(arcade.load_texture("other/karta2.png"))
        self.text_lis.append(arcade.load_texture("other/karta3.png"))
        self.text_lis.append(arcade.load_texture("other/karta4.png"))
        self.text_lis.append(arcade.load_texture("other/karta5.png"))

        self.orihime_textures=[]
        self.orihime_textures.append(arcade.load_texture("other/orihime.png",scale=0.85))
        self.orihime_textures.append(arcade.load_texture("other/orihime1.png",scale=0.85))
        self.orihime_textures.append(arcade.load_texture("other/orihime2.png",scale=0.85))

        self.map=Map(sc,self.lvl,self.text_lis)
        self.map.center_y+=1000
        self.map.center_x+=2100
        self.op=0

        self.knopka_list=[]
        self.olp=0
        self.gameover=False
        # Set up the player
        self.money = 0
        self.flc=0
        self.plbegintexture=0
        self.plendtexture=0
        self.lpose="rs"
        self.ex=0
        self.ey=0
        self.ww=0
        self.jj1=0


        character_scale = 0.85

        for i in range(4):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand{}.png".format(i),
                                                                   scale=character_scale))
        for i in range(4):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_stand{}.png".format(i),
                                                                   scale=character_scale, mirrored=True))


        for i in range(8):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg{}.png".format(i),
                                                                   scale=character_scale))

        for i in range(8):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_beg{}.png".format(i),
                                                                  scale=character_scale, mirrored=True))

        for i in range(7):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak{}.png".format(i),
                                                            scale=character_scale))

        for i in range(7):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_atak{}.png".format(i),
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(   arcade.load_texture("ichigoanim/ichigo_flash.png",scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_flash.png",scale=character_scale,mirrored=True))
        for i in range(3):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_aatak{}.png".format(i),scale=character_scale))

        for i in range(3):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_aatak{}.png".format(i), scale=character_scale,mirrored=True))


#BANKAI
        for i in range(4):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_b_s{}.png".format(i),
                                                                   scale=character_scale))
        for i in range(4):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_b_s{}.png".format(i),
                                                                   scale=character_scale, mirrored=True))


        for i in range(8):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_b_a{}.png".format(i),
                                                                   scale=character_scale))

        for i in range(8):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_b_a{}.png".format(i),
                                                                  scale=character_scale, mirrored=True))

        for i in range(6):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_b_atak{}.png".format(i),
                                                            scale=character_scale))

        for i in range(6):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_b_atak{}.png".format(i),
                                                            scale=character_scale, mirrored=True))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_b_flash.png",scale=character_scale))
        self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_b_flash.png",scale=character_scale,mirrored=True))
        for i in range(3):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_b_aa{}.png".format(i),scale=character_scale))

        for i in range(3):
            self.player_texture_list.append(arcade.load_texture("ichigoanim/ichigo_b_aa{}.png".format(i), scale=character_scale,mirrored=True))
        i = 0
        for j in range(108):
            if j == 15 - 1 or j == 42 - 1 or j == 61 - 1 or j == 83 - 1 or j == 101 - 1:
                i += 1
            self.player_texture_list.append(arcade.load_texture("ichigoanim/20190725_15403{}_{}.png".format(i, j + 1),scale=character_scale))
        i=0
        for j in range(108):
            if j == 15 - 1 or j == 42 - 1 or j == 61 - 1 or j == 83 - 1 or j == 101 - 1:
                i += 1
            self.player_texture_list.append(arcade.load_texture("ichigoanim/20190725_15403{}_{}.png".format(i, j + 1),scale=character_scale,mirrored=True))



#shou
        # self.iok = 0
        # for j in range(108):
        #     if j == 15 - 1 or j == 42 - 1 or j == 61 - 1 or j == 83 - 1 or j == 101 - 1:
        #         self.iok += 1
        #     print("3{}---{}".format(self.iok, j + 1))
#shou
#BANKAI
        self.player=heroy(self.player_texture_list)
        self.player.center_x=50000
        self.player.center_y=500
        self.mos=Mos(100,100)
        self.mos.angle=45
        self.poi=0
        self.poi1=0
        self.win=False

        # -- Set up several columns of walls
        x=0
        y=0
        for row in self.level:
            for col in row:
                if col == "-":

                    wall = arcade.Sprite("block.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y

                    self.wall_list.append(wall)
                x+=50
            y+=50
            x=0
        for i in range(COIN_COUNT):
            self.coin_placed_successfully = False
            coin = Coin()
            while not self.coin_placed_successfully:
                coin.center_x = random.randint(100,4100)
                coin.center_y = random.randint(100,2000)
                self.wall_hit_list=arcade.check_for_collision_with_list(coin,self.wall_list)
                self.coin_hit_list=arcade.check_for_collision_with_list(coin,self.coin_list)
                if len(self.wall_hit_list)==0 and len(self.coin_hit_list)==0:
                    self.coin_placed_successfully=True


            self.coin_list.append(coin)
        self.engine_list=[]
        self.threadenemy_list=[]


        for i in range(ENEMY_COUNT):
            enemy=Enemy(1,self.lvl*2)
            self.enemy_placed_successfully=False
            while not self.enemy_placed_successfully:
                enemy.center_x=random.randint(BOUNX,self.LEVELw)
                enemy.center_y=random.randint(100,self.LEVELh)
                enemy.boundary_right = enemy.center_x + BOUNX * 1
                enemy.boundary_left = enemy.center_x - BOUNX * 1
                enemy.change_x=5
                self.wall_hit_list=arcade.check_for_collision_with_list(enemy,self.wall_list)
                if len(self.wall_hit_list)==0:
                    self.enemy_placed_successfully=True
            self.physics_engine1=arcade.PhysicsEnginePlatformer(enemy,self.wall_list,gravity_constant=-self.GRAVITY)

            self.enemy_list.append(enemy)
            self.engine_list.append(self.physics_engine1)

            #t=threading.Thread(target = enemy_update,name="thread{}".format(i),args=(enemy))
            #self.threadenemy_list.append(t)
            #t.start()

        self.physics_engine=arcade.PhysicsEnginePlatformer(self.player,self.wall_list,gravity_constant=-self.GRAVITY)
        if self.d==1 and self.lvl==5:
            self.physics_engineo=arcade.PhysicsEnginePlatformer(self.orihime,self.wall_list,gravity_constant=-self.GRAVITY)
        #self.physics_engine=arcade.PhysicsEnginePlatformer(enemy,self.wall_list,gravity_constant=-self.GRAVITY)
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)


        self.view_left = 0
        self.view_bottom = 0
        self.kp=[]
        self.col=[]
        self.x=[]
        self.y=[]
        self.kp.append("")
        self.col.append(arcade.color.BLACK)
        self.size1 = 35
        self.kp.append("MENU")
        self.size2 = 25
        self.kp.append("OPTIONS")

        self.kp.append("EXIT")
        self.kp.append("Screen size 1350 * 600")

        self.kp.append("Screen size 1000 * 445")

        self.size3=25
        self.col.append(arcade.color.BLACK)
        self.col.append(arcade.color.BLACK)
        self.col.append(arcade.color.BLACK)
        self.col.append(arcade.color.BLACK)
        self.col.append(arcade.color.BLACK)


    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()
        if self.player.center_y>2100 and self.lvl<5 and self.player.lvl>self.lvl*5:
            self.lvl+=1
            self.map.new_lvl(self.lvl-1)
            self.player.center_y=100
        self.map.draw()
        # Draw all the sprites.

        for wall in self.coin_list:
            if wall.center_x > self.view_left-100 and wall.center_x < SCREEN_WIDTH + self.view_left+100 and wall.center_y > self.view_bottom-100 and wall.center_y < self.view_bottom + SCREEN_HEIGHT+100:
                wall.draw()
        for wall in self.wall_list:
            if wall.center_x > self.view_left-100 and wall.center_x < SCREEN_WIDTH + self.view_left+100 and wall.center_y > self.view_bottom-100 and wall.center_y < self.view_bottom + SCREEN_HEIGHT+100:
                wall.draw()


        #self.wall_list.draw()

        for wall in self.enemy_list:
            if wall.center_x > self.view_left and wall.center_x < SCREEN_WIDTH + self.view_left and wall.center_y > self.view_bottom and wall.center_y < self.view_bottom + SCREEN_HEIGHT:
                wall.draw()

        #self.enemy_list.draw()

        self.player.draw()
        self.mos.draw()

        self.napr="p"
        if self.player.ojk==True:
            if self.volna_c==0:
                if self.player.lpose=="ls" or self.player.lpose=="lw" or self.player.lpose=="laa" or self.player.lpose=="lf":
                    self.napr = "left"
                self.volna=volna(self.napr,self.player.bankai)
                if self.napr=="left":
                    self.volna.center_x=self.player.center_x-100
                else:
                    self.volna.center_x=self.player.center_x+100
                self.volna.center_y=self.player.center_y+20
            self.volna_c=1
            self.volna.draw()
        self.inn=False
        self.in_options=False
        if self.lvl==5:
            if self.d==0:
                self.orihime=Orihime(self.orihime_textures)
                self.orihime.center_x=4020
                self.orihime.center_y=1900
                self.orihime_engine=arcade.PhysicsEnginePlatformer(self.orihime,self.wall_list,gravity_constant=0.5)
                self.d=1
            self.orihime.draw()

        # Put the text on the screen.
        output = f"Gold: {self.money}"
        arcade.draw_text(output, self.xx,self.yy, arcade.color.WHITE, 14)
        output1=f"Hp: {self.player.hp}/{self.player.max_hp}"
        output2=f"Xp: {self.player.xp}"
        output4=f"/{self.player.new_lvl}"
        output5=f"Mana: {self.player.mana}/{self.player.max_mana}"
        output6=f"Lvl: {self.player.lvl}"
        output7=f"Streng:{self.player.damage}"
        if self.player.lvl>self.lvl*5:
            output3="Next Level"
        else:
            output3="You so weak!"

        arcade.draw_text(output1,self.xx+20,self.yy+SCREEN_HEIGHT-20,arcade.color.RED_DEVIL,20)
        arcade.draw_text(output2+output4,self.xx+20,self.yy+SCREEN_HEIGHT-40,arcade.color.DARK_BLUE_GRAY,15)
        arcade.draw_text(output3,3950,2080,arcade.color.GREEN,25)

        arcade.draw_text(output5,self.xx+20,self.yy+SCREEN_HEIGHT-60,arcade.color.BLUE,20)
        arcade.draw_text(output6,self.xx+20,self.yy+SCREEN_HEIGHT-80,arcade.color.DARK_BLUE_GRAY,15)
        arcade.draw_text(output7,self.xx+20,self.yy+SCREEN_HEIGHT-100,arcade.color.ALLOY_ORANGE,15)
        if self.gameover:
            menu=Menu()

            arcade.draw_rectangle_filled(self.xx+700, self.yy+300, 310, 410,
                                         color=arcade.color.BLACK)
            arcade.draw_rectangle_filled(self.xx+700,self.yy+300,300,400,color=arcade.color.WHITE)
            menu.center_x=self.xx+700
            menu.center_y=self.yy+300

            menu.draw()

            if self.inn==False:
                self.y.append(0)
                self.y.append(self.yy + 460)
                self.y.append(self.yy + 400)
                self.y.append(self.yy + 100)
                self.x.append(0)
                self.x.append(self.xx + 650)
                self.x.append(self.xx + 650)
                self.x.append(self.xx + 670)
            self.x[1]=self.xx+650
            self.x[2]=self.xx+640
            self.x[3]=self.xx+670
            self.y[1]=self.yy+460
            self.y[2]=self.yy+400
            self.y[3]=self.yy+100
            arcade.draw_text(self.kp[1], self.x[1], self.y[1], self.col[1], self.size1)
            arcade.draw_text(self.kp[2],self.x[2],self.y[2], self.col[2], self.size2)
            arcade.draw_text("(doesn't work!)",self.x[2]-30,self.y[2]-20,self.col[2],18)
            arcade.draw_text(self.kp[3],self.x[3], self.y[3],self.col[3],  self.size3)
            # if self.inn==True and self.in_options==True:
            #     arcade.draw_text(self.kp[2], self.xx + 650, self.yy + 460, self.col[2], self.size1)
            #     arcade.draw_text(self.kp[4],self.xx + 650, self.yy + 400, self.col[4], self.size2)
            #     arcade.draw_text(self.kp[5],self.xx + 650, self.yy + 360, self.col[5], self.size2)


            #arcade.draw_text("menu", self.xx + 650, self.yy + 450, arcade.color.PURPLE, 30)
            self.mos.draw()
        for enemy in self.enemy_list:
            enemy.output=f"hp: {enemy.hp}"

            arcade.draw_text(enemy.output, enemy.center_x-20, enemy.center_y + 30, arcade.color.RED_ORANGE, 10)
        if self.win==True:
            arcade.draw_text("YOU WIN!!!!",self.xx,self.yy,arcade.color.GREEN,100)
            if self.ww==0:
                arcade.play_sound(sound=arcade.load_sound("win.wav"))
                self.ww=1
            self.gameover=True
        if self.gameover==True and self.player.hp<=0:
            arcade.draw_text("YOU DIED!!!!",self.xx+450,self.yy+SCREEN_HEIGHT-70,arcade.color.RED_DEVIL,60)




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
            if self.player.ar==False:
                if self.player.center_x>self.mos.center_x:
                    self.player.lpose="la"
                    self.player.ata_m="left"
                if self.player.center_x<self.mos.center_x:
                    self.player.lpose="ra"
                    self.player.ata_m="right"

                self.player.atak=True
            if self.player.ar==True and self.player.mana>100 and self.player.lvl>=5:
                if self.player.center_x>self.mos.center_x:
                    self.player.lpose="laa"
                if self.player.center_x<self.mos.center_x:
                    self.player.lpose="raa"
                self.player.mana-=100
        if button == arcade.MOUSE_BUTTON_RIGHT and self.player.mana>50 and self.player.lvl>=2:
            if self.player.center_x<self.mos.center_x:
                self.player.lpose ="rf"
            if self.player.center_x>self.mos.center_x:
                self.player.lpose="lf"
            self.player.move_x=self.mos.center_x
            self.player.move_y=self.mos.center_y
            self.flc=1
            if self.player.bankai:
                self.player.mana-=10
            else:
                self.player.mana-=50
            self.player.flash=True
            arcade.play_sound(self.ichigo_flash)





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

        if key == arcade.key.A and self.player.hp>0:
            self.player.change_x = -self.movespeed
            self.last_move = "left"
            self.player.lpose = "lw"
            self.player.pl = 0
        elif key == arcade.key.ESCAPE:
            if self.gameover==True:
                self.gameover=False
            if self.gameover==False:
                self.gameover=True
        elif key == arcade.key.LCTRL:
            self.player.ar=True
        elif key == arcade.key.DOWN and self.gameover==True:
            self.olp+=1

            if self.olp==1:
                self.col[1]=arcade.color.GREEN
                for i in range(len(self.col)):
                    if  not(i==self.olp):
                        self.col[i]=arcade.color.BLACK

            if self.olp==2:
                self.col[2]=arcade.color.GREEN
                for i in range(len(self.col)):
                    if  not(i==self.olp):
                        self.col[i]=arcade.color.BLACK
            if self.olp==3:
                self.col[3]=arcade.color.GREEN
                for i in range(len(self.col)):
                    if  not(i==self.olp):
                        self.col[i]=arcade.color.BLACK



            if self.olp>3 :
                self.olp=0

        elif key == arcade.key.UP and self.gameover==True:
            self.olp -= 1
            if self.olp == 1:
                self.col[1]=arcade.color.GREEN
                for i in range(len(self.col)):
                    if  not(i==self.olp):
                        self.col[i]=arcade.color.BLACK


            if self.olp == 2:
                self.col[2]=arcade.color.GREEN
                for i in range(len(self.col)):
                    if  not(i==self.olp):
                        self.col[i]=arcade.color.BLACK
            if self.olp == 3:
                self.col[3]=arcade.color.GREEN
                for i in range(len(self.col)):
                    if  not(i==self.olp):
                        self.col[i]=arcade.color.BLACK


            if self.olp <1 :
                self.olp = 4
            #if self.olp<4 and self.in_options==True:
             #   self.olp=6


        elif key == arcade.key.D and self.player.center_x<=self.LEVELw-100 and self.player.hp>0:
            self.player.change_x = self.movespeed
            self.last_move = "right"
            self.player.lpose = "rw"
            self.player.pl = 0
        elif key == arcade.key.P:
            self.atak = True
        elif key == arcade.key.LSHIFT and self.player.center_x < self.LEVELw - 1000 and self.player.center_y < self.LEVELh - 250 and self.player.center_y > 50 and self.player.center_x > 500:
            self.movespeed = 25
        elif key == arcade.key.SPACE and self.player.hp>0:
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
        elif key == arcade.key.TAB and self.player.lvl>=10 and self.player.mana>500:
            if self.player.lpose=="rs":
                self.player.lpose="bankaibegin"
            else:
                self.player.lpose="bankaibegin1"
            self.player.mana-=500
            arcade.play_sound(self.ichigo_bankai)
        elif key == arcade.key.A or key == arcade.key.D:
            self.player.change_x = 0
        elif key==arcade.key.P:
            self.atak=False
        elif key == arcade.key.LCTRL:
            self.player.ar=False
        elif key==arcade.key.ESCAPE:
            self.gameover=False
        elif key == arcade.key.ENTER and self.gameover==True:
            if self.olp==3:
                sys.exit()
            # if self.olp==2 and self.inn==True:
            #     self.kp[1]="OPTIONS"
            #     self.x[1]-=50
            #     self.kp[2]=self.kp[4]
            #     self.size2=18
            #     self.x[2]-=100
            #     self.kp[3]=self.kp[5]
            #     self.x[3]-=120
            #     self.size3=18
            #     self.y[3]=300
            #     self.poi=0
            #     self.in_options=True
            #     self.inn=True
            # if self.poi==0 and self.inn==True:
            #     self.olp=1
            #     self.poi=1
            # if self.olp==2 and self.inn==True:
            #     self.file = open("save", "w")
            #     self.file.write("1350")
            #     self.file.write("600")
            #     self.file.close()
            #     self.kp[1] = "MENU"
            #     self.x[1] += 50
            #     self.kp[2] = "Options"
            #     self.size2 = 25
            #     self.x[2] += 100
            #     self.kp[3] = "EXIT"
            #     self.x[3] += 120
            #     self.size3 = 25
            #     self.y[3] = 100
            #     self.poi1=0
            #
            #     self.inn=False
            #     self.in_options = False
            #
            # if self.olp==3 and self.inn==True:
            #     self.file = open("save", "w")
            #     self.file.write("1000")
            #     self.file.write("445")
            #     self.file.close()
            #
            #     self.kp[1] = "MENU"
            #     self.x[1] += 50
            #     self.kp[2] = "Options"
            #     self.size2 = 25
            #     self.x[2] += 100
            #     self.kp[3] = "EXIT"
            #     self.x[3] += 120
            #     self.size3 = 25
            #     self.y[3] = 100
            #     self.poi1=0
            #     self.in_options = False
            #
            #     self.inn=False
            #     self.in_options = False
            # if self.poi1==0 and self.inn==False:
            #     self.olp=1
            #     self.poi1=1
        elif key==arcade.key.LSHIFT or not(self.player.center_x<self.LEVELw-1000 and self.player.center_y<self.LEVELh-250 and self.player.center_y>250 and self.player.center_x>500 ):
            self.movespeed=20

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
            self.player.t=False
            if self.player.bankai==True and time.time()-self.player.timebegin==60:
                arcade.stop_sound(self.ichigo_bankai)
                self.player.bankai=False
            if self.d==1 and self.orihime.center_x-500<self.player.center_x and self.orihime.center_y-30<self.player.center_y:
                self.win=True
            if self.player.center_y>2300 or self.player.center_x>4200 or self.player.center_x<0:
                self.player.center_y=2000
                self.player.center_x=4000
            self.io=len(self.coin_list)
            if self.jj1==0 and self.lvl==5:
                self.l5=time.time()
                arcade.play_sound(self.lvl5)
                self.jj1=1
            if self.io<COIN_COUNT:
                for self.io in range(COIN_COUNT):
                    coin = Coin()
                    self.coin_placed_successfully=False
                    while not self.coin_placed_successfully:
                        coin.center_x = random.randint(100, 4100)
                        coin.center_y = random.randint(100, 2000)
                        self.wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                        self.coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)
                        if len(self.wall_hit_list) == 0 and len(self.coin_hit_list) == 0:
                            self.coin_placed_successfully = True

                    self.coin_list.append(coin)
            if self.d==1:
                self.orihime_engine.update()
            self.e=len(self.enemy_list)
            if self.d==1 and self.lvl==5:
                self.orihime.update()
            self.player.t=False
            if self.e<ENEMY_COUNT:
                for self.e in range(ENEMY_COUNT):
                    enemy = Enemy(1,self.lvl*2)
                    self.enemy_placed_successfully=False
                    while not self.enemy_placed_successfully:
                        enemy.center_x = random.randint(100, 4100)
                        enemy.center_y = random.randint(100, 2000)
                        enemy.boundary_right = enemy.center_x + 600 * 1
                        enemy.boundary_left = enemy.center_x - 600 * 1
                        enemy.change_x = 5
                        self.wall_hit_list=arcade.check_for_collision_with_list(enemy,self.wall_list)
                        if len(self.wall_hit_list)==0:
                            self.enemy_placed_successfully=True
                    self.physics_engine1 = arcade.PhysicsEnginePlatformer(enemy, self.wall_list,
                                                                          gravity_constant=-self.GRAVITY)

                    self.enemy_list.append(enemy)
                    enemy.engine=self.physics_engine1
                    self.engine_list.append(self.physics_engine1)
                    #t = threading.Thread(target=enemy_update, name="thread", args=(hp, self.player.hp))
                    #self.threadenemy_list.append(t)
                   # t.start()

            changed=False

            self.onground=False
            hp=self.player.hp
            if self.player.center_x+100>self.LEVELw-100:
                self.movespeed=10
                self.player.center_x=self.LEVELw-200
            self.last_x = self.player.center_x
            self.last_y = self.player.center_y

            self.physics_engine.update()

            if self.player.ojk==True:
                self.volna.update()
                if self.volna.center_x==self.volna.lb:
                    self.volna.kill()
                    self.volna_c=0
                    self.player.ojk=False

            self.threadenemy_list=[]
            #for i in self.engine_list:
                #u=threading.Thread(target=i.update,name="",args=())
                #self.threadenemy_list.append(u)
                #u.start()
                #u.join()

            for p in self.engine_list:
                try:
                    i=self.engine_list.index(p)
                    if self.enemy_list[i].center_x > self.view_left and self.enemy_list[i].center_x < SCREEN_WIDTH + self.view_left and self.enemy_list[i].center_y > self.view_bottom and self.enemy_list[i].center_y < self.view_bottom + SCREEN_HEIGHT:
                        p.update()
                except IndexError:
                    i=self.engine_list.index(p)+1
           # for i in self.engine_list:
            #    u=Process(target=i.update,args=())

              #  u.start()
            for wall in self.coin_list:
                if wall.center_x > self.view_left - 100 and wall.center_x < SCREEN_WIDTH + self.view_left + 100 and wall.center_y > self.view_bottom - 100 and wall.center_y < self.view_bottom + SCREEN_HEIGHT + 100:
                    wall.update()
                #self.coin_list.update()
                #self.coin_list.update_animation()
            opl=0
            for enemy in self.enemy_list:
                opl+=1
                if enemy.center_x > self.view_left and enemy.center_x < SCREEN_WIDTH + self.view_left and enemy.center_y > self.view_bottom and enemy.center_y < self.view_bottom + SCREEN_HEIGHT:
                    enemy.update(hp, self.player.hp)
                    enemy.atak = False
                    enemy.getdamage = False
                    # If the enemy hit a wall, reverse
                    if len(arcade.check_for_collision_with_list(enemy, self.wall_list)) > 0:
                        enemy.change_x *= -1
                        if enemy.lpose == "rw":
                            enemy.lpose = "lw"
                        if enemy.lpose == "lw":
                            enemy.lpose = "rw"
                    # If the enemy hit the left boundary, reverse
                    elif enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
                        enemy.change_x *= -1
                        enemy.lpose = "rw"
                    # If the enemy hit the right boundary, reverse
                    elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
                        enemy.change_x *= -1
                        enemy.lpose = "lw"
                    elif self.player.ojk==True:
                        if arcade.check_for_collision(self.volna,enemy):
                            enemy.getdamage=True
                            arcade.play_sound(self.ichigo_hit)
                            enemy.hp-=self.player.damage*2
                            if enemy.hp <= 0:
                                self.money += enemy.hp1//10
                                self.player.xp+=enemy.hp1
                                try:
                                    self.engine_list.remove(self.engine_list[opl-1])
                                except IndexError:
                                    pass
                                finally:
                                    enemy.kill()

                    elif arcade.check_for_collision(self.player, enemy) and self.player.hp > 0 and (enemy.center_x > self.view_left-100 and enemy.center_x < SCREEN_WIDTH + self.view_left+100 and enemy.center_y > self.view_bottom-100 and enemy.center_y < self.view_bottom + SCREEN_HEIGHT+100):
                        enemy.atak = True
                        enemy.change_x =0
                        enemy.kk+=1
                        #arcade.play_sound(self.ichigo_hit)
                        if enemy.kk>=10:
                            self.player.hp -= enemy.attak // self.player.shit
                            arcade.play_sound(self.ichigo_hit)
                            enemy.kk=0
                        if self.player.hp <= 0:
                            arcade.play_sound(self.ichigo_died)
                            self.gameover = True
                        if self.player.atak == True and self.player.lpose == "la" and enemy.center_x < self.player.center_x:
                            enemy.atak == False
                            enemy.getdamage = True
                            if self.player.a >= 5:
                                arcade.play_sound(self.ichigo_hit)
                                enemy.hp -= self.player.damage
                                self.player.t=True
                                self.player.a = 0
                            if enemy.hp <= 0:
                                self.money += enemy.hp1//10
                                self.player.xp+=enemy.hp1
                                try:
                                    self.engine_list.remove(self.engine_list[opl-1])
                                except IndexError:
                                    pass
                                finally:
                                    enemy.kill()

                        if self.player.atak == True and self.player.lpose == "ra" and enemy.center_x > self.player.center_x:
                            enemy.atak == False
                            enemy.getdamage = True
                            if self.player.a >= 5:
                                arcade.play_sound(self.ichigo_hit)
                                enemy.hp -= self.player.damage
                                self.player.t=True
                                self.player.a = 0
                            if enemy.hp <= 0:
                                self.money += enemy.hp1//10
                                self.player.xp+=enemy.hp1
                                try:
                                    self.engine_list.remove(self.engine_list[opl-1])
                                except IndexError:
                                    pass
                                finally:
                                    enemy.kill()


                    elif enemy.atak == False and enemy.change_x == 0:
                        enemy.change_x = enemy.l_x

            if self.player.center_x == self.last_x and self.player.center_y == self.last_y and self.l >= 10 and not (self.player.lpose=="bankaibegin") and not (self.player.lpose=="bankaibegin1"):
                if self.last_move == "left":
                    self.player.lpose = "ls"
                else:
                    self.player.lpose = "rs"
                self.l = 0

            self.player.update()
            hit_listt= arcade.check_for_collision_with_list(self.player,self.enemy_list)

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
            #if not(self.player.t) and (self.player.atak):
               # arcade.play_sound(self.ichigo_nothit)
            #if self.kk==0 and self.player.atak==True:
               # arcade.play_sound(self.ichigo_nothit)
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.money += 1
                self.player.xp+=10
                arcade.play_sound(self.ichio_hit_coin)
                coin.kill()

       # if self.atak==True:
        #    if self.last_move=="left":
         #       self.player_list.update_texture(self.player_stand.textures[2])

        # Scroll left
            if self.player.center_y<50:
                self.player.center_y=100
            if self.view_left>0:
                left_bndry = self.view_left + VIEWPORT_MARGIN+500
            else:
                left_bndry = self.view_left + VIEWPORT_MARGIN
            if self.player.left < left_bndry:
                self.view_left -= left_bndry - self.player.left
                self.mos.center_x-=left_bndry-self.player.left
                self.xx=self.view_left
                changed = True

        # Scroll right
            if self.view_left+SCREEN_WIDTH<self.LEVELw:
                right_bndry = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN-500
            else:
                right_bndry = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
            if self.player.right > right_bndry:
                self.view_left += self.player.right - right_bndry
                self.mos.center_x+=self.player.right-right_bndry
                self.xx=self.view_left
                changed = True

        # Scroll up
            top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN-300
            if self.player.top > top_bndry:
                self.view_bottom += self.player.top - top_bndry
                self.mos.center_y+=self.player.top-top_bndry
                self.yy=self.view_bottom
                changed = True

        # Scroll down

            if self.view_bottom>0:
                bottom_bndry = self.view_bottom + VIEWPORT_MARGIN+300
            else:
                bottom_bndry=self.view_bottom+VIEWPORT_MARGIN
            if self.player.bottom< bottom_bndry:
                self.view_bottom -= bottom_bndry - self.player.bottom
                self.mos.center_y-=bottom_bndry-self.player.bottom

                self.yy=self.view_bottom
                changed = True

            if changed:


                arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        if self.gameover:

            self.gameover=True


def main():
    """ Main method """
    file = open("save")

    SCREEN_WIDTH = int(file.read(4))
    SCREEN_HEIGHT = int(file.read(4))
    file.close()

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()