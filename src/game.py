import json
from pathlib import Path
from .utils import load_scene_texts


class Game:
	def __init__(self):
		self.settings = self.load_settings()
		self.player_name = self.settings["player_settings"]["player_name"]
		self.max_attempts = self.settings["game_settings"]["max_attempts"]
		self.articles_to_guess = self.settings["game_settings"]["articles_to_guess"]
		self.scene_texts = load_scene_texts()
		# Import ici pour éviter les dépendances circulaires
		from .scenes import MenuScene, GameScene, EndScene, SettingsScene
		self.scenes = {
			"menu": MenuScene(self),
			"game": GameScene(self),
			"end": EndScene(self),
			"settings": SettingsScene(self)
		}
		self.current_scene = "menu"
		self.results_board = []

	def load_settings(self):
		"""Charge les paramètres du jeu depuis settings.json."""
		config_path = Path(__file__).parent.parent / "config" / "settings.json"
		try:
			with open(config_path, "r", encoding="utf-8") as file:
				settings = json.load(file)
				return settings
		except FileNotFoundError:
			default_settings = {
				"game_settings": {
					"max_attempts": 10,
					"articles_to_guess": 2
				},
				"player_settings": {
					"player_name": "Player1"
				}
			}
			with open(config_path, "w", encoding="utf-8") as file:
				json.dump(default_settings, file, indent=4)
			return default_settings

	def set_settings(self, max_attempts, articles_to_guess, player_name=None):
		"""Modifie les paramètres du jeu et les sauvegarde."""
		self.settings["game_settings"]["max_attempts"] = max_attempts
		self.settings["game_settings"]["articles_to_guess"] = articles_to_guess
		if player_name is not None:
			self.settings["player_settings"]["player_name"] = player_name
			self.player_name = player_name
		self.max_attempts = max_attempts
		self.articles_to_guess = articles_to_guess
		config_path = Path(__file__).parent.parent / "config" / "settings.json"
		with open(config_path, "w", encoding="utf-8") as file:
			json.dump(self.settings, file, indent=4)

	def get_random_article(self):
		"""Retourne un article aléatoire depuis articles.json."""
		from random import randint
		config_path = Path(__file__).parent.parent / "config" / "articles.json"
		with open(config_path, "r", encoding="utf-8") as file:
			articles = json.load(file)
			index = randint(0, len(articles) - 1)
		return articles[index]

	def run(self):
		"""Boucle principale du jeu."""
		from .utils import clear_screen
		print("Bienvenue dans le jeu du Juste Prix !")
		while True:
			clear_screen()
			next_scene = self.scenes[self.current_scene].display()
			if next_scene == "quit":
				print("Merci d'avoir jouer au juste prix. À bientôt !")
				break
			self.current_scene = next_scene
