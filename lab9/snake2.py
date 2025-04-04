import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

# Ойынның константалары
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 10  # Бір клетканың өлшемі

# Терезе құру
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")
clock = pygame.time.Clock()

# Шрифттер
font = pygame.font.Font(None, 30)

# Түстер
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Змейканың параметрлері
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
speed = 10  # Бастапқы жылдамдық

game_score = 0
level = 1

# Әр түрлі салмағы бар азық-түлік тізімі
food_items = []

# Азықтың ең жоғары салмағы бар уақыт计
FOOD_LIFETIME = 5000  # Азықтың өмір сүру уақыты (миллисекундпен)
last_food_spawn_time = pygame.time.get_ticks()

# Азық генерациялау функциясы
def generate_food():
    while True:
        food = {
            "pos": [random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE,
                     random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE],
            "weight": random.randint(1, 3),  # Азықтың салмағы (1, 2 немесе 3 ұпай)
            "spawn_time": pygame.time.get_ticks()
        }
        if food["pos"] not in [f["pos"] for f in food_items] and food["pos"] not in snake_body:
            food_items.append(food)
            break

# Алғашқы азықты генерациялау
generate_food()

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)  # Әрбір секунд сайын азық тексеріледі

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
        elif event.type == timer_event:
            current_time = pygame.time.get_ticks()
            food_items = [food for food in food_items if food["weight"] < 3 or current_time - food["spawn_time"] < FOOD_LIFETIME]
            if len(food_items) == 0:
                generate_food()

    # Змейканың қозғалысы
    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= CELL_SIZE
    elif snake_direction == "DOWN":
        snake_pos[1] += CELL_SIZE
    elif snake_direction == "LEFT":
        snake_pos[0] -= CELL_SIZE
    elif snake_direction == "RIGHT":
        snake_pos[0] += CELL_SIZE

    # Змейканың басының жаңа орнын қосу
    snake_body.insert(0, list(snake_pos))

    # Змейка азықты жегенін тексеру
    for food in food_items[:]:
        if snake_pos == food["pos"]:
            game_score += food["weight"]
            food_items.remove(food)
            generate_food()
            break
    else:
        snake_body.pop()

    # Қабырғалармен соқтығысуды тексеру
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False

    # Өзімен соқтығысуды тексеру
    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False

    # Деңгей тексерісі (әр 3 ұпай сайын)
    new_level = game_score // 3 + 1
    if new_level > level:
        level = new_level
        speed += 2  # Деңгей көтерілгенде жылдамдықты арттыру

    # Экранды бейнелеу
    screen.fill(BLACK)
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], CELL_SIZE, CELL_SIZE))
    
    # Азықтарды салмағына қарай әртүрлі түстерде көрсету
    for food in food_items:
        color = RED if food["weight"] == 1 else YELLOW if food["weight"] == 2 else WHITE
        pygame.draw.rect(screen, color, pygame.Rect(food["pos"][0], food["pos"][1], CELL_SIZE, CELL_SIZE))

    # Ұпай мен деңгей көрсетілуі
    score_text = font.render(f"Score: {game_score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (20, 20))

    pygame.display.update()
    clock.tick(speed)  # Ойынның жылдамдығын реттеу

# Ойын аяқталған экран
screen.fill(BLACK)
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rectangle = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(2000)
pygame.quit()
sys.exit()
