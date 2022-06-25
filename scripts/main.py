from operator import is_
import pygame, sys
import numpy as np

pygame.init()

# SIZES
width = 600
height = 600
line_width = 15
board_rows = 3
board_cols = 3

player = 1

# COLORS
background_red = (255, 0, 0)
background_color = (154, 100, 204)
line_color = (108, 64, 160)

screen = pygame.display.set_mode( (width, height) )
pygame.display.set_caption('TIC TAC TOE')
screen.fill( background_color )

# BOARD
board = np.zeros( (board_rows, board_cols) )
# print(board)

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

def mark_square(row, col, player):
  board[row][col] = player

def available_square(row, col):
  return board[row][col] == 0

  # if board[row] [col] == 0:
  #   return True
  # else:
  #   return False


def is_board_full():
  for row in range(board_rows):
    for col in range(board_cols):
      if board[row] [col] == 0:
        return False

  return True

# False
# print(is_board_full())

# Marking all squares
for row in range(board_rows):
  for col in range(board_cols):
    mark_square( row, col, 1 )

# Board is full - True
# print(is_board_full())    

draw_lines()

# main_loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:

      mouse_x = event.pos[0] # X
      mouse_y = event.pos[1] # Y

      clicked_row = int(mouse_y // 200)
      clicked_col = int(mouse_x // 200)

      if available_square( clicked_row, clicked_col ):
        if player == 1:
          mark_square( clicked_row, clicked_col, 1 )
          player = 2

        elif player == 2:
          mark_square( clicked_row, clicked_col, 2 )
          player = 1

      print(board)

  pygame.display.update()