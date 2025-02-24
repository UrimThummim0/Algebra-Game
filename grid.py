import sdl2
import sdl2.ext

# Initialize SDL
sdl2.ext.init()

# Create a window
window = sdl2.ext.Window("Tilemap with Images", size=(800, 600))
window.show()

# Create a renderer
renderer = sdl2.ext.Renderer(window)
# Set the background color to white
renderer.clear(sdl2.ext.Color(255, 255, 255))
# Load tile images as textures
tile_textures = {
    0: sdl2.ext.Texture(renderer, sdl2.ext.load_image("assets/OP_RECT.png")),  # Grass
    1: sdl2.ext.Texture(renderer, sdl2.ext.load_image("assets/CONST_RECT.png")),  # Water
    2: sdl2.ext.Texture(renderer, sdl2.ext.load_image("assets/X_RECT.png")),   # Wall
}

#   TILEMAP, 
tilemap = [
    [0, 0, 0, 1, 0],
    [0, 2, 0, 1, 0],
    [0, 2, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
]

# Define tile size
tile_size = 40  # Each tile is 40x40 pixels

# Draw the tilemap
for y, row in enumerate(tilemap):
    for x, tile in enumerate(row):
        # Get the texture for the current tile
        texture = tile_textures[tile]
        # Calculate the position of the tile
        dst_rect = sdl2.SDL_Rect(x * tile_size, y * tile_size, tile_size, tile_size)
        # Render the texture
        renderer.copy(texture, dstrect=dst_rect)

# Present the renderer to update the window
renderer.present()


# Main loop
running = True
while running:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            running = False
            break

    # Update the window
    window.refresh()
    

# Clean up and quit
sdl2.ext.quit()