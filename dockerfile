# Utiliser l'image officielle Python 3.10.12
FROM python:3.10.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY . /app

# Installer les dépendances à partir de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Charger les variables d'environnement à partir du fichier .env
# Si vous utilisez python-dotenv dans votre application, cela fonctionne directement
RUN pip install python-dotenv

# Exposer le port utilisé par Streamlit (port 8501)
EXPOSE 8501

# Commande pour démarrer l'application Streamlit
CMD ["streamlit", "run", "app.py"]