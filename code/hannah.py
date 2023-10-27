import pygame
import string
import tools


def main():
    pygame.init()

    x_screen = 300
    y_screen = 300

    x_surface = 300
    y_surface = 600

    screen = pygame.display.set_mode((x_screen, y_screen))
    intermediate = pygame.surface.Surface((x_surface, y_surface))
    i_a = intermediate.get_rect()
    x1 = i_a[0]
    x2 = x1 + i_a[2]
    a, b = (255, 0, 0), (60, 255, 120)
    y1 = i_a[1]
    y2 = y1 + i_a[3]
    h = y2 - y1
    rate = (float((b[0] - a[0]) / h),
            (float(b[1] - a[1]) / h),
            (float(b[2] - a[2]) / h)
            )
    for line in range(y1, y2):
        color = (min(max(a[0] + (rate[0] * line), 0), 255),
                 min(max(a[1] + (rate[1] * line), 0), 255),
                 min(max(a[2] + (rate[2] * line), 0), 255)
                 )
        pygame.draw.line(intermediate, color, (x1, line), (x2, line))

    y = 20
    f = pygame.font.SysFont('', 17)
    for l in string.ascii_uppercase:
        intermediate.blit(f.render(l, True, (255, 255, 255)), (10, y))
        y += 20

    clock = pygame.time.Clock()

    scroller = tools.Scroller(screen, intermediate)

    quit_game = False
    while not quit_game:

        quit_game = pygame.event.get(pygame.QUIT)

        scroller.handle_scroll()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()