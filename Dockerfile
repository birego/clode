# Utilisez une image de base Python
FROM python:3.8

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de votre application dans le conteneur
COPY . /app

# Installez les dépendances de l'application
RUN pip install Flask scikit-learn

# Exposez le port sur lequel l'application Flask écoute
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "app.py"]
