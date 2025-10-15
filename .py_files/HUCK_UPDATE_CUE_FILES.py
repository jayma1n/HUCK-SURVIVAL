import pygame
import random as rm
import os, os.path
import math
import time
from classes import Survivor
from classes import Companion
from classes import Enemy
from classes import Mouse_hit_box
from perlin_noise import PerlinNoise
pygame.init()
# initializing variables and setting up the screen
global block_size
block_size = 20
WHITE = (255, 255, 255)
GREEN = (94, 157, 52)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
YELLOW = (225, 190, 128)
caption = "HUCK SURVIVAL"
size = [1000,840]
pointsx = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,
          210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,
          390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,
          570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,
          750,760,770,780,790,800,810,820,830,840,850,860,870,880,890,900,910,920,
          930,940,950,960,970,980,990,1000,1010,1020,1030,1040,1050,1060,1070,1080,
          1090,1100,1110,1120,1130,1140,1150,1160,1170,1180,1190,1200,1210,1220,1230,
          1240,1250,1260,1270,1280,1290,1300,1310,1320,1330,1340,1350,1360,1370,1380,
          1390,1400,1410,1420,1430,1440,1450,1460,1470,1480,1490,1500,1510,1520,1530,
          1540,1550,1560,1570,1580,1590,1600]
pointsy = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,
            210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,
            390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,
            570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,
            750,760,770,780,790,800]

screen = pygame.display.set_mode( size , pygame.RESIZABLE)
pygame.display.set_caption(caption)
Clock = pygame.time.Clock()
height = size[1]
width = size[0]
seed = rm.randint(0, 10000000000)
player_sprites = pygame.sprite.Group()
Companion_sprites = pygame.sprite.Group()
Player_Char = Survivor(rm.choice(pointsx), rm.choice(pointsy))
Dog = Companion(rm.choice(pointsx), rm.choice(pointsy))
enemy = Enemy(rm.choice(pointsx), rm.choice(pointsy))
starting_health = 100
player_sprites.add(Player_Char)
Companion_sprites.add(Dog)
enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(enemy)
tile = pygame.image.load(os.path.join("assets", "tile.png"))
tile_scaled = pygame.transform.scale(tile, (block_size,block_size))
sand_tile = pygame.image.load(os.path.join("assets", "sand tile.png"))
sand_tile_rotated = pygame.transform.rotate(sand_tile, 90)
sand_tile_scaled = pygame.transform.scale(sand_tile_rotated, (block_size,block_size))

water_tile = pygame.image.load(os.path.join("assets", "water tile.png"))
water_tile_scaled = pygame.transform.scale(water_tile, (block_size,block_size))
mouse_box = Mouse_hit_box()

def mouse_circle():
    # Define the area around the player within which the mouse can move
    area_radius = 50  # Radius of the allowed area around the player

    player_center_x = Player_Char.rect.centerx
    player_center_y = Player_Char.rect.centery

    mouse_pos = pygame.mouse.get_pos()
    mouse_x, mouse_y = mouse_pos
    distance_x = mouse_x - player_center_x
    distance_y = mouse_y - player_center_y
    angle = math.atan2(distance_y, distance_x)
    x = player_center_x + area_radius * math.cos(angle)
    y = player_center_y + area_radius * math.sin(angle)

    mouse_pos = pygame.mouse.get_pos()
    mouse_x, mouse_y = mouse_pos

    # Calculate the distance from the player center to the mouse position
    distance_x = mouse_x - player_center_x
    distance_y = mouse_y - player_center_y

    # Clamp the mouse position within the defined radius around the player
    if distance_x**2 + distance_y**2 > area_radius**2:
        angle = math.atan2(distance_y, distance_x)
        x = player_center_x + area_radius * math.cos(angle)
        y = player_center_y + area_radius * math.sin(angle)
    else:
        mouse_x = mouse_x
        mouse_y = mouse_y
    pygame.mouse.set_visible(False)

    mouse_hit = pygame.draw.circle(screen, RED, (int(x), int(y)), 10)
    if enemy.rect.collidepoint((int(x), int(y))) and pygame.mouse.get_pressed()[0]:
        enemy.rect.x = rm.choice(pointsx)
        enemy.rect.y = rm.choice(pointsy)

    #pygame.mouse.set_visible(False)

mouse_sprites = pygame.sprite.Group()
mouse_sprites.add(mouse_box)
player_image_path = os.path.join("assets", "HUCK.png")
player_image = pygame.image.load(player_image_path)
player_scaled = pygame.transform.scale(player_image, (40, 60))
enemy_image_path = os.path.join("assets", "zomboid.png")
enemy_image = pygame.image.load(enemy_image_path)
enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(enemy)
companion_image_path = os.path.join("assets", "HUCK_DOG.png")
companion_image = pygame.image.load(companion_image_path)
companion_scaled = pygame.transform.scale(companion_image, (60, 40))
companion_scaled_flip = pygame.transform.flip(companion_scaled, True, False)

def player_chase():
    if Player_Char.rect.x + 50 < Dog.rect.x:
        Dog.rect.x -= 5
    elif Player_Char.rect.x + 50 > Dog.rect.x:
        Dog.rect.x += 5
    if Player_Char.rect.y < Dog.rect.y:
        Dog.rect.y -= 5
    elif Player_Char.rect.y > Dog.rect.y:
        Dog.rect.y += 5
def enemy_player_chase():
    if Player_Char.rect.x < enemy.rect.x:
        enemy.rect.x -= 5
    elif Player_Char.rect.x > enemy.rect.x:
        enemy.rect.x += 5
    if Player_Char.rect.y < enemy.rect.y:
        enemy.rect.y -= 5
    elif Player_Char.rect.y > enemy.rect.y:
        enemy.rect.y += 5
global noise     
noise = PerlinNoise(octaves = 1.5, seed = seed)

    #sprite_colide_list = pygame.sprite.spritecollide(mouse_sprites, enemy_sprites, False)
    
def proc_gen():
    # generating the map
    global map_list
    map_list = []
    
    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            n = noise([x / width, y / height])
            g = int((n + 1) / 2 * 255)  # Scale noise value to 0-255
            if n < 0:
                g = GREEN
            elif n < 0.0084:
                g = YELLOW
                screen.blit(sand_tile_scaled, (x, y))
            if g == GREEN:
                screen.blit(tile_scaled, (x, y))
            elif n > 0.0084:
                screen.blit(water_tile_scaled, (x, y))

current_health = starting_health

def coliding():
    sprite_colide_list = pygame.sprite.spritecollide(Player_Char, enemy_sprites, False)
    for sprite in sprite_colide_list:
        return True


def health_bar():
    font = pygame.font.SysFont(None, 200)
    global current_health
    
    if coliding() == True:
        current_health = current_health - 1
    if current_health <= -1:
        render_font = font.render("Game Over", False, (0,0,0))
        screen.blit(render_font, (width/2 - 400,height/2-100))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
    pygame.draw.rect(screen, GRAY, (0, 0, 120, 40))
    
    player_health = pygame.draw.rect(screen, GREEN, (10, 10, current_health, 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Game Over")
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        Player_Char.rect.x -= 10
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        Player_Char.rect.x += 10
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        Player_Char.rect.y -= 10
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        Player_Char.rect.y += 10
    Clock.tick(1000)
      # Clear the screen before drawing the new map
    player_chase()
    proc_gen()
    coliding()
    health_bar()
    enemy_player_chase()
    mouse_circle()
    screen.blit(player_scaled,(Player_Char.rect.x, Player_Char.rect.y))
    screen.blit(enemy_image, (enemy.rect.x, enemy.rect.y))
    if Player_Char.rect.x < Dog.rect.x:
        screen.blit(companion_scaled, (Dog.rect.x, Dog.rect.y))
    else:
        screen.blit(companion_scaled_flip, (Dog.rect.x, Dog.rect.y))    
    pygame.display.update()
    pygame.display.flip()
    size = screen.get_size()
    mouse_sprites.update()
    mouse_sprites.draw(screen)
    height = size[1]
    width = size[0] 
