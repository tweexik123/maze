#создай игру "Лабиринт"!
from pygame import *
win_width = 700
win_height = 500
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((win_width, win_height))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))
treasure = transform.scale(image.load('treasure.png'), (100, 100))

cyborg = Enemy('cyborg.png', win_width - 80, 280, 2)
hero = Player('hero.png', 2, win_height - 80, 2)
treasure = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w5 = Wall(154, 205, 50, 180, 100, 300, 10)
w6 = Wall(154, 205, 50, 550, 20, 10, 380)
w7 = Wall(154, 205, 50, 270, 175, 290, 10)
w8 = Wall(154, 205, 50, 180, 250, 300, 10)
w9 = Wall(154, 205, 50, 270, 325, 290, 10)
w10 = Wall(154, 205, 50, 270, 400, 290, 10)


game = True
finish = False
run = True
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        hero.update()
        cyborg.update()
        window.blit(background,(0, 0))
        
        cyborg.reset()
        hero.reset()
        treasure.reset()
        
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
    
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()

    if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, w7) or sprite.collide_rect(hero, w8) or sprite.collide_rect(hero, w9) or sprite.collide_rect(hero, w10):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()

    if sprite.collide_rect(hero, treasure):
        finish = True
        window.blit(win, (200, 200))
        money.play()


    display.update()
    clock.tick(FPS)