import numpy as np

def create_board():
  a = np.zeros(64, dtype=int)
  a[27] = a[36] = 1
  a[28] = a[35] = 2
  return a

def print_bord(a):
  print('  a b c d e f g h')
  for i in range(8):
    print(i+1, end=' ')
    print(' '.join('.*o'[j] for j in a[i*8:][:8]))

def put_piece(a, p ,w, puton=True, chk=True):
  t,x,y = 0, p%8, p//8
  


if __name__ == "__main__":
  a = create_board()
  print_bord(a)

  

