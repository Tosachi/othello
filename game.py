import pygame
import sys
from pygame.locals import *

WDTH = 50  # 盤上に並べるタイルの幅
TNUM = 8   # 一辺のタイルの数：総数はTNUM*TNUMになる
BLACK = 1
WHITE = 2
BLANK = 0

SCR = WDTH * TNUM # ウィンドウの大きさ

# 初期設定
pygame.init()
screen = pygame.display.set_mode( (SCR, SCR) )

koma = [[0 for x in range(TNUM)] for x in range(TNUM)]
can_put = [[0 for x in range(TNUM)] for x in range(TNUM)]

line = [1, -1, 0, 0, 1, 1, -1, -1]
row = [0, 0, 1, -1, 1, -1, 1, -1]

# ひっくり返せるかどうかを判定
def check(l, r, x, y, color):
  if x+l < 0 or x+l >= TNUM or y+r < 0 or y+r >= TNUM: return False
  if koma[x+l][y+r] == color or koma[x+l][y+r] == BLANK: return False
  x += (l * 2)
  y += (r * 2)
  if x < 0 or x >= TNUM or y < 0 or y >= TNUM: return False
  if koma[x][y] == BLANK: return False
  while 1:
    if x < 0 or x >= TNUM or y < 0 or y >= TNUM: return False
    if koma[x][y] == color: return True
    x += l
    y += r

# ひっくり返す
def reverse(l, r, x, y, color):
  if check(l, r, x, y, color) == False: return
  
  while 1:
    x += l
    y += r
    if koma[x][y] == color: return
    koma[x][y] = color

# 碁盤
def board():
  for i in range(0,SCR,WDTH):
    pygame.draw.line(screen, (0,0,0), (0, i), (SCR, i), 5)
    pygame.draw.line(screen, (0,0,0), (i, 0), (i, SCR), 5)

# コマの情報を更新
def koma_update(color):
  can_put = [[0 for x in range(TNUM)] for x in range(TNUM)]
  for x in range(TNUM):
    for y in range(TNUM):
      if koma[x][y] == WHITE:
        # 白コマを描く
        pygame.draw.ellipse(screen,(255,255,255),((x*WDTH)+5,(y*WDTH)+5,40,40))
      if koma[x][y] == BLACK:
        # 黒コマを描く
        pygame.draw.ellipse(screen,(0,0,0),((x*WDTH)+5,(y*WDTH)+5,40,40))
      elif koma[x][y] == BLANK:
        for i in range(8):
          if check(line[i], row[i], x, y, color):
            can_put[x][y] = 1

def play(x, y, color):  
  for i in range(8):
    reverse(line[i], row[i], x, y, color)
        
  if color == BLACK: color = WHITE
  else: color = BLACK

  board()       
  koma_update(color)

def main():
  screen.fill((0,0,0))
  pygame.display.set_caption('Mini Othello')

  pygame.mouse.set_visible(True)
  color = BLACK    # どちらの順番かを記録しておく変数

  koma[int(TNUM/2)][int(TNUM/2)] = BLACK
  koma[int(TNUM/2)-1][int(TNUM/2)-1] = BLACK
  koma[int(TNUM/2)-1][int(TNUM/2)] = WHITE
  koma[int(TNUM/2)][int(TNUM/2)-1] = WHITE

  screen.fill((0,100,0))
  board()
  koma_update(BLACK)
  print(koma)
  # print(can_put)

  pygame.display.flip()

  while 1:
    for event in pygame.event.get():
      if (event.type == KEYDOWN and event.key == K_ESCAPE or event.type == QUIT):
        pygame.quit()
        sys.exit()
      # if event.type == MOUSEBUTTONDOWN:                
      #   x = int(pygame.mouse.get_pos()[0]/WDTH)
      #   y = int(pygame.mouse.get_pos()[1]/WDTH)
      #   print(x,y)

      if color == BLACK: print("black")
      else: print("white")
      
      x,y = map(int, input().split())

      # print(can_put[x][y])

      # if can_put[x][y] == 1:
      play(x, y, color)
      pygame.display.flip()
  

if __name__ == '__main__':
    main()
