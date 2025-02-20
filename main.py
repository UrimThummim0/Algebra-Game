import sdl2
import sdl2.ext

class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

def main():
    # Initialize SDL2
    sdl2.ext.init()

    # Create a window
    window = sdl2.ext.Window("Algebra Block Builder", size=(800, 600))
    window.show()

    # Create a renderer
    renderer = sdl2.ext.Renderer(window)

    # Create a rectangle
    rect = Rectangle(100, 100, 50, 50, sdl2.ext.Color(255, 0, 0))

    # Main loop to keep the window open
    running = True
    while running:
        # Handle events
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                running = False

        # Handle keyboard input
        keys = sdl2.SDL_GetKeyboardState(None)
        if keys[sdl2.SDL_SCANCODE_UP]:
            rect.move(0, -5)
        if keys[sdl2.SDL_SCANCODE_DOWN]:
            rect.move(0, 5)
        if keys[sdl2.SDL_SCANCODE_LEFT]:
            rect.move(-5, 0)
        if keys[sdl2.SDL_SCANCODE_RIGHT]:
            rect.move(5, 0)

        # Clear the screen
        renderer.clear(sdl2.ext.Color(0, 0, 0))

        # Draw the rectangle
        sdl2.SDL_SetRenderDrawColor(renderer.renderer, rect.color.r, rect.color.g, rect.color.b, rect.color.a)
        sdl2.SDL_RenderFillRect(renderer.renderer, sdl2.SDL_Rect(rect.x, rect.y, rect.width, rect.height))

        # Update the screen
        renderer.present()

        # Cap the frame rate
        sdl2.SDL_Delay(16)

    # Clean up
    sdl2.ext.quit()

if __name__ == "__main__":
    main()