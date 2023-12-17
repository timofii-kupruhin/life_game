# 	---- modules ---- 
from settings import * 
# 	---- modules ---- 

class Menu(Settings):
	def is_pressed(self, mouse_coords, game_running=False):
		buttons = self.game_btn_coords if game_running else self.menu_btn_coords

		for button in buttons:
			if button.left < mouse_coords[0] < button.right \
				and button.top < mouse_coords[1] < button.bottom:
					return buttons.index(button)+1

	def show_saves(self):
		self.display.fill(self.beige)  # background
		saves = os.listdir("saves")[::-1]
		y = 200

		for save in range(len(saves)):
			s = saves[save].split("_")
			save_text = self.standart_font.render(f"Save № {s[0]}, date: {s[1].split('.')[0]}", False, self.black)
			save_text_rect = save_text.get_rect(center=((self.WINDOW_SIZE[0] // 2)-100, y))
			self.display.blit(save_text, save_text_rect)
			y += 100
					
		while 1:
			for event in pg.event.get():
				if event.type == pg.MOUSEBUTTONDOWN:
					if self.is_pressed(event.pos, True) == 2:
						self.menu(); return 
			
				self.quit_event(event)
				
				# self.mouse_events(event)
			
			self.display.blit(self.menu_text, self.menu_text_rect)
			self.refresh()
			
	def draw_mode(self):
		...

	def menu(self):
		self.display.fill(self.beige) # background
		# menu text 
		self.display.blit(self.welcome_text, self.welcome_text_rect)
		self.display.blit(self.start_game_text, self.start_game_text_rect)
		# self.display.blit(self.draw_mode_text, self.draw_mode_text_rect)
		# self.display.blit(self.saves_text, self.saves_text_rect)
		self.display.blit(self.exit_text, self.exit_text_rect)
		
		for event in pg.event.get():
			self.mouse_events(event)
			self.quit_event(event)

		self.refresh()
	
	def mini_menu(self, game_running=False):
		self.display.fill(self.beige) # background

		while 1:
			if not game_running:
				...
			else:
				...
			self.refresh()

	# events handlers
	def quit_event(self, event):
		if event.type == pg.QUIT:
			self.quit()

		if event.type == pg.KEYDOWN: # if button is pressed:	
			if event.key == pg.K_ESCAPE: # quit
				self.quit()
	# mouse events
	def mouse_events(self, event, game_running=False):
		if event.type == pg.MOUSEBUTTONDOWN:
			if game_running:
				# game buttons events			
				if self.is_pressed(event.pos, True) == 1:  # 1 - save game
					self.make_save() # making save
					self.show_saved_text = True
					if self.show_saved_text:
						self.display.blit(self.completed_save_text, self.completed_save_text_rect)
						current_time = time.time()  # show time text - 3 seconds

						if current_time - 0 >= 3:
							self.show_saved_text = False
			else:
				# function is returning a index of button in self.btn_list
				if self.is_pressed(event.pos) == 1: # 1 - start game 
					self.start_game(); return
				# elif self.is_pressed(event.pos) == 2: # 2 - draw mode
				# 	self.draw_mode(); return
				# elif self.is_pressed(event.pos) == 3: # 3 - saves
				# 	self.show_saves(); return	
				elif self.is_pressed(event.pos) == 4: # 4 - Exit 
					self.quit()
	# keyboard events
	def keyboard_events(self, event):
		if event.type == pg.KEYDOWN: # if button is pressed:	
			if event.key == pg.K_TAB: # menu on tab
				self.menu(); return