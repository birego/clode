# Utilisez une image Python officielle comme base
FROM python:3.8-slim

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt et installez les dépendances
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiez tous les fichiers de votre application dans le conteneur
COPY . .

# Exposez le port sur lequel votre application Flask écoute
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "app.py"]
