import pygame
from pytmx.util_pygame import load_pygame
import tools


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


def update(screen, surface, sprite_group, mover=None, zoomer=None):
    sprite_group.draw(surface)
    screen.fill('black')
    mover.move()
    # zoomer.zoom()
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

    for obj in tmx_data.objects:
        pos = obj.x, obj.y
        if obj.type in ('Building', 'Vegetation'):
            Tile(pos=pos, surf=obj.image, groups=sprite_group)

    for obj in tmx_data.objects:
        if obj.type == 'Shape':
            if obj.name == 'Marker':
                pygame.draw.circle(screen, 'red', (obj.x, obj.y), 5)
            if obj.name == 'Rectangle':
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                pygame.draw.rect(screen, 'yellow', rect)

            if obj.name == 'Ellipse':
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                pygame.draw.ellipse(screen, 'blue', rect)

            if obj.name == 'Polygon':
                points = [(point.x, point.y) for point in obj.points]
                pygame.draw.polygon(screen, 'green', points)

    clock = pygame.time.Clock()

    mover = tools.Mover(screen, surface)
    # zoomer = tools.Zoomer(screen, surface)

    update(screen, surface, sprite_group, mover=mover, zoomer=None)
    quit_game = False
    while not quit_game:

        quit_game = pygame.event.get(pygame.QUIT)

        move_requested = mover.check_for_move_request()
        if move_requested:
            update(screen, surface, sprite_group, mover=mover, zoomer=None)

        clock.tick(60)


if __name__ == "__main__":
    main()
