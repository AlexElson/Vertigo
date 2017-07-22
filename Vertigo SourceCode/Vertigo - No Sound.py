import pygame, sys
import time
import random
import math
from math import *
import platform
from pygame.locals import *
pygame.init()
fps=60

WIDTH=int(640)
HEIGHT=int(480)
screen=pygame.display.set_mode((WIDTH,HEIGHT))
Clock=pygame.time.Clock()
font1 = pygame.font.SysFont("Verdana", 14)
font2 = pygame.font.SysFont("Verdana", 10)

#Load Files
cloud01=pygame.image.load("Images/cloud01.png").convert_alpha()
cloud02=pygame.image.load("Images/cloud02.png").convert_alpha()
cloud03=pygame.image.load("Images/cloud03.png").convert_alpha()
cloud04=pygame.image.load("Images/cloud04.png").convert_alpha()
cloud05=pygame.image.load("Images/cloud05.png").convert_alpha()
cloud06=pygame.image.load("Images/cloud06.png").convert_alpha()
cloud07=pygame.image.load("Images/cloud07.png").convert_alpha()
dustfx=pygame.image.load("Images/dust.png").convert_alpha()
brightfx=pygame.image.load("Images/bright.png").convert_alpha()
sparkfx=pygame.image.load("Images/spark.png").convert_alpha()
scrapfx=pygame.image.load("Images/scrap.png").convert_alpha()
bloodimg=pygame.image.load("Images/blood.png").convert_alpha()
bloodpart=pygame.image.load("Images/bloodpart.png").convert_alpha()
shieldimg=pygame.image.load("Images/shield.png").convert_alpha()

tileset=pygame.image.load("Images/tileset.png").convert_alpha()
sky=pygame.image.load("Images/sky.png").convert_alpha()
ground=pygame.image.load("Images/ground.png").convert_alpha()
grass=pygame.image.load("Images/grass.png").convert_alpha()

copterblack=pygame.image.load("Images/helicopter1.png").convert_alpha()
copterwhite=pygame.image.load("Images/helicopter2.png").convert_alpha()
coptercrash=pygame.image.load("Images/helicoptercrash.png").convert_alpha()

buildings=pygame.image.load("Images/buildings.png").convert_alpha()
glassCracked=pygame.image.load("Images/cracked.png").convert_alpha()
fireimg=pygame.image.load("Images/fire.png").convert_alpha()
shard=pygame.image.load("Images/shard.png").convert_alpha()
bulletspark=pygame.image.load("Images/bulletspark.png").convert_alpha()
bomb1=pygame.image.load("Images/bomb1.png").convert_alpha()
bombexploded=pygame.image.load("Images/bombexploded.png").convert_alpha()

vertigologo=pygame.image.load("Images/vertigologo.png").convert_alpha()
blackimg=pygame.image.load("Images/black.png").convert()
sidebar=pygame.image.load("Images/sidebar.png").convert_alpha()
arrowleft=pygame.image.load("Images/arrowleft.png").convert_alpha()
arrowright=pygame.image.load("Images/arrowright.png").convert_alpha()
arrowleft_bright=pygame.image.load("Images/arrowleft_bright.png").convert_alpha()
arrowright_bright=pygame.image.load("Images/arrowright_bright.png").convert_alpha()
level1=pygame.image.load("Images/level1.png").convert_alpha()
level2=pygame.image.load("Images/level2.png").convert_alpha()
level3=pygame.image.load("Images/level3.png").convert_alpha()
level4=pygame.image.load("Images/level4.png").convert_alpha()
level5=pygame.image.load("Images/level5.png").convert_alpha()
level6=pygame.image.load("Images/level6.png").convert_alpha()
level7=pygame.image.load("Images/level7.png").convert_alpha()
level8=pygame.image.load("Images/level8.png").convert_alpha()
level8b=pygame.image.load("Images/level8b.png").convert_alpha()
level9=pygame.image.load("Images/level9.png").convert_alpha()
level10=pygame.image.load("Images/level10.png").convert_alpha()
pausedimg=pygame.image.load("Images/paused.png").convert_alpha()
button=pygame.image.load("Images/button.png").convert_alpha()
keyboard=pygame.image.load("Images/keyboardoverlay.png").convert_alpha()
iconimg=pygame.image.load("Images/iconguy.png").convert_alpha()
pygame.display.set_icon(iconimg)

    
npc=[] #NPCs
npcx=[]
npcy=[]
npcframe=[]
npcdir=[]
npcalive=[]
npcaliveold=[]
npcdx=[]
npcmove=[]
npcfloor=[]
shootDelay=[]
blood=[]
bloodx=[]
bloody=[]
bloodtrail=[]
bloodtrailx=[]
bloodtraily=[]
for n in range(12):
    npc.append(n); npc[n]=""
    npcx.append(n); npcx[n]=0.0
    npcy.append(n); npcy[n]=0.0
    npcframe.append(n); npcframe[n]=0.0
    npcdir.append(n); npcdir[n]=0
    npcalive.append(n); npcalive[n]=1
    npcaliveold.append(n); npcaliveold[n]=1
    npcdx.append(n); npcdx[n]=0.0
    npcmove.append(n); npcmove[n]=0.0
    npcfloor.append(n); npcfloor[n]=-1
    shootDelay.append(n); shootDelay[n]=0
    blood.append(n); blood[n]=-1
    bloodx.append(n); bloodx[n]=0
    bloody.append(n); bloody[n]=0
    bloodtrail.append(n); bloodtrail[n]=0.0
    bloodtrailx.append(n); bloodtrailx[n]=0.0
    bloodtraily.append(n); bloodtraily[n]=0.0
stance=-1
firstshot=0
alive=1
frame=0
framechange=0
framedir=1
invinsible=0
shield=0
shielddir=0

copter=[] #Copter
copterx=[]
coptery=[]
blades=[]
engine=[]
coptervelx=[]
coptervely=[]
rotation=[]
rotationacc=[]
damage=[]
copterfire=[]
sprayBullets=[]
sprayBulletsDelay=[]
for n in range(12):
    copter.append(n); copter[n]=""
    copterx.append(n); copterx[n]=0.0
    coptery.append(n); coptery[n]=0.0
    blades.append(n); blades[n]=random.randint(0,628); blades[n]=blades[n]/100.0
    engine.append(n); engine[n]=0.0
    rotation.append(n); rotation[n]=0.0
    rotationacc.append(n); rotationacc[n]=0.0
    coptervelx.append(n); coptervelx[n]=0.0
    coptervely.append(n); coptervely[n]=0.0
    damage.append(n); damage[n]=0.0
    copterfire.append(n); copterfire[n]=0.0
    sprayBullets.append(n); sprayBullets[n]=0
    sprayBulletsDelay.append(n); sprayBulletsDelay[n]=0
copteracc=.0025
copterspeed=.15
enemyacc=.0025
enemyspeed=.15
mycopter="Black"

camera=0 #Camera and Mouse
camerax=-40
cameray=-40
selectx=npcx[0]
selecty=npcy[0]
mousex=0.0
mousey=0.0
up=0; down=0; left=0; right=0
cameraback=0

grassMove=2.0 #Grass
grassDir=0

left2=0; right2=0; up2=0; down2=0 #Player Movement Variables
jump=0; jumpacc=0.0; jumpy=0.0; velx=0.0 
enter=0; lastdir=0

#Buildings and Floors
building=[] 
buildingheight=[]
buildingwidth=[]
buildingx=[]
buildingfloor1=[]
buildingfloor1doorup=[]
buildingfloor1doordown=[]
roofentry=[]
for n in range(10):
    building.append(n); building[n]=""
    buildingheight.append(n); buildingheight[n]=0.0
    buildingwidth.append(n); buildingwidth[n]=0.0
    buildingx.append(n); buildingx[n]=0.0
    buildingfloor1.append(n); buildingfloor1[n]=-1
    buildingfloor1doorup.append(n); buildingfloor1doorup[n]=0
    buildingfloor1doordown.append(n); buildingfloor1doordown[n]=0
    roofentry.append(n); roofentry[n]=0
door=0

#Glass Shards
glassLeft=[[0 for y in range(30)] for x in range(10)]
glassRight=[[0 for y in range(30)] for x in range(10)]
glassShard=[] 
glassShardx=[]
glassShardy=[]
glassSharddx=[]
glassSharddy=[]
glassBlood=[]
for n in range(80):
    glassShard.append(n); glassShard[n]=0
    glassShardx.append(n); glassShardx[n]=0
    glassShardy.append(n); glassShardy[n]=0
    glassSharddx.append(n); glassSharddx[n]=0
    glassSharddy.append(n); glassSharddy[n]=0
    glassBlood.append(n); glassBlood[n]=0
for n in range(10):
    for nn in range(30):
        glassLeft[n][nn]=100
        glassRight[n][nn]=100

#Bullets
bullet=[]
bulletx=[]
bullety=[]
bulletdx=[]
bulletdy=[]
bulletenemy=[]
for n in range(35):
    bullet.append(n); bullet[n]=False
    bulletx.append(n); bulletx[n]=0.0
    bullety.append(n); bullety[n]=0.0
    bulletdx.append(n); bulletdx[n]=0.0
    bulletdy.append(n); bulletdy[n]=0.0
    bulletenemy.append(n); bulletenemy[n]=0
spacefire=0

#Clouds
cx=[]; cy=[]; cc=[]; cs=[]
for n in range(5):
    cx.append(n); cx[n]=random.randint(-100,WIDTH+100)
    cy.append(n); cy[n]=random.randint(-120,0)
    cc.append(n); cc[n]=random.randint(1,7)
    cs.append(n); cs[n]=random.randint(0,3)
speed=0

#Explosion
dust=[]; dustup=[]
dustx=[]; dusty=[]; dustdx=[]; dustdy=[]
for n in range(90):
    dust.append(n); dust[n]=0.0
    dustup.append(n); dustup[n]=0
    dustx.append(n); dustx[n]=0.0
    dustdx.append(n); dustdx[n]=0.0
    dusty.append(n); dusty[n]=0.0
    dustdy.append(n); dustdy[n]=0.0
trail=[]; trailx=[]; traily=[]; trailsize=[]
for n in range(200):
    trail.append(n); trail[n]=0.0
    trailx.append(n); trailx[n]=0.0
    traily.append(n); traily[n]=0.0
    trailsize.append(n); trailsize[n]=0.0
spark=[]; sparkdx=[]; sparkdy=[]
sparkx=[]; sparky=[]; sparkDelay=[]
for n in range(20):
    spark.append(n); spark[n]=0.0
    sparkdx.append(n); sparkdx[n]=0.0
    sparkdy.append(n); sparkdy[n]=0.0
    sparkx.append(n); sparkx[n]=0.0
    sparky.append(n); sparky[n]=0.0
    sparkDelay.append(n); sparkDelay[n]=0.0
bright=0.0; brightx=0.0 ; brighty=0.0

#Fire
fire=[]
firex=[]
firey=[]
fireani=[]
for n in range(75):
    fire.append(n); fire[n]=0.0
    firex.append(n); firex[n]=0.0
    firey.append(n); firey[n]=0.0
    fireani.append(n); fireani[n]=0.0; fireani[n]=random.randint(100,600)/100.0
    
    
 
#Bombs
bomb=[]
bombactive=[]
bombtime=[]
bombtimemax=[]
bombx=[]
for n in range(5):
    bomb.append(n); bomb[n]=-1
    bombactive.append(n); bombactive[n]=0
    bombtime.append(n); bombtime[n]=0.0
    bombtimemax.append(n); bombtimemax[n]=0.0
    bombx.append(n); bombx[n]=0

#Level Arrays
leveltype=[]
levelvar1=[]
levelvar2=[]
for n in range(17):
    leveltype.append(n); leveltype[n]=""
    levelvar1.append(n); levelvar1[n]=0
    levelvar2.append(n); levelvar2[n]=0

#Menu Variables
fade=255
mainmenu=1
levelselect=0
levelselecting=1
levelprog=1
levelmax=10
level=0
arrowleftjump=0
arrowrightjump=0
shopselect=0
optionselect=0
objectiveText=0
won=0
paused=0
failed=0

#Options Menu
particlesopt=2
bloodopt=1
cloudsopt=1

#Colors
BLACK=(0,0,0)
WHITE=(255,255,255)
GOLD=(200,200,90)

#check if file exists
levelp=1
a=0
try:
    with open('Images/Progress.txt'): a=1
except IOError:
    a=0
    
if (a==1):    #Load level
    load=open("Images/Progress.txt","r")
    levelp=load.readline()
    levelprog=int(levelp)
    load.close()








autocamera=0
def generateLevel(lvl):
    global selectx, selecty, camerax, cameray, cameraback, autocamera
    autocamera=0
    if (lvl==1):
        leveltype[lvl]="Shatter"; levelvar1[lvl]=5
        building[0]="Glass"
        buildingheight[0]=random.randint(3,10)
        buildingwidth[0]=random.randint(3,8)
        buildingx[0]=random.randint(5,10)
        buildingfloor1[0]=random.randint(0,buildingheight[0]-2)
        buildingfloor1doorup[0]=random.randint(16,buildingwidth[0]*38-32)
        roofentry[0]=random.randint(0,buildingwidth[0]*38-24)
        npc[0]="Ally"
        copter[0]=mycopter
        copterx[0]=-5; coptery[0]=0
        
    if (lvl==2):
        leveltype[lvl]="Defuse"; levelvar1[lvl]=2
        building[0]="Glass"
        buildingheight[0]=random.randint(3,10)
        buildingwidth[0]=random.randint(3,8)
        buildingx[0]=random.randint(5,6)
        buildingfloor1[0]=random.randint(0,buildingheight[0]-2)
        buildingfloor1doorup[0]=random.randint(16,buildingwidth[0]*38-32)
        roofentry[0]=random.randint(0,buildingwidth[0]*38-24)
        building[1]="Glass"
        buildingheight[1]=random.randint(4,10)
        buildingwidth[1]=random.randint(3,8)
        buildingx[1]=-10-buildingwidth[1]*2
        buildingfloor1[1]=random.randint(1,buildingheight[1]-2)
        buildingfloor1doorup[1]=random.randint(16,buildingwidth[1]*38-32)
        buildingfloor1doordown[1]=random.randint(16,buildingwidth[1]*38-32)
        roofentry[1]=random.randint(0,buildingwidth[1]*38-24)
        building[2]="Glass"
        buildingheight[2]=buildingheight[1]
        buildingwidth[2]=buildingwidth[1]
        buildingx[2]=buildingx[1]
        buildingfloor1[2]=0
        buildingfloor1doorup[2]=random.randint(16,buildingwidth[1]*38-32)
        bomb[0]=0; bombtime[0]=3900.0; bombx[0]=random.randint(24,buildingwidth[0]*38-40); bombactive[0]=1; bombtimemax[0]=bombtime[0]
        bomb[1]=1; bombtime[1]=4000.0; bombx[1]=random.randint(24,buildingwidth[1]*38-40); bombactive[1]=1; bombtimemax[1]=bombtime[1]
        npc[0]="Ally"
        copter[0]=mycopter
        copterx[0]=-5; coptery[0]=0

    if (lvl==3):
        leveltype[lvl]="Helicopter"; levelvar1[lvl]=1
        npc[0]="Ally"
        copter[0]=mycopter
        copterx[0]=-5; coptery[0]=0
        copter[1]="Black"
        copterx[1]=-19; coptery[1]=0

    if (lvl==4):
        leveltype[lvl]="Eliminate"; levelvar1[lvl]=4
        building[0]="Glass"
        buildingheight[0]=random.randint(8,12)
        buildingwidth[0]=random.randint(5,8)
        buildingx[0]=random.randint(12,16)
        buildingfloor1[0]=random.randint(2,buildingheight[0]-2)
        buildingfloor1doorup[0]=random.randint(16,buildingwidth[0]*38-32)
        buildingfloor1doordown[0]=random.randint(16,buildingwidth[0]*38-32)
        roofentry[0]=random.randint(0,buildingwidth[0]*38-24)
        building[1]="Glass"; closeObjects()
        buildingheight[1]=buildingheight[0]
        buildingwidth[1]=buildingwidth[0]
        buildingx[1]=buildingx[0]
        buildingfloor1[1]=random.randint(1,buildingfloor1[0]-1)
        buildingfloor1doorup[1]=buildingfloor1doordown[0]
        buildingfloor1doordown[1]=random.randint(16,buildingwidth[0]*38-32)
        building[2]="Glass"; closeObjects()
        buildingheight[2]=buildingheight[0]
        buildingwidth[2]=buildingwidth[0]
        buildingx[2]=buildingx[0]
        buildingfloor1[2]=random.randint(0,buildingfloor1[1]-1)
        buildingfloor1[2]=0
        buildingfloor1doorup[2]=buildingfloor1doordown[1]
        npc[0]="Ally"
        npc[1]="Enemy"; npcx[1]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[1]=0
        npc[2]="Enemy"; npcx[2]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[2]=2
        #npc[4]="Enemy"; npcx[4]=30; npcfloor[4]=-1
        npc[4]="Enemy"; npcx[4]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[4]=random.randint(0,2)
        npc[5]="Enemy"; npcx[5]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[5]=random.randint(0,2)
        copter[0]=mycopter
        copterx[0]=-5; coptery[0]=0

    if (lvl==5):
        leveltype[lvl]="Defuse"; levelvar1[lvl]=3; farthestx=0; amount=10
        for nn in range(amount):
            if (building[nn]==""):
                building[nn]="Glass"
                buildingheight[nn]=random.randint(6,12)
                floorsmax=random.randint(2,buildingheight[nn]-2)
                if (nn+floorsmax>=10): floorsmax=0
                buildingwidth[nn]=random.randint(4,8)
                buildingx[nn]=farthestx+random.randint(2,8); farthestx=buildingx[nn]+buildingwidth[nn]*38.0/16
                buildingfloor1[nn]=random.randint(floorsmax,buildingheight[nn]-2)
                buildingfloor1doorup[nn]=random.randint(16,buildingwidth[nn]*38-32)
                buildingfloor1doordown[nn]=random.randint(16,buildingwidth[nn]*38-32)
                roofentry[nn]=random.randint(0,buildingwidth[nn]*38-24)
                n=floorsmax
                if (floorsmax>0):
                    for n in range(1,floorsmax):
                        building[n+nn]="Glass"; closeObjects(); buildingheight[n+nn]=buildingheight[nn]; buildingwidth[n+nn]=buildingwidth[nn]; buildingx[n+nn]=buildingx[nn]; buildingfloor1[n+nn]=random.randint(floorsmax-n,buildingfloor1[nn+n-1]-1); buildingfloor1doorup[n+nn]=buildingfloor1doordown[n+nn-1]; buildingfloor1doordown[n+nn]=random.randint(16,buildingwidth[nn]*38-32)
                a=random.randint(0,1)
                if (a==0): buildingfloor1[nn+n]=0
                buildingfloor1doordown[nn+n]=0
        bomb[0]=random.randint(0,amount-2); bombtime[0]=15000.0; bombx[0]=random.randint(24,buildingwidth[0]*38-40); bombactive[0]=1; bombtimemax[0]=bombtime[0]
        bomb[1]=random.randint(0,amount-2); bombtime[1]=14900.0; bombx[1]=random.randint(24,buildingwidth[1]*38-40); bombactive[1]=1; bombtimemax[1]=bombtime[1]
        bomb[2]=random.randint(0,amount-2); bombtime[2]=14800.0; bombx[2]=random.randint(24,buildingwidth[2]*38-40); bombactive[2]=1; bombtimemax[2]=bombtime[2]
        for n in range(1,amount+2):
            a=random.randint(0,amount)
            for nn in range(amount):
                if (building[nn]!="" and a==nn):
                    npc[n]="Enemy"; npcx[n]=buildingwidth[nn]+random.randint(1,int(buildingwidth[nn]*38.0/16)); npcfloor[n]=random.randint(0,9)
        npc[0]="Ally"
        copter[0]=mycopter
        copterx[0]=buildingx[0]+2; coptery[0]=(-buildingheight[0]*36.0-7)/16
        npcx[0]=copterx[0]+5; npcy[0]=coptery[0]
        copter[1]="Black"
        copterx[1]=-40; coptery[1]=0

    if (lvl==6):
        leveltype[lvl]="Helicopter"; levelvar1[lvl]=1
        nn=0; floorsmax=10-1
        building[nn]="Glass"
        buildingheight[nn]=30
        buildingwidth[nn]=random.randint(5,8)
        buildingx[nn]=4
        buildingfloor1[nn]=random.randint(floorsmax,buildingheight[nn]-20)
        buildingfloor1doorup[nn]=random.randint(16,buildingwidth[nn]*38-32)
        buildingfloor1doordown[nn]=random.randint(16,buildingwidth[nn]*38-32)
        roofentry[nn]=random.randint(0,buildingwidth[nn]*38-24)
        for n in range(1,floorsmax):
            building[n]="Glass"; closeObjects(); buildingheight[n]=buildingheight[nn]; buildingwidth[n]=buildingwidth[nn]; buildingx[n]=buildingx[nn]; buildingfloor1[n]=random.randint(floorsmax-n,buildingfloor1[n-1]-1); buildingfloor1doorup[n]=buildingfloor1doordown[n-1]; buildingfloor1doordown[n]=random.randint(16,buildingwidth[nn]*38-32)
        buildingfloor1[floorsmax-1]=0
        buildingfloor1doordown[floorsmax-1]=0
        npc[0]="Ally"
        copter[0]=mycopter
        copterx[0]=buildingx[0]+2; coptery[0]=(-buildingheight[0]*36.0-7)/16
        copter[1]="Black"
        copterx[1]=30; coptery[1]=0; engine[1]=.4
        autocamera=1; camerax=copterx[0]+2; cameray=coptery[0]; selectx=camerax; selecty=cameray; cameraback=50

    if (lvl==8):
        leveltype[lvl]="Defuse"; levelvar1[lvl]=5; farthestx=0; amount=10
        for nn in range(amount):
            if (building[nn]==""):
                building[nn]="Glass"
                buildingheight[nn]=30
                floorsmax=9; f=28
                if (nn+floorsmax>=10): floorsmax=0
                buildingwidth[nn]=random.randint(4,8)
                buildingx[nn]=farthestx+random.randint(2,8); farthestx=buildingx[nn]+buildingwidth[nn]*38.0/16
                buildingfloor1[nn]=f
                buildingfloor1doorup[nn]=random.randint(16,buildingwidth[nn]*38-32)
                buildingfloor1doordown[nn]=random.randint(16,buildingwidth[nn]*38-32)
                roofentry[nn]=random.randint(0,buildingwidth[nn]*38-24)
                n=floorsmax
                if (floorsmax>0):
                    for n in range(1,floorsmax):
                        ff=random.randint(0,1)
                        if (ff==0): f-=random.randint(2,3)
                        if (ff==1): f-=random.randint(1,3)
                        if (f<1): f=1
                        building[n+nn]="Glass"; closeObjects(); buildingheight[n+nn]=buildingheight[nn]; buildingwidth[n+nn]=buildingwidth[nn]; buildingx[n+nn]=buildingx[nn]; buildingfloor1[n+nn]=f; buildingfloor1doorup[n+nn]=buildingfloor1doordown[n+nn-1]; buildingfloor1doordown[n+nn]=random.randint(16,buildingwidth[nn]*38-32)
                buildingfloor1[nn+floorsmax-1]=0
                buildingfloor1doordown[nn+floorsmax-1]=0
                break
        bomb[0]=random.randint(0,amount-3); bombtime[0]=3800.0; bombx[0]=random.randint(24,buildingwidth[0]*38-40); bombactive[0]=1; bombtimemax[0]=bombtime[0]
        bomb[1]=random.randint(0,amount-3); bombtime[1]=3700.0; bombx[1]=random.randint(24,buildingwidth[0]*38-40); bombactive[1]=1; bombtimemax[1]=bombtime[1]
        bomb[2]=random.randint(0,amount-3); bombtime[2]=3600.0; bombx[2]=random.randint(24,buildingwidth[0]*38-40); bombactive[2]=1; bombtimemax[2]=bombtime[2]
        bomb[3]=random.randint(0,amount-3); bombtime[3]=3500.0; bombx[3]=random.randint(24,buildingwidth[0]*38-40); bombactive[3]=1; bombtimemax[3]=bombtime[3]
        bomb[4]=random.randint(0,amount-3); bombtime[4]=3400.0; bombx[4]=random.randint(24,buildingwidth[0]*38-40); bombactive[4]=1; bombtimemax[4]=bombtime[4]
        for n in range(1,amount+2):
            a=random.randint(0,amount)
            for nn in range(amount):
                if (building[nn]!="" and a==nn):  
                    npc[n]="Enemy"; npcx[n]=buildingwidth[nn]+random.randint(1,int(buildingwidth[nn]*38.0/16)); npcfloor[n]=random.randint(0,amount-4)
        npc[0]="Ally"
        copter[0]=mycopter
        copterx[0]=buildingx[0]+2; coptery[0]=(-buildingheight[0]*36.0-7)/16

    if (lvl==7):
        leveltype[lvl]="Eliminate"; levelvar1[lvl]=10
        building[0]="Glass"; buildingheight[0]=10; buildingwidth[0]=4; buildingx[0]=8; buildingfloor1[0]=random.randint(4,buildingheight[0]-2); buildingfloor1doorup[0]=random.randint(16,buildingwidth[0]*38-32); buildingfloor1doordown[0]=random.randint(16,buildingwidth[0]*38-32)
        roofentry[0]=random.randint(0,buildingwidth[0]*38-24)
        building[1]="Glass"; closeObjects(); buildingheight[1]=buildingheight[0]; buildingwidth[1]=buildingwidth[0]; buildingx[1]=buildingx[0]; buildingfloor1[1]=random.randint(3,buildingfloor1[0]-1)
        buildingfloor1doorup[1]=buildingfloor1doordown[0]; buildingfloor1doordown[1]=random.randint(16,buildingwidth[0]*38-32)
        building[2]="Glass"; closeObjects(); buildingheight[2]=buildingheight[0]; buildingwidth[2]=buildingwidth[0]; buildingx[2]=buildingx[0]; buildingfloor1[2]=random.randint(2,buildingfloor1[1]-1)
        buildingfloor1doorup[2]=buildingfloor1doordown[1]; buildingfloor1doordown[2]=random.randint(16,buildingwidth[0]*38-32)
        building[3]="Glass"; closeObjects(); buildingheight[3]=buildingheight[0]; buildingwidth[3]=buildingwidth[0]; buildingx[3]=buildingx[0]; buildingfloor1[3]=random.randint(1,buildingfloor1[2]-1); buildingfloor1doorup[3]=buildingfloor1doordown[2]
        buildingfloor1doordown[3]=random.randint(16,buildingwidth[0]*38-32)
        n=4; building[n]="Glass"; closeObjects(); buildingheight[n]=buildingheight[0]; buildingwidth[n]=buildingwidth[0]; buildingx[n]=buildingx[0]; buildingfloor1[n]=0; buildingfloor1doorup[n]=buildingfloor1doordown[n-1]
        nn=5
        n=5; building[n]="Glass"; closeObjects(); buildingheight[n]=10; buildingwidth[n]=4; buildingx[n]=-20; buildingfloor1[n]=random.randint(4,buildingheight[nn]-2); buildingfloor1doorup[n]=random.randint(16,buildingwidth[nn]*38-32)
        buildingfloor1doordown[n]=random.randint(16,buildingwidth[nn]*38-32)
        n=6; building[n]="Glass"; closeObjects(); buildingheight[n]=buildingheight[nn]; buildingwidth[n]=buildingwidth[nn]; buildingx[n]=buildingx[nn]; buildingfloor1[n]=random.randint(3,buildingfloor1[n-1]-1); buildingfloor1doorup[n]=buildingfloor1doordown[n-1]
        buildingfloor1doordown[n]=random.randint(16,buildingwidth[nn]*38-32)
        n=7; building[n]="Glass"; closeObjects(); buildingheight[n]=buildingheight[nn]; buildingwidth[n]=buildingwidth[nn]; buildingx[n]=buildingx[nn]; buildingfloor1[n]=random.randint(2,buildingfloor1[n-1]-1)
        buildingfloor1doorup[n]=buildingfloor1doordown[n-1]; buildingfloor1doordown[n]=random.randint(16,buildingwidth[nn]*38-32)
        n=8; building[n]="Glass"; closeObjects(); buildingheight[n]=buildingheight[nn]; buildingwidth[n]=buildingwidth[nn]; buildingx[n]=buildingx[nn]
        buildingfloor1[n]=random.randint(1,buildingfloor1[n-1]-1); buildingfloor1doorup[n]=buildingfloor1doordown[n-1]; buildingfloor1doordown[n]=random.randint(16,buildingwidth[nn]*38-32)
        n=9; building[n]="Glass"; closeObjects(); buildingheight[n]=buildingheight[nn]; buildingwidth[n]=buildingwidth[nn]; buildingx[n]=buildingx[nn]; buildingfloor1[n]=0; buildingfloor1doorup[n]=buildingfloor1doordown[n-1]
        npc[0]="Ally"
        npc[1]="Enemy"; npcx[1]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[1]=random.randint(0,4)
        npc[2]="Enemy"; npcx[2]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[2]=random.randint(0,4)
        npc[3]="Enemy"; npcx[3]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[3]=random.randint(0,4)
        npc[4]="Enemy"; npcx[4]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[4]=random.randint(0,4)
        npc[5]="Enemy"; npcx[5]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[5]=random.randint(0,4)
        npc[6]="Enemy"; npcx[6]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[6]=random.randint(5,9)
        npc[7]="Enemy"; npcx[7]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[7]=random.randint(5,9)
        npc[8]="Enemy"; npcx[8]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[8]=random.randint(5,9)
        npc[9]="Enemy"; npcx[9]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[9]=random.randint(5,9)
        npc[10]="Enemy"; npcx[10]=buildingwidth[0]+random.randint(1,int(buildingwidth[0]*38.0/16)); npcfloor[10]=random.randint(5,9)
        copter[0]=mycopter
        copterx[0]=-5; coptery[0]=0
        npcx[0]=-1.5

    if (lvl==9):
        leveltype[lvl]="Helicopter"; levelvar1[lvl]=3; farthestx=0; amount=5
        for nn in range(amount):
            if (building[nn]==""):
                building[nn]="Glass"
                buildingheight[nn]=random.randint(6,12)
                floorsmax=random.randint(2,buildingheight[nn]-2)
                if (nn+floorsmax>=10): floorsmax=0
                buildingwidth[nn]=random.randint(4,8)
                buildingx[nn]=farthestx+random.randint(2,8); farthestx=buildingx[nn]+buildingwidth[nn]*38.0/16
                buildingfloor1[nn]=random.randint(floorsmax,buildingheight[nn]-2)
                buildingfloor1doorup[nn]=random.randint(16,buildingwidth[nn]*38-32)
                buildingfloor1doordown[nn]=random.randint(16,buildingwidth[nn]*38-32)
                roofentry[nn]=random.randint(0,buildingwidth[nn]*38-24)
                n=floorsmax
                if (floorsmax>0):
                    for n in range(1,floorsmax):
                        building[n+nn]="Glass"; closeObjects(); buildingheight[n+nn]=buildingheight[nn]; buildingwidth[n+nn]=buildingwidth[nn]; buildingx[n+nn]=buildingx[nn]; buildingfloor1[n+nn]=random.randint(floorsmax-n,buildingfloor1[nn+n-1]-1); buildingfloor1doorup[n+nn]=buildingfloor1doordown[n+nn-1]; buildingfloor1doordown[n+nn]=random.randint(16,buildingwidth[nn]*38-32)
                a=random.randint(0,1)
                if (a==0): buildingfloor1[nn+n]=0
                buildingfloor1doordown[nn+n]=0
                for n in range(10):
                    for nnn in range(30):
                        if (n==nn):
                            glassLeft[n][nnn]=100; glassRight[n][nnn]=100
        for n in range(1,amount+2):
            a=random.randint(0,amount)
            for nn in range(amount):
                if (building[nn]!="" and a==nn):  
                    npc[n]="Enemy"; npcx[n]=buildingwidth[nn]+random.randint(1,int(buildingwidth[nn]*38.0/16)); npcfloor[n]=random.randint(0,4)
        npc[0]="Ally"
        copter[0]=mycopter
        copterx[0]=buildingx[0]+2; coptery[0]=(-buildingheight[0]*36.0-7)/16
        npcx[0]=copterx[0]+5; npcy[0]=coptery[0]

    if (lvl==10):
        leveltype[lvl]="Shatter"; levelvar1[lvl]=25; amount=0; nn=0
        if True:
            if (building[nn]==""):
                building[nn]="Glass"
                buildingheight[nn]=15
                floorsmax=9
                buildingwidth[nn]=random.randint(4,5)
                buildingx[nn]=-40
                buildingfloor1[nn]=random.randint(floorsmax,buildingheight[nn]-2)
                buildingfloor1doordown[nn]=random.randint(16,buildingwidth[nn]*38-32)
                buildingfloor1doorup[nn]=random.randint(16,buildingwidth[nn]*38-32)
                roofentry[nn]=random.randint(0,buildingwidth[nn]*38-24)
                if (floorsmax>0):
                    for n in range(1,floorsmax):
                        building[n+nn]="Glass"; closeObjects(); buildingheight[n+nn]=buildingheight[nn]; buildingwidth[n+nn]=buildingwidth[nn]; buildingx[n+nn]=buildingx[nn]; buildingfloor1[n+nn]=random.randint(floorsmax-n,buildingfloor1[nn+n-1]-1); buildingfloor1doorup[n+nn]=buildingfloor1doordown[n+nn-1]; buildingfloor1doordown[n+nn]=random.randint(16,buildingwidth[nn]*38-32)
                buildingfloor1[nn+n]=0
                buildingfloor1doordown[nn+n]=0
        for n in range(1,12):
            npc[n]="Enemy"; npcx[n]=201+random.randint(0,7); npcfloor[n]=random.randint(0,8)
        npc[0]="Ally"
        copter[0]=mycopter
        copterx[0]=0; coptery[0]=0
        npcx[0]=copterx[0]+5; npcy[0]=coptery[0]
        for n in range(1,4):
            if (copter[n]==""):
                copter[n]="Black"
                copterx[n]=-125+n*50
                coptery[n]=0
        autocamera=1; cameraback=50
        camerax=-35; cameray=-12; selectx=camerax; selecty=cameray

    for n in range(10):
        for nn in range(30):
            if (buildingx[n]==buildingx[n-1] and n>0):
                glassLeft[n][nn]=0
                glassRight[n][nn]=0   

    if (autocamera==0):
        selectx=npcx[0] #Camera Swipe After Entering Level
        selecty=npcy[0]
        camerax=selectx+random.randint(-40,40)
        cameray=selecty+random.randint(-40,40)
        if (cameray>-4): cameray=-4
    closeObjects()

def closeObjects():
    for m in range(38*8):
        for n in range(10):
            if (buildingfloor1doordown[n]>0):
                if (buildingfloor1doorup[n]>=buildingfloor1doordown[n]-32 and buildingfloor1doorup[n]<=buildingfloor1doordown[n]+16):
                    buildingfloor1doordown[n]+=1
                if (buildingfloor1doordown[n]>buildingwidth[n]*38-16):
                    buildingfloor1doordown[n]=16
                if (buildingfloor1[n]==0):
                    buildingfloor1doordown[n]=0
            for nn in range(5):
                if (bomb[nn]==n):
                    if (bombx[nn]>=buildingfloor1doorup[n]-32 and bombx[nn]<=buildingfloor1doorup[n]+16): bombx[nn]+=1
                    if (bombx[nn]>=buildingfloor1doordown[n]-32 and bombx[nn]<=buildingfloor1doordown[n]+16): bombx[nn]+=1
                    if (bombx[nn]>buildingwidth[n]*38-16): bombx[nn]=24
                
        

def clearLevel():
    global alive, stance, firstshot, firesoundplay
    for n in range(10):
        building[n]=""
        buildingheight[n]=0.0
        buildingwidth[n]=0.0
        buildingx[n]=0.0
        buildingfloor1[n]=-1
        buildingfloor1doorup[n]=0
        buildingfloor1doordown[n]=0
        roofentry[n]=0
    for n in range(12):
        npc[n]=""
        npcx[n]=0
        npcy[n]=0
        npcframe[n]=0.0
        npcalive[n]=1
        npcaliveold[n]=1
        npcdx[n]=0
        npcfloor[n]=-1
        npcmove[n]=0
        blood[n]=-1
        bloodx[n]=0
        bloody[n]=0
        bloodtrail[n]=0
        bloodtrailx[n]=0
        bloodtraily[n]=0
        copter[n]=""
        copterx[n]=0.0
        coptery[n]=0.0
        blades[n]=random.randint(0,628); blades[n]=blades[n]/100.0
        engine[n]=0.0
        rotation[n]=0.0
        rotationacc[n]=0.0
        coptervelx[n]=0.0
        coptervely[n]=0.0
        damage[n]=0.0
        copterfire[n]=0.0
        sprayBullets[n]=0
        sprayBulletsDelay[n]=0
    for n in range(80):
        glassShard[n]=0
        glassBlood[n]=0
    for n in range(90):
        dust[n]=0.0
        dustup[n]=0
    for n in range(200):
        trail[n]=0.0
    for n in range(20):
        spark[n]=0.0
    for n in range(17):
        levelvar1[n]=0
        levelvar2[n]=0
    for n in range(10):
        for nn in range(30):
            glassLeft[n][nn]=100
            glassRight[n][nn]=100
    for n in range(75):
        fire[n]=0.0
        firex[n]=0.0
        firey[n]=0.0
        fireani[n]=random.randint(100,600)/100.0
    for n in range(5):
        bomb[n]=-1
    alive=1    
    stance=-1
    firstshot=0
    firesoundplay=0
    coptersoundplay=0

def displaySky():
    screen.blit(sky,(0,0))

def displayClouds():
    global stance
    for n in range(5):
        a=cameray*4+50
        if (stance>=0): speed=coptervelx[camera]*2+.1
        if (stance<0): speed=velx*2+.1
        if (cc[n]==1): screen.blit(cloud01,(cx[n],cy[n]-a))
        if (cc[n]==2): screen.blit(cloud02,(cx[n],cy[n]-a))
        if (cc[n]==3): screen.blit(cloud03,(cx[n],cy[n]-a))
        if (cc[n]==4): screen.blit(cloud04,(cx[n],cy[n]-a))
        if (cc[n]==5): screen.blit(cloud02,(cx[n],cy[n]-a))
        if (cc[n]==6): screen.blit(cloud07,(cx[n],cy[n]-a))
        if (cc[n]==7): screen.blit(cloud01,(cx[n],cy[n]-a))
        d=cs[n]/5.0*speed
        cx[n]=cx[n]-speed-d
        if (cx[n]<-320):
            cx[n]=random.randint(WIDTH,WIDTH+100)
            cy[n]=random.randint(-120,0)
            cc[n]=random.randint(1,7)
            cs[n]=random.randint(0,3)
        if (cx[n]>WIDTH+150):
            cx[n]=random.randint(-300,-280)
            cy[n]=random.randint(-120,0)
            cc[n]=random.randint(1,7)
            cs[n]=random.randint(0,3)

def displayGround():
    screen.blit(ground,(0,HEIGHT-160-64-cameray*16))

def displayGrass():
    for n in range(6):
        screen.blit(grass,(n*128-(camerax*16)%128,HEIGHT-160-64-20-cameray*16),(0,int(grassMove)*32,128,20))

def displayEffects(): 
    global bright, brightx, brighty, particlesopt, bloodopt
    for n in range(75): #Fire
        if (particlesopt==0 and n%2): fire[n]=0
        if (fire[n]>0): 
            if (fireani[n]>=1):
                if (fireani[n]<2):
                    effect=fireimg.copy(); effect.fill((255,255,255,255*(fireani[n]-1)), None, pygame.BLEND_RGBA_MULT)
                    screen.blit(effect,(firex[n]*16-camerax*16+WIDTH/2,-firey[n]*16-cameray*16+HEIGHT/2),(int(fireani[n])*16,0,16,16))
                else:
                    screen.blit(fireimg,(firex[n]*16-camerax*16+WIDTH/2,-firey[n]*16-cameray*16+HEIGHT/2),(int(fireani[n])*16,0,16,16))                    
                firey[n]+=.075
                firex[n]-=.03
            a=random.randint(100,120)/1000.0
            fireani[n]+=a
            if (fireani[n]>=6.0): fireani[n]=random.randint(0,100)/100.0; fire[n]=0
    for n in range(200):  #Trail Effect
        if (particlesopt==0): trail[n]=0
        #if (n%2 and particlesopt==1): trail[n]=0
        if (trail[n]>0):
            c=(255-trailsize[n])/15
            effect=dustfx.copy(); effect.fill((255,255,255,trail[n]), None, pygame.BLEND_RGBA_MULT)
            effect=pygame.transform.scale(effect,(int(8+c),int(8+c)))
            screen.blit(effect,(trailx[n]*16-camerax*16+WIDTH/2-c/2-2,traily[n]*16-cameray*16+HEIGHT/2-c/2-2))
            trail[n]=trail[n]-.5; trailsize[n]=trailsize[n]-1
            if (trail[n]<0): trail[n]=0
            if (trailsize[n]<0): trailsize[n]=0
    for n in range(90):  #Dust Effect
        if (n%2 and particlesopt<=1): dust[n]=0
        if (dust[n]<0): dust[n]=0
        if (dust[n]>0 or dustup[n]==1):
            if (dustup[n]==1): dust[n]+=15
            if (dust[n]>=255): dustup[n]=0; dust[n]=255
            c=(255-dust[n])/10
            if (dustup[n]==1): c=0
            effect=dustfx.copy(); effect.fill((255,255,255,dust[n]), None, pygame.BLEND_RGBA_MULT)
            effect=pygame.transform.scale(effect,(int(40+c),int(40+c)))
            screen.blit(effect,(dustx[n]*16-camerax*16+WIDTH/2-c/2,dusty[n]*16-cameray*16+HEIGHT/2-c/2))
            dustx[n]+=dustdx[n]*(dust[n]/255.0)*.1
            dusty[n]+=dustdy[n]*(dust[n]/255.0)*.1
            dust[n]=dust[n]*.995-.001
    for n in range(20): #Spark Effect
        if (particlesopt<=1 and n<17): spark[n]=0
        if (particlesopt==0): spark[n]=0
        if (spark[n]<0): spark[n]=0
        if (spark[n]>0):
            a=spark[n]*4; c=(spark[n])/50
            if (a>255): a=255
            if (n>16):
                effect=sparkfx.copy(); effect.fill((255,255,255,a), None, pygame.BLEND_RGBA_MULT)
                effect=pygame.transform.scale(effect,(int(5+c),int(5+c)))
                screen.blit(effect,(sparkx[n]*16-camerax*16+WIDTH/2-c/2,sparky[n]*16-cameray*16+HEIGHT/2-c/2))
            if (n<=16):
                screen.blit(scrapfx,(sparkx[n]*16-camerax*16+WIDTH/2,sparky[n]*16-cameray*16+HEIGHT/2))
            if (sparkDelay[n]<=0 and n>16):
                sparkDelay[n]=4
                if (sparkDelay[n]<1): sparkDelay[n]=1
                for nn in range(200):
                    if (trail[nn]<=0): trail[nn]=spark[n]; trailsize[nn]=255; trailx[nn]=sparkx[n]; traily[nn]=sparky[n]; break
            if (sparky[n]>1): sparkdy[n]=-sparkdy[n]*.8; sparky[n]=1
            sparkDelay[n]-=1
            sparkx[n]+=sparkdx[n]*2
            sparky[n]-=sparkdy[n]*2
            sparkdy[n]-=0.002
            spark[n]=spark[n]*.99-.001
            for nn in range(10): #Dust Building Collision
                if (building[nn]!=""):
                    if (sparky[n]>=(-buildingheight[nn]*36.0+16-8)/16+sparkdy[n]*2 and sparkx[n]>=buildingx[nn]-sparkdx[n]*2 and sparkx[n]<=buildingx[nn]+buildingwidth[nn]*38.0/16-sparkdx[n]*2):                          
                        if (sparky[n]<(-buildingheight[nn]*36.0+16-8)/16): sparky[n]=(-buildingheight[nn]*36.0+16-8)/16; sparkdy[n]=-sparkdy[n]*.8
                        if (sparkx[n]<buildingx[nn]): sparkx[n]=buildingx[nn]; sparkdx[n]=-sparkdx[n]
                        if (sparkx[n]>buildingx[nn]+buildingwidth[nn]*38.0/16): sparkx[n]=buildingx[nn]+buildingwidth[nn]*38.0/16; sparkdx[n]=-sparkdx[n]
    if (bright>0): #Bright Effect
        a=bright
        if (a>255): a=255
        effect=brightfx.copy(); effect.fill((255,255,255,a), None, pygame.BLEND_RGBA_MULT)
        c=(255-bright)
        effect=pygame.transform.scale(effect,(int(40+c),int(40+c)))
        screen.blit(effect,(brightx*16-camerax*16+WIDTH/2-c/2,brighty*16-cameray*16+HEIGHT/2-c/2))
        bright=bright-7.5
        for n in range(12): #Explosion Kills NPCs
            a=brightx-npcx[n]
            b=brighty-npcy[n]
            c=(a*a+b*b)**.5
            if (c<5):
                npcalive[n]=0; npcframe[n]=0
                if (n==camera): frame=0

def moveCamera():
    global camerax, cameray, camera, cameraback, autocamera
    global selectx, selecty
    if (cameraback>0): cameraback=cameraback-1
    if (camerax!=selectx or cameray!=selecty):
        a=camerax-selectx
        b=cameray-selecty
        c=(a*a+b*b)**.5
        if (c==0): c=.01
        aa=math.acos(a/c)
        bb=math.asin(b/c)
        camerax=camerax-math.cos(aa)*c*1.5/16
        cameray=cameray-math.sin(bb)*c*1.5/16
        if (camerax<selectx+0.03 and camerax>selectx-0.03): camerax=selectx
        if (cameray<selecty+0.03 and cameray>selecty-0.03): cameray=selecty
    if (cameraback<=0):
        selectx=npcx[camera]; selecty=npcy[camera]
        if (autocamera==1): autocamera=0
    if (cameraback>0 and autocamera==0):
        if (npcx[0]<camerax-20 or npcx[0]>camerax+20 or npcy[0]<cameray-16 or npcy[0]>cameray+16): cameraback=0
    if (selecty>0-4): selecty=0-4

def createFire(x,y,amount,nn):
    for n in range(nn*15,nn*15+int(amount)):
        if (n<75):
            if (fire[n]<=0):
                fire[n]=1
                a=random.randint(-110,70)/100.0
                b=random.randint(-75,-25)/100.0
                firex[n]=x+a
                firey[n]=y+b
            

def displayGlassShards():
    global particlesopt
    for n in range(80):
        if (particlesopt==0): glassShard[n]=0; glassBlood[n]=0
        if (glassShard[n]==1):
            if (glassBlood[n]==0): screen.blit(shard,(glassShardx[n]*16-camerax*16+WIDTH/2,glassShardy[n]-cameray*16+HEIGHT/2))
            if (glassBlood[n]==1): screen.blit(bloodpart,(glassShardx[n]*16-camerax*16+WIDTH/2,glassShardy[n]-cameray*16+HEIGHT/2))
            if (glassBlood[n]>=2):
                screen.blit(bulletspark,(glassShardx[n]*16-camerax*16+WIDTH/2,glassShardy[n]-cameray*16+HEIGHT/2))
                glassBlood[n]-=2
                if (glassBlood[n]==2): glassShard[n]=0
            glassSharddy[n]=glassSharddy[n]+.05
            glassShardx[n]+=glassSharddx[n]
            glassShardy[n]+=glassSharddy[n]
            if (glassShardy[n]+glassSharddy[n]>16):
                aa=random.randint(30,90)/100.0
                glassSharddy[n]=-glassSharddy[n]*aa; glassShardy[n]=16; glassSharddx[n]=glassSharddx[n]*.8
            if (glassShardy[n]>=16 and abs(glassSharddx[n])<.005): glassShard[n]=0
            for nn in range(10):
                if (building[nn]!=""):
                    if (glassShardx[n]>buildingx[nn] and glassShardx[n]<buildingx[nn]+buildingwidth[nn]*38.0/16):
                        b=0
                        for m in range(10):
                            if (buildingx[nn]==buildingx[m]):
                                if (glassShardy[n]<-buildingfloor1[m]*36.0+16 and glassShardy[n]>-buildingfloor1[m]*36.0-32):
                                    if (glassShardy[n]+glassSharddy[n]>-buildingfloor1[m]*36.0+13):
                                        glassSharddy[n]=-glassSharddy[n]*.5
                                        glassSharddx[n]=glassSharddx[n]*.8
                                        glassShardy[n]=-buildingfloor1[m]*36.0+13
                                        if (glassBlood[n]>=2): glassBlood[n]=0; glassShard[n]=0
                                    b=1
                                    break
                        if (b==0): glassSharddx[n]=-glassSharddx[n]
                        break

def createShards(x,y):
    amount=5; am=0; remove=0
    for n in range(80):
        if (glassShard[n]==0 or remove==1):
            glassShard[n]=1
            glassBlood[n]=0
            glassShardx[n]=x
            glassShardy[n]=y+am*6
            glassSharddx[n]=random.randint(1,100)/1000.0
            if (x<npcx[camera]): glassSharddx[n]=-glassSharddx[n]
            glassSharddy[n]=random.randint(0,50)/1000.0
            am=am+1
        if (n>=70-1): remove=1
        if (am>=amount): remove=0; break

def createSpark(x,y):
    amount=3; count=0
    for n in range(80):
        if (glassShard[n]==0):
            count+=1
            glassBlood[n]=30
            glassShard[n]=1
            glassShardx[n]=x
            glassShardy[n]=y*16
            glassSharddx[n]=random.randint(-50,50)/1000.0
            glassSharddy[n]=random.randint(-100,50)/100.0
        if (count>=amount): break

def createBlood(x,y,n):
    global bloodopt
    blood[n]=random.randint(0,3)
    bloodx[n]=x
    bloody[n]=y+random.randint(-20,-5)/100.0
    bloodtrail[n]=random.randint(0,1)
    bloodtrailx[n]=bloodx[n]+random.randint(-10,10)/100.0+.4
    bloodtraily[n]=bloody[n]+random.randint(-10,0)/100.0+.4
    amount=5; count=0
    for n in range(80):
        if (bloodopt==0): break
        if (glassShard[n]==0):
            count+=1
            glassShard[n]=1
            glassBlood[n]=1
            glassShardx[n]=x+.4
            glassShardy[n]=y*16+.2
            glassSharddx[n]=random.randint(-50,50)/1000.0
            glassSharddy[n]=random.randint(-100,50)/100.0
        if (count>=amount): break

def displayBlood():
    for n in range(12):
        if (blood[n]>=0):
            for nn in range(10):
                a=0
                if (building[nn]!="" and bloodx[n]>buildingx[nn]+.2 and bloodx[n]<buildingx[nn]+buildingwidth[nn]*38.0/16-1 and bloody[n]>-buildingheight[nn]*36.0/16): a=1
                if (a==1):
                    screen.blit(bloodimg,(bloodx[n]*16-camerax*16+WIDTH/2,bloody[n]*16-cameray*16+HEIGHT/2),(blood[n]*16,0,16,16))
                    if (bloodtrail[n]>0):
                        pygame.draw.line(screen, (255,0,0), (bloodtrailx[n]*16-camerax*16+WIDTH/2,bloodtraily[n]*16-cameray*16+HEIGHT/2),(bloodtrailx[n]*16-camerax*16+WIDTH/2,bloodtraily[n]*16-cameray*16+HEIGHT/2+bloodtrail[n]))
                        if (bloodtrail[n]<20): bloodtrail[n]+=.01

def createBullets(x1,y1,x2,y2):
    for n in range(35):
        if (bullet[n]==False):
            bullet[n]=True
            bulletx[n]=x1; bullety[n]=y1
            a=x1-x2
            b=y1-y2
            if (a==0): a=.001
            c=atan(b/a)
            a=sin(c)*1.5
            b=cos(c)*1.5
            if (x2>=x1): bulletdx[n]=b; bulletdy[n]=a
            if (x2<x1): bulletdx[n]=-b; bulletdy[n]=-a
            break
 
def displayBullets():
    global invinsible, frame, alive
    f=0
    for n in range(12):
        if (sprayBulletsDelay[n]>0): sprayBulletsDelay[n]-=1
        if (sprayBullets[n]==1 and sprayBulletsDelay[n]<=0 and alive==1): #Helicopter Bullets
            sprayBulletsDelay[n]=10
            if (n==0):
                createBullets(npcx[camera]+cos(rotation[camera])*2,npcy[camera]-sin(rotation[camera])*2,npcx[camera]+cos(rotation[camera])*2+cos(rotation[camera]),npcy[camera]-sin(rotation[camera])-sin(rotation[camera])*2)
            if (n>0):
                for nn in range(35):
                    if (bullet[nn]==0):
                        bulletenemy[nn]=2
                        break
                createBullets((copterx[n]+3.5)-cos(rotation[n])*2,(coptery[n])-sin(rotation[n])*2,(copterx[n]+3.5)-cos(rotation[n])*2-cos(rotation[n]),(coptery[n])-sin(rotation[n])-sin(rotation[n])*2)
    for n in range(35):
        if (bullet[n]==True):
            bulletx[n]+=bulletdx[n]
            bullety[n]+=bulletdy[n]
            a=bulletx[n]*16-camerax*16+WIDTH/2
            b=bullety[n]*16-cameray*16+HEIGHT/2
            if (bulletx[n]>npcx[camera]+(WIDTH/16) or bulletx[n]<npcx[camera]-(WIDTH/16)): bullet[n]=False; f=1
            if (bullety[n]<npcy[camera]-(HEIGHT/16)): bullet[n]=False; f=1
            if (bullety[n]>1): bullet[n]=False
            for nn in range(12): #Shooting Helicopters
                if (copter[nn]!=""):
                    if (bulletx[n]>copterx[nn]+2 and bulletx[n]<copterx[nn]+4 and bullety[n]>coptery[nn]-1 and bullety[n]<coptery[nn]+1):
                        bullet[n]=False
                        if (copter[nn]!="Crash"): damage[nn]=damage[nn]+5
            for nn in range(10):
                if (building[nn]=="Glass" or building[nn]=="Stone"):
                    if (bulletx[n]>=buildingx[nn]-.7 and bulletx[n]<=buildingx[nn]+buildingwidth[nn]*38.0/16+.7): #Bullet Collides with Building 
                        if (bullety[n]>=(-buildingheight[nn]*36.0+16)/16-.5): bullet[n]=False
                        if (bullety[n]<=(-buildingfloor1[nn]*36.0+16)/16 and bullety[n]>=(-buildingfloor1[nn]*36.0+16-38)/16): bullet[n]=True
                        for m in range(10):
                            if (buildingx[nn]==buildingx[m]):
                                if (bullety[n]<=(-buildingfloor1[m]*36.0+16)/16 and bullety[n]>=(-buildingfloor1[m]*36.0+16-38)/16): bullet[n]=True
                    if (building[nn]=="Glass"):
                        for m in range(buildingheight[nn]): #Breaking Glass
                            if (bullety[n]<=(-m*36.0+16)/16 and bullety[n]>=(-m*36.0+16-38)/16):
                                if (bulletx[n]>=buildingx[nn]-abs(bulletdx[n]/2) and bulletx[n]<=buildingx[nn]+abs(bulletdx[n]/2)):
                                    d=0
                                    for mm in range(10):
                                        if (buildingx[mm]==buildingx[nn] and mm!=nn):
                                            if (glassLeft[mm][m]>0): d=1; break
                                    if (glassLeft[nn][m]>0 or d==1):
                                        glassLeft[nn][m]-=25; bullet[n]=False
                                        if (glassLeft[nn][m]<=0 and d==0):
                                            for mmm in range(10):
                                                if (buildingx[nn]==buildingx[mmm]):
                                                    if (bullety[n]<=(-buildingfloor1[mmm]*36.0+16)/16 and bullety[n]>=(-buildingfloor1[mmm]*36.0+16-38)/16): bullet[n]=True; break
                                            glassLeft[nn][m]=0; createShards(buildingx[nn],-m*36.0-20)
                                            if (leveltype[level]=="Shatter"): levelvar2[level]+=1
                                if (bulletx[n]>=buildingx[nn]+buildingwidth[nn]*38.0/16-abs(bulletdx[n]/2) and bulletx[n]<=buildingx[nn]+buildingwidth[nn]*38.0/16+abs(bulletdx[n]/2)):
                                    d=0
                                    for mm in range(10):
                                        if (buildingx[mm]==buildingx[nn] and mm!=nn):
                                            if (glassRight[mm][m]>0): d=1; break
                                    if (glassRight[nn][m]>0 or d==1):
                                        glassRight[nn][m]-=25; bullet[n]=False
                                        if (glassRight[nn][m]<=0 and d==0):
                                            for mmm in range(10):
                                                if (buildingx[nn]==buildingx[mmm]):
                                                    if (bullety[n]<=(-buildingfloor1[mmm]*36.0+16)/16 and bullety[n]>=(-buildingfloor1[mmm]*36.0+16-38)/16): bullet[n]=True; break
                                            glassRight[nn][m]=0; createShards(buildingx[nn]+buildingwidth[nn]*38.0/16,-m*36.0-20); 
                                            if (leveltype[level]=="Shatter"): levelvar2[level]+=1
            for nn in range(12): #Shooting NPCs
                if (npc[nn]!="" and npcalive[nn]==1 and bullet[n]==True):
                    if (bulletx[n]>=npcx[nn]-1 and bulletx[n]<=npcx[nn]+abs(bulletdx[n])+.3 and bullety[n]>npcy[nn]-.5 and bullety[n]<npcy[nn]+1.2):
                        if ((bulletenemy[n]==0 or bulletenemy[n]==2) and nn>0): #NPC Shot
                            bullet[n]=False
                            npcalive[nn]=0; npcframe[nn]=1.9;
                            f=random.randint(0,2)
                            createBlood(npcx[nn],npcy[nn],nn)
                        if (bulletenemy[n]>=1 and npc[nn]==npc[camera] and invinsible<=0 and stance<0 and fade<100): #Player Shot
                            if (shield==1 and shootDelay[camera]<=18):
                                if (bulletx[n]>npcx[camera]+.6-bulletdx[n]*2 and shielddir==1): bullet[n]=False; 
                                if (bulletx[n]<npcx[camera]+.6-bulletdx[n] and shielddir==0): bullet[n]=False; 
                            if (bullet[n]==True):
                                bullet[n]=False
                                npcalive[nn]=0; frame=1.9
                                createBlood(npcx[nn],npcy[nn],nn)
            if (bullet[n]==True):
                pygame.draw.line(screen, WHITE, (a,b), (a-bulletdx[n]*16,b-bulletdy[n]*16))
                pygame.draw.line(screen, GOLD, (a,b), (a-bulletdx[n]*16/2,b-bulletdy[n]*16/2))
            if (bullet[n]==False):
                if (f==0): createSpark(bulletx[n],bullety[n])
                bulletenemy[n]=0

def displayRoofEntry():
    for n in range(10):
        if (building[n]=="Glass"):
            if (n==0 or buildingx[n-1]!=buildingx[n]):
                screen.blit(buildings, (buildingx[n]*16-camerax*16+WIDTH/2+roofentry[n],-36*(buildingheight[n]-1)-7-cameray*16+HEIGHT/2-20-32), (0,36,24,32)) #Display Roof Entry

def displayBuildingInterior():
    global bright, brightx, brighty, failed
    for n in range(10):
        if (building[n]=="Glass"):
            for nn in range(buildingheight[n]):
                for m in range(buildingwidth[n]): #Display Floors
                    if (m==0): a=0
                    if (m>0 and m<buildingwidth[n]): a=1
                    if (m==buildingwidth[n]-1): a=2
                    if (buildingfloor1[n]==nn): screen.blit(buildings, (buildingx[n]*16-camerax*16+WIDTH/2+38*m,-36*(nn)-cameray*16+HEIGHT/2-20), (50+38*a,0,38,36))
                if (buildingfloor1[n]==nn):
                    for m in range(5):
                        if (bomb[m]==n): #Display Exploded Bombs
                            if (bombtime[m]<=0):
                                break
                                #screen.blit(bombexploded,(buildingx[n]*16+bombx[m]-camerax*16+WIDTH/2,(-buildingfloor1[n]*36.0)-cameray*16+HEIGHT/2-18))
                    screen.blit(buildings, (buildingx[n]*16-camerax*16+WIDTH/2+buildingfloor1doorup[n],-36*(nn)-cameray*16+HEIGHT/2-4), (0,68,13,18)) #Display Door Up
                    if (buildingfloor1doordown[n]>0):
                        screen.blit(buildings, (buildingx[n]*16-camerax*16+WIDTH/2+buildingfloor1doordown[n],-36*(nn)-cameray*16+HEIGHT/2-4), (5,50,13,18)) #Display Door Up
                    for m in range(5):
                        if (bomb[m]==n): #Display Bombs
                            if (bombactive[m]==1 and bombtime[m]>0):
                                bombtime[m]-=1
                                if (bombtime[m]<=0):
                                    amount=20; a=0; failed=1
                                    bright=255; brightx=bombx[m]/16+buildingx[n]+.5; brighty=(-buildingfloor1[n]*36.0)/16-.5; #dustup[mm]=1
                                    a=npcx[camera] #Bomb Explosion Shattering Glass
                                    npcx[camera]=buildingx[n]+bombx[m]/16.0
                                    for mmm in range(10):
                                        if (buildingx[mmm]==buildingx[n]):
                                            if (glassLeft[mmm][buildingfloor1[n]]>0): glassLeft[mmm][buildingfloor1[n]]=0; createShards(buildingx[n],-buildingfloor1[n]*36.0-20)
                                            if (glassRight[mmm][buildingfloor1[n]]>0): glassRight[mmm][buildingfloor1[n]]=0; createShards(buildingx[n]+buildingwidth[n]*38.0/16,-buildingfloor1[n]*36.0-20)
                                    npcx[camera]=a
                                #Display Bomb Image and Bar
                                screen.blit(bomb1, (buildingx[n]*16+bombx[m]-camerax*16+WIDTH/2,(-buildingfloor1[n]*36.0)-cameray*16+HEIGHT/2+3))
                                pygame.draw.line(screen, (0,255,0), (buildingx[n]*16+bombx[m]-camerax*16+WIDTH/2+2,(-buildingfloor1[n]*36.0)-cameray*16+HEIGHT/2+4),  (buildingx[n]*16+bombx[m]-camerax*16+WIDTH/2+13*(bombtime[m]/bombtimemax[m])+2,(-buildingfloor1[n]*36.0)-cameray*16+HEIGHT/2+4))
                                pygame.draw.line(screen, (0,255,0), (buildingx[n]*16+bombx[m]-camerax*16+WIDTH/2+2,(-buildingfloor1[n]*36.0)-cameray*16+HEIGHT/2+5),  (buildingx[n]*16+bombx[m]-camerax*16+WIDTH/2+13*(bombtime[m]/bombtimemax[m])+2,(-buildingfloor1[n]*36.0)-cameray*16+HEIGHT/2+5))
                            if (bombactive[m]<=0):
                                screen.blit(bomb1, (buildingx[n]*16+bombx[m]-camerax*16+WIDTH/2,(-buildingfloor1[n]*36.0)-cameray*16+HEIGHT/2+3))
                                pygame.draw.line(screen, (0,100,0), (buildingx[n]*16+bombx[m]-camerax*16+WIDTH/2+2,(-buildingfloor1[n]*36.0)-cameray*16+HEIGHT/2+4),  (buildingx[n]*16+bombx[m]-camerax*16+WIDTH/2+13*(bombtime[m]/bombtimemax[m])+2,(-buildingfloor1[n]*36.0)-cameray*16+HEIGHT/2+4))
                                pygame.draw.line(screen, (0,100,0), (buildingx[n]*16+bombx[m]-camerax*16+WIDTH/2+2,(-buildingfloor1[n]*36.0)-cameray*16+HEIGHT/2+5),  (buildingx[n]*16+bombx[m]-camerax*16+WIDTH/2+13*(bombtime[m]/bombtimemax[m])+2,(-buildingfloor1[n]*36.0)-cameray*16+HEIGHT/2+5))
                            if (bombactive[m]==1 and bombtime[m]>0 and npcy[camera]<=(-buildingfloor1[n]*36.0+16)/16 and npcy[camera]>=(-buildingfloor1[n]*36.0+16)/16-2):
                                if (npcx[camera]*16.0<=buildingx[n]*16+bombx[m]+16 and npcx[camera]*16.0>=buildingx[n]*16+bombx[m]-16):
                                    bombactive[m]=0
                                    if (leveltype[level]=="Defuse"): levelvar2[level]+=1; break
                            

def displayBuildings():
    global door, camera, invinsible
    for n in range(10):
        if (building[n]=="Glass" or building[n]=="Stone"):
            if (buildingx[n]<camerax+20 and buildingx[n]>camerax-32-buildingwidth[n] and (buildingx[n]!=buildingx[n-1] or n==0)):
                for nn in range(buildingheight[n]):
                    for m in range(buildingwidth[n]): #Display Floors
                        if (m==0): a=0
                        if (m>0 and m<buildingwidth[n]): a=1
                        if (m==buildingwidth[n]-1): a=2
                        if (buildingfloor1[n]!=nn):
                            b=0
                            for mm in range(n,10):
                                if (buildingfloor1[mm]==nn and buildingx[mm]==buildingx[n]): b=1; break
                            if (b==0): screen.blit(buildings, (buildingx[n]*16-camerax*16+WIDTH/2+38*m,-36*(nn)-cameray*16+HEIGHT/2-20), (50+38*a,36,38,36))
            else: nn=buildingheight[n]-1
            if (door==1): #Enter Doors
                if (alive==1 and invinsible<=0):
                    if (npcx[camera]>=roofentry[n]/16.0+buildingx[n]-.5 and npcx[camera]<=roofentry[n]/16.0+.5+buildingx[n] and npcy[camera]==(-buildingheight[n]*36.0+16)/16-1.45):
                        npcx[camera]=buildingfloor1doorup[n]/16.0+buildingx[n]
                        npcy[camera]=((buildingfloor1[n])*-36.0)/16
                        invinsible=50
                    if (npcx[camera]>=buildingfloor1doorup[n]/16.0+buildingx[n]-.5 and npcx[camera]<=buildingfloor1doorup[n]/16.0+.5+buildingx[n] and npcy[camera]==(-buildingfloor1[n]*36.0+16+5)/16-1.45):
                        npcx[camera]=roofentry[n]/16.0+buildingx[n]+.3
                        npcy[camera]=((buildingheight[n])*-36.0)/16
                        invinsible=50
                        if (buildingx[n-1]==buildingx[n]):
                            npcx[camera]=buildingfloor1doordown[n-1]/16.0+buildingx[n]
                            npcy[camera]=((buildingfloor1[n-1])*-36.0)/16+.3                        
                    if (npcx[camera]>=buildingfloor1doordown[n]/16.0+buildingx[n]-.5 and npcx[camera]<=buildingfloor1doordown[n]/16.0+.5+buildingx[n] and npcy[camera]==(-buildingfloor1[n]*36.0+16+5)/16-1.45 and buildingfloor1doordown[n]>0):
                        npcx[camera]=buildingfloor1doorup[n+1]/16.0+buildingx[n]
                        npcy[camera]=((buildingfloor1[n+1])*-36.0)/16
                        invinsible=50
            for m in range(buildingwidth[n]): #Display Roof
                if (m==0): a=0
                if (m>0 and m<buildingwidth[n]): a=1
                if (m==buildingwidth[n]-1): a=2
                screen.blit(buildings, (buildingx[n]*16-camerax*16+WIDTH/2+38*m,-36*(nn)-7-cameray*16+HEIGHT/2-20), (50+38*a,72,38,7))
                screen.blit(buildings, (buildingx[n]*16-camerax*16+WIDTH/2+38*m,-cameray*16+HEIGHT/2+16), (50+38*a,34,38,2))
            if (building[n]=="Glass"):
                for m in range(buildingheight[n]): #Glass Windows
                    if (glassLeft[n][m]>0): screen.blit(buildings, (buildingx[n]*16-camerax*16+WIDTH/2,-36*(m+1)-cameray*16+HEIGHT/2+16), (2,0,4,36))
                    if (glassRight[n][m]>0): screen.blit(buildings, (buildingx[n]*16-camerax*16+WIDTH/2+buildingwidth[n]*38-4,-36*(m+1)-cameray*16+HEIGHT/2+16), (2,0,4,36))
            for nn in range(12):
                if (copter[nn]!=""): #Building Crashes/Rotor Touching Building
                    if (copterx[nn]+6>buildingx[n] and copterx[nn]<buildingx[n]+buildingwidth[n]*38.0/16 and coptery[nn]+1>(-buildingheight[n]*36.0+16)/16):
                        if (copterx[nn]+5>buildingx[n]): #Front Hitting Building
                            if ((abs(coptervelx[nn])>.15 or abs(rotation[nn])>1) and nn==0): copterCrash(nn); copter[nn]=""
                            if (abs(coptervelx[nn])<=.15):
                                if (copterx[nn]<buildingx[n]): copterx[nn]=buildingx[n]-5; coptervelx[nn]=-coptervelx[nn]
                        if (copterx[nn]+6>buildingx[n]): #Front Rotor Hitting Building
                            coptervelx[nn]-=.005
                        if (copterx[nn]<buildingx[n]+buildingwidth[n]*38.0/16): #Tail Hitting Building
                            if (abs(coptervelx[nn])>.15 or abs(rotation[nn])>1): copterCrash(nn); copter[nn]=""
                            if (abs(coptervelx[nn])<=.15):
                                if (copterx[nn]>buildingx[n]): copterx[nn]=buildingx[n]+buildingwidth[n]*38.0/16; coptervelx[nn]=-coptervelx[nn]
                    if (copterx[nn]+5>buildingx[n] and copterx[nn]+2<buildingx[n]+buildingwidth[n]*38.0/16 and coptery[nn]+1>=(-buildingheight[n]*36.0-7)/16):
                        if (coptery[nn]>=(-buildingheight[n]*36.0-7)/16): #Top of Buidling
                            coptery[nn]=(-buildingheight[n]*36.0-7)/16
                            if ((abs(coptervelx[nn])>.1 or abs(coptervely[nn])>.1 or abs(rotation[nn])>.7) and copter[nn]!="Crash"): #Cause Explosion
                                copterCrash(nn)   
                            else: coptervelx[nn]=coptervelx[nn]*1
                            if ((abs(rotation[nn])<.1 and abs(coptervely[nn])<.1) or copter[nn]=="Crash"):
                                rotation[nn]=0; rotationacc[nn]=0; coptervely[nn]=0; coptervelx[nn]=coptervelx[nn]*.98
                            else:
                                coptervely[nn]=-coptervely[nn]*3
                                if (rotation[nn]>0): rotationacc[nn]=-.02
                                if (rotation[nn]<0): rotationacc[nn]=.02

firesoundplay=0; coptersoundplay=0
def displayCopters():
    global enter, stance, jumpacc, velx, speed, bright, brightx, brighty, up2, down2, alive, level, firesoundplay, coptersoundplay, level
    for n in range(12):
        if (copter[n]!=""):
            if (copter[n]=="Black"): coptertype=copterblack
            if (copter[n]=="White"): coptertype=copterwhite 
            if (copter[n]=="Crash"): coptertype=coptercrash
            if (copterfire[n]>0):
                createFire(copterx[n]+3, -coptery[n]+1, copterfire[n],n)
                if (firesoundplay==0):
                    firesoundplay=1
            oldCenter=coptertype.get_size()
            copterRot=pygame.transform.rotate(coptertype,rotation[n]*57.3)
            rect=copterRot.get_rect()
            rect.center=oldCenter
            if (n>0): copterRot=pygame.transform.flip(copterRot,True,False)
            screen.blit(copterRot, (copterx[n]*16-camerax*16+WIDTH/2+rect[0]-oldCenter[0]/2,coptery[n]*16-cameray*16+HEIGHT/2-16+rect[1]-oldCenter[1]/2))

            c=blades[n]
            d=rotation[n]
            if (n==0):
                a=copterx[n]*16-camerax*16+WIDTH/2+50-cos(rotation[n]-.05)*42 #Tail Rotor
                b=coptery[n]*16-cameray*16+HEIGHT/2+sin(rotation[n]-.05)*42
                pygame.draw.line(screen, BLACK, (a-cos(c)*10,b-sin(c)*10), (a+cos(c)*10,b+sin(c)*10))
                pygame.draw.line(screen, BLACK, (a-cos(c+3.14/2)*10,b-sin(c+3.14/2)*10), (a+cos(c+3.14/2)*10,b+sin(c+3.14/2)*10))
            if (n>0):
                a=copterx[n]*16-camerax*16+WIDTH/2+50+cos(rotation[n]-.05)*42 #NPC Copter Rotors
                b=coptery[n]*16-cameray*16+HEIGHT/2+sin(rotation[n]-.05)*42
                pygame.draw.line(screen, BLACK, (a-cos(c)*10,b-sin(c)*10), (a+cos(c)*10,b+sin(c)*10))
                pygame.draw.line(screen, BLACK, (a-cos(c+3.14/2)*10,b-sin(c+3.14/2)*10), (a+cos(c+3.14/2)*10,b+sin(c+3.14/2)*10))
            if (n==0): a=copterx[n]*16-camerax*16+WIDTH/2+50-cos(rotation[n]-3.14/2-.5)*15 #Top Rotor
            if (n>0): a=copterx[n]*16-camerax*16+WIDTH/2+50+cos(rotation[n]-3.14/2-.5)*15
            b=coptery[n]*16-cameray*16+HEIGHT/2+sin(rotation[n]-3.14/2-.5)*15
            c=-rotation[n]
            ee=blades[n]
            if (ee>3.14): ee-=3.14
            e=ee
            if (e>3.14/2): e=3.14/2-(e-3.14/2)
            d=45-e*12
            if (n==0): pygame.draw.line(screen, BLACK, (a-cos(c)*d,b-sin(c)*d+1), (a+cos(c)*d,b+sin(c)*d+1))
            if (n>0): pygame.draw.line(screen, BLACK, (a-cos(-c)*d,b-sin(-c)*d+1), (a+cos(-c)*d,b+sin(-c)*d+1))
            
        if (enter==1 and copter[n]!="Crash" and alive==1 and copter[n]!=""): #Entering and Exiting Copter
            enter=0; up2=0; down2=0
            if (stance>=0): velx=coptervelx[stance]; jumpacc=-coptervely[stance]; stance=-2; npcx[camera]=copterx[n]+3.5; npcy[camera]=coptery[n]-.5
            if (stance==-1 and jumpacc==0 and npcx[camera]>copterx[n]+3 and npcx[camera]<copterx[n]+5):
                if (npcy[camera]>coptery[n]-1 and npcy[camera]<coptery[n]+2): stance=n
            if (stance==-2): stance=-1; alive=1; npcalive[0]=1
            if (jumpacc<0 and stance==n): jumpacc=0

        if (copter[n]!=""): #Copter Movement
            if (engine[n]>0): blades[n]+=engine[n]/1.5
            if (n==0):
                if (engine[n]>.3):
                    if (coptersoundplay==0): coptersoundplay=1
                if (engine[n]<=.3):
                    if (coptersoundplay==1): coptersoundplay=0
            if (blades[n]>=3.14*2): blades[n]-=3.14*2
            if (copter[n]=="Crash" and engine[n]>0): engine[n]=engine[n]-.001
            if (engine[n]<0): engine[n]=0
            rotation[n]+=rotationacc[n]
            coptervelx[n]-=(engine[n]-.5)*.12*((rotation[n])/(3.14*16))
            coptervely[n]-=(engine[n]-.5)*.06*-((abs(rotation[n])-3.14/2)/(3.14/2))
            coptervely[n]=coptervely[n]*.97+abs(rotation[n]*.005)
            if (n==0): coptervelx[n]=coptervelx[n]*.97-rotation[n]*.01
            if (n>0): coptervelx[n]=coptervelx[n]*.97+rotation[n]*.01
            rotation[n]=rotation[n]*.99
            rotationacc[n]=rotationacc[n]*.99
            coptery[n]+=coptervely[n]
            copterx[n]+=coptervelx[n]
            if (n>0 and copter[n]!="Crash"): #Enemy Copter AI
                if (engine[n]>=.4 and alive==1):
                    if (npcy[camera]<coptery[n] and engine[n]<.6): engine[n]+=enemyacc*abs(npcy[camera]-coptery[n])*.06; engine[n]+=.0003
                    if (npcy[camera]>coptery[n] and engine[n]>.4 and coptery[n]<=-4): engine[n]-=enemyacc*abs(npcy[camera]-coptery[n])*.06; engine[n]-=.0003
                    if (abs(npcy[camera]-coptery[n])<6 and coptery[n]<=-4 and copterx[n]>npcx[camera] and alive==1 and (stance>=0 or npcy[camera]<-2)):
                        if (sprayBullets[n]==0 and copterx[n]>npcx[camera] and coptery[n]<=-4): sprayBullets[n]=1 #When to Fire Bullets
                    else:
                        if (sprayBullets[n]==1): sprayBullets[n]=0
                    if (copterx[n]>npcx[camera]+1 and copterx[n]<npcx[camera]+16 and stance<0 and coptery[n]<=-2 and sprayBulletsDelay[n]<=0):
                        for nn in range(35):
                            if (bullet[nn]==0):
                                bulletenemy[nn]=2
                                break
                        if (level!=6):
                            createBullets((copterx[n]+3.5)-cos(rotation[n])*2,(coptery[n])-sin(rotation[n])*2,npcx[camera]+.4+random.randint(-10,10)/10.0,npcy[camera]+.5+random.randint(-10,10)/10.0);
                        sprayBulletsDelay[n]=25
                if (coptery[n]>-4):
                    engine[n]+=enemyacc*.5;
                    if (coptervely[n]>.2): coptery[n]-=.02
                d=0
                for nn in range(10):
                    if (building[nn]!="" and (buildingx[nn]!=buildingx[nn-1] or nn==0)):
                        if (copterx[n]<buildingx[nn]+buildingwidth[nn]*38.0/16+10 and copterx[n]>buildingx[nn]-30):
                            if (coptery[n]>-buildingheight[nn]*36.0/16):
                                if (copterx[n]>buildingx[nn]+2): rotationacc[n]=rotationacc[n]+.00004; coptery[n]-=.04*abs(rotation[n])*2; engine[n]+=.001*abs(rotation[n]); d=1
                                if (copterx[n]<buildingx[nn]+2): rotationacc[n]=rotationacc[n]-.00004; coptery[n]-=.04*abs(rotation[n])*2; engine[n]+=.001*abs(rotation[n]); d=1
                            if (coptery[n]<-buildingheight[nn]*36.0/16 and coptery[n]>-buildingheight[nn]*36.0/16-10 and copterx[n]<buildingx[nn]+buildingwidth[nn]*38.0/16+2 and copterx[n]>buildingx[nn]-5):
                                engine[n]+=.002
                        if (copterx[n]<buildingx[nn]+buildingwidth[nn]*38.0/16+30 and coptervelx[n]<-.12):
                            if (copterx[n]>buildingx[nn]+2):
                                rotationacc[n]=rotationacc[n]+.0001; coptery[n]-=.04*abs(rotation[n])*2; engine[n]+=.001*abs(rotation[n]); d=1
                if (copterx[n]<npcx[camera]+6 and d==0): rotationacc[n]=rotationacc[n]+.00006; coptery[n]-=.04*abs(rotation[n])*2; engine[n]+=.001*abs(rotation[n])
                if (copterx[n]>npcx[camera]+6 and d==0): rotationacc[n]=rotationacc[n]-.00006; coptery[n]-=.04*abs(rotation[n])*2; engine[n]+=.001*abs(rotation[n])
                if (copterx[n]>npcx[camera]+2 and copterx[n]<npcx[camera]+10): rotationacc[n]=rotationacc[n]*.98

            if (n==0): #Bumping into other Helicopters
                for nn in range(12):
                    if (nn>0):
                        if (copter[nn]!=""):
                            if (copterx[n]>copterx[nn]-4 and copterx[n]<copterx[nn]+6):
                                if (coptery[n]<coptery[nn]+2.5 and coptery[n]>coptery[nn]-2):
                                    if (copterx[n]<copterx[nn]+2):
                                        coptervelx[n]=-.1; rotationacc[n]+=.002
                                        coptervelx[nn]=.1; rotationacc[nn]-=.001
                                    if (copterx[n]>copterx[nn]+2):
                                        coptervelx[n]=.1; rotationacc[n]-=.002
                                        coptervelx[nn]=-.1; rotationacc[nn]+=.001

                    
            if (n>0 and copter[n]=="Crash"):
                engine[n]=engine[n]*.999
            a=0
            for nn in range(10):
                if (coptery[n]==(-buildingheight[nn]*36.0-7)/16+coptervely[n]): a=1
            if (coptery[n]<=0 and a==0):
                if (engine[n]>.5): engine[n]=engine[n]-.001
                if (engine[n]<.5): engine[n]=engine[n]+.001
                if (abs(rotation[n])>1 and coptervely[n]<-.1 and copter[n]!="Crash"):
                    copterCrash(n)
                if (abs(rotation[n])>6): rotation[n]=0; rotationacc[n]=0
            if (coptery[n]>0):
                coptery[n]=0
                if ((abs(coptervelx[n])>.1 or abs(coptervely[n])>.1 or abs(rotation[n])>.7) and copter[n]!="Crash" and n==0): #Cause Explosion
                    copterCrash(n)   
                else: coptervelx[n]=coptervelx[n]*1
                if ((abs(rotation[n])<.1 and abs(coptervely[n])<.1) or copter[n]=="Crash"):
                    rotation[n]=0; rotationacc[n]=0; coptervely[n]=0; coptervelx[n]=coptervelx[n]*.98
                else:
                    coptervely[n]=-coptervely[n]*3
                    if (rotation[n]>0): rotationacc[n]=-.02
                    if (rotation[n]<0): rotationacc[n]=.02                

        if (damage[n]>=100): #Helicopter Damage/Fire
            if (n>0): copterfire[n]+=.025
            if (n==0): copterfire[n]+=.018
            damage[n]=100
            if (copterfire[n]>=15):
                copterCrash(n); copter[n]=""; damage[n]=0
                if (coptery[n]>=0): copter[n]="Crash"
            
        if (stance!=n and coptery[n]<0 and n==0): #Exited in Air
            rotation[n]=rotation[n]*1.02-.001
            if (engine>0): engine[n]=engine[n]-.001
            coptervelx[n]=coptervelx[n]*.9

    if (leveltype[level]=="Helicopter" and levelvar2[level]<levelvar1[level]): #Spawn Helicopters
        a=1
        for n in range(12): #Spawn Helicopters
            if (copter[n]!="" and copter[n]!="Crash" and n>0):  a=0
        if (a==1):
            a=0
            for nn in range(12):
                if (copter[nn]==""):
                    copter[nn]="Black"
                    b=random.randint(0,1)
                    if (b==0): copterx[nn]=copterx[0]+random.randint(40,60)
                    if (b==1): copterx[nn]=copterx[0]+random.randint(-60,-40)
                    coptery[nn]=coptery[0]-10
                    damage[nn]=0; copterfire[nn]=0
                    engine[nn]=.6
                    a+=1
                if (levelvar2[level]+a>=levelvar1[level] or a>=2):
                    break


def copterCrash(n):
    global enter, stance, jumpacc, velx, speed, bright, brightx, brighty
    if (stance>-1): velx=coptervelx[n]; jumpacc=0; down2=1; up2=1; left2=1; right2=1
    copter[n]="Crash"; sprayBullets[n]=0; copterfire[n]=15
    if (n>0 and leveltype[level]=="Helicopter"): levelvar2[level]+=1
    if (stance==n): stance=-1
    engine[n]=engine[n]*.8; coptervelx[n]=coptervelx[n]*.3
    amount=30; a=0
    for nn in range(90):
        if (dust[nn]<=0 or nn>=65): #Dust, Scrap, and Trail Spawn
            bright=255; brightx=copterx[n]+2; brighty=coptery[n]-2; dustup[nn]=1
            dustx[nn]=copterx[n]+random.randint(-10,50)/10.0; dustdx[nn]=random.randint(-100,100)/1000.0
            dusty[nn]=coptery[n]-random.randint(-20,40)/10.0; dustdy[nn]=random.randint(-100,0)/2000.0
            a=a+1
            if (a>=amount): break
    a=random.randint(18,20)
    for nn in range(a):
        spark[nn]=255
        if (nn<=16):
            sparkx[nn]=copterx[n]+2; sparky[nn]=coptery[n]-random.randint(1,2)
            sparkdx[nn]=random.randint(-6*4,6*4)/400.0
            sparkdy[nn]=random.randint(6*4,10*4)/400.0
        if (nn>16):
            sparkx[nn]=copterx[n]+random.randint(2,5); sparky[nn]=coptery[n]-random.randint(1,2)
            sparkdx[nn]=random.randint(-8*4,8*4)/400.0
            sparkdy[nn]=random.randint(5*4,8*4)/400.0    

def displayNPCs():
    global frame, framechange, framedir, door, alive, firstshot, fade
    door=0
    for n in range(12):
        if (npc[n]=="Ally" and stance==-1):
            if (npcalive[n]==0 and alive==1): alive=0
            if (alive==1 or jumpacc!=0): screen.blit(tileset,(npcx[n]*16-camerax*16+WIDTH/2,npcy[n]*16-cameray*16+HEIGHT/2),(int(frame)*16,0,16,16))
            if (alive==0 and jumpacc==0): screen.blit(tileset,(npcx[n]*16-camerax*16+WIDTH/2,npcy[n]*16-cameray*16+HEIGHT/2),(int(frame)*16,16,16,16))
            if (alive==0 and frame>0): frame-=.1
        if (npc[n]=="Enemy"):
            if (npcalive[n]==1): screen.blit(tileset,(npcx[n]*16-camerax*16+WIDTH/2,npcy[n]*16-cameray*16+HEIGHT/2),(int(npcframe[n])*16,0,16,16))
            if (npcalive[n]==0 and npcx[camera]<npcx[n]): screen.blit(tileset,(npcx[n]*16-camerax*16+WIDTH/2,npcy[n]*16-cameray*16+HEIGHT/2),(int(npcframe[n])*16,16,16,16))
            if (npcalive[n]==0 and npcx[camera]>npcx[n]): screen.blit(tileset,(npcx[n]*16-camerax*16+WIDTH/2,npcy[n]*16-cameray*16+HEIGHT/2),(int(npcframe[n])*16+3*16,16,16,16))
            if (npcalive[n]==0 and npcframe[n]>0): npcframe[n]-=.1
            if (alive==1):
                d=10
                if (stance<0): d=1.5
                if (firstshot==1): d=10
                if (npcalive[n]==1 and npcy[n]>npcy[camera]-d and npcy[n]<npcy[camera]+d):
                    if (firstshot==0): d=10
                    if (firstshot==1 or stance>=0): d=30
                    if (npcx[n]<npcx[camera]-3 and npcx[camera]<npcx[n]-d): npcdx[n]+=.002
                    if (npcx[n]>npcx[camera]+4 and npcx[camera]>npcx[n]+d): npcdx[n]-=.002
                    if (shootDelay[n]<=0 and npcx[camera]>npcx[n]-d and npcx[camera]<npcx[n]+d and fade<100): #NPCs Shooting
                      f=1
                      if (npcx[camera]>npcx[n]-5 and npcx[camera]<npcx[n]+5 and npcy[camera]>npcy[n]+3): f=0
                      if (f==1):
                        for m in range(35):
                            if (bullet[m]==False):
                                bulletenemy[m]=1; break
                        if (npcx[n]<npcx[camera]+10 and npcx[n]>npcx[camera]-10): createBullets(npcx[n]+.4,npcy[n]+.5,npcx[camera]+.4+random.randint(-5,5)/10.0,npcy[camera]+.5+random.randint(-5,5)/10.0)
                        else: createBullets(npcx[n]+.4,npcy[n]+.5,npcx[camera]+.4+random.randint(-20,20)/10,npcy[camera]+.5+random.randint(-20,20)/10.0)
                        shootDelay[n]=random.randint(50,60)
            if (npcalive[n]==1): #Random NPC Movement
                if (npcy[n]<npcy[camera]-1.5 or npcy[n]>npcy[camera]+1.5 or npcx[camera]<npcx[n]-10 or npcx[camera]>npcx[n]+11):
                    if (npcmove[n]>0): npcdx[n]+=.002; npcmove[n]-=.025
                    if (npcmove[n]<0): npcdx[n]-=.002; npcmove[n]+=.025
            if (npcalive[n]!=npcaliveold[n]):
                if (leveltype[level]=="Eliminate"): levelvar2[level]+=1
                npcaliveold[n]=0
            if (npcdx[n]>.04): npcdx[n]=.04
            if (npcdx[n]<-.04): npcdx[n]=-.04
            if (npcdx[n]>0): npcdx[n]-=.0005
            if (npcdx[n]<0): npcdx[n]+=.0005
            npcx[n]+=npcdx[n]
            if (npcmove[n]<.05 and npcmove[n]>-.05): npcmove[n]=random.randint(-5,5)
            if (npcfloor[n]>=0): npcy[n]=-buildingfloor1[npcfloor[n]]*36.0/16-.1
            for nn in range(10): #Enemy Building Collision
                if (building[nn]!="" and npcfloor[n]==nn):
                    if (npcx[n]<buildingx[nn]+.5):
                        npcx[n]=buildingx[nn]+.5
                        if (npcalive[n]==1): npcframe[n]=0
                    if (npcx[n]>buildingx[nn]+buildingwidth[nn]*38.0/16-1.4):
                        npcx[n]=buildingx[nn]+buildingwidth[nn]*38.0/16-1.4
                        if (npcalive[n]==1): npcframe[n]=0
                if (building[nn]!="" and npcfloor[n]==-1):
                    if (npcx[n]>=buildingx[nn]-.8 and npcx[n]<=buildingx[nn]+buildingwidth[nn]*38.0/16+.1):
                        if (npcx[n]<buildingx[nn]+2): npcx[n]=buildingx[nn]-.81; npcframe[n]=0
                        if (npcx[n]>buildingx[nn]+2): npcx[n]=buildingx[nn]+buildingwidth[nn]*38.0/16+.11; npcframe[n]=0
            if (npcdir[n]==0 and npcalive[n]==1): npcframe[n]+=abs(npcdx[n]*4) #NPC Frame Change
            if (npcdir[n]==1 and npcalive[n]==1): npcframe[n]-=abs(npcdx[n]*4)
            if (npcframe[n]>=4.5): npcdir[n]=1
            if (npcframe[n]<=0.5): npcdir[n]=0
        if (shootDelay[n]>0):
            shootDelay[n]-=1
            
    if (alive==1): 
        framechange=framechange+abs(velx) #Player Frame Change
        if (framechange>.5):
            framechange-=.25
            frame+=framedir
        if (frame>3 and framedir==1): framedir=-1
        if (frame<1 and framedir==-1): framedir=1

def displayShield():
    global shield, shielddir, left2, right2, stance, alive, camera
    if (shield==1):
        shield=0
    if (level==8):
        shield=1
    if (shield==1 and stance<0):
        if (left2==1): shielddir=1
        if (right2==1): shielddir=0
        if (shootDelay[camera]<=18):
            if (shielddir==0): screen.blit(shieldimg,(npcx[camera]*16-camerax*16+WIDTH/2-5,npcy[camera]*16-cameray*16+HEIGHT/2-3),(20,0,20,20))
            if (shielddir==1): screen.blit(shieldimg,(npcx[camera]*16-camerax*16+WIDTH/2-1,npcy[camera]*16-cameray*16+HEIGHT/2-3),(0,0,20,20))
        else:
            screen.blit(shieldimg,(npcx[camera]*16-camerax*16+WIDTH/2-3,npcy[camera]*16-cameray*16+HEIGHT/2-3),(40,0,20,20))

def movePlayer():
    global jump, jumpacc, velx, alive, invinsible, frame
    global right2, left2, lastdir
    if (invinsible>0): invinsible-=1
    if (stance==-1): #Walking
        if (npcy[camera]>=0 or jumpacc==0):
            if (right2==1 and velx<.1): velx+=.003; lastdir=0 #Movement
            if (left2==1 and velx>-.1): velx-=.003; lastdir=1
            if (right2==0 and left2==0): velx=velx*.9
        if (alive==0): right2=0; left2=0
        a=0
        for n in range(10): #Building Collision 
            if (building[n]!=""):
                if (npcy[camera]>=(-buildingheight[n]*36.0+16)/16-1.45+jumpacc and npcx[camera]>=buildingx[n]-.8-velx and npcx[camera]<=buildingx[n]+buildingwidth[n]*38.0/16-velx):
                    if (npcy[camera]<=(-buildingheight[n]*36.0+16)/16+jumpacc):
                        if (jumpacc<-.3): alive=0; frame=0
                        npcy[camera]=(-buildingheight[n]*36.0+16)/16-1.45; jumpacc=0; a=1
                    for nn in range(buildingheight[n]):
                        if (npcy[camera]>=(-nn*36.0+16-36)/16+jumpacc and npcy[camera]<=(-nn*36.0+16)/16+jumpacc):
                            b=0
                            for m in range(10):
                                if (buildingx[m]==buildingx[n]):
                                    if (nn==buildingfloor1[m]): b=1
                            if (npcx[camera]<=buildingx[n]-.8 and (glassLeft[n][nn]>0 or b==0)): npcx[camera]=buildingx[n]-.81; velx=0
                            if (npcx[camera]>=buildingx[n]+buildingwidth[n]*38.0/16 and (glassRight[n][nn]>0 or b==0)): npcx[camera]=buildingx[n]+buildingwidth[n]*38.0/16+.01; velx=0
                    for nn in range(buildingheight[n]):
                        if (npcx[camera]>=buildingx[n]-.6-velx and npcx[camera]<=buildingx[n]+buildingwidth[n]*38.0/16-velx-.2 and npcy[camera]>=(-nn*36.0+16-36)/16+jumpacc and npcy[camera]<=(-nn*36.0+16)/16+jumpacc):
                            if (glassLeft[n][nn]>0 and npcx[camera]<buildingx[n]+.2): npcx[camera]=buildingx[n]+.2; velx=0
                            if (glassRight[n][nn]>0 and npcx[camera]>buildingx[n]+buildingwidth[n]*38.0/16-1.1): npcx[camera]=buildingx[n]+buildingwidth[n]*38.0/16-1.1; velx=0
                    if (npcy[camera]<=(-buildingfloor1[n]*36.0+16+5)/16+jumpacc and npcy[camera]>=(-buildingfloor1[n]*36.0+16+5)/16-1.45):
                        npcy[camera]=(-buildingfloor1[n]*36.0+16+5)/16-1.45; jumpacc=0; a=1
        npcx[camera]+=velx
        if (jump==1 and (npcy[camera]>=0 or a==1) and alive==1): jump=0; jumpacc=.1 #Jumping
        npcy[camera]-=jumpacc
        if (npcy[camera]>0):
            if (jumpacc<-.3): alive=0; frame=0
            jumpacc=0; npcy[camera]=0
        if (npcy[camera]<0 and a==0): jumpacc=jumpacc-.01
    if (stance>=0): #In a Helicopter
        npcx[stance]=copterx[stance]+3
        npcy[stance]=coptery[stance]
        if (velx!=0): velx=0
        if (jumpacc!=0): jumpacc=0
        a=0
        for n in range(10):
            if (coptery[stance]==(-buildingheight[n]*36.0-7)/16+coptervely[stance]): a=1
        if (coptery[stance]>=0 and a==0):
            if (up2==1 and engine[stance]<.5): engine[stance]+=copteracc
            if (down2==1 and engine[stance]>0): engine[stance]-=copteracc
        if (coptery[stance]<0 and a==0):
            if (up2==1 and engine[stance]<.6): engine[stance]+=copteracc
            if (down2==1 and engine[stance]>.4): engine[stance]-=copteracc
            if (right2==1): rotationacc[stance]-=copteracc/4
            if (left2==1): rotationacc[stance]+=copteracc/4
        if (coptery[stance]<0 or a==1):
            if (up2==1 and engine[stance]<.6): engine[stance]+=copteracc
            if (down2==1 and engine[stance]>0): engine[stance]-=copteracc            

def moveGrass():
    global grassMove, grassDir
    if (grassDir==0): grassMove=grassMove+0.1*fpsFix
    if (grassDir==1): grassMove=grassMove-0.1*fpsFix
    if (grassMove>=4.4): grassDir=1
    if (grassMove<=0.5): grassDir=0

def Selector():
    global selectx, selecty, select, cameraback, stance
    global right, left, down, up
    global mousex, mousey, mx, my
    if (right==1): selectx=selectx+.6; cameraback=1000000
    if (left==1): selectx=selectx-.6; cameraback=1000000
    if (down==1): selecty=selecty+.6; cameraback=1000000
    if (up==1): selecty=selecty-.6; cameraback=100000
    mousex=int(mx/16)
    mousey=int(my/16)

controlshow=0
def displayPaused():
    global paused, fade, up2, down2, left2, right2, spacefire, controlshow
    if (paused==1):
        if (controlshow==0):
            screen.blit(pausedimg,(WIDTH/2-100,HEIGHT/2-125))
            text=font1.render("Menu",1,WHITE)
            screen.blit(text,(WIDTH/2-25+1,HEIGHT/2-125+10-2))
            if (mx<WIDTH/2+80 and mx>WIDTH/2-80 and my>HEIGHT/2-125+40 and my<HEIGHT/2-125+65): text=font1.render("Retry",1,GOLD)
            else: text=font1.render("Retry",1,WHITE)
            screen.blit(text,(WIDTH/2-25,HEIGHT/2-125+40))
            if (mx<WIDTH/2+80 and mx>WIDTH/2-80 and my>HEIGHT/2-125+70 and my<HEIGHT/2-125+95): text=font1.render("Controls",1,GOLD)
            else: text=font1.render("Controls",1,WHITE)
            screen.blit(text,(WIDTH/2-38+2,HEIGHT/2-125+70))
            if (mx<WIDTH/2+80 and mx>WIDTH/2-80 and my>HEIGHT/2-125+100 and my<HEIGHT/2-125+125): text=font1.render("Exit",1,GOLD)
            else: text=font1.render("Exit",1,WHITE) 
            screen.blit(text,(WIDTH/2-20+2,HEIGHT/2-125+100))
        if (controlshow==1): screen.blit(keyboard,(WIDTH/2-int(445/2),HEIGHT/2-int(116/2)))
        fade=100
        up2=0; down2=0; left2=0; right2=0; spacefire=0
    if (paused==0 and controlshow==1): controlshow=0

def displayObjective():
    global objectiveText, level, mainmenu, fade, won, paused, levelprog, failed, levelselecting
    global camerax, cameray, selectx, selecty, cameraback, spacefire
    if ((alive==0 or failed==1) and won==0):
        text=font1.render("Failure",1,WHITE) 
        screen.blit(text,(WIDTH-75,HEIGHT-20))   
    if (objectiveText>0 or paused==1):
        if (objectiveText>0): objectiveText-=1
        if (paused==1): objectiveText=255
        a=objectiveText
        if (a>255): a=255
        if (leveltype[level]=="Shatter"):
            text=font1.render("Shatter "+str(levelvar1[level])+" Windows",1,(a,a,a))
            screen.blit(text,(10,HEIGHT-20))
        if (leveltype[level]=="Defuse"):
            text=font1.render("Defuse "+str(levelvar1[level])+" Bombs",1,(a,a,a))
            screen.blit(text,(10,HEIGHT-20))
        if (leveltype[level]=="Helicopter"):
            if (levelvar2[level]>=2): text=font1.render("Destroy "+str(levelvar1[level])+" Enemy Helicopters",1,(a,a,a))
            if (levelvar2[level]<=1): text=font1.render("Destroy "+str(levelvar1[level])+" Enemy Helicopter",1,(a,a,a))
            screen.blit(text,(10,HEIGHT-20))
        if (leveltype[level]=="Eliminate"):
            text=font1.render("Eliminate "+str(levelvar1[level])+" Enemies",1,(a,a,a))
            screen.blit(text,(10,HEIGHT-20))
    if (leveltype[level]!=""): #Win by Shattering Windows/Defusing Bombs/Elimination/Ect
        if (levelvar2[level]>=levelvar1[level] and alive==1 and failed==0): won=1; paused=0
    if (won==1 and objectiveText<=100):
        a=fade
        if (a>255): a=255
        a=255-a
        text=font1.render("Victory!",1,(a,a,a))
        screen.blit(text,(10,HEIGHT-20))
        fade=fade*1.02+3.01
        if (fade>=255):
            if (levelprog<=level): levelprog=levelprog+1
            save = open("Images/Progress.txt", "w") #Erases old file and writes new
            save.write(str(levelprog))
            save.close()
            camerax=0; cameray=-4; selecty=-4; selectx=0; cameraback=0; spacefire=0
            level=0; mainmenu=1; won=0; failed=0; clearLevel()
            

def displayMenu():
    global fade, camerax, cameray, arrowrightjump, arrowleftjump, levelselecting, pressedControl
    if (copter[0]!="" and mainmenu==1 and controlMenu==0): copter[0]=""; clearLevel()
    if (mainmenu!=0): #Main Menu
        camerax=0
        cameray=-4

        screen.blit(vertigologo,(WIDTH/2-250,120))
        
        text = font2.render("   v1.0 - Created by Alex Elson in Python+Pygame", 1, WHITE)
        screen.blit(text,(WIDTH-270+1,2))

        if ((mx>30 and my>365 and mx<100 and my<380) or levelselect!=0): text = font1.render("Play", 1, GOLD)
        else: text = font1.render("Play", 1, WHITE)
        screen.blit(text,(30,365-2))
        if ((mx>30 and my>390 and mx<100 and my<405) or shopselect!=0): text = font1.render("Controls", 1, GOLD)
        else: text = font1.render("Controls", 1, WHITE)
        screen.blit(text,(30,390-2))
        if ((mx>30 and my>415 and mx<100 and my<430) or optionselect!=0): text = font1.render("Options", 1, GOLD)
        else: text = font1.render("Options", 1, WHITE)
        screen.blit(text,(30,415-2))
        if ((mx>30 and my>440 and mx<100 and my<455)): text = font1.render("Quit", 1, GOLD)
        else: text = font1.render("Quit", 1, WHITE)
        screen.blit(text,(30,440-2))
        
    if (levelselect!=0): #Level Selection
        lvlname=""
        if (levelselecting==1): screen.blit(level1,(WIDTH/2-int(73/2),370)); lvlname="       Window Pain"
        if (levelselecting==2): screen.blit(level2,(WIDTH/2-int(73/2),370)); lvlname="    Harmless Defusal"
        if (levelselecting==3): screen.blit(level3,(WIDTH/2-int(73/2),370)); lvlname="         First Bogey"
        if (levelselecting==4): screen.blit(level4,(WIDTH/2-int(73/2),370)); lvlname="    Easy Elimination"
        if (levelselecting==5): screen.blit(level5,(WIDTH/2-int(73/2),370)); lvlname="     Anti-Demolition"
        if (levelselecting==6): screen.blit(level6,(WIDTH/2-int(73/2),370)); lvlname="        Drag Race"
        if (levelselecting==7): screen.blit(level7,(WIDTH/2-int(73/2),370)); lvlname="        Surrounded"
        if (levelselecting==8):
            if (bloodopt==1): screen.blit(level8,(WIDTH/2-int(73/2),370)); lvlname="         Riot Squad"
            if (bloodopt==0): screen.blit(level8b,(WIDTH/2-int(73/2),370)); lvlname="         Riot Squad"
        if (levelselecting==9): screen.blit(level9,(WIDTH/2-int(73/2),370)); lvlname="      Triple Assault"
        if (levelselecting==10): screen.blit(level10,(WIDTH/2-int(73/2),370)); lvlname="         Book Ends"
        text = font2.render(str(levelselecting), 1, WHITE) #Description Text
        screen.blit(text,(WIDTH/2-2-(len(str(levelselecting))-1)*3,355))
        text = font2.render(lvlname, 1, WHITE)
        screen.blit(text,(int(WIDTH/2-60),450))
        if (mx>WIDTH/2-45-60 and mx<WIDTH/2-45-60+45 and my>370 and my<370+73 and levelselecting>1): #Arrows
            screen.blit(arrowleft_bright,(WIDTH/2-45-60,370+arrowleftjump))
        else: screen.blit(arrowleft,(WIDTH/2-45-60,370+arrowleftjump))
        if (mx>WIDTH/2+60 and mx<WIDTH/2+60+45 and my>370 and my<370+73 and levelselecting<levelprog and levelselecting<levelmax):
            screen.blit(arrowright_bright,(WIDTH/2+60,370+arrowrightjump))
        else: screen.blit(arrowright,(WIDTH/2+60,370+arrowrightjump))
        if (arrowleftjump>0): arrowleftjump-=1
        if (arrowrightjump>0): arrowrightjump-=1
        
    if (shopselect!=0): #Shop Selection
        None 
    if (optionselect!=0): #Options Selection
        text = font2.render(" Particles", 1, WHITE)
        screen.blit(text,(300-6,355-2))
        if (particlesopt==0): a=50; b=0; c=0
        if (particlesopt==1): a=0; b=50; c=0
        if (particlesopt==2): a=0; b=0; c=50
        screen.blit(button,(300-60,367),(a,0,50,26))
        screen.blit(button,(300+50,367),(c,0,50,26))
        screen.blit(button,(300-5,367),(b,0,50,26))
        text = font2.render("Low", 1, WHITE)
        screen.blit(text,(300-60+12,367+8-2))
        text = font2.render("Med", 1, WHITE)
        screen.blit(text,(300-5+12+2,367+8-2))
        text = font2.render("High", 1, WHITE)
        screen.blit(text,(300+50+12,367+8-2))
        
        text = font2.render(" Clouds", 1, WHITE)
        screen.blit(text,(300-3,395-2))
        if (cloudsopt==0): a=0; b=50
        if (cloudsopt==1): a=50; b=0
        screen.blit(button,(300-35,407),(b,0,50,26))
        screen.blit(button,(300+20,407),(a,0,50,26))
        text = font2.render("Off", 1, WHITE)
        screen.blit(text,(300-35+15,407+8-2))
        text = font2.render("On", 1, WHITE)
        screen.blit(text,(300+20+15,407+8-2))
        
        text = font2.render(" Blood", 1, WHITE)
        screen.blit(text,(300,435-2))
        if (bloodopt==0): a=0; b=50
        if (bloodopt==1): a=50; b=0
        screen.blit(button,(300-35,447),(b,0,50,26))
        screen.blit(button,(300+20,447),(a,0,50,26))
        text = font2.render("Off", 1, WHITE)
        screen.blit(text,(300-35+15,447+8-2))
        text = font2.render("On", 1, WHITE)
        screen.blit(text,(300+20+15,447+8-2))
        
    if (fade>0 and fade<256): blackimg.set_alpha(255)
    if (fade>0): fade-=3; blackimg.set_alpha(fade); screen.blit(blackimg,(0,0))
    if (fade<0): fade=0

controlMenu = 0
pressedControl=0
def displayControls():
    global controlMenu, mainmenu, copter, copterx, coptery, stance, camerax, cameray, selectx, selecty, pressedControl
    if (pressedControl==1):
        controlMenu = 1; pressedControl=0
        mainmenu = 1
    if (controlMenu==1):
        screen.blit(keyboard,(140,350))

	
if (level==1): generateLevel(0)
mainloop=True
while mainloop:

    Clock.tick(fps)
    fpsFix=60/fps
    mx,my=pygame.mouse.get_pos()

    Selector()
    moveCamera()
    moveGrass()
    if (mainmenu==0 or controlMenu==1): movePlayer()

    displaySky()
    displayGrass()
    if (cloudsopt==1): displayClouds()
    displayRoofEntry()
    displayCopters()
    displayBuildingInterior()
    if (bloodopt==1): displayBlood()
    displayEffects()
    displayShield()
    displayBuildings()
    displayNPCs()
    displayGlassShards()
    displayBullets()
    displayGround()
    displayMenu()
    displayPaused()
    displayObjective()
    displayControls()

    for event in pygame.event.get():
        if (event.type==KEYDOWN and mainmenu==0): #Pan Camera
            if (event.key==pygame.K_RIGHT): right=1
            if (event.key==pygame.K_LEFT): left=1
            if (event.key==pygame.K_DOWN): down=1
            if (event.key==pygame.K_UP): up=1
            if (event.key==pygame.K_ESCAPE and (fade<=0 or paused==1)):
                if (cameraback<=0): paused=1-paused #Pause Menu
                if (cameraback>0): cameraback=0
        if (event.type==KEYUP and mainmenu==0): 
            if (event.key==pygame.K_RIGHT): right=0
            if (event.key==pygame.K_LEFT): left=0
            if (event.key==pygame.K_DOWN): down=0
            if (event.key==pygame.K_UP): up=0
            if (event.key==pygame.K_q): enter=1; door=1 #Enter/Exit Vehicles

        if (event.type==KEYDOWN and stance==-1 and alive==1 and paused==0):  #Move Player
            if (event.key==pygame.K_d): right2=1
            if (event.key==pygame.K_a): left2=1
            if (event.key==pygame.K_w and jump==0): jump=1
            if (event.key==pygame.K_SPACE): spacefire=1
        if (event.type==KEYUP and stance==-1 and alive==1):  #Move Player
            if (event.key==pygame.K_d): right2=0
            if (event.key==pygame.K_a): left2=0

        if (event.type==KEYDOWN and stance>=0): #Move Copter
            if (event.key==pygame.K_w): up2=1
            if (event.key==pygame.K_s): down2=1
            if (event.key==pygame.K_d): right2=1
            if (event.key==pygame.K_a): left2=1
            if (event.key==pygame.K_SPACE): spacefire=1
        if (event.type==KEYUP and stance>=0):
            if (event.key==pygame.K_w): up2=0
            if (event.key==pygame.K_s): down2=0
            if (event.key==pygame.K_d): right2=0
            if (event.key==pygame.K_a): left2=0
            if (event.key==pygame.K_SPACE): spacefire=0
        if (mainmenu==0):
            if (((event.type==pygame.MOUSEBUTTONDOWN and event.button==1) or (spacefire==1 and stance>=0)) and stance==-1 and alive==1 and paused==0 and shootDelay[camera]<=0): #Using Weapons
                if (mx<npcx[camera]*16+WIDTH/2-camerax*16 and fade<100): createBullets(npcx[camera]+1,npcy[camera]+.5,mx/16.0+camerax-WIDTH/2/16.0,my/16.0+cameray-HEIGHT/2/16.0); shootDelay[camera]=30; firstshot=1
                if (mx>npcx[camera]*16+WIDTH/2-camerax*16 and fade<100): createBullets(npcx[camera],npcy[camera]+.5,mx/16.0+camerax-WIDTH/2/16.0,my/16.0+cameray-HEIGHT/2/16.0); shootDelay[camera]=30; firstshot=1
            if (spacefire==1 and stance==-1 and shootDelay[camera]<=0 and paused==0 and alive==1):
                if (lastdir==1): spacefire=0; createBullets(npcx[camera]+1,npcy[camera]+.5,npcx[camera],npcy[camera]+.5); shootDelay[camera]=30; firstshot=1
                if (lastdir==0): spacefire=0; createBullets(npcx[camera],npcy[camera]+.5,npcx[camera]+1,npcy[camera]+.5); shootDelay[camera]=30; firstshot=1
            if (((event.type==pygame.MOUSEBUTTONDOWN and event.button==1) or spacefire==1) and stance>=0 and alive==1 and paused==0):
                sprayBullets[camera]=1
            if ((((event.type==pygame.MOUSEBUTTONUP and event.button==1) or spacefire==0) or alive==0 or stance==-1) and sprayBullets[camera]==1): firstshot=1; sprayBullets[camera]=0

        if (mainmenu!=0):
            if (event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and mx>30 and my>365 and mx<100 and my<380): #Open Level Selection
                levelselect=1; shopselect=0; optionselect=0; controlMenu=0
            if (event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and mx>30 and my>390 and mx<100 and my<405): #Open Shop Selection
                shopselect=1; levelselect=0; optionselect=0; pressedControl=1
            if (event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and mx>30 and my>415 and mx<100 and my<430): #Open Options Selection
                optionselect=1; levelselect=0; shopselect=0; controlMenu=0
            if (event.type==pygame.MOUSEBUTTONUP and event.button==1 and mx>30 and my>440 and mx<100 and my<455): #Quitting Option
                mainloop=False
            if (levelselect!=0):
                if (event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and mx>WIDTH/2-45-60 and mx<WIDTH/2-45-60+45 and my>370 and my<370+73 and levelselecting>1):
                    levelselecting-=1; arrowleftjump=5
                if (event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and mx>WIDTH/2+60 and mx<WIDTH/2+60+45 and my>370 and my<370+73 and levelselecting<levelprog and levelselecting<levelmax):
                    levelselecting+=1; arrowrightjump=5
                if (event.type==pygame.MOUSEBUTTONUP and event.button==1 and mx>WIDTH/2-int(73/2) and mx<WIDTH/2+int(73/2) and my>370 and my<370+73):
                    generateLevel(levelselecting); jumpacc=0; alive=1; stance=-1; mainmenu=0; won=0; level=levelselecting; levelselect=0; fade=255; objectiveText=455 #Start Level
            if (optionselect!=0):
                if (event.type==pygame.MOUSEBUTTONDOWN):
                    if (mx>300-35 and mx<300-35+50 and my>447 and my<447+26): bloodopt=0
                    if (mx>300+20 and mx<300+20+50 and my>447 and my<447+26): bloodopt=1
                    if (mx>300-35 and mx<300-35+50 and my>407 and my<407+26): cloudsopt=0
                    if (mx>300+20 and mx<300+20+50 and my>407 and my<407+26): cloudsopt=1
                    if (mx>300-60 and mx<300-60+50 and my>367 and my<367+26): particlesopt=0
                    if (mx>300+50 and mx<300+50+50 and my>367 and my<367+26): particlesopt=2
                    if (mx>300-5 and mx<300-5+50 and my>367 and my<367+26): particlesopt=1

        if (paused==1):
            if (event.type==pygame.MOUSEBUTTONDOWN and event.button==1): #Paused Menu Buttons
                if (mx<WIDTH/2+80 and mx>WIDTH/2-80 and my>HEIGHT/2-125+40 and my<HEIGHT/2-125+65): spacefire=0; failed=0; paused=0; fade=255; clearLevel(); generateLevel(level); alive=1; jumpacc=0
                if (mx<WIDTH/2+80 and mx>WIDTH/2-80 and my>HEIGHT/2-125+70 and my<HEIGHT/2-125+95): controlshow=1
                if (mx<WIDTH/2+80 and mx>WIDTH/2-80 and my>HEIGHT/2-125+100 and my<HEIGHT/2-125+125): jumpacc=0; spacefire=0; failed=0; camerax=0; cameray=-4; selecty=-4; selectx=0; mainmenu=1; paused=0; fade=355; clearLevel(); level=0; objectiveText=0

  
        if (event.type==QUIT): #Quitting
            mainloop=False

    pygame.display.set_caption("FPS: "+str(int(Clock.get_fps())))
    pygame.display.flip()

pygame.quit()
