import pygame as pg
from utils import load_and_scale, read_config
from random import randint, choice

class SpriteConfig(pg.sprite.Sprite):
    def __init__(self, config, **kwargs):
        pg.sprite.Sprite.__init__(self)

        if config:
            self._attributes = read_config(config)
        if kwargs:
            self._attributes = self.attributes(kwargs)

        self.image = load_and_scale("data/" + self.attributes.image_path, self.attributes.scale)
        self.rect = self.image.get_rect()
        self.rect.center = (self.attributes.start_pos[0], self.attributes.start_pos[1])
        self.move = self.attributes.move
        screen = pg.display.get_surface()
        self.area = screen.get_rect()

    @property
    def attributes(self):
        return self._attributes
    
    @attributes.setter
    def attributes(self, **kwargs):
        if kwargs:
                self._attributes.update(kwargs)
    


class Pipette(SpriteConfig):
    """A little imp that saves your lab."""
    def __init__(self, config, **kwargs):
        super().__init__(config, **kwargs)
        
    def move_left(self):
        if self.tube_id > 0:
            self.set_current_tube(self.tube_id - 1)
            
    def move_right(self):
        if self.tube_id < len(self.tube_list) - 1:
            self.set_current_tube(self.tube_id + 1)
        
    def set_tube_list(self, tube_list):
        self.tube_list = tube_list

    def set_current_tube(self, tube_id):
        self.tube_id = tube_id
        self.current_tube = self.tube_list[tube_id]
        self.rect.center = (self.current_tube.rect.center[0] + 90, self.current_tube.rect.center[1] - 300)
        
    def get_current_tube(self):
        return self.current_tube
    ## Add methods to move your sprite below , call them in the update function above. 


class TestTube(SpriteConfig):
    """Falling testubes."""
    def __init__(self,config, background, colour, xpos, ypos=None, **kwarg):
        super().__init__(config, **kwarg)
        self.area= background.get_rect()
        self.set_x_pos(xpos)
        if ypos is not None:
            self.set_y_pos(xpos,ypos)
        self.level = 3
        self.colour = colour
        if colour == 'empty':
            self.attributes.scale = 1.1
            self.rect.center = (self.rect.center[0], self.attributes.start_pos[1] - 50)
        self.redraw()
        
    def decrease_level(self):
        if self.level > 1:
            self.level -= 1
        else:
            self.level = 0
            self.colour = 'empty'
        self.redraw()

    def redraw(self):
        if self.colour == 'empty':
            image_path = "empty_test_tube.png"
        else:
            image_path = f"test_tube_{self.level}_{self.colour}.png"
        self.image = load_and_scale("data/" + image_path, self.attributes.scale)
        
    
    def set_x_pos(self, x):
        self.rect.center = (x, self.rect.center[1])

    def set_y_pos(self, x, y):
        self.rect.center = (x, y)

    def update(self):
        newpos= self.rect.move(( 0, self.move))
        self.rect = newpos

        if  self.rect.bottom > self.area.bottom:
            self.rect.center = (self.new_x_pos, self.attributes.start_pos[1])
    
    def catch(self):
        self.rect.inflate(40,40)







        


