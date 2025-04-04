import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

# Ойын тұрақтылары
CELL_SIZE = 10  # Бір ұяшықтың өлшемі

# Терезе жасау
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake Game with Levels")
clock = pygame.time.Clock()

# Қаріптер
font = pygame.font.Font(None, 30)

# Түстер
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Жыланның параметрлері
snake_pos = [50, 100]
snake_body = [[50, 100], [50, 90], [50, 80]]
snake_direction = "RIGHT"
change_to = snake_direction
speed = 10  # Бастапқы жылдамдық

# Бастапқы тамақ генерациясы

def generate_food():
    while True:
        food = [random.randrange(1, 600 // CELL_SIZE) * CELL_SIZE, 
                random.randrange(1, 400 // CELL_SIZE) * CELL_SIZE]
        if food not in snake_body:  # Тамақ жыланмен қабаттасып қалмауын тексереміз
            return food

food_pos = generate_food()
game_score = 0
level = 1

isRunning = True

while isRunning:
    # Оқиғаларды өңдеу
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"

    # Жыланның қозғалысы
    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= CELL_SIZE
    elif snake_direction == "DOWN":
        snake_pos[1] += CELL_SIZE
    elif snake_direction == "LEFT":
        snake_pos[0] -= CELL_SIZE
    elif snake_direction == "RIGHT":
        snake_pos[0] += CELL_SIZE

    # Жыланның басының жаңа орнын тізімге қосу
    snake_body.insert(0, list(snake_pos))

    # Жылан тамақты жеді ме?
    if snake_pos == food_pos:
        game_score += 1
        food_pos = generate_food()
    else:
        snake_body.pop()

    # Қабырғамен соқтығысуын тексеру
    if snake_pos[0] < 0 or snake_pos[0] >= 600 or snake_pos[1] < 0 or snake_pos[1] >= 400:
        isRunning = False

    # Өзімен соқтығысуын тексеру
    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False

    # Деңгейді тексеру (әр 3 ұпай сайын)
    new_level = game_score // 3 + 1
    if new_level > level:
        level = new_level
        speed += 2  # Деңгей көтерілген сайын жылдамдық артады

    # Экранды сызу
    screen.fill(BLACK)
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    # Ұпай мен деңгейді көрсету
    score_text = font.render(f"Ұпай: {game_score}  Деңгей: {level}", True, WHITE)
    screen.blit(score_text, (20, 20))

    pygame.display.update()
    clock.tick(speed)  # Ойын жылдамдығын реттеу

# Ойын аяқталған экран
screen.fill(BLACK)
game_over_text = font.render("ОЙЫН АЯҚТАЛДЫ", True, WHITE)
game_over_rectangle = game_over_text.get_rect(center=(600 / 2, 400 / 2))
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(2000)
pygame.quit()
sys.exit()
