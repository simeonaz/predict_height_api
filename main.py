import pickle
import numpy as np
from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurer CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://predict-height-simeon-azogbonon.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Charger le modèle de régression linéaire
with open("model_taille.pkl", "rb") as f:
    model = pickle.load(f)


# Modèle Pydantic pour l'input
class AgeInput(BaseModel):
    age: int


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get(
    "/ping",
    tags=["Maintenir l'app active"],
)
def ping():
    return {"status": "alive"}


@app.post(
    "/predict",
    tags=["Prédiction de la taille"],
    description="Prédit la taille en fonction de l'âge.",
)
def predict_height(input_data: AgeInput):
    age = np.array([[input_data.age]])
    taille_predite = model.predict(age)[0]
    return {"age": input_data.age, "taille_predite": round(taille_predite, 2)}
