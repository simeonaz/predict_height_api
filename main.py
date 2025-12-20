import pickle
import numpy as np
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

# Charger le modèle de régression linéaire
with open("model_taille.pkl", "rb") as f:
    model = pickle.load(f)


# Modèle Pydantic pour l'input
class AgeInput(BaseModel):
    age: int


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.post(
    "/predict",
    tags=["Prédiction de la taille"],
    description="Prédit la taille en fonction de l'âge.",
)
def predict_taille(input_data: AgeInput):
    age = np.array([[input_data.age]])
    taille_predite = model.predict(age)[0]
    return {"age": input_data.age, "taille_predite": round(taille_predite, 2)}
