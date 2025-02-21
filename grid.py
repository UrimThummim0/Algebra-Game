import sdl2
import sdl2.ext
import math
import sdl2.sdlttf as sdlttf

import materials


WIDTH = 1024
HEIGHT = 768

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

WIDTH_RECT = 50
HEIGHT_RECT = 50

#inversible operators
plus_minus = ['+', '-']
times_divide = ['x', '/']

def main():
    # Initialize SDL2
    sdl2.ext.init()
    sdlttf.TTF_Init()

    # Create a window
    
    window = sdl2.ext.Window("Algebra Block Builder", size=(WIDTH, HEIGHT), flags=sdl2.SDL_WINDOW_RESIZABLE)
    window.show()

    # Create a renderer
    renderer = sdl2.ext.Renderer(window)

    # Load a font
    font = sdlttf.TTF_OpenFont(b"assets/NotoSansMath-Regular.ttf", 24)  # Increased font size

    # Set font hinting for subpixel smoothing
    sdlttf.TTF_SetFontHinting(font, sdlttf.TTF_HINTING_LIGHT_SUBPIXEL)

    # Create rectangles with constants and x
    rectangles = [
        materials.Rectangle(100, 100, WIDTH_RECT, HEIGHT_RECT, sdl2.ext.Color(255, 0, 0), 'left', 'x'),
        materials.Rectangle(200, 100, WIDTH_RECT, HEIGHT_RECT, sdl2.ext.Color(0, 255, 0), 'right', '3'),
        materials.Rectangle(500, 100, WIDTH_RECT, HEIGHT_RECT, sdl2.ext.Color(0, 0, 255), 'right', '2'),
        materials.Rectangle(600, 100, WIDTH_RECT, HEIGHT_RECT, sdl2.ext.Color(255, 255, 0), 'right', '4')
    ]
    # Create circles with operators
    rectangles_ops = [
        materials.Rectangle_ops(100, 200, WIDTH_RECT, HEIGHT_RECT, sdl2.ext.Color(255, 0, 0), 'left', plus_minus[0]),
        materials.Rectangle_ops(200, 200, WIDTH_RECT, HEIGHT_RECT, sdl2.ext.Color(255, 0, 0), 'left', plus_minus[1]),
        materials.Rectangle_ops(500, 200, WIDTH_RECT, HEIGHT_RECT, sdl2.ext.Color(255, 0, 0), 'left', times_divide[0]),
        materials.Rectangle_ops(600, 200, WIDTH_RECT, HEIGHT_RECT, sdl2.ext.Color(255, 0, 0), 'left', times_divide[1])
    ]

    # Main loop to keep the window open
    running = True
    while running:
        # Handle events
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False

            elif event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                for rect in rectangles:
                    if rect.contains(event.motion.x, event.motion.y):
                        rect.is_dragging = True

                for circle in rectangles_ops:
                    if circle.contains(event.motion.x, event.motion.y):
                        circle.is_dragging = True

            elif event.type == sdl2.SDL_MOUSEBUTTONUP:
                for rect in rectangles:
                    rect.is_dragging = False

                for circle in rectangles_ops:
                    circle.is_dragging = False

            elif event.type == sdl2.SDL_MOUSEMOTION:
                for rect in rectangles:
                    if rect.is_dragging:
                        print(f"x_pointer={event.motion.x}, y_pointer={event.motion.y}")
                        rect.move(event.motion.xrel, event.motion.yrel)
                        # Check if the rectangle has crossed to the other side
                        print(f"x_rect={rect.x}, y_rect={rect.y}, rect_side={rect.side}")

                        if rect.x + rect.width > CENTER_X and rect.side == 'left':
                            rect.side = 'right'
                            
                        if rect.x < CENTER_X and rect.side == 'right':
                            rect.side = 'left'

                for rect_ops in rectangles_ops:
                    if rect_ops.is_dragging:
                        rect_ops.move(event.motion.xrel, event.motion.yrel)
                        print(rect_ops.side)

                        # Check if operator has crossed to the other side
                        if rect_ops.x + rect_ops.width > CENTER_X and rect_ops.side == 'left':
                            rect_ops.side = 'right'
                            if rect_ops.value == plus_minus[0]:
                                rect_ops.value = plus_minus[1]
                            elif rect_ops.value == plus_minus[1]:
                                rect_ops.value = plus_minus[0]
                            
                            if rect_ops.value == times_divide[0]:
                                rect_ops.value = times_divide[1]
                            elif rect_ops.value == times_divide[1]:
                                rect_ops.value = times_divide[0]
            
                        if rect_ops.x < CENTER_X and rect_ops.side == 'right':
                            rect_ops.side = 'left'
                            if rect_ops.value == plus_minus[1]:
                                rect_ops.value = plus_minus[0]
                            elif rect_ops.value == plus_minus[0]:
                                rect_ops.value = plus_minus[1]
                            
                            if rect_ops.value == times_divide[0]:
                                rect_ops.value = times_divide[1]
                            elif  rect_ops.value == times_divide[1]:
                                rect_ops.value = times_divide[0]
                            
                            
        # Clear the screen
        renderer.clear(sdl2.ext.Color(0, 0, 0))

        # Draw the dividing line
        sdl2.SDL_SetRenderDrawColor(renderer.renderer, 255, 255, 255, 255)
        sdl2.SDL_RenderDrawLine(renderer.renderer, CENTER_X, 0, CENTER_X, HEIGHT)

        # Draw the rectangles and their values
        for rect in rectangles:
            sdl2.SDL_SetRenderDrawColor(renderer.renderer, rect.color.r, rect.color.g, rect.color.b, rect.color.a)
            sdl2.SDL_RenderFillRect(renderer.renderer, sdl2.SDL_Rect(rect.x, rect.y, rect.width, rect.height))

            # Render the value text
            text_surface = sdlttf.TTF_RenderText_Blended(font, bytes(rect.value, 'utf-8'), sdl2.SDL_Color(255, 255, 255))
            text_texture = sdl2.SDL_CreateTextureFromSurface(renderer.renderer, text_surface)
            sdl2.SDL_FreeSurface(text_surface)

            text_rect = sdl2.SDL_Rect(rect.x + 10, rect.y + 10, 30, 30)
            sdl2.SDL_RenderCopy(renderer.renderer, text_texture, None, text_rect)
            sdl2.SDL_DestroyTexture(text_texture)

        # Draw the circles and their values
        for circle in rectangles_ops:
            sdl2.SDL_SetRenderDrawColor(renderer.renderer, circle.color.r, circle.color.g, circle.color.b, circle.color.a)

            # Render the value text
            text_surface = sdlttf.TTF_RenderText_Blended(font, bytes(circle.value, 'utf-8'), sdl2.SDL_Color(255, 255, 255))
            text_texture = sdl2.SDL_CreateTextureFromSurface(renderer.renderer, text_surface)
            sdl2.SDL_FreeSurface(text_surface)

            text_rect = sdl2.SDL_Rect(circle.x - 10, circle.y - 10, 30, 30)
            sdl2.SDL_RenderCopy(renderer.renderer, text_texture, None, text_rect)
            sdl2.SDL_DestroyTexture(text_texture)

        # Update the screen
        renderer.present()

        # Cap the frame rate
        sdl2.SDL_Delay(16)

    # Clean up
    sdl2.sdlttf.TTF_CloseFont(font)
    sdl2.sdlttf.TTF_Quit()
    sdl2.ext.quit()

if __name__ == "__main__":
    main()