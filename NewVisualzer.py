import math
import pygame
import os
import random
pygame.init()
data= ["Bubble","Insertion","Merge","Selection"]
var = 0
class Toggle():
    def __init__(self,data,X,Y):
        self.data = data
        self.font =pygame.font.SysFont("comicsans", 30)
        self.X =X 
        self.Y=Y
    def display(self,text,screen,text_col):
        self.surf = self.font.render(text,True,text_col)
        screen.blit(self.surf,(self.X,self.Y))  

    def change(self,key,screen,back_col,H,W):
        pygame.draw.rect(screen,back_col,(self.X,self.Y,H,W))
        global var 
        if key =="UP":
            if var != 0:
                var-=1
        elif key=="DOWN":
            if var != len(data)-1:
                var +=1
class DrawInformation():
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	BACKGROUND_COLOR = WHITE

	GRADIENTS = [
(99,199,77),
(62,137,72),
(38,92,66)


	]


	FONT = pygame.font.SysFont('comicsans', 25)

	SIDE_PAD = 100
	TOP_PAD = 200

	def __init__(self, width, height, lst):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Sorting Algorithm Visualization")
		pygame.display.set_icon(pygame.image.load('icon.png'))
		self.set_list(lst)

	def set_list(self, lst):
		self.lst = lst
		self.min_val = min(lst)
		self.max_val = max(lst)

		self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
		self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
		self.start_x = self.SIDE_PAD // 2

def draw(draw_info, toggle_c,algo_name=0, ascending=0,):
	draw_info.window.fill(draw_info.BACKGROUND_COLOR)

	controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | Arrow key - Change Sorting Algorithm",
		1, (38,92,66))
	draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2,20))

	current_A =toggle_c.font.render("Current Algorithm :- ",1,(38,92,66))
	draw_info.window.blit(current_A,(50,90))
	toggle_c.display(data[var],draw_info.window,(38,92,66))
	draw_list(draw_info)
	pygame.display.update()

def generate_starting_list(n):
	l=[x for x in range(n)]
	random.shuffle(l)
	return l

def draw_list(draw_info,color_positions={}, clear_bg=False):
	lst = draw_info.lst

	for i, val in enumerate(lst):
		x = draw_info.start_x + i * draw_info.block_width
		y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

		color = draw_info.GRADIENTS[i % 3]
		if i in color_positions:
			color = color_positions[i] 
		pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
def insertion_sort(draw_info,arr, n,toggle_):
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
        draw_info.window.fill(draw_info.BACKGROUND_COLOR)
        draw(draw_info,toggle_)
        pygame.display.update()
def bubble_sort(draw_info ,height,toggle_):
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
        draw_info.window.fill(draw_info.BACKGROUND_COLOR)
        draw(draw_info,toggle_)
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
def merge_sort(draw_info,data, start, end,toggle_):

    if start < end:
        mid = int((start + end) / 2)
        merge_sort(draw_info,data, start, mid,toggle_)
        merge_sort(draw_info,data, mid+1, end,toggle_)

        merge(data, start, mid, end)
        draw_info.window.fill(draw_info.BACKGROUND_COLOR)
        draw(draw_info,toggle_)
        pygame.display.update()
        
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    draw(draw_info,toggle_)
def selection_sort(draw_info,arr, n,toggle_):
    for i in range(n):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.time.delay(100)
        ## to store the index of the minimum element
        min_element_index = i
        for j in range(i + 1, n):
            ## checking and replacing the minimum element index
            if arr[j] < arr[min_element_index]:
                min_element_index = j
        ## swaping the current element with minimum element
        arr[i], arr[min_element_index] = arr[min_element_index], arr[i]
        draw_info.window.fill(draw_info.BACKGROUND_COLOR)
        draw(draw_info,toggle_)
def main():
	run = True
	clock = pygame.time.Clock()

	n = 100
	
	lst = generate_starting_list(n)
	draw_info = DrawInformation(800, 600, lst)
	toggle = Toggle(data,340,90)
	while run:
		clock.tick(60)

		
		draw(draw_info,toggle)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type != pygame.KEYDOWN:
				continue
			if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
				toggle.change("UP",draw_info.window,(0,0,0),200,200)
			if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
				toggle.change("DOWN",draw_info.window,(0,0,0),200,200)
			if event.key == pygame.K_r:
				lst = generate_starting_list(n)
				draw_info.set_list(lst)

			elif event.key == pygame.K_SPACE:
				if data[var] =="Insertion":
					insertion_sort(draw_info,lst,len(lst),toggle)
				if data[var] =="Bubble":
					bubble_sort(draw_info,lst,toggle)
				if data[var]=="Merge":
					merge_sort(draw_info,lst,0,len(lst)-1,toggle)
				if data[var]=="Selection":
					selection_sort(draw_info,lst,len(lst),toggle)

            
		
	pygame.quit()
if __name__ == "__main__":
	main()