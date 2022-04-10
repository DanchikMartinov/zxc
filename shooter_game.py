import pygame
from pygame import *
from random import randint
from sys import *
#С„РѕРЅРѕРІР°СЏ РјСѓР·С‹РєР°
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
font.init()
#С€СЂРёС„С‚С‹ Рё РЅР°РґРїРёСЃРё
font1 = font.Font(None, 80)
win = font1.render('You win! ', True, (255,255,255))
lose = font1.render('You loser! ', True, (180,0,0))

font2 = font.SysFont(None, 36)
#РЅР°Рј РЅСѓР¶РЅС‹ С‚Р°РєРёРµ РєР°СЂС‚РёРЅРєРё:
img_back = "galaxy.jpg" # С„РѕРЅ РёРіСЂС‹
img_hero = "rocket.png" # РіРµСЂРѕР№
img_enemy = "ufo.png" # РІСЂР°Рі
img_bullet = "bullet.png"

goal = 100
score = 0 #СЃР±РёС‚Рѕ РєРѕСЂР°Р±Р»РµР№
lost = 0 #РїСЂРѕРїСѓС‰РµРЅРѕ РєРѕСЂР°Р±Р»РµР№
max_lost = 3
bullets = sprite.Group()
#РєР»Р°СЃСЃ-СЂРѕРґРёС‚РµР»СЊ РґР»СЏ РґСЂСѓРіРёС… СЃРїСЂР°Р№С‚РѕРІ
class GameSprite(sprite.Sprite):
 #РєРѕРЅСЃС‚СЂСѓРєС‚РѕСЂ РєР»Р°СЃСЃР°
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Р’С‹Р·С‹РІР°РµРј РєРѕРЅСЃС‚СЂСѓРєС‚РѕСЂ РєР»Р°СЃСЃР° (Sprite):
       sprite.Sprite.__init__(self)
 
       #РєР°Р¶РґС‹Р№ СЃРїСЂР°Р№С‚ РґРѕР»Р¶РµРЅ С…СЂР°РЅРёС‚СЊ СЃРІРѕР№СЃС‚РІРѕ image - РёР·РѕР±СЂР°Р¶РµРЅРёРµ
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #РєР°Р¶РґС‹Р№ СЃРїСЂР°Р№С‚ РґРѕР»Р¶РµРЅ С…СЂР°РЅРёС‚СЊ СЃРІРѕР№СЃС‚РІРѕ rect - РїСЂСЏРјРѕСѓРіРѕР»СЊРЅРёРє, РІ РєРѕС‚РѕСЂС‹Р№ РѕРЅ РІРїРёСЃР°РЅ
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #РјРµС‚РѕРґ, РѕС‚СЂРёСЃРѕРІС‹РІР°СЋС‰РёР№ РіРµСЂРѕСЏ РЅР° РѕРєРЅРµ
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
#РєР»Р°СЃСЃ РіР»Р°РІРЅРѕРіРѕ РёРіСЂРѕРєР°
class Player(GameSprite):
   #РјРµС‚РѕРґ РґР»СЏ СѓРїСЂР°РІР»РµРЅРёСЏ СЃРїСЂР°Р№С‚РѕРј СЃС‚СЂРµР»РєР°РјРё РєР»Р°РІРёР°С‚СѓСЂС‹
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
 #РјРµС‚РѕРґ "РІС‹СЃС‚СЂРµР»" (РёСЃРїРѕР»СЊР·СѓРµРј РјРµСЃС‚Рѕ РёРіСЂРѕРєР°, С‡С‚РѕР±С‹ СЃРѕР·РґР°С‚СЊ С‚Р°Рј РїСѓР»СЋ)
   def fire(self):
       bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15,20, -15)
       bullets.add(bullet)
 
#РєР»Р°СЃСЃ СЃРїСЂР°Р№С‚Р°-РІСЂР°РіР°  
class Enemy(GameSprite):
   #РґРІРёР¶РµРЅРёРµ РІСЂР°РіР°
   def update(self):
       self.rect.y += self.speed
       global lost
       #РёСЃС‡РµР·Р°РµС‚, РµСЃР»Рё РґРѕР№РґРµС‚ РґРѕ РєСЂР°СЏ СЌРєСЂР°РЅР°
       if self.rect.y > win_height:
           self.rect.x = randint(80, win_width - 80)
           self.rect.y - 0
           lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


#РЎРѕР·РґР°С‘Рј РѕРєРѕС€РєРѕ
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
 
#СЃРѕР·РґР°С‘Рј СЃРїСЂР°Р№С‚С‹
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
 
monsters = sprite.Group()
for i in range(1, 6):
   monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
   monsters.add(monster)
 
#РїРµСЂРµРјРµРЅРЅР°СЏ "РёРіСЂР° Р·Р°РєРѕРЅС‡РёР»Р°СЃСЊ": РєР°Рє С‚РѕР»СЊРєРѕ С‚Р°Рј True, РІ РѕСЃРЅРѕРІРЅРѕРј С†РёРєР»Рµ РїРµСЂРµСЃС‚Р°СЋС‚ СЂР°Р±РѕС‚Р°С‚СЊ СЃРїСЂР°Р№С‚С‹
finish = False
#РћСЃРЅРѕРІРЅРѕР№ С†РёРєР» РёРіСЂС‹:
run = True #С„Р»Р°Рі СЃР±СЂР°СЃС‹РІР°РµС‚СЃСЏ РєРЅРѕРїРєРѕР№ Р·Р°РєСЂС‹С‚РёСЏ РѕРєРЅР°
while run:
   #СЃРѕР±С‹С‚РёРµ РЅР°Р¶Р°С‚РёСЏ РЅР° РєРЅРѕРїРєСѓ вЂњР—Р°РєСЂС‹С‚СЊвЂќ
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
                fire_sound.play()  
    if not finish:
        #РѕР±РЅРѕРІР»СЏРµРј С„РѕРЅ
        window.blit(background,(0,0))
        #РїСЂРѕРёР·РІРѕРґРёРј РґРІРёР¶РµРЅРёСЏ СЃРїСЂР°Р№С‚РѕРІ
        ship.update()
        monsters.update()
        bullets.update()  
        #РѕР±РЅРѕРІР»СЏРµРј РёС… РІ РЅРѕРІРѕРј РјРµСЃС‚РѕРїРѕР»РѕР¶РµРЅРёРё РїСЂРё РєР°Р¶РґРѕР№ РёС‚РµСЂР°С†РёРё С†РёРєР»Р°
        ship.reset()
        monsters.draw(window)
        bullets.draw(window) 
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200,200))
        
        if score >= 100:
            finish = True
            window.blit(win, (200,200))
         #РїРёС€РµРј С‚РµРєСЃС‚ РЅР° СЌРєСЂР°РЅРµ
        text = font2.render("Счёт: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        text_lose = font2.render("пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        display.update()
    #С†РёРєР» СЃСЂР°Р±Р°С‚С‹РІР°РµС‚ РєР°Р¶РґСѓСЋ 0.05 СЃРµРєСѓРЅРґ
    time.delay(50)
