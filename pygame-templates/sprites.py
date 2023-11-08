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
    


class FranklinImp(SpriteConfig):
    """A little imp that saves your lab."""
    def __init__(self, config, **kwargs):
        super().__init__(config, **kwargs)
        self.direction = 1
    def update(self, direction):
        self.direction= direction
        self._walk()

    def _walk(self):
        newpos = self.rect.move((self.direction*self.move, 0))
        self.rect = newpos

    def jump(self):
        self.direction = -1*self.direction
        newpos = self.rect.move((0, self.direction*20 ))
        self.rect = newpos

    def your_methods():
        pass
    ## Add methods to move your sprite below , call them in the update function above. 
    
    
class Pipette(SpriteConfig):
    def __init__(self, config, **kwargs):
        super().__init__(config)


class TestTube(SpriteConfig ):
    """Falling testubes."""
    def __init__(self,config, background, **kwarg):
        super().__init__(config, **kwarg)
        
        self.area= background.get_rect()
        
    @property
    def new_x_pos(self):

        self._new_x_pos =randint(self.area.left+self.rect.width, self.area.right-self.rect.width)
        return self._new_x_pos

    def update(self):
        newpos= self.rect.move(( 0, self.move))
        self.rect = newpos

        if  self.rect.bottom > self.area.bottom:
            self.rect.center = (self.new_x_pos, self.attributes.start_pos[1])
    
    def catch(self):
        self.rect.inflate(40,40)







        


