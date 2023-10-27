import pygame


class Mover:

    def __init__(self, screen, surface, pos_x, pos_y):
        self.screen = screen
        self.surface = surface
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.key_is_down = False
        self.key = None

    def check_for_move_request(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.key_is_down = True
                self.key = event.key
            elif event.type == pygame.KEYUP:
                self.key_is_down = False
                self.key = None

        return self.key_is_down

    def move(self):

        if self.key_is_down:

            if self.key == pygame.K_w:
                self.pos_y = min(self.pos_y + 15, 0)

            elif self.key == pygame.K_s:
                self.pos_y = max(self.pos_y - 15, -4096)

            elif self.key == pygame.K_a:
                self.pos_x = min(self.pos_x + 15, 0)

            elif self.key == pygame.K_d:
                self.pos_x = max(self.pos_x - 15, -4480)

        pos = (self.pos_x, self.pos_y)

        self.screen.blit(self.surface, pos)

class Scroller:

    def __init__(self, display, surface, scroll_y):
        self.scroll_y = scroll_y
        self.display = display
        self.surface = surface

    def handle_scroll(self):

        MOUSE_WHEEL_SCROLL_UP = 4
        MOUSE_WHEEL_SCROLL_DOWN = 5

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == MOUSE_WHEEL_SCROLL_UP:
                    self.scroll_y = min(self.scroll_y + 15, 0)
                if event.button == MOUSE_WHEEL_SCROLL_DOWN:
                    self.scroll_y = max(self.scroll_y - 15, -1280)

        self.display.blit(self.surface, (0, self.scroll_y))


class Printer:

    def print_pygame(self, tmx_data):

        # get layers
        print(tmx_data.layers) # get all layers
        for layer in tmx_data.visible_layers: # get visible layers
            print(layer)

        print(tmx_data.layernames) # get all layer names as dict

        print(tmx_data.get_layer_by_name('Floor')) # get one layer by name

        for obj in tmx_data.objectgroups: # get object layers
            print(obj)

        # get tiles
        layer = tmx_data.get_layer_by_name('Floor')
        for x,y,surf in layer.tiles(): # get all the information
            print(x * 128)
            print(y * 128)
            print(surf)

        print(layer.data)

        print(layer.name)
        print(layer.id)

        # get objects
        object_layer = tmx_data.get_layer_by_name('Objects')
        for obj in object_layer:
            # print(obj.x)
            # print(obj.y)
            # print(obj.image)
            if obj.type == 'Shape':
                if obj.name == 'Marker':
                    print(obj.x)
                    print(obj.y)
                if obj.name == 'Rectangle':
                    print(obj.x)
                    print(obj.y)
                    print(obj.width)
                    print(obj.height)
                    print(obj.as_points)

                if obj.name == 'Ellipse':
                    print(dir(obj))

                if obj.name == 'Polygon':
                    print(obj.as_points)
                    print(obj.points)

        for obj in tmx_data.objects:
            print(obj)

        for obj in tmx_data.objects:
            pos = obj.x, obj.y
            if obj.type == 'Shape':
                if obj.name == 'Marker':
                    pygame.draw.circle(self.screen, 'red', (obj.x, obj.y), 5)
                if obj.name == 'Rectangle':
                    rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                    pygame.draw.rect(self.screen, 'yellow', rect)

                if obj.name == 'Ellipse':
                    rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                    pygame.draw.ellipse(self.screen, 'blue', rect)

                if obj.name == 'Polygon':
                    points = [(point.x, point.y) for point in obj.points]
                    pygame.draw.polygon(self.screen, 'green', points)
