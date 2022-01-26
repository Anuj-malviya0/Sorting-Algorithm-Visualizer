import pygame
import math
import random
import os
pygame.init()
class DrawInformation():
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	BACKGROUND_COLOR = WHITE

	GRADIENTS = [
		(128, 128, 128),
		(160, 160, 160),
		(192, 192, 192)
	]


	FONT = pygame.font.SysFont('comicsans', 30)
	LARGE_FONT = pygame.font.SysFont('comicsans', 40)

	SIDE_PAD = 100
	TOP_PAD = 150

	def __init__(self, width, height, lst):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Sorting Algorithm Visualization")
		self.set_list(lst)

	def set_list(self, lst):
		self.lst = lst
		self.min_val = min(lst)
		self.max_val = max(lst)

		self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
		self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
		self.start_x = self.SIDE_PAD // 2

def draw(draw_info, algo_name=0, ascending=0):
	draw_info.window.fill(draw_info.BACKGROUND_COLOR)

	# title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.GREEN)
	# draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2 , 5))

	# controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)
	# draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2 , 45))

	# sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.BLACK)
	# draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2 , 75))

	draw_list(draw_info)
	pygame.display.update()


def draw_list(draw_info,color_positions={}, clear_bg=False):
	lst = draw_info.lst

	for i, val in enumerate(lst):
		x = draw_info.start_x + i * draw_info.block_width
		y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

		color = draw_info.GRADIENTS[i % 3]
		if i in color_positions:
			color = color_positions[i] 

		pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
def generate_starting_list(n):
	l=[x for x in range(n)]
	random.shuffle(l)
	return l
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

	n = 50
	
	lst = generate_starting_list(n)
	draw_info = DrawInformation(800, 600, lst)
	sorting = False
	# ascending = True

	# sorting_algorithm = bubble_sort
	# sorting_algo_name = "Bubble Sort"
	# sorting_algorithm_generator = None

	while run:
		clock.tick(60)

		
		draw(draw_info)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type != pygame.KEYDOWN:
				continue

			if event.key == pygame.K_r:
				lst = generate_starting_list(n)
				draw_info.set_list(lst)
			elif event.key == pygame.K_SPACE:
				selection_sort(draw_info,lst,len(lst),toggle)


	pygame.quit()


if __name__ == "__main__":
	main()