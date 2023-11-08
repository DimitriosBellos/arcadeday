import pygame as pg
from arena import Arena
from sprites import Pipette, TestTube, SpriteConfig
from utils import get_instructions

def main():
        """this function is called when the program starts.
        it initializes everything it needs, then runs in
        a loop until the function returns."""
        # Initialize Game
        pg.init()

         # Initialize Arena
        arena = Arena(config="configs/arena_config.yml")
        arena.create_background()
        arena.display()
        pg.display.flip()

        # Initialize Sprites
        num_tubes = 5
        tubes = []
        tubes.append(TestTube("configs/testtube_config.yml", arena.background, 'a', 1000))
        tubes.append(TestTube("configs/testtube_config.yml", arena.background, 'b', 1250))
        tubes.append(TestTube("configs/testtube_config.yml", arena.background, 'empty', 1500))
        target = tubes[-1]
        target.level = 0
        tubes.append(TestTube("configs/testtube_config.yml", arena.background, 'c', 1750))
        tubes.append(TestTube("configs/testtube_config.yml", arena.background, 'd', 2000))
        
        pipette = Pipette("configs/sprite_config.yml")
        pipette.set_tube_list(tubes)
        pipette.set_current_tube(num_tubes // 2)
        #tube = TestTube("configs/testtube_config.yml", arena.background)
        allsprites = pg.sprite.Group(pipette, *tubes) # You can create groups of sprites for updates
        tubes = pg.sprite.Group(*tubes)

        #Intilize clock sets the frame update rate in the game
        clock = pg.time.Clock()
        
        current_instruction = 0
        payload = None
        
        score_timer = 100 * 60
        font = pg.font.SysFont(None, 24)
        img = font.render('hello', True, (100, 0, 0))
        arena.screen.blit(img, (20, 20))

        # Instructions
        instructions = get_instructions(5)
        instructions_test_tubes = [
            TestTube("configs/testtube_config.yml", arena.background, instruction, 1000 + 100 * i, 100)
            for i, instruction in enumerate(instructions)
        ]
        allsprites = pg.sprite.Group(pipette, *tubes, *instructions_test_tubes) # You can create groups of sprites for updates
        instructions_test_tubes = pg.sprite.Group(*instructions_test_tubes)

        # The Game Loop
        going = True
        while going:
            clock.tick(60)              

            # Handle Input Events
            for event in pg.event.get():
                # Quit the program
                if event.type == pg.QUIT:
                    going = False
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    going = False

                # Move the sprite
                elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                     pipette.move_left()
                elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                     pipette.move_right()
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                     tube = pipette.get_current_tube()
                     if tube == target:
                        if payload is not None:
                            if payload == instructions[current_instruction]:
                                current_instruction += 1
                                target.colour = payload
                                if target.level < 3:
                                    target.level += 1
                                target.redraw()
                                if current_instruction >= len(instructions):
                                    game_over=SpriteConfig("configs/win.yml")
                                    allsprites.add(game_over)
                            else:
                                game_over=SpriteConfig("configs/game_over_config.yml")
                                allsprites.add(game_over)  
                            payload = None                      
                     else:
                         payload = tube.colour    
                         tube.decrease_level()
                
                # Sprite Interactions
                if pg.sprite.spritecollide(pipette, tubes, 1):
                     #tube.catch()
                     pipette.jump()
                     #tube.update()
                     game_over= SpriteConfig("configs/game_over_config.yml")
                     allsprites.add(game_over)

            # Update the characters with current state
            arena.screen.blit(arena.background, (0, 0))
            allsprites.draw(arena.screen)
            # Display changes.
            pg.display.flip()     

        pg.quit()

if __name__=='__main__':
    main()

