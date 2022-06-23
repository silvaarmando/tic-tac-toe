import pygame, sys

pygame.init()

# SIZES
width = 600
height = 600
line_width = 15

# COLORS
background_red = (255, 0, 0)
background_color = (154, 100, 204)
line_color = (108, 64, 160)

screen = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('TIC🪨 TAC🧻 TOE✂️')
screen.fill( background_color )

# pygame.draw.line( screen, background_red, (10, 10), (300, 300), 10 )

def draw_lines():
  # 1ª horizontal
  pygame.draw.line( screen, line_color, (20, 200), (580, 200), line_width )
  
  # 2ª horizontal
  pygame.draw.line( screen, line_color, (20, 400), (580, 400), line_width )

  # 1ª vertical
  pygame.draw.line( screen, line_color, (200, 20), (200, 580), line_width )

  # 2ª vertical
  pygame.draw.line( screen, line_color, (400, 20), (400, 580), line_width)

draw_lines()

# main_loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  pygame.display.update()