# Predict Height API

Une API FastAPI simple pour prédire la taille d'une personne basée sur son âge, utilisant un modèle de régression linéaire.

## 🚀 Fonctionnalités

- Prédiction de taille à partir de l'âge
- Interface API RESTful
- Documentation automatique avec Swagger

## 📦 Installation

1. Clonez le repository :
   ```bash
   git clone https://github.com/simeonaz/predict_height_api.git
   cd predict_height_api
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Assurez-vous que le modèle `model_taille.pkl` est présent (généré à partir du notebook).

## 🏃 Utilisation

Lancez l'API :
```bash
uvicorn main:app --reload
```

L'API sera accessible sur `http://127.0.0.1:8000`.

## 📋 Endpoints

- `GET /` : Message de bienvenue
- `POST /predict` : Prédire la taille
  - Body : `{"age": 25}`
  - Response : `{"age": 25, "taille_predite": 175.0}`

Consultez la documentation complète sur `http://127.0.0.1:8000/docs`.

## 🛠 Technologies

- FastAPI
- Scikit-learn
- NumPy
- Pydantic

## 📄 Licence

MIT
