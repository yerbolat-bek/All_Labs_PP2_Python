import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Music Player')

musics = r"C:\Users\erbol\Downloads"

if not os.path.exists(musics):
    print("Музыка не найдена")
    exit()

playlist = []
for file in os.listdir(musics):
    if file.endswith(".mp3"):
        playlist.append(os.path.join(musics, file))

if not playlist:
    print("Плейлист пуст!")
    exit()

current_music = 0

font = pygame.font.Font(None, 36)

def play_music():
    pygame.mixer.music.load(playlist[current_music])
    if not pygame.mixer.music.get_busy(): 
        pygame.mixer.music.play()  
    pygame.mixer.music.pause() 


def stop_music():
    pygame.mixer.music.stop()

def next_music():
    global current_music
    current_music += 1
    if current_music >= len(playlist):
        current_music = 0
    play_music()

def prev_music():
    global current_music
    current_music -= 1
    if current_music < 0:
        current_music = len(playlist) - 1
    play_music()

def toggle_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def display_text(text, x, y, font, color=(255, 255, 255)):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

play_music()

t = True
while t:
    screen.fill((0, 0, 0))

    display_text(f"Текущий трек: {os.path.basename(playlist[current_music])}", 10, 10, font)

    display_text("Плейлист:", 10, 50, font)
    for i, track in enumerate(playlist):
        display_text(f"{i + 1}. {os.path.basename(track)}", 10, 90 + i * 30, font)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            t = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                toggle_pause()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_music()
            elif event.key == pygame.K_LEFT:
                prev_music()

pygame.quit()
