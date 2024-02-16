import pygame
from pytmx.util_pygame import load_pygame
import tools

TILE_WIDTH = 128
TILE_HEIGHT = 128


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


def setup(tmx_data, sprite_group):

    for layer in tmx_data.visible_layers:
        # if layer.name in ('Floor', 'Plants and rocks', 'Pipes')
        if hasattr(layer, 'data'):
            for x, y, surf in layer.tiles():
                pos = (x * TILE_WIDTH, y * TILE_HEIGHT)
                Tile(pos=pos, surf=surf, groups=sprite_group)

    for obj in tmx_data.objects:
        pos = obj.x, obj.y
        if obj.type in ('Building', 'Vegetation'):
            Tile(pos=pos, surf=obj.image, groups=sprite_group)


def update(screen, surface, pos, sprite_group, mover=None, zoomer=None):

    sprite_group.draw(surface)
    screen.fill('black')

    zoom_size = zoomer.get_zoom_size()
    zoom = zoomer.get_zoom()
    pos = mover.get_new_pos(pos, zoom)
    surface = pygame.transform.scale(surface, zoom_size)
    screen.blit(surface, pos)

    pygame.display.flip()
    pygame.display.update()


def run(screen, surface, sprite_group):

    clock = pygame.time.Clock()

    mover = tools.Mover(screen, surface)
    zoomer = tools.Zoomer(screen)
    pos = [0, 0]

    update(screen, surface, pos, sprite_group, mover=mover, zoomer=zoomer)

    quit_game = False
    while not quit_game:

        quit_game = pygame.event.get(pygame.QUIT)

        move_requested = mover.check_for_move_request()
        if move_requested:
            update(screen, surface, pos, sprite_group, mover=mover, zoomer=zoomer)

        clock.tick(60)


def main():
    pygame.init()

    x = 640
    y = 360
    screen_size = (x, y)
    screen = pygame.display.set_mode(screen_size)

    tmx_data = load_pygame('../data/tmx/basic.tmx')

    x2 = tmx_data.tilewidth * tmx_data.width
    y2 = tmx_data.tileheight * tmx_data.height

    surface_size = (x2, y2)
    surface = pygame.surface.Surface(surface_size)

    sprite_group = pygame.sprite.Group()

    setup(tmx_data, sprite_group)

    run(screen, surface, sprite_group)


if __name__ == "__main__":
    main()
