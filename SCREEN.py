import sdl2
import sdl2.ext
import sdl2.sdlttf as sdlttf

import ENGINE

class ScalableWindow:
    def __init__(self, title, width, height, padding_left,padding_right, padding_top):
        self.title = title
        self.width = width
        self.height = height
        self.window = None
        self.renderer = None
        self.running = False
        self.font = None
        self.text_texture = None
        self.padding_left = padding_left
        self.padding_right = padding_right
        self.padding_top = padding_top
        self.inputted_text = []
        self.text_lines = 0
        self.text_textures = []
        self.TEXT_SECTION = []
    
    def initialize(self):
        """Initialize SDL, create a resizable window, and load a font."""
        if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) != 0:
            raise RuntimeError(f"Failed to initialize SDL: {sdl2.SDL_GetError()}")

        # Initialize SDL_ttf
        if sdlttf.TTF_Init() != 0:
            raise RuntimeError(f"Failed to initialize SDL_ttf: {sdlttf.TTF_GetError()}")

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

        # Load a font
        self.font = sdlttf.TTF_OpenFont(b"assets/NotoSansMath-Regular.ttf", 24)

        if not self.font:
            raise RuntimeError(f"Failed to load font: {sdlttf.TTF_GetError()}")

        # Render text to a texture

        self.create_text_texture()

    def create_text_texture(self):


        text_surface = sdlttf.TTF_RenderText_Solid(
            self.font,
            ENGINE.TEXT.encode('utf-8'),
            sdl2.SDL_Color(255, 255, 255)  # White color
        )
        if not text_surface:
            raise RuntimeError(f"Failed to render text: {sdlttf.TTF_GetError()}")

        # Create a texture from the surface
        self.text_texture = sdl2.SDL_CreateTextureFromSurface(self.renderer, text_surface)
        if not self.text_texture:
            raise RuntimeError(f"Failed to create texture: {sdl2.SDL_GetError()}")
        
        

        self.text_width = text_surface.contents.w
        self.text_height = text_surface.contents.h

    #def update_text(self, text):
     #       if text_container.w >= self.width - self.padding_right:
    def render(self):
        """Render the current frame, including tsext."""
        # Clear the screen with a black color
        sdl2.SDL_SetRenderDrawColor(self.renderer, 0, 0, 0, 255)
        sdl2.SDL_RenderClear(self.renderer)

        text_container = sdl2.SDL_Rect(
            self.padding_left,  # Center horizontally
            self.padding_top,  # Center vertically
            self.text_width,  # Width of the text area
            self.text_height ) # Height of the text area
        
        sdl2.SDL_RenderCopy(self.renderer, self.text_texture, None, text_container)
        print(text_container )



            
        # Update the screen
        sdl2.SDL_RenderPresent(self.renderer)


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

    def cleanup(self):
        """Clean up resources and quit SDL."""
        if self.text_texture:
            sdl2.SDL_DestroyTexture(self.text_texture)
        if self.font:
            sdlttf.TTF_CloseFont(self.font)
        if self.renderer:
            sdl2.SDL_DestroyRenderer(self.renderer)
        if self.window:
            sdl2.SDL_DestroyWindow(self.window)
        sdlttf.TTF_Quit()
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
    app = ScalableWindow("Scalable Window with Text", 800, 600, 50, 50, 50)
    app.run()