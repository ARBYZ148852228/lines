import pygame
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('рисование линий')

BACKGROUND = (0, 0, 0)
PREVIEW_COLOR = (192, 192, 192)
LINE_COLOR = (255, 255, 255)

show_preview = True
screen.fill(BACKGROUND)

FPS = 60
clock = pygame.time.Clock()
running = True

points = []
lines = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                points.append(event.pos)
            elif event.button == 3:
                if len(points) > 1:
                    lines.append(points)
                points = []
                show_preview = True

        screen.fill(BACKGROUND)


        for line in lines:
            for i in range(len(line) - 1):
                start_point = line[i]
                end_point = line[i + 1]
                pygame.draw.line(screen, LINE_COLOR, start_point, end_point, 3)


        if len(points) > 0:
            for i in range(len(points) - 1):
                start_point = points[i]
                end_point = points[i + 1]
                pygame.draw.line(screen, LINE_COLOR, start_point, end_point, 3)


        if len(points) > 0 and show_preview:
            last_point = points[-1]
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.aaline(screen, PREVIEW_COLOR, last_point, mouse_pos, 3)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
