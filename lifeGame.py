# 	---- modules ---- 
from menu import * 
# 	---- modules ---- 

class Game(Menu):
	show_saved_text = False

	def draw_grid(self):
		# vertical lines
		for x in np.arange(0, self.WINDOW_SIZE[0], self.CELL_WIDTH):
			pg.draw.line(self.display, self.black, (x, 0), (x, self.WINDOW_SIZE[1]))
		
		# horizontal lines
		for y in np.arange(0, self.WINDOW_SIZE[1], self.CELL_HEIGHT):
			pg.draw.line(self.display, self.black, (0, y), (self.WINDOW_SIZE[0], y))

	def draw_matrix(self):
		x, y = 0, 0 # coords

		for lst in self.matrix:
			for num in lst:
				if num: # red if 1
					pg.draw.rect( self.display, self.red, [x, y, self.CELL_WIDTH, self.CELL_HEIGHT]) 
				else: # white if 0
					pg.draw.rect( self.display, self.white, [x, y, self.CELL_WIDTH, self.CELL_HEIGHT])
				x += self.CELL_WIDTH # moving right
			x = 0; y += self.CELL_HEIGHT # moving down

	def game_of_life(self):	
		back = 0 # variable that doesnt access move out the array
		count = 0 # count of 1 in lists
		start, end = 0, 0 # np.arange of lists

		for lst in np.arange(len(self.matrix)): 
			for num in np.arange(len(self.matrix[lst])):
				# checking element position 
				if num-1 < 0: 
					back = 0
				else: back = 1	
				# checking array positions
				# in the middle of matrix
				if lst > 0 and lst < len(self.matrix)-1:	
					start, end = -1, 2		
				# start of matrix
				elif lst == 0:
					start, end = 0, 2	
				# at the end
				elif lst == len(self.matrix)-1:
					start, end = -1, 1

				# counting 1	
				count = sum([np.count_nonzero(self.matrix[lst+i][num-back:num+2]) for i in np.arange(start, end)])
				
				# GAME CONDITIONS "life game"
				if self.matrix[lst][num] == 1 and count < 2 or count > 3:
					self.matrix[lst][num] = 0
					
				elif self.matrix[lst][num] == 0 and count >= 3:
					self.matrix[lst][num] = 1
	
	def make_save(self):
		current_date = str(datetime.datetime.now().date()) # date for today
		if not os.path.exists("saves"): # if folder not exist 
			os.mkdir("saves") # create

		data = {"matrix": self.matrix.tolist(), "generation": self.generation, "date":current_date} # data dict
		
		with open(f"saves/save{random.randrange(0, 200000)}_{current_date}.json", 'w') as f:
			json.dump(data, f) 
			f.close()

	def start_game(self):
		# restarting game every time we calling this method
		# you can choose amount of dots in matrix the first arg (in percents)
		self.matrix = np.random.choice([1, 0], size = self.GRID, p=[0.7, 0.3]) 
		self.generation = 0

		while 1:
			self.display.fill(self.white)

			self.game_of_life()
			self.draw_matrix()
			self.draw_grid()

			self.generation += 1 # counting generation
			
			# You can choose cooldown 
			time.sleep(0.3)

			# placing text 
			self.generation_text = self.standart_font.render(f'Generation {self.generation}', False, self.white, self.black)				
			self.display.blit(self.generation_text, self.generation_text_rect)
			self.display.blit(self.make_save_text, self.make_save_text_rect)
			self.display.blit(self.menu_text, self.menu_text_rect)
			
			for event in pg.event.get():
				if event.type == pg.MOUSEBUTTONDOWN:
					if self.is_pressed(event.pos, True) == 2:
						self.menu(); return 

				self.mouse_events(event, True)
				self.keyboard_events(event)
				self.quit_event(event)
			
			self.refresh()
		
	def run(self):
		pg.init()
		pg.display.set_caption("Game of Life")
		while 1:
			self.menu()		
						
	def quit(self):
		pg.quit(); sys.exit()

def main():
	game = Game()
	game.run()

if __name__== "__main__":
	main()