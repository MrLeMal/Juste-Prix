import time


class Scene:
	"""Classe de base pour toutes les scènes."""
	def __init__(self, game):
		self.game = game

	def display(self):
		"""Affiche la scène et retourne la scène suivante."""
		pass


class MenuScene(Scene):
	"""Scène du menu principal."""
	def display(self):
		menu_text = self.game.scene_texts["menu"]
		print(f"\n{menu_text['title']} (Joueur : {self.game.player_name})")
		for opt in menu_text["options"]:
			print(opt)
		while True:
			choice = input("Votre choix : ").strip()
			if choice == '1':
				return "game"
			elif choice == '2':
				return "settings"
			elif choice == '3':
				return "quit"
			else:
				print("Choix invalide. Veuillez entrer 1, 2 ou 3.")


class GameScene(Scene):
	"""Scène du jeu principal."""
	def display(self):
		game_text = self.game.scene_texts["game"]
		self.game.results_board = []
		for _ in range(self.game.articles_to_guess):
			article = self.game.get_random_article()
			price = article["prix"]
			attempts = 0
			found = False
			print(f"\n{game_text['title']}\nDevinez le prix de l'article : {article['nom']}")
			while not found and attempts < self.game.max_attempts:
				try:
					guess = int(input(game_text["prompt"]))
					attempts += 1
					if guess < price:
						print("C'est plus !")
					elif guess > price:
						print("C'est moins !")
					else:
						print(f"Bravo ! Vous avez trouvé le juste prix en {attempts} essais.")
						found = True
				except ValueError:
					print("Veuillez entrer un nombre valide.")
			self.game.results_board.append((article['nom'], price, attempts, found))
		print("Fin de la partie.")
		time.sleep(3)
		return "end"


class EndScene(Scene):
	"""Scène de fin de partie avec récapitulatif."""
	def display(self):
		end_text = self.game.scene_texts["end"]
		print(f"\n{end_text['title']}")
		print("--- Récapitulatif de la partie ---")
		for result in self.game.results_board:
			name, price, attempts, found = result
			status = "Trouvé" if found else "Non trouvé"
			print(f"Article : {name}")
			print(f"  Prix à trouver : {price} €")
			print(f"  Nombre d'essais effectués : {attempts}")
			print(f"  Statut : {status}\n")
		print("-------------------------------")
		for opt in end_text["options"]:
			print(opt)
		while True:
			choice = input(end_text["prompt"]).strip()
			if choice == '1':
				return "menu"
			elif choice == '2':
				return "game"
			elif choice == '3':
				return "quit"
			else:
				print("Choix invalide. Veuillez entrer 1, 2 ou 3.")


class SettingsScene(Scene):
	"""Scène de modification des paramètres."""
	def display(self):
		settings_text = self.game.scene_texts["settings"]
		print(settings_text["title"])

		while True:
			try:
				max_attempts = int(input(f"{settings_text['prompt_attempts']} (actuel: {self.game.max_attempts}): "))
				articles_to_guess = int(input(f"{settings_text['prompt_articles']} (actuel: {self.game.articles_to_guess}): "))
				player_name = input(f"{settings_text['prompt_name']} (actuel: {self.game.player_name}): ").strip()
				if player_name == '':
					player_name = self.game.player_name
				self.game.set_settings(max_attempts, articles_to_guess, player_name)
				print("Paramètres mis à jour avec succès.")
			except ValueError:
				print("Entrée invalide. Les paramètres n'ont pas été modifiés.")
			print("Que souhaitez-vous faire ?")
			print("1. Modifier à nouveau les paramètres")
			print("2. Retourner au menu principal")
			choice = input("Votre choix : ").strip()
			if choice == '1':
				continue
			elif choice == '2':
				return "menu"
			else:
				print("Choix invalide. Veuillez entrer 1 ou 2.")
