Détection de Changement de Voie (Cut-In) pour Véhicules Autonomes
Cette implémentation est une extension de recherche basée sur l'architecture YOLOv8, optimisée pour la détection en temps réel des véhicules s'insérant dans la voie de circulation. Ce projet explore l'intersection de la Vision par Ordinateur et de la Sécurité des Systèmes Autonomes.

Caractéristiques Techniques
Modèle: YOLOv8 (Ultralytics) pour une inférence à faible latence.

Analyse de Performance: Script de profilage inclus pour mesurer la latence d'inférence (ms) et les images par seconde (FPS).

Objectif de Recherche: Évaluer la robustesse du modèle face aux changements brusques de trajectoire dans des environnements urbains denses.

Installation
Créez un environnement virtuel : python -m venv venv

Installez les dépendances : pip install -r requirements.txt

Lancez l'analyse de déploiement : python deployment_stats.py

Vision et Impact
Dans le cadre de mon Master en Informatique à UTEP, ce projet sert de base pour l'étude de la sécurité cyber-physique. L'objectif est de garantir que les systèmes d'aide à la conduite (ADAS) restent résilients face aux données bruitées ou aux cyber-attaques adverses.