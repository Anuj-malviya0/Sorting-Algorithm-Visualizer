import sys
import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "Hide"
import pygame


#defining colour in RGB format
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
GREEN   = (0, 255, 0)
BLUE_G  = (21, 32, 43)
GRAY_L  = (223,226,219)
CREAM   = (191,179,172)
BROWN   = (55,41,36)

#variables that controles colours
COLOR_1 = BLUE_G
COLOR_2 = GRAY_L


#pygame initilization
pygame.init()
#creating a object of class text
txt = Text('cambriacambriamath',40)
# setting window size
win = pygame.display.set_mode((1200, 600))
# setting title to the window
pygame.display.set_caption("Sorting Visualizer")
pygame.display.set_icon(pygame.image.load('icon.png'))
# initial position
x = 320
y = 40
# width of each bar
width = 15
  
#generating random data for sorting  
height = [x for x in range(1,51)]
random.shuffle(height) 
 

# function to draw border rectangles
def draw_rect(col,x,y,w,h):
    pygame.draw.rect(win,col,(x,y,w,h),width=5)
    pygame.display.update()
# function to show the list of height   
def show(height): 
    for i in range(len(height)):
        line =  pygame.Rect(x +17 * i, y, width,height[i]*10)
        # drawing each bar with respective gap
        pygame.draw.rect(win, COLOR_1,line)
# implementing bubble sort
def bubble_sort(height):
    for i in range(len(height) - 1):
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        for j in range(len(height) - i - 1):
            if height[j] > height[j + 1]:
                t = height[j]
                height[j] = height[j + 1]
                height[j + 1] = t
        win.fill(COLOR_2)
        show(height)
        detail_text("Bubble sort","O(n^2)","O(1)")
        # txt.Render("Bubble sort",40,30)

        # txt.Render("Time",85 ,90)
        # txt.Render("Complexity :- ",35 ,130)
        # txt.Render("O(n^2)",60,175)

        # txt.Render("Space",85 ,250)
        # txt.Render("Complexity :- ",35 ,290)
        # txt.Render("O(1)",60,330)
        # txt.Render("Delay :- 100",40,515)
        draw_rect(COLOR_1,20,20,250,550)
        draw_rect(COLOR_1,290,20,900,550)
	
# implementing insertin sort
def insertion_sort(arr, n):
    for i in range(1, n):
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        current_position = i
        current_element = arr[i]
        while current_position > 0 and current_element < arr[current_position - 1]:
            arr[current_position] = arr[current_position - 1]
            current_position -= 1
        arr[current_position] = current_element
        win.fill(COLOR_2)
        print(end="")
        show(height)
        
        draw_rect(COLOR_1,20,20,250,550)
        draw_rect(COLOR_1,290,20,900,550)
        detail_text("Insertion sort","O(n^2)","O(1)")
        display_time()
        pygame.display.update()
# implementing merge sort
# merge sort requires two functions one for merginf the sub arrays and one for 
# recursive call
def merge(data, start, mid, end):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.delay(100)
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1
def merge_sort(data, start, end):

    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid)
        merge_sort(data, mid+1, end)

        merge(data, start, mid, end)
        win.fill(COLOR_2)
        print(end="")
        show(height)
        detail_text("Merge sort","O(n log n)","O(1)")
        draw_rect(COLOR_1,20,20,250,550)
        draw_rect(COLOR_1,290,20,900,550)
        display_time()
        pygame.display.update()
        
    show(height)
    pygame.display.update()
