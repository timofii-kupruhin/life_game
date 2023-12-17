# 	---- modules ---- 
import numpy as np
import pygame as pg
import time, sys, os
import datetime
import random
import json
# 	---- modules ---- 

class Settings():
	# window size
	WINDOW_SIZE = (1080, 1080)
	display = pg.display.set_mode(WINDOW_SIZE)  # SETTING WINDOW SIZE

	# grid size | matrix size
	GRID = (270, 270)

	# calculating sizes of cells
	CELL_WIDTH, CELL_HEIGHT = WINDOW_SIZE[0] // GRID[0], WINDOW_SIZE[1] // GRID[1]
		
	# colors
	black = (0, 0, 0)
	red = (255, 0, 0)
	white = (255, 255, 255)
	beige = (250, 240, 190)
	green = (0, 255, 0)
	grey = (211, 211, 211)
	
	# setting fonts 
	pg.font.init()
	h4_font = pg.font.SysFont('Arial', 24)
	standart_font = pg.font.SysFont('Arial', 48)
	h1_font = pg.font.SysFont('Arial', 72)
	mega_font = pg.font.SysFont('Arial', 144)
	
	# menu text
	welcome_text = h1_font.render("Welcome to the Game !!!", False, black)
	welcome_text_rect = welcome_text.get_rect(center=(WINDOW_SIZE[0] // 2, 200))
	
	# menu list
	start_game_text = standart_font.render("Start game", False, black)
	start_game_text_rect = start_game_text.get_rect(center=(WINDOW_SIZE[0] // 2, 550))

	draw_mode_text = standart_font.render("Draw mode", False, black)
	draw_mode_text_rect = draw_mode_text.get_rect(center=(WINDOW_SIZE[0] // 2, 600))

	saves_text = standart_font.render("Saved games", False, black)
	saves_text_rect = saves_text.get_rect(center=(WINDOW_SIZE[0] // 2, 700))
	
	exit_text = standart_font.render("Exit", False, black)
	exit_text_rect = exit_text.get_rect(center=(WINDOW_SIZE[0] // 2, 650))

	# game text 
	generation_text = standart_font.render("Generation 0", False, white, black)
	generation_text_rect = generation_text.get_rect(center=(WINDOW_SIZE[0] // 2, 60)) # making rect behind text

	make_save_text = standart_font.render("Save", False, white, black)
	make_save_text_rect = make_save_text.get_rect(center=(150, 60))

	completed_save_text = mega_font.render("Saved", False, green)
	completed_save_text_rect = completed_save_text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))

	menu_text = standart_font.render("Menu", False, white, black)
	menu_text_rect = menu_text.get_rect(center=(960, 60))

	# buttons coords
	menu_btn_coords = [start_game_text_rect, draw_mode_text_rect, saves_text_rect, exit_text_rect]
	game_btn_coords =  [make_save_text_rect, menu_text_rect]

	FPS = 60
	clock = pg.time.Clock()

	def refresh(self):
		pg.display.update()
		self.clock.tick(self.FPS)
