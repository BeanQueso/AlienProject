'''
"Survive"
Eshaan Tripathi
2/27/23
Travel the alien spaceship and reach the end by all costs.
'''

#import pygame and random functions
import pygame
import random


#create gamewall class
class gameWall(pygame.sprite.Sprite):
    #define attributes
    def __init__(self,x,y,w,l):
        #initialize sprite
        pygame.sprite.Sprite.__init__(self)
        #set surface
        self.image = pygame.Surface([w,l])
        #set colorkey
        self.image.set_colorkey((0,0,0))
        #set id
        self.id = ""
        #set rectangle attributes
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #blit blank image onto surface
        self.image.blit(pygame.image.load("blank image.jpeg"),(0,0))


#create human class
class Human(pygame.sprite.Sprite):
    #set attributes
    def __init__(self,x,y,screen):
        #set sprite
        pygame.sprite.Sprite.__init__(self)
        #create image surface
        self.image = pygame.Surface([20,20])
        #set image colorkey
        self.image.set_colorkey((0,0,0))
        
        #define rect attribute
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #set and transform character image
        characterImg = pygame.image.load("Superhero.png")
        characterImg = pygame.transform.scale(characterImg,(20,20))

        #blit character image
        self.image.blit(characterImg,(0,0))
    #define move function
    def move(self,movement):
        #all x movement is set with a normal integer, so it fits into the try statement
        try:
            movement = int(movement)
            self.rect.x+=movement
        #all y movement is a string so it would be excepted, and the 0th index of the string would be the y movement.
        except:
            if len(movement) == 2:
                movement = int(movement[0])
            else:
                movement = int(movement[0:2])

            self.rect.y+=movement
    #detect collisions
    def is_collided_with(self, sprite):
        #if collided,
        if self.rect.colliderect(sprite.rect):
            #adjust movement
            if movetype == "left":
                character.rect.x+=1
            if movetype == "right":
                character.rect.x-=1
            if movetype == "up":
                character.rect.y+=1
            if movetype == "down":
                character.rect.y-=1

#make infoblock class
class infoBlock(pygame.sprite.Sprite):
    #define attributes
    def __init__(self,x,y,id):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60,60])
        self.id = id

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        question = pygame.image.load(id).convert()
        question = pygame.transform.scale(question,(60,60))

        self.image.blit(question,(0,0))
    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

class Alien(pygame.sprite.Sprite):
    def __init__(self,screen,x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60,60])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = random.randint(1,280)
        self.direction = "forward"

        alien = pygame.image.load("alien.png").convert()
        alien = pygame.transform.scale(alien,(60,60))

        self.image.blit(alien,(0,0))


    def detect_collision(self):
        if self.rect.colliderect(border1.rect):
            return "gofor"
        elif self.rect.colliderect(border2.rect):
            return "goback"
        elif self.rect.colliderect(character.rect) and stage != "end":
            character.kill()
            pygame.quit()
                
    def move(self,screen):

        if self.detect_collision() == "goback":
            self.direction = "backward"
        elif self.detect_collision() == "gofor":
            self.direction = "forward"
            
        if self.direction == "forward":
            self.rect.x+=9
        elif self.direction == "backward":
            self.rect.x-=9






pygame.init()

screen = pygame.display.set_mode([900,800])
infoBlockGroup = pygame.sprite.Group()
gameWallGroup = pygame.sprite.Group()
topWallGroup = pygame.sprite.Group()
sideWallGroup = pygame.sprite.Group()
characterGroup = pygame.sprite.Group()
alienGroup = pygame.sprite.Group()

character = Human(40,700,screen)
characterGroup.add(character)

border1 = gameWall(0,0,10,800)
border2 = gameWall(890,0,10,800)
border3 = gameWall(0,0,900,10)
border4 = gameWall(0,790,900,10)

border1.id = "leftwall"
border2.id = "rightwall"

entryRoomWall1 = gameWall(0,350,650,50)
entryRoomWallExtension = gameWall(460,350,600,50)
entryRoomWall2 = gameWall(270,500,50,300)

oxyRoomWall1 = gameWall(570,500,50,300)

infoBlock1 = infoBlock(210,620,"question1.png")

infoBlockGroup.add(infoBlock1)

gameWallGroup.add(entryRoomWall1)
gameWallGroup.add(entryRoomWallExtension)
gameWallGroup.add(entryRoomWall2)
gameWallGroup.add(oxyRoomWall1)

gameWallGroup.add(border1)
gameWallGroup.add(border2)
gameWallGroup.add(border3)
gameWallGroup.add(border4)




movement = 0
movetype = ""

pygame.display.set_caption("Survive")
done = False
clock = pygame.time.Clock()
screenimg = pygame.image.load("bg.png")
set_ticks = 0

stage = "start"

font = pygame.font.Font(None,36)

startBlockHit = False
oxyBlockHit = False
weaponBlockHit = False

showGunMouse = False

mouse = pygame.transform.scale(pygame.image.load("mouse.png").convert(),(20,20))
mouse.set_colorkey((0,0,0))

def spawnAlien(screen):
    global alien
    alien1 = Alien(screen,30)
    alien2 = Alien(screen,40)
    alienGroup.add(alien1)
    alienGroup.add(alien2)

while done == False:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done == True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movetype = "left"
                movement = -1
                if character.rect.x == 0:
                    movement = 0
            if event.key == pygame.K_RIGHT:
                movetype = "right"
                movement = 1
                if character.rect.x == 890:
                    movement = 0
            if event.key == pygame.K_UP:
                movetype = "up"
                movement = "-1b"
                if character.rect.y == 10:
                    movement = 0
            if event.key == pygame.K_DOWN:
                movetype = "down"
                movement = "1b"
                if character.rect.y == 770:
                    movement = 0
                
        if event.type == pygame.KEYUP:
            movement = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if stage == "breakout":
                pos = pygame.mouse.get_pos()
                for alien in alienGroup.sprites():
                    if pos[0] > alien.rect.x-60 and pos[0] < alien.rect.x+60:
                        if pos[1] > alien.rect.y-60 and pos[1] < alien.rect.y+60:
                            alien.kill()
                            spawnAlien(screen)

    wallCollisions = pygame.sprite.groupcollide(gameWallGroup,characterGroup,False,False)
    if len(wallCollisions) > 0:
        movement = 0
        if movetype == "left":
            character.rect.x+=1
        if movetype == "right":
            character.rect.x-=1
        if movetype == "up":
            character.rect.y+=1
        if movetype == "down":
            character.rect.y-=1
        
    wallCollisions = 0

    infoBlockId = ""

    for eachInfoBlock in infoBlockGroup:
        if eachInfoBlock.is_collided_with(character):
            infoBlockId = eachInfoBlock.id
            if eachInfoBlock.id == "question1.png":
                current_ticks = pygame.time.get_ticks()
                set_ticks = current_ticks + 6000
                if movetype == "left":
                    character.rect.x+=1
                if movetype == "right":
                    character.rect.x-=1
                if movetype == "up":
                    character.rect.y+=1
                if movetype == "down":
                    character.rect.y-=1

                if startBlockHit == False:
                    infoImage = pygame.image.load("info1.png").convert()
                    stage = "oxygen"
                    oxytimer = 1200
                    startBlockHit = True
                    infoBlock2 = infoBlock(510,620,"oxyvent.png")
                    infoBlockGroup.add(infoBlock2)
                    infoImage = pygame.transform.scale(infoImage,(320,320))



            if eachInfoBlock.id == "oxyvent.png":
                current_ticks = pygame.time.get_ticks()
                set_ticks = current_ticks + 6000
                if movetype == "left":
                    character.rect.x+=1
                if movetype == "right":
                    character.rect.x-=1
                if movetype == "up":
                    character.rect.y+=1
                if movetype == "down":
                    character.rect.y-=1

                if oxyBlockHit == False:
                    infoImage = pygame.image.load("info2.png").convert()
                    stage = "weapon"
                    weapontimer = 1200
                    oxyBlockHit = True

                    infoBlock3 = infoBlock(720,620,"gun.png")
                    infoBlockGroup.add(infoBlock3)
                    
                    infoImage = pygame.transform.scale(infoImage,(320,320))
                    


            if eachInfoBlock.id == "gun.png":
                current_ticks = pygame.time.get_ticks()
                set_ticks = current_ticks + 9000
                if movetype == "left":
                    character.rect.x+=1
                if movetype == "right":
                    character.rect.x-=1
                if movetype == "up":
                    character.rect.y+=1
                if movetype == "down":
                    character.rect.y-=1
                
                if weaponBlockHit == False:
                    infoImage = pygame.image.load("info3.png").convert()
                    pygame.mouse.set_visible(False)
                    showGunMouse = True
                    stage = "breakout"
                    breakouttimer = 6000
                    weaponBlockHit = True
                    entryRoomWallExtension.kill()
                    infoBlock4 = infoBlock(390,10,"vent.png")
                    infoBlockGroup.add(infoBlock4)

                    infoImage = pygame.transform.scale(infoImage,(320,320))
                    spawnAlien(screen)

            if eachInfoBlock.id == "vent.png":
                stage = "end"
                '''infoBlockGroup = pygame.sprite.Group()
                gameWallGroup = pygame.sprite.Group()
                topWallGroup = pygame.sprite.Group()
                sideWallGroup = pygame.sprite.Group()
                characterGroup = pygame.sprite.Group()
                alienGroup = pygame.sprite.Group()'''

                groups = [infoBlockGroup,gameWallGroup,topWallGroup,sideWallGroup,characterGroup,alienGroup]
                for i in groups:
                    for x in i.sprites():
                        x.kill()

    
            
    
    character.move(movement)

    screen.blit(screenimg,[0,0])
    if set_ticks > pygame.time.get_ticks():
        screen.blit(infoImage,[250,15])

    if stage == "oxygen":
        if oxyBlockHit == False:
            oxytimer-=1
            try:
                textImg = font.render(str(oxytimer),1,(255,255,255))
                if oxytimer < 300:
                    textImg = font.render(str(oxytimer),1,(255,0,0))
                screen.blit(textImg,(20,10))
            except:
                pass
            if oxytimer == 0:
                pygame.quit()

    if stage == "weapon":
        if weaponBlockHit == False:
            weapontimer-=1
            try:
                textImg = font.render(str(weapontimer),1,(255,255,255))
                if weapontimer < 300:
                    textImg = font.render(str(weapontimer),1,(255,0,0))
                screen.blit(textImg,(20,10))
            except:
                pass
            if weapontimer == 0:
                pygame.quit()
    if stage == "breakout":
        for alien in alienGroup.sprites():
            alien.move(screen)

    if stage == "end":
        endImg = pygame.image.load("end.png").convert()
        endImg = pygame.transform.scale(endImg,(800,800))
        screen.blit(endImg,(50,0))
   
    characterGroup.draw(screen)
    gameWallGroup.draw(screen)
    infoBlockGroup.draw(screen)
    alienGroup.draw(screen)
    if showGunMouse == True:
        screen.blit(mouse,(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]))

    pygame.display.flip()
    clock.tick(100)