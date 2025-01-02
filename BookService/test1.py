import os

# Spécifiez le chemin du fichier JSON
file_path = 'instance.txt'

# Vérifier si le fichier existe
if not os.path.exists(file_path):
    # Si le fichier n'existe pas, on le crée avec des données vides ou par défaut
    with open(file_path, 'w') as file:
        # Par exemple, créer un dictionnaire vide ou ajouter des données par défaut
        file.write("instance=1")
    print(f"Le fichier {file_path} a été créé avec des données vides.")
else:
    # Si le fichier existe, le lire
    with open(file_path, 'r') as file:
        data = file.read()
    print(data)
