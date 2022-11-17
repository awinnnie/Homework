from mimetypes import init
import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((720, 500))
r = pygame.Rect(0, 0, 500, 500)

class Square():
    def __init__(self, X_coord, Y_coord, white=False, number_of_neigh=0):
        self.X_coord = X_coord
        self.Y_coord = Y_coord
        self.white = white
        self.number = number_of_neigh

    def is_neigh(self,other):
        if (other.X_coord == self.X_coord) and (abs(other.Y_coord - self.Y_coord)==50):
            return True
        elif (other.Y_coord == self.Y_coord) and (abs(other.X_coord - self.X_coord)==50):
            return True
        elif abs(other.X_coord - self.X_coord)==50 and abs(other.Y_coord - self.Y_coord)==50:
            return True
        return False

    def show(self):
        return (self.X_coord, self.Y_coord, self.white)
   
myboard = [[Square(j,i) for i in range(0,451,50)] for j in range(0,451,50)]

pygame.draw.rect(screen, (255, 255, 255), r, 1)
for i in range(10):
    for j in range(10):
        pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(i*50, j*50, 50, 50), 1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(pos[0]-pos[0]%50, pos[1]-pos[1]%50, 50, 50), 0)
            myboard[pos[0]//50][pos[1]//50].white = True
            myboard[pos[0]//50][(pos[1]//50)+1].number+=1
            myboard[pos[0]//50][(pos[1]//50)-1].number+=1
            myboard[(pos[0]//50)+1][pos[1]//50].number+=1
            myboard[(pos[0]//50)-1][pos[1]//50].number+=1
            myboard[(pos[0]//50)+1][(pos[1]//50)-1].number+=1
            myboard[(pos[0]//50)-1][(pos[1]//50)+1].number+=1
            myboard[(pos[0]//50)+1][(pos[1]//50)+1].number+=1
            myboard[(pos[0]//50)-1][(pos[1]//50)-1].number+=1

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
