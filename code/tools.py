import pygame


class Mover:

    MOVE_KEYS = [
        pygame.K_LEFT,
        pygame.K_RIGHT,
        pygame.K_UP,
        pygame.K_DOWN
    ]

    def __init__(self, screen, surface):
        self.screen = screen
        self.surface = surface

        self.move_key_is_down = False
        self.key = None

    def check_for_move_request(self):

        for event in pygame.event.get():

            if (event.type == pygame.KEYDOWN) and (event.key in self.MOVE_KEYS):
                self.move_key_is_down = True
                self.key = event.key
            elif event.type == pygame.KEYUP:
                self.move_key_is_down = False
                self.key = None

        return self.move_key_is_down

    def new_pos(self, pos, zoom):

        w = self.screen.get_size()[0]
        h = self.screen.get_size()[1]

        if self.key == pygame.K_LEFT:
            pos[0] = min(pos[0] + 15, 0)

        elif self.key == pygame.K_RIGHT:
            pos[0] = max(pos[0] - 15, -(w / zoom - w))  # TODO makes no sense

        elif self.key == pygame.K_UP:
            pos[1] = min(pos[1] + 15, 0)

        elif self.key == pygame.K_DOWN:
            pos[1] = max(pos[1] - 15, -(h / zoom - h))  # TODO makes no sense

        return pos

    def get_new_pos(self, pos, zoom):

        if not self.move_key_is_down:
            return pos

        return self.new_pos(pos, zoom)


class Zoomer:
    """ https://stackoverflow.com/questions/56407891/pygame-transform-scale-does-not-work-on-the-game-surface """

    def __init__(self, screen):
        self.screen = screen
        self.zoom = 0.25

    def get_zoom(self):
        return self.zoom

    def get_zoom_size(self):
        """zoom=1 shows the full surface, 0.5 shows the top quarter,..."""
        wnd_w, wnd_h = self.screen.get_size()
        return round(wnd_w / self.zoom), round(wnd_h / self.zoom)
