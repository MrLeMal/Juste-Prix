# Jeu du Juste Prix

Un jeu en console où le joueur doit deviner le prix de différents articles avec un nombre d'essais limité.

## Fonctionnalités

- **Menu principal** : Joueur, Paramètres, Quitter
- **Jeu interactif** : Devinez les prix d'articles avec des indices "C'est plus !" ou "C'est moins !"
- **Paramètres personnalisables** : Nombre d'essais, nombre d'articles à deviner, nom du joueur
- **Récapitulatif de partie** : Voir le résumé des articles trouvés ou non
- **Architecture modulaire** : Code bien organisé en fichiers et dossiers séparés

## Structure du projet

```
JustePrix/
├── main.py                    # Point d'entrée principal
├── src/                       # Code source
│   ├── __init__.py
│   ├── game.py               # Classe Game (logique du jeu)
│   ├── scenes.py             # Classes des différentes scènes
│   └── utils.py              # Fonctions utilitaires
├── config/                    # Fichiers de configuration
│   ├── articles.json         # Liste des articles à deviner
│   ├── settings.json         # Paramètres du jeu
│   └── scenes_display.json   # Textes d'affichage
└── README.md                  # Cette documentation
```

## Installation

### Prérequis

- Python 3.7+
- Aucune dépendance externe (utilise uniquement la stdlib)

### Étapes

1. Clonez ou téléchargez le projet puis se rendre dans le dossier depuis le terminal:
```bash
cd JustePrix
```

2. (Optionnel) Créez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```


## Utilisation

Lancez le jeu avec :

```bash
python main.py
```

### Menu Principal

- **1. Jouer** : Démarrer une nouvelle partie
- **2. Paramètres** : Modifier les paramètres du jeu (nombre d'essais, nombre d'articles, nom du joueur)
- **3. Quitter** : Quitter le jeu

### Déroulement d'une partie

1. Le jeu affiche le nom d'un article
2. Vous devez proposer un prix
3. Le jeu vous indique si c'est "plus" ou "moins"
4. Continuez jusqu'à trouver le juste prix ou épuiser vos essais
5. À la fin, consultez le récapitulatif de votre performance

## Personnalisation

### Ajouter des articles

Modifiez `config/articles.json` :
```json
[
  {"nom": "Votre article", "prix": 5000},
  ...
]
```

### Modifier les textes

Modifiez `config/scenes_display.json` pour personnaliser les messages affichés.

## Architecture

Le projet utilise un **pattern de scènes** :
- `Scene` : classe de base pour toutes les scènes
- `MenuScene` : menu principal
- `GameScene` : écran de jeu
- `EndScene` : récapitulatif de fin
- `SettingsScene` : modification des paramètres

Cette architecture rend le code **modulaire** et **facile à étendre**.

## Auteur

Créé par MrLeMal avec utilisation de copilot pour test.

## Licence

Libre d'utilisation.
