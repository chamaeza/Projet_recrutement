import os
import subprocess
from datetime import datetime, timedelta
import random

# --- CONFIGURATION ---
YEAR = 2023
TOTAL_COMMITS = 176  # <-- Nombre de commits pour le Projet 1
file_path = "info.txt"

# --- FONCTION POUR EXÉCUTER DES COMMANDES GIT ---
def run_git(command):
    subprocess.run(command, shell=True, text=True, capture_output=True)

# --- GÉNÉRATION DES DATES ALÉATOIRES ---
start_date = datetime(YEAR, 1, 1)
end_date = datetime(YEAR, 12, 31)
total_days = (end_date - start_date).days

# On tire 176 jours au hasard dans l'année et on les trie
random_days = sorted(random.sample(range(total_days + 1), TOTAL_COMMITS))

print(f"Génération de {TOTAL_COMMITS} commits pour l'année {YEAR}...")

# --- BOUCLE PRINCIPALE ---
for i, day_offset in enumerate(random_days):
    # Calcul de la date exacte
    current_date = start_date + timedelta(days=day_offset)
    # On ajoute une heure aléatoire pour faire plus réaliste
    current_date = current_date.replace(hour=random.randint(8, 22), minute=random.randint(0, 59))
    
    date_str = current_date.strftime("%Y-%m-%dT%H:%M:%S")
    
    # 1. Écrire dans le fichier
    with open(file_path, "a") as f:
        f.write(f"Projet 2023 - Commit n°{i+1} du : {date_str}\n")
    
    # 2. Ajouter et Commit
    run_git("git add .")
    commit_message = f"Update Projet 1 - {date_str[:10]}"
    
    # 3. Forcer la date
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    
    subprocess.run(
        f'git commit -m "{commit_message}"',
        shell=True,
        env=env,
        capture_output=True,
        text=True
    )
    
    print(f"Commit {i+1}/{TOTAL_COMMITS} créé pour le : {date_str}")

print("Terminé !")