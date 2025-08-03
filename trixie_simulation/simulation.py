from PIL import Image
from pathlib import Path
import pygame


class LedMatrixPreview:
    def __init__(self,pixels: list[list[tuple[int, int, int]]], matrix_size: tuple[int, int], image_path: Path, led_size: int = 30, margin: int = 2, circle_pixels: bool = False, ):
        self.pixels = pixels
        self.matrix_size : tuple[int, int] = matrix_size
        self.image_path = image_path
        self.led_size = led_size
        self.margin = margin
        self.circle_pixels = circle_pixels

        pygame.init()
        self.screen = pygame.display.set_mode(((self.led_size + self.margin) * self.matrix_size[0],
                                        (self.led_size + self.margin) * self.matrix_size[1]))
        pygame.display.set_caption(f" {self.matrix_size[0]}x{self.matrix_size[1]} LED Matrix Image Preview")


    def draw_image(self):
        self.screen.fill((0, 0, 0))
        for y in range(self.matrix_size[1]):
            for x in range(self.matrix_size[0]):
                color = self.pixels[x, y]
                rect = pygame.Rect(x * (self.led_size + self.margin),
                                y * (self.led_size + self.margin),
                                self.led_size,
                                self.led_size)
                if self.circle_pixels:
                    pygame.draw.circle(self.screen, color, rect.center, self.led_size // 2)
                else:
                    pygame.draw.rect(self.screen, color, rect)
        pygame.display.flip()


    def run(self):
        self.draw_image()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

