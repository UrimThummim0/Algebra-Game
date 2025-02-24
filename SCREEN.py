import sdl2
import sdl2.ext

class ScalableWindow:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.window = None
        self.renderer = None
        self.running = False

    def initialize(self):
        """Initialize SDL and create a resizable window and renderer."""
        if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) != 0:
            raise RuntimeError(f"Failed to initialize SDL: {sdl2.SDL_GetError()}")

        # Create a resizable window
        self.window = sdl2.SDL_CreateWindow(
            self.title.encode('utf-8'),
            sdl2.SDL_WINDOWPOS_CENTERED,
            sdl2.SDL_WINDOWPOS_CENTERED,
            self.width,
            self.height,
            sdl2.SDL_WINDOW_SHOWN | sdl2.SDL_WINDOW_RESIZABLE
        )
        if not self.window:
            raise RuntimeError(f"Failed to create window: {sdl2.SDL_GetError()}")

        # Create a renderer for the window
        self.renderer = sdl2.SDL_CreateRenderer(
            self.window,
            -1,
            sdl2.SDL_RENDERER_ACCELERATED
        )
        if not self.renderer:
            raise RuntimeError(f"Failed to create renderer: {sdl2.SDL_GetError()}")

    def handle_events(self):
        """Handle SDL events, including window resizing."""
        for event in sdl2.ext.get_events():
            if event.type == sdl2.SDL_QUIT:
                self.running = False
            elif event.type == sdl2.SDL_WINDOWEVENT:
                if event.window.event == sdl2.SDL_WINDOWEVENT_RESIZED:
                    # Update the window dimensions when resized
                    self.width = event.window.data1
                    self.height = event.window.data2
                    print(f"Window resized to: {self.width}x{self.height}")

    def render(self):
        """Render the current frame, scaling content to the new window size."""
        # Clear the screen with a black color
        sdl2.SDL_SetRenderDrawColor(self.renderer, 0, 0, 0, 255)
        sdl2.SDL_RenderClear(self.renderer)

        # Draw a simple rectangle that scales with the window size
        rect = sdl2.SDL_Rect(
            int(self.width * 0.25),  # 25% from the left
            int(self.height * 0.25),  # 25% from the top
            int(self.width * 0.5),  # 50% of the width
            int(self.height * 0.5)  # 50% of the height
        )
        sdl2.SDL_SetRenderDrawColor(self.renderer, 255, 0, 0, 255)  # Red color
        sdl2.SDL_RenderFillRect(self.renderer, rect)

        # Update the screen
        sdl2.SDL_RenderPresent(self.renderer)

    def cleanup(self):
        """Clean up resources and quit SDL."""
        if self.renderer:
            sdl2.SDL_DestroyRenderer(self.renderer)
        if self.window:
            sdl2.SDL_DestroyWindow(self.window)
        sdl2.SDL_Quit()

    def run(self):
        """Run the main loop of the application."""
        self.initialize()
        self.running = True

        while self.running:
            self.handle_events()
            self.render()

        self.cleanup()

if __name__ == "__main__":
    # Create and run the scalable window
    app = ScalableWindow("Scalable Window", 800, 600)
    app.run()