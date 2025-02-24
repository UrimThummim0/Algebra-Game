import os
import sys
import sdl2
import sdl2.ext
import sdl2.sdlttf

class TileFontRenderer:
    def __init__(self):
        # Ensure SDL2 video is initialized
        if not sdl2.SDL_WasInit(sdl2.SDL_INIT_VIDEO):
            sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)
        
        sdl2.ext.init()

        self.window = sdl2.ext.Window("Tilemap Font", size=(400, 100))
        self.renderer = sdl2.ext.Renderer(self.window)

        # Load font with absolute path
        FONT_PATH = os.path.abspath("/home/samsung/Algebra-Game/assets/NotoSansMath-Regular.ttf")  # Change this to your font
        if not os.path.exists(FONT_PATH):
            raise FileNotFoundError(f"Font file not found: {FONT_PATH}")s
        
        self.font_manager = sdl2.sdlttf.(FONT_PATH, size=48)

        self.tilemap = ['2', 'x', '+', '3']
        self.spacing = 50

    def run(self):
        running = True
        while running:
            for event in sdl2.ext.get_events():
                if event.type == sdl2.SDL_QUIT:
                    running = False
            
            self.render()
            sdl2.SDL_Delay(16)
        
        sdl2.ext.quit()
    
    def render(self):
        self.renderer.clear(sdl2.ext.Color(0, 0, 0))

        x_offset = 20
        y_offset = 20
        
        for char in self.tilemap:
            text_surface = self.font_manager.render(char, (255, 255, 255, 255))
            self.renderer.copy(text_surface, dstrect=(x_offset, y_offset, 40, 50))
            x_offset += self.spacing
        
        self.renderer.present()

if __name__ == "__main__":
    app = TileFontRenderer()
    app.run()
