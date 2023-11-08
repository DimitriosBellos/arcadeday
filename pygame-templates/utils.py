import pygame as pg
from pathlib import Path
import yaml
from munch import Munch
from random import randint

def load_and_scale( image_path, scale_factor):
    try:
        image = pg.image.load(image_path)
    except pg.error:
        raise SystemExit(f'Could not load image "{file}" {pg.get_error()}')
    size = image.get_size()
    size = (size[0] * scale_factor, size[1] * scale_factor)
    image = pg.transform.scale(image, size)
    return image

def read_config(config):
        with open(config, 'r') as file:
            attributes = Munch(yaml.safe_load(file))
        return attributes


def get_instructions():
    options = ["a", "b", "c", "d"]
    instructions = [
        options[randint(0,3)], options[randint(0,3)], options[randint(0,3)], options[randint(0,3)]
    ]
    return instructions