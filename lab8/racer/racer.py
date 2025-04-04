import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# FPS (секундына кадрлар саны)
FPS = 60
FramePerSec = pygame.time.Clock()

# Түстер
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ойын экранының өлшемдері
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Бастапқы жылдамдық және ұпайлар
SPEED = 3
SCORE = 0
COINS = 0

# Қаріптер және ойын соңындағы хабарлама
font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Фондық суретті жүктеу
background = pygame.image.load(r"C:\Users\erbol\OneDrive - АО Казахстанско-Британский Технический Университет\Жұмыс үстелі\PythonLabs\Labs\lab8\racer\AnimatedStreet.png")

# Ойын терезесін құру
screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)
pygame.display.set_caption("Racer")

# Жаудың (машинаның) класы
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\erbol\OneDrive - АО Казахстанско-Британский Технический Университет\Жұмыс үстелі\PythonLabs\Labs\lab8\racer\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Жаудың қозғалысы
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):  # Егер жау экранның төменгі жағына жетсе
            SCORE += 1  # Ұпай қосылады
            self.rect.top = 0  # Жаңа жау жоғарыдан қайта басталады
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Монеталардың класы
c1, c2, c3, c4, c5 = False, False, False, False, False
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\erbol\OneDrive - АО Казахстанско-Британский Технический Университет\Жұмыс үстелі\PythonLabs\Labs\lab8\racer\coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

    # Монетаны жинау және жылдамдықты арттыру
    def move(self):
        global COINS

        COINS += 1

        # Монета жаңа орынға ауыстырылады
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

# Ойыншының (машинаның) класы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\erbol\OneDrive - АО Казахстанско-Британский Технический Университет\Жұмыс үстелі\PythonLabs\Labs\lab8\racer\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (210, 520)

    # Ойыншының қозғалысы
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:  # Солға қозғалу
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:  # Оңға қозғалу
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.top > 0:  # Жоғарыға қозғалу
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:  # Төменге қозғалу
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)

# Объектілерді құру
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Спрайттар топтары
enemies = pygame.sprite.Group()
enemies.add(E1)
coinss = pygame.sprite.Group()
coinss.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Жылдамдықты арттыру оқиғасы
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Ойын аяқталған кездегі экран
def game_over_screen():
    screen.fill(RED)
    screen.blit(game_over, (30, 250))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return True  # Ойынды қайта бастау
                elif event.key == K_ESCAPE:
                    return False  # Ойынды жабу

# Апат болған жағдайда
def handle_crash():
    time.sleep(2)

# Фон қозғалысы үшін айнымалы
background_y = 0 

# Ойынның негізгі циклі
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1  # Уақыт өте келе жылдамдық артады
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Егер ойыншы жаумен соқтығысса
    if pygame.sprite.spritecollideany(P1, enemies):
        continue_game = handle_crash()
        if not continue_game:
            pygame.quit()
            sys.exit()

    # Фонды жылжыту
    background_y = (background_y + SPEED) % background.get_height()
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    # Ұпай мен монеталарды көрсету
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))

    coins = font_small.render(str(COINS), True, BLACK)
    screen.blit(coins, (370, 10))

    # Барлық объектілерді көрсету және жылжыту
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

        if entity == C1:
            if pygame.sprite.spritecollideany(P1, coinss):
                entity.move()
        else:
            entity.move()

    # Монеталарды төмен жылжыту
    for coin in coinss:
        coin.rect.y += SPEED

        if coin.rect.top > SCREEN_HEIGHT:
            coin.rect.y = -coin.rect.height
            coin.rect.x = random.randint(40, SCREEN_WIDTH - 40)

    pygame.display.update()
    FramePerSec.tick(FPS)
