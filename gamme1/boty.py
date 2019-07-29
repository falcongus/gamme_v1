import arcade
import os
import random
from multiprocessing import Process

monsters_scale=2
SPRITE_NATIVE_SIZE=41
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * monsters_scale)

class Enemy(arcade.Sprite):
    """
    Bot now it is on 1 lvl

    """
    def __init__(self,scale,lvl):
        """ Set up the space ship. """

        # Call the parent Sprite constructor
        super().__init__("images/1/1_enemies_1_walk_000.png", scale)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Info on where we are going.
        # Angle comes in automatically from the parent class.
        self.level=random.randint(1,327)
        self.attak=1
        self.kk=0
        self.j=0
        self.monster_texture_list=[]
        if (self.level<=100) and (lvl>=1):
            for j in range(10) :
                if j==1:
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
        elif (self.level>100) and (self.level<=180) and (lvl>=2):
            self.attak=2
            for j in range(10):
                if j==2 and j<=lvl:
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
        elif (self.level>180) and (self.level<=240) and (lvl>=3):
            self.attak=3
            for j in range(10):
                if j==3 and j<=lvl:
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
        elif (self.level>240) and (self.level<=280) and (lvl>=4):
            self.attak=4
            for j in range(10):
                if j==4 and j<=lvl:
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
        elif (self.level>280) and (self.level<=300) and (lvl>=5):
            self.attak=5
            for j in range(10):
                if j==5 and j<=lvl:
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
        elif (self.level>300) and (self.level<=310) and (lvl>=6):
            self.attak=6
            for j in range(10):
                if j==6 and j<=lvl:
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
        elif (self.level>310) and (self.level<=318) and (lvl>=7):
            self.attak=7
            for j in range(10):
                if j==7 and j<=lvl:
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
        elif (self.level>323) and (self.level<=326) and (lvl>=8):
            self.attak=8
            for j in range(10):
                if j==8 and j<=lvl:
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))

        elif (self.level>326) and (self.level<=327) and (lvl>=10):
            self.attak=10
            for j in range(11):
                if j==10 and j<=lvl:
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_walk_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_attack_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))

                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale))
                    for i in range(20):
                        if (i < 10):
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_00{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))
                        else:
                            self.monster_texture_list.append(
                                arcade.load_texture("images/{}/{}_enemies_{}_hurt_0{}.png".format(j,j,1,i), scale=monsters_scale,
                                                    mirrored=True))

        self.speed = 10
        self.current_texture = 0
        self.plbegintexture = 0
        self.plendtexture = 0
        self.k = self.center_x
        self.lpose = ""
        self.p = 0
        self.pl = 1

        self.attak*=10*lvl
        self.hp =lvl* (self.attak*self.attak)
        self.hp1=self.hp
        self.textures=self.monster_texture_list
        self.l_x=0
        self.engine=None
        # Set boundaries on the left/right the enemy can't cross
        self.left=SPRITE_SIZE*2
        self.bottom=SPRITE_SIZE

        self.change_x = 2
        self.atak=False
        self.getdamage=False
        self.output=""
        self.plp=0
        # Mark that we are respawning.


    def update(self,hp,plhp):
        self.plp+=1
        self.j+=1
        if self.j>=50:
            self.center_y+=20
            self.j=0
        if self.hp>0 and self.plp>=5:
            if self.change_x>0 or self.change_x<0:
                self.l_x=self.change_x
            self.center_x+=self.change_x
            if self.change_x>0:
                self.lpose="rw"

            if self.change_x<0:
                self.lpose="lw"
            if self.lpose == "rw":
                self.plbegintexture = 0
                self.plendtexture = 19
            if self.lpose == "lw":
                self.plbegintexture = 20
                self.plendtexture = 39
            if plhp<=0:
                self.atak=False
            if self.atak==True :
                if self.lpose=="rw":
                    self.lpose="ra"
                    self.plbegintexture=40
                    self.plendtexture=59
                if self.lpose=="lw":
                    self.lpose="la"
                    self.plbegintexture=60
                    self.plendtexture=79
            if self.getdamage==True:
                if self.lpose=="rw" or self.lpose=="ra":
                    self.lpose="rd"
                    self.plbegintexture=80
                    self.plendtexture=99
                if self.lpose=="lw" or self.lpose=="la":
                    self.lpose="ld"
                    self.plbegintexture=100
                    self.plendtexture=119
            if (self.center_x-self.k<=-10 or self.center_x-self.k>=10) and (self.lpose=="lw" or self.lpose=="rw" ):
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
            if self.atak:
                self.current_texture+=1
                if self.current_texture < len(self.textures):
                    if self.current_texture >= self.plbegintexture and self.current_texture <= self.plendtexture:
                        self.set_texture(self.current_texture)
                    else:
                        self.current_texture = self.plbegintexture
                else:
                    self.current_texture = 0
                if self.current_texture >= self.plendtexture:
                    self.current_texture = self.plbegintexture
            if self.getdamage:
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
            self.plp=0








