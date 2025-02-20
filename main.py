import sdl2
import sdl2.ext

class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.is_dragging = False

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def contains(self, x, y):
        return (self.x <= x <= self.x + self.width and
                self.y <= y <= self.y + self.height)

def main():
    # Initialize SDL2
    sdl2.ext.init()

    # Create a window
    window = sdl2.ext.Window("Algebra Block Builder", size=(800, 600))
    window.show()

    # Create a renderer
    renderer = sdl2.ext.Renderer(window)

    # Create multiple rectangles
    rectangles = [
        Rectangle(100, 100, 50, 50, sdl2.ext.Color(255, 0, 0)),
        Rectangle(200, 200, 50, 50, sdl2.ext.Color(0, 255, 0)),
        Rectangle(300, 300, 50, 50, sdl2.ext.Color(0, 0, 255))
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
            elif event.type == sdl2.SDL_MOUSEBUTTONUP:
                for rect in rectangles:
                    rect.is_dragging = False
            elif event.type == sdl2.SDL_MOUSEMOTION:
                for rect in rectangles:
                    if rect.is_dragging:
                        rect.move(event.motion.xrel, event.motion.yrel)

        # Clear the screen
        renderer.clear(sdl2.ext.Color(0, 0, 0))

        # Draw the rectangles
        for rect in rectangles:
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