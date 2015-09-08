import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))

offset = (160,60)

pygame.font.init()
font = pygame.font.SysFont("calibri",60)
font.set_bold(True)

class MenueAssets:

	button_surface = None
	background_surface = None

	def load_assets(style):
		menue_path = "Assets/"+style+"/Menue/"

		MenueAssets.button_surface = load_image(menue_path + "button.png")
		MenueAssets.background_surface = load_image(menue_path + "background.png")


class LobbyAssets:

	button_surface = None
	background_surface = None

	def load_assets(style):
		lobby_path = "Assets/"+style+"/Lobby/"

		LobbyAssets.button_surface = load_image(lobby_path + "button.png")
		LobbyAssets.background_surface = load_image(lobby_path + "background.png")

class ChessBoardAssets:

	black_pawn_surface = None
	white_pawn_surface = None
	board_surface = None

	def load_assets(style):
		piece_path = "Assets/"+style+"/Pieces/"
		tile_path = "Assets/"+style+"/Tiles/"

		ChessBoardAssets.black_pawn_surface = load_image(piece_path + "Pawn_Black.png")
		ChessBoardAssets.white_pawn_surface = load_image(piece_path + "Pawn_White.png")

		ChessBoardAssets.white_tile_surface = load_image(tile_path + "Tile_White.png")
		ChessBoardAssets.black_tile_surface = load_image(tile_path + "Tile_Black.png")

		ChessBoardAssets.background = load_image(tile_path + "background.png")


def load_image(path):
	surface = pygame.image.load(path).convert()
	surface.set_colorkey((0,100,100))

	return surface

def render_text(text, color = (0, 0, 0)):
	return font.render(text, 1, color)


