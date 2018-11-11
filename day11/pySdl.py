import os
os.environ["PYSDL2_DLL_PATH"] = "C:\\Users\\lifei\\Downloads\\SDL2-2.0.9-win32-x64"
from sdl2 import *


class Display:
    window:SDL_Window = None
    renderer:SDL_Renderer = None
    def __init__(self):
        SDL_Init(SDL_INIT_VIDEO)
        self.window = SDL_CreateWindow(b"Window", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,640,300,SDL_WINDOW_SHOWN)
        self.renderer = SDL_CreateRenderer(self.window,-1, SDL_RENDERER_SOFTWARE)
    
    def loop(self, update, render):
        running = True
        event = SDL_Event()
        while running:
            SDL_PollEvent(event)
            if event.type == SDL_QUIT:
                running = False
            update()
            render()
        SDL_DestroyRenderer(self.renderer)
        SDL_DestroyWindow(self.window)
        SDL_Quit()
            
    def update(self):
        pass
    def render(self):
        SDL_SetRenderDrawColor(self.renderer, 128,255,255,255)
        SDL_RenderClear(self.renderer)
        SDL_RenderPresent(self.renderer)
x = Display()
x.loop(x.update,x.render)