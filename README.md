![Advertising](img/advertising.jpeg)

Ce projet propose un défi pédagogique en **Machine Learning** visant à entraîner un modèle de **régression linéaire** pour prédire une variable continue à partir de données d'entrée.  
Il est conçu pour mettre en pratique les concepts fondamentaux de la régression linéaire appliquée à un problème de prédiction.

## Objectifs pédagogiques

- Comprendre les étapes de prétraitement des données  
- Apprendre à construire et entraîner un modèle de régression linéaire  
- Évaluer les performances du modèle sur des données de test  

## Prérequis

- Python ≥ 3.10  
- Environnement Jupyter (ou autre IDE compatible)  
- Bibliothèques de Machine Learning (par exemple, scikit-learn)  
- Connaissances en apprentissage automatique  

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/Sengsathit/Teaching-ML_challenge_linear_regression.git
   cd Teaching-ML_challenge_linear_regression
   ```

2. Créez un environnement virtuel (optionnel mais recommandé) :

   ```bash
   python -m venv venv
   source venv/bin/activate  # ou .\venv\Scripts\activate sous Windows
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Lancez le notebook :

   ```bash
   jupyter notebook
   ```

## Structure du projet

- `challenge_linear_regression.ipynb` : notebook principal illustrant le processus de régression linéaire  
- `data/` : dossier contenant les données utilisées pour l'entraînement et le test  
- `img/` : ressources visuelles pour la présentation  
- `models/` : dossier pour enregistrer les modèles entraînés  
- `app.py` : script pour déployer une application simple utilisant le modèle entraîné  
- `requirements.txt` : liste des dépendances Python nécessaires