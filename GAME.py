import pygame 
import random 
pygame.init() 

WIDTH = 650
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

munch_sound = pygame.mixer.Sound('nom.wav')
win_sound = pygame.mixer.Sound('trumpet.mp3')                               
hero = pygame.sprite.Sprite()

hero.image = pygame.image.load('hero.png')
hero.rect = hero.image.get_rect()
hero_group = pygame.sprite.GroupSingle(hero) 

TILE_SIZE = hero.rect.width 
NUM_TILES_WIDTH = WIDTH / TILE_SIZE 
NUM_TILES_HEIGHT = HEIGHT / TILE_SIZE 

candies = pygame.sprite.OrderedUpdates()
def add_candy(candies):
    candy = pygame.sprite.Sprite()
    candy.image = pygame.image.load('candy.png')
    candy.rect = candy.image.get_rect()
    candy.rect.left = random.randint(0, NUM_TILES_WIDTH - 1) *     TILE_SIZE
    candy.rect.top = random.randint(0, NUM_TILES_HEIGHT - 1) * TILE_SIZE
    candies.add(candy)

for i in range(10):
    add_candy(candies)
pygame.time.set_timer(pygame.USEREVENT, 3000)


finish = False 
win = False

while finish != True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            finish = True 
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finish = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hero.rect.top -= TILE_SIZE
            elif event.key == pygame.K_DOWN:
                hero.rect.top += TILE_SIZE
            elif event.key == pygame.K_RIGHT:
                hero.rect.right += TILE_SIZE
            elif event.key == pygame.K_LEFT:
                hero.rect.right -= TILE_SIZE           
        if event.type == pygame.USEREVENT:
            if win == False:
                add_candy(candies)       
    screen.fill((0, 0, 0)) 
    candies.draw(screen)  
    
    collides = pygame.sprite.groupcollide(hero_group, candies, False, True)
    if len(collides) > 0:
        munch_sound.play()

    if len(candies) == 0:
        win = True
        if win:
            font = pygame.font.Font(None, 36)
            text_image = font.render("You Win!", True, (255, 255, 255))
            win_sound.play()
            text_rect = text_image.get_rect(centerx=WIDTH/2, centery=100)
            screen.blit(text_image, text_rect)
    hero_group.draw(screen) 
    pygame.display.update() 
    
    


pygame.quit() 