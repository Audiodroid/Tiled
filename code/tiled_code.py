import pygame
from pytmx.util_pygame import load_pygame
import tools


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


def update(screen, surface, sprite_group, mover):
    sprite_group.draw(surface)
    screen.fill('black')
    mover.move()
    pygame.display.flip()
    pygame.display.update()


def main():
    pygame.init()

    x = 1280
    y = 720
    screen_size = (x, y)
    screen = pygame.display.set_mode(screen_size)

    x2 = 4480
    y2 = 4096
    surface_size = (x2, y2)
    surface = pygame.surface.Surface(surface_size)

    tmx_data = load_pygame('../data/tmx/basic.tmx')
    sprite_group = pygame.sprite.Group()

    # cycle through all layers
    for layer in tmx_data.visible_layers:
        # if layer.name in ('Floor', 'Plants and rocks', 'Pipes')
        if hasattr(layer, 'data'):
            for x, y, surf in layer.tiles():
                pos = (x * 128, y * 128)
                Tile(pos=pos, surf=surf, groups=sprite_group)

    # for obj in tmx_data.objects:
    #     pos = obj.x, obj.y
    #     if obj.type in ('Building', 'Vegetation'):
    #         Tile(pos=pos, surf=obj.image, groups=sprite_group)

    clock = pygame.time.Clock()

    pos_x = 0
    pos_y = 0
    mover = tools.Mover(screen, surface, pos_x, pos_y)

    update(screen, surface, sprite_group, mover)
    quit_game = False
    while not quit_game:

        quit_game = pygame.event.get(pygame.QUIT)

        move_requested = mover.check_for_move_request()
        if move_requested:
            update(screen, surface, sprite_group, mover)

        clock.tick(60)


if __name__ == "__main__":
    main()
