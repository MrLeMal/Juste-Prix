import os
import json
from pathlib import Path


def clear_screen():
	"""Nettoie l'écran du terminal."""
	os.system('cls' if os.name == 'nt' else 'clear')


def load_scene_texts():
	"""Charge les textes d'affichage des scènes depuis le fichier JSON."""
	config_path = Path(__file__).parent.parent / "config" / "scenes_display.json"
	with open(config_path, "r", encoding="utf-8") as file:
		return json.load(file)
