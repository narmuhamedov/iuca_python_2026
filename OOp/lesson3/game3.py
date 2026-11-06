import pygame
import random
import sys

pygame.init()

# Настройки
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🍩 УГАРНЫЙ ПОНЧИК 🍺")
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 30, bold=True)
big_font = pygame.font.SysFont("comicsansms", 70, bold=True)

# Цвета
BG = (30, 10, 50)
WHITE = (255, 255, 255)
PINK = (255, 105, 180)
GREEN = (50, 200, 50)
YELLOW = (255, 220, 50)
RED = (255, 60, 60)

def draw_donut(surf, x, y):
    # Пончик = розовый круг с дыркой
    pygame.draw.circle(surf, (200, 80, 140), (x, y), 25)
    pygame.draw.circle(surf, PINK, (x, y), 24)
    pygame.draw.circle(surf, BG, (x, y), 10)
    # Глазки
    pygame.draw.circle(surf, WHITE, (x-8, y-5), 5)
    pygame.draw.circle(surf, WHITE, (x+8, y-5), 5)
    pygame.draw.circle(surf, (0,0,0), (x-8, y-5), 2)
    pygame.draw.circle(surf, (0,0,0), (x+8, y-5), 2)
    # Улыбка
    pygame.draw.arc(surf, (0,0,0), (x-10, y+2, 20, 12), 3.14, 0, 2)

def draw_cucumber(surf, x, y):
    pygame.draw.ellipse(surf, GREEN, (x-20, y-12, 40, 24))
    # Злой взгляд
    pygame.draw.line(surf, (0,0,0), (x-10, y-4), (x-4, y), 2)
    pygame.draw.line(surf, (0,0,0), (x+10, y-4), (x+4, y), 2)
    pygame.draw.circle(surf, (0,0,0), (x-8, y+2), 2)
    pygame.draw.circle(surf, (0,0,0), (x+8, y+2), 2)

def draw_beer(surf, x, y):
    pygame.draw.rect(surf, (255, 200, 50), (x-12, y-18, 24, 30))
    pygame.draw.rect(surf, WHITE, (x-12, y-18, 24, 6))
    pygame.draw.rect(surf, WHITE, (x+12, y-10, 6, 15))
    # Пузырьки
    pygame.draw.circle(surf, (255, 255, 200), (x-5, y-8), 2)
    pygame.draw.circle(surf, (255, 255, 200), (x+3, y-2), 2)

def game():
    px, py = WIDTH // 2, HEIGHT - 80
    speed = 7
    enemies = []
    beers = []
    score = 0
    lives = 3
    spawn_timer = 0
    beer_timer = 0
    level = 1
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if not game_over:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                px -= speed
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                px += speed
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                py -= speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                py += speed

            px = max(30, min(WIDTH - 30, px))
            py = max(30, min(HEIGHT - 30, py))

            # Спавн огурцов
            spawn_timer += 1
            if spawn_timer > max(15, 45 - level * 3):
                spawn_timer = 0
                enemies.append([random.randint(30, WIDTH-30), -30, random.uniform(3, 5 + level)])

            # Спавн пива
            beer_timer += 1
            if beer_timer > 90:
                beer_timer = 0
                beers.append([random.randint(30, WIDTH-30), -30])

            # Движение огурцов
            for e in enemies[:]:
                e[1] += e[2]
                if e[1] > HEIGHT + 30:
                    enemies.remove(e)
                    score += 1
                    if score % 10 == 0:
                        level += 1
                elif abs(e[0]-px) < 30 and abs(e[1]-py) < 30:
                    enemies.remove(e)
                    lives -= 1
                    if lives <= 0:
                        game_over = True

            # Движение пива
            for b in beers[:]:
                b[1] += 3
                if b[1] > HEIGHT + 30:
                    beers.remove(b)
                elif abs(b[0]-px) < 30 and abs(b[1]-py) < 30:
                    beers.remove(b)
                    lives += 1
                    score += 5

        # Рисуем
        screen.fill(BG)

        # Звёздочки на фоне
        for i in range(0, WIDTH, 100):
            for j in range(0, HEIGHT, 100):
                pygame.draw.circle(screen, (60, 40, 80), ((i + j*3) % WIDTH, (j + i*2) % HEIGHT), 1)

        for e in enemies:
            draw_cucumber(screen, int(e[0]), int(e[1]))
        for b in beers:
            draw_beer(screen, int(b[0]), int(b[1]))

        draw_donut(screen, int(px), int(py))

        # UI
        score_text = font.render(f"Счёт: {score}  Уровень: {level}", True, YELLOW)
        screen.blit(score_text, (10, 10))
        lives_text = font.render(f"Жизни: {'❤' * max(0, lives)}", True, RED)
        screen.blit(lives_text, (WIDTH - 250, 10))

        if game_over:
            over = big_font.render("ТЫ ПРОИГРАЛ!", True, RED)
            screen.blit(over, (WIDTH//2 - over.get_width()//2, HEIGHT//2 - 80))
            restart = font.render("Нажми R чтобы ещё раз угареть", True, WHITE)
            screen.blit(restart, (WIDTH//2 - restart.get_width()//2, HEIGHT//2 + 20))
            if keys[pygame.K_r]:
                game()
                return

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    game()