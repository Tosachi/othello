import pygame
from pygame.locals import *
import sys
import random

class Game:

  def __init__(self):
    self.axis = [0, 100, 200, 300, 400]
    self.x_me = []
    self.y_me = []

    self.x_enemy = []
    self.y_enemy = []

    self.flag = [[True for i in range(4)] for i in range(4)]

    # スクリーンの横と縦
    self.scr_w = 400
    self.scr_h = 400
  
  
  def main_game(self):
    i = 0

    pygame.init()
    self.screen = pygame.display.set_mode((self.scr_w, self.scr_h))

    pygame.display.set_caption("othello")

    while(True):
      self.screen.fill((0,100,0))
      self.board()
      self.white()
      pygame.display.update()

      
      for event in pygame.event.get():
        print(str(event))
        if event.type == QUIT:
          pygame.quit()
          sys.exit()  

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
          print(str(event))
          x,y = event.pos
          i+=1
          # x = int(pygame.mouse.get_pos()[0])
          # y = int(pygame.mouse.get_pos()[1])
          print(int(pygame.mouse.get_pos()[0]), int(pygame.mouse.get_pos()[1]),i)
          self.play(int(x),int(y))
          # event.type = null
          # pygame.draw.ellipse(self.screen,(255,255,255),(self.axis[-1]+10,self.axis[-1]+10,80,80))     # 円を描画(塗りつぶし)

      # if num == 0:
      # self.me()


  def board(self):
    for i in self.axis:
      pygame.draw.line(self.screen, (0,0,0), (0, i), (self.scr_w, i), 5)
      pygame.draw.line(self.screen, (0,0,0), (i, 0), (i, self.scr_h), 5)

  def white(self):
    for x,y in zip(self.x_me, self.y_me):
      pygame.draw.ellipse(self.screen,(255,255,255),(self.axis[x]+10,self.axis[y]+10,80,80))     # 円を描画(塗りつぶし)
         
  # def me(self):
  #   for event in pygame.event.get():
  #     if event.type == MOUSEBUTTONDOWN:
    # x, y = event.pos
    # print(x, y)
    # self.play(int(x),int(y))
        # pygame.draw.ellipse(self.screen,(255,255,255),(self.axis[-1]+10,self.axis[-1]+10,80,80))     # 円を描画(塗りつぶし)
  #       return True

  #     if event.type == QUIT:
  #         pygame.quit()
  #         sys.exit()

  def play(self, x, y):
    for i in range(1,len(self.axis)):
      if(self.axis[i-1] < x and self.axis[i] > x):
        self.x_me.append(i-1)
      if(self.axis[i-1] < y and self.axis[i] > y):
        self.y_me.append(i-1)

    # デバッグ
    print(self.x_me[-1],self.y_me[-1],self.flag[self.x_me[-1]][self.y_me[-1]])
      
    if self.flag[self.x_me[-1]][self.y_me[-1]]:    
      self.flag[self.x_me[-1]][self.y_me[-1]] = False

  # def enemy(self):
  #   self.x_enemy.append(random.randrange(16))
  #   self.y_enemy.append(random.randrange(16))
  #   if self.flag[self.x_enemy[-1]][self.y_enemy[-1]]:    
  #     self.flag[self.x_enemy[-1]][self.y_enemy[-1]] = False
    
    

if __name__ == "__main__":
  game = Game()
  while(True):
    game.main_game()
    print("------------")
