import pygame
from logic import Core

size = (500, 500)
rect_width = 63
black = (0, 0, 0)
white = (255, 255, 255)
simil_black = (139, 69, 19)

pygame.init()
screen = pygame.display.set_mode(size)


def draw_field():
	count_line = 0
	count_column = 0

	for i in range(1, 65):
		if count_line in [0, 2, 4, 6]:
			if i % 2 == 0:
				pygame.draw.rect(screen, white, [count_column*rect_width, count_line*rect_width, rect_width, rect_width])
				if count_column < 7:
					count_column += 1
				else:
					count_column = 0
			else:
				pygame.draw.rect(screen, simil_black, [count_column*rect_width, count_line*rect_width, rect_width, rect_width])
				if count_column < 7:
					count_column += 1
				else:
					count_column = 0
		else:
			if i % 2 == 0:
				pygame.draw.rect(screen, simil_black, [count_column*rect_width, count_line*rect_width, rect_width, rect_width])
				if count_column < 7:
					count_column += 1
				else:
					count_column = 0
			else:
				pygame.draw.rect(screen, white, [count_column*rect_width, count_line*rect_width, rect_width, rect_width])
				if count_column < 7:
					count_column += 1
				else:
					count_column = 0

		if i in [item for item in range(1, 65) if item % 8 == 0]:
			count_line += 1


def main():
	counter = 1
	pos = [(31, 472), (94, 472), (157, 472), (220, 472), (283, 472), (346, 472), (409, 472), (472, 472), (31, 409), (94, 409), (157, 409), (220, 409), (283, 409), (346, 409), (409, 409), (472, 409), (31, 94), (94, 94), (157, 94), (220, 94), (283, 94), (346, 94), (409, 94), (472, 94), (31, 31), (94, 31), (157, 31), (220, 31), (283, 31), (346, 31), (409, 31), (472, 31)]
	draw_field()
	core = Core(screen)
	core.draw_board(pos)
	internal_command = False
	move = []
	go = True
	while go:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				go = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				position_click = event.pos
				if not internal_command:
					before_move = move
					before_internal_command = internal_command
					core.return_counter(counter)
					internal_command, move = core.move(position_click, pos, before_internal_command, before_move)[0], core.move(position_click, pos, before_internal_command, before_move)[1]
				elif internal_command and move:
					before_move = move
					before_internal_command = internal_command
					before_pos = pos
					core.return_counter(counter)
					internal_command, move, pos = core.move(position_click, before_pos, before_internal_command, before_move)[0], core.move(position_click, before_pos, before_internal_command, before_move)[1], core.move(position_click, before_pos, before_internal_command, before_move)[2]
					draw_field()
					core.draw_board(pos)
					counter += 1
				else:
					pass
			elif event.type == pygame.MOUSEWHEEL:
				starter_pos = [(31, 472), (94, 472), (157, 472), (220, 472), (283, 472), (346, 472), (409, 472), (472, 472), (31, 409), (94, 409), (157, 409), (220, 409), (283, 409), (346, 409), (409, 409), (472, 409), (31, 94), (94, 94), (157, 94), (220, 94), (283, 94), (346, 94), (409, 94), (472, 94), (31, 31), (94, 31), (157, 31), (220, 31), (283, 31), (346, 31), (409, 31), (472, 31)]
				draw_field()
				core.return_counter(counter)
				core.draw_board(starter_pos)
				internal_command = False
				move = []
				pos = starter_pos
				counter = 1
		pygame.display.flip()

	pygame.quit()


if __name__ == '__main__':
	main()

