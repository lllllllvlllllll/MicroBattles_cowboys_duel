import pygame
from random import randint
import sys
from players_score import *
import time
pygame.init()

window_width = 867
window_height = 548

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Window')

font = pygame.font.Font('Minecraft.ttf',32)

bg = pygame.image.load('bg.png')

#print(score['BLUE'], score['RED'])

class Projectile(object):
	def __init__(self, x, y, color, vel, radius = 3):
		#pygame.sprite.Sprite.__init__(self)
		self.vel = vel
		self.x = x
		self.y = y
		self.speed = 10
		self.color = color
		self.radius = 5
		self.width = 10
		self.height = 5		
		self.rect = (self.x, self.y, self.width, self.height)
		self.random = 0
		self.double_from_stone = True

	def draw(self, window):
		#pygame.draw.rect(window, self.color, self.rect)
		pygame.draw.circle(window, self.color, (self.x,self.y), self.radius)
	def ricochet_from_cactus(self):
		self.random = randint(-5,5)
	def ricochet_from_stone(self):
		self.random = randint(-3,3)
	def slowness_from_barrel(self):
		self.speed = 5	

class Cactus(pygame.Rect):
	def __init__(self, x, y, width, height, color):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.rect = (x, y, width, height)
		self.hitbox = (0,0, 10, 40)

	def draw(self, window):
		#pygame.draw.rect(window, self.color, self.rect)
		self.hitbox = (self.x, self.y, 10, 40) #defining this var again 
		#pygame.draw.rect(window, (255,0,0), self.hitbox,2) # To draw the hit box around the cactus

class Stone(object):
	def __init__(self, x, y, width, height, color):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.rect = (x, y, width, height)
		self.hitbox = (0,0, 20, 20)

	def draw(self, window):
		#pygame.draw.rect(window, self.color, self.rect)
		self.hitbox = (self.x, self.y, 20, 20) #defining this var again 
		#pygame.draw.rect(window, (255,0,0), self.hitbox,2) # To draw the hit box around the cactus

class Barrel(object):
	def __init__(self, x, y, width, height, color):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.rect = (x, y, width, height)
		self.hitbox = (0,0, 20, 20)

	def draw(self, window):
		#pygame.draw.rect(window, self.color, self.rect)
		self.hitbox = (self.x, self.y, 20, 20) #defining this var again 
		#pygame.draw.rect(window, (255,0,0), self.hitbox,2) # To draw the hit box around the cactus


class Player(pygame.Rect):
	def __init__(self, x, y, width, height, color):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.rect = (x, y, width, height)
		self.speed = 3
		self.DIRECTION = True
		self.hitbox = (0,0, 30, 30) # NEW

	def draw(self, window):
		#pygame.draw.rect(window, self.color, self.rect)
		self.hitbox = (self.x, self.y, 30, 50) #defining this var again => moving with the player
		#pygame.draw.rect(window, (255,0,0), self.hitbox,2) # To draw the hit box around the player
	def move(self):
		#keys = pygame.key.get_pressed()

		if self.y < 70:
			self.DIRECTION = True
			self.y += self.speed
		if self.y > window_height-120:
			self.DIRECTION = False 
			self.y -= self.speed
			
		#if self.DIRECTION == True:
		#	self.DIRECTION = False
			#self.y -= self.speed
		
		#elif self.DIRECTION == False:
		#	self.DIRECTION = True
			#self.y -= self.speed

		if self.DIRECTION:
			self.y += self.speed
		elif not self.DIRECTION:
			self.y -= self.speed

		self.rect = (self.x, self.y, self.width, self.height)

	def change_dir(self):
		if self.DIRECTION == False:
			self.DIRECTION = True
		elif self.DIRECTION == True:
			self.DIRECTION = False
	def hit(self):
		print('player hit')		

class Enemy(pygame.Rect):
	def __init__(self, x, y, width, height, color):
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.rect = (x, y, width, height)
		self.speed = 3
		self.DIRECTION = True
		self.hitbox = (470,0, 30, 500) # NEW

	def draw(self, window):
		pygame.draw.rect(window, self.color, self.rect)
		self.hitbox = (self.x, self.y, 30, 50) #defining this var again => moving with the player
		pygame.draw.rect(window, (255,0,0), self.hitbox,2) # To draw the hit box around the player
	def move(self):
		#keys = pygame.key.get_pressed()

		if self.y < 70:
			self.DIRECTION = True
			self.y += self.speed
		if self.y > window_height-120:
			self.DIRECTION = False 
			self.y -= self.speed
			
		#if self.DIRECTION == True:
		#	self.DIRECTION = False
			#self.y -= self.speed
		
		#elif self.DIRECTION == False:
		#	self.DIRECTION = True
			#self.y -= self.speed

		if self.DIRECTION:
			self.y += self.speed
		elif not self.DIRECTION:
			self.y -= self.speed

		self.rect = (self.x, self.y, self.width, self.height)

	def change_dir(self):
		if self.DIRECTION == False:
			self.DIRECTION = True
		elif self.DIRECTION == True:
			self.DIRECTION = False
	def hit(self):
		print('hit')			

def show_score():
	global player1_score, player2_score, window_width, window_height, color
	
	text = font.render(f"{player1_score}  --  {player2_score}", True, color)
	text_rect = text.get_rect(center=(window_width-430, window_height-40))
	window.blit(text, text_rect)

def show_score_gameover(winner):
	global player1_score, player2_score, window_width, window_height, color
	font = pygame.font.Font('Minecraft.ttf',64)
	window.fill((0,0,0))
	text = font.render(f"{winner}   WON", True, color)
	text_rect = text.get_rect(center=(window_width-430, window_height-240))
	window.blit(text, text_rect)


def redrawWindow():		
	#window.fill((0,0,0))
	#bg_image, bg_rect = load_image('bg.png', 0,0, (window_width, window_height))
	#window.blit(bg_image, bg_rect)
	window.blit(bg, (0,0))
	show_score()
	#window.blit(bg, (0,0))
	#window.blit(cactus_img, cactus_rect)
	player.draw(window)
	player_img, player_rect = load_image('player_mb.png', player.x+20, player.y+30, (50,70))
	window.blit(player_img, player_rect)

	enemy.draw(window)
	enemy_img, enemy_rect = load_image('enemy_mb.png', enemy.x+5, enemy.y+30, (50,70))
	window.blit(enemy_img, enemy_rect)
	for cactus in cactuses:
		cactus.draw(window)
		cactus_img, cactus_rect = load_image('cactus_mb.png', cactus.x+10, cactus.y+30, (50,70))
		window.blit(cactus_img, cactus_rect)
	for stone in stones:
		stone.draw(window)	
		stone_img, stone_rect = load_image('stone_mb.png', stone.x+11, stone.y+15, (30,30))
		window.blit(stone_img, stone_rect)
		
	for barrel in barrels:
		barrel.draw(window)
		barrel_img, barrel_rect = load_image('barrel_mb.png', barrel.x+11, barrel.y+15, (30,30))
		window.blit(barrel_img, barrel_rect)
						
	for bullet in bullets:
		bullet.draw(window)
		#bullet_img, bullet_rect = load_image('barrel_mb.png', bullet.x+11, bullet.y+15, (30,30))
		#window.blit(bullet_img, bullet_rect)		
	
	pygame.display.update()

def drawCactus(window, cactus):		
	window.fill((0,0,0))
	cactus.draw(window)
	pygame.display.update()	

def collide(player, cactus):
	#if pygame.sprite.collide_rect(player, cactus):
	if player.colliderect(cactus):
		if player.x < cactus.x:
			player.x = cactus.x - 30
	elif cactus.colliderect(player):
		if cactus.x < player.x:
			player.x = cactus.x - 10
		#player.y = cactus.y

def load_image(src, x, y, obj):
	image = pygame.image.load(src).convert()
	image = pygame.transform.scale(image, obj)
	rect = image.get_rect(center=(x, y))

	transparent = image.get_at((0,0))
	image.set_colorkey(transparent)

	return image, rect

	
def gameover():
	global player1_score, player2_score, score
	if player1_score == 5:
		score["BLUE"] = 1
		return True
	elif player2_score == 5:
		return True
	elif (player1_score and player2_score) == 5:
		return True		
	return False	
#bg_img, bg = load_image('cowbows_duel.png', 0,0)
#left_player_img, left_player = load_image()

player = Player(0,0, 30,50, (200,200,200))
enemy = Player(window_width-30,0,30,50,(50,243,193))
cactuses = []
stones = []
barrels = []
bullets = []
speed = 5
color = (255,255,255)

player1_score, player2_score = 0,0

#def respawn_object(obj):
#	obj.x = randint(100,window_width-160)
#	obj.y = randint(80,window_height-100)
#	if obj.colliderect(obj) or obj.colliderect(stone) or obj.colliderect(barrel):
#		respawn_object(obj)
#	return obj.x, obj.y		
def spawn_objects():
	for i in range(randint(1,4)): #creating from 1 - 4 cactuses
		cactus = Cactus(randint(100,window_width-160), randint(80,window_height-100), 10, 40, (0,140,0))
		if cactus.colliderect(cactus) or cactus.colliderect(stone) or cactus.colliderect(barrel):
			print('cactus collided')
			#cactus.x,cactus.y = respawn_object(cactus)
		cactuses.append(cactus)
	for j in range(randint(1,3)): #creating from 1 - 3 stones
		stone = Stone(randint(120,window_width-140), randint(80,window_height-120), 20, 20, (150,150,150))
		stones.append(stone)
	for k in range(randint(1,2)): #creating from 1 - 1 barrels
		barrel = Barrel(randint(130,window_width-150), randint(80,window_height-110), 20, 20, (191, 116, 23))
		barrels.append(barrel)	
print(len(cactuses))
print(cactuses)

def MM_text():
	#global game_points

	font = pygame.font.Font('Minecraft.ttf',64)
	text = font.render(f"Main menu", True, color)
	text_rect = text.get_rect(center=(400,100))
	window.blit(text, text_rect)
	font = pygame.font.Font('Minecraft.ttf',48)
	text = font.render(f"start", True, color)
	text_rect = text.get_rect(center=(400,300))
	window.blit(text, text_rect)
	text = font.render(f"settings", True, color)
	text_rect = text.get_rect(center=(400,400))
	window.blit(text, text_rect)		

def respawn_objects():
	cactuses.clear()
	stones.clear()
	barrels.clear()
	spawn_objects()
#for cactus in cactuses:
#	cactus_img, cactus_rect = load_image('cactus_mb.png', cactus.x, cactus.y)

#def main():

#bg_main = pygame.image.load('C:/Users/Banan/Desktop/Sowtware/IT/python_projects/pygame_prj/bg2.png')
#menu = pygame.image.load("fff.png").convert()
bg_main_menu = pygame.image.load('bg_main_menu.png')
bg_main_menu = pygame.transform.scale(bg_main_menu, (window_width, window_height))
game = True
main_menu = True
run = False
gameover_menu = False

test_rect = pygame.Rect(270,250,250,100)
test_rect2 = pygame.Rect(270,350,250,100)
#bg = pygame.Surface((window_width, window_height))
#bg.fill((200,200,200))
while game:
	#global player1_score, player2_score, window_width, window_height
	keys = pygame.key.get_pressed()
	allow_to_shoot_player, allow_to_shoot_enemy = True, True
	
	stone_hit = False
	spawn_objects()
	#player = Rect(0,0,30,30)

	while main_menu:
		window.blit(bg_main_menu,(0,0))
		MM_text()
		mouse_pos = pygame.mouse.get_pos()
		#pygame.draw.rect(screen, (64, 128, 255), test_rect2, 2)
		if test_rect.collidepoint(mouse_pos):
			font= pygame.font.Font("Minecraft.ttf",48)
			text = font.render(f"start",False,(255,0,0))
			text_rect=text.get_rect(center=(400,300))
			window.blit(text, text_rect)
		if test_rect2.collidepoint(mouse_pos):
			#pygame.draw.rect(screen, (200, 200, 200), (270,350,250,100))
			font= pygame.font.Font("Minecraft.ttf",48)
			text = font.render(f"settings",False,(255,0,0))
			text_rect=text.get_rect(center=(400,400))
			window.blit(text, text_rect)
			#pygame.draw.rect(screen, (50, 50, 50), test_rect2, 5)			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				main_menu = False
				game = False
				quit()
			#if event.type == pygame.KEYDOWN:
			#	main_menu = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					main_menu = False
					run = True
		pygame.event.pump()
		pygame.display.flip()		
		pygame.display.update()

	while gameover_menu:
		window.blit(bg,(0,0))
		#MM_text()
		mouse_pos = pygame.mouse.get_pos()
		if player1_score == 5:
			show_score_gameover('BLUE')
		if player2_score == 5:
			show_score_gameover('RED')
		player1_score, player2_score = 0, 0
		#pygame.draw.rect(screen, (64, 128, 255), test_rect2, 2)			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				main_menu = False
				game = False
				quit()
			#if event.type == pygame.KEYDOWN:
			#	main_menu = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					main_menu = False
					run = True
		pygame.event.pump()
		pygame.display.flip()		
		pygame.display.update()
		time.sleep(5)
		gameover_menu = False
		main_menu = True	

	clock = pygame.time.Clock()
	while run:
		clock.tick(60) #60 FPS
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit(0)
			if event.type == pygame.KEYUP:
				#print(pygame.KEYUP)
				if event.key == pygame.K_w:
					player.change_dir()
				#controls of left player	
				if event.key == pygame.K_SPACE:
					if len(bullets) < 3 and allow_to_shoot_player:
						bullets.append(Projectile(36, player.y+15, (70,70,70), 1))
						allow_to_shoot_player = False
					if not allow_to_shoot_player:
						player.change_dir()
				#controls of right player		
				if event.key == pygame.K_UP:
					if len(bullets) < 3 and allow_to_shoot_enemy:
						bullets.append(Projectile(window_width-35, enemy.y+15, (70,70,70), -1))
						print('enemy shot')
						allow_to_shoot_enemy = False
					if not allow_to_shoot_enemy:
						enemy.change_dir()						
				if event.key == pygame.K_r:
					allow_to_shoot = True
					#print(cactus.hitbox[0],cactus.hitbox[1],cactus.hitbox[2],cactus.hitbox[3])
					#print(cactuses)
		#if both havent shot or have missed:			
		if len(bullets) == 0:
			allow_to_shoot_enemy, allow_to_shoot_player = True, True					
		for bullet in bullets:
			#if left player hits right:
			if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]: # Checks x coords
				if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
					enemy.hit()
					player1_score += 1
					bullets.pop(bullets.index(bullet))
					#bullets.clear()
					#cactuses.clear()
					#stones.clear()
					#barrels.clear()
					#spawn_objects()
					respawn_objects()
			#if right player hits left:		
			if bullet.y - bullet.radius < player.hitbox[1] + player.hitbox[3] and bullet.y + bullet.radius > player.hitbox[1]: # Checks x coords
				if bullet.x + bullet.radius > player.hitbox[0] and bullet.x - bullet.radius < player.hitbox[0] + player.hitbox[2]:
					#enemy.hit()
					player2_score += 1
					bullets.pop(bullets.index(bullet))
					#bullets.clear()
					#cactuses.clear()
					#stones.clear()
					#barrels.clear()
					respawn_objects()									
			for cactus in cactuses: #CACTUS VAR MUST BE UPDATED	
				if bullet.y - bullet.radius < cactus.hitbox[1] + cactus.hitbox[3] and bullet.y + bullet.radius > cactus.hitbox[1]: # Checks x coords
					if bullet.x + bullet.radius > cactus.hitbox[0] and bullet.x - bullet.radius < cactus.hitbox[0] + cactus.hitbox[2]:
						bullet.ricochet_from_cactus()
						#bullets.pop(bullets.index(bullet))
			if bullet.double_from_stone: #to avoid double every spawned bullet		
				for stone in stones:
					if bullet.y - bullet.radius < stone.hitbox[1] + stone.hitbox[3] and bullet.y + bullet.radius > stone.hitbox[1]: # Checks x coords
						if bullet.x + bullet.radius > stone.hitbox[0] and bullet.x - bullet.radius < stone.hitbox[0] + stone.hitbox[2]:
							#bullets.pop(bullets.index(bullet))
							tmp_vel = bullet.vel #makes second bullet for enemy player go in the right direction
							bullets.append(Projectile(bullet.x, bullet.y, (70,70,70), 1*tmp_vel)) #doubles the bullet amount on screen
							for bullet in bullets:
								bullet.double_from_stone = False
								bullet.ricochet_from_stone()
			for barrel in barrels: #BARREL VAR MUST BE UPDATED	
				if bullet.y - bullet.radius < barrel.hitbox[1] + barrel.hitbox[3] and bullet.y + bullet.radius > barrel.hitbox[1]: # Checks x coords
					if bullet.x + bullet.radius > barrel.hitbox[0] and bullet.x - bullet.radius < barrel.hitbox[0] + barrel.hitbox[2]:
						bullet.slowness_from_barrel()								
			if bullet.x > 0 and bullet.x < window_width and bullet.y > 0 and bullet.y < window_height:
				bullet.x += bullet.speed*bullet.vel
				bullet.y += bullet.random
				print(bullet.x)
			else:
				bullets.pop(bullets.index(bullet))	 			
		player.move()
		enemy.move()
		if gameover():
			#pygame.display.quit()
			run = False
			gameover_menu = True

			#return True
		#	pygame.quit()
		#	sys.exit()
		show_score()
		redrawWindow()
		pygame.event.pump()
	#else:
		#while True:
			#if player1_score == 5:
				#show_score_gameover(player1_score)
			#elif player2_score == 5:
				#show_score_gameover(player2_score)	
'''		
#main()
window_new = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Window')
clock_new = pygame.time.Clock()
score_screen = True
while score_screen:
	clock_new.tick(120) #60 FPS
	if player1_score == 5:
		show_score_gameover('BLUE')
	elif player2_score == 5:
		show_score_gameover('RED')

	pygame.event.pump()
	pygame.display.update()
	pygame.display.flip()
#player2 = Player(200,400, 30,30, (0,255,0))
'''