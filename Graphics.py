import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))

offset = (160,60)

pygame.font.init()
font = pygame.font.SysFont("calibri", 60)
font.set_bold(True)

font_small = pygame.font.SysFont("calibri", 24)
font_small.set_bold(True)

tile_size = 60

style = "Default"

class MenueAssets:

	button_surface = None
	background_surface = None

	def load_assets():
		menue_path = "Assets/"+style+"/Menue/"

		MenueAssets.button_surface = load_image(menue_path + "button.png")
		MenueAssets.background_surface = load_image(menue_path + "background.png")


class LobbyAssets:

	button_surface = None
	background_surface = None
	player_slot_surface = None
	button_small_surface = None

	def load_assets():
		lobby_path = "Assets/"+style+"/Lobby/"

		LobbyAssets.button_surface = load_image(lobby_path + "button.png")
		LobbyAssets.background_surface = load_image(lobby_path + "background.png")
		LobbyAssets.button_small_surface = load_image(lobby_path + "button_small.png")
		LobbyAssets.player_slot_surface = load_image(lobby_path + "player_slot.png")

class ChessBoardAssets:

	black_pawn_surface = None
	white_pawn_surface = None
	board_surface = None

	def load_assets():
		piece_path = "Assets/"+style+"/Pieces/"
		tile_path = "Assets/"+style+"/Tiles/"

		ChessBoardAssets.black_pawn_surface = load_image(piece_path + "Pawn_Black.png")
		ChessBoardAssets.white_pawn_surface = load_image(piece_path + "Pawn_White.png")

		ChessBoardAssets.white_tile_surface = load_image(tile_path + "Tile_White.png")
		ChessBoardAssets.black_tile_surface = load_image(tile_path + "Tile_Black.png")

		ChessBoardAssets.background = load_image(tile_path + "background.png")

		ChessBoardAssets.possible_move = get_transparent_color_surface(tile_size, tile_size, (135, 230, 153), 100)
		ChessBoardAssets.possible_capture = get_transparent_color_surface(tile_size, tile_size, (189, 69, 45), 100)
		ChessBoardAssets.selected_piece = get_transparent_color_surface(tile_size, tile_size, (50, 50, 150), 100)

		ChessBoardAssets.numbers = []
		ChessBoardAssets.letters = []
		letters = list("ABCDEFGH")
		for n in range(8):
			ChessBoardAssets.numbers.append(render_text(str(n+1)))
			ChessBoardAssets.letters.append(render_text(letters[n]))



def load_image(path):
	surface = pygame.image.load(path).convert()
	surface.set_colorkey((0,100,100))

	return surface

def render_text(text, color = (0, 0, 0), font_size = 'big'):
	if font_size == 'big':
		return font.render(text, 1, color)
	elif font_size == 'small':
		return font_small.render(text, 1, color)

def get_transparent_color_surface(w, h, color, alpha):
	s = pygame.Surface((w, h))
	s.set_alpha(alpha)
	s.fill(color)
	
	return s
