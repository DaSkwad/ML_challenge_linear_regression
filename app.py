import joblib
import numpy as np

model = joblib.load("models/model_regression.pkl")
scaler_X = joblib.load("models/scaler_x.pkl")
scaler_y = joblib.load("models/scaler_y.pkl")

print("Bienvenue dans l'outil de prédiction des ventes.")

while True:

    tv = float(input("Montant de l'investissement TV : "))
    radio = float(input("Montant de l'investissement Radio : "))

    X_input = np.array([[tv, radio]])
    X_scaled = scaler_X.transform(X_input)

    y_pred_scaled = model.predict(X_scaled)
    y_pred = scaler_y.inverse_transform(y_pred_scaled)

    print(f"Estimation des ventes : {y_pred}")

    continuer = input("Souhaitez-vous prédire d'autres ventes ? (o/n)").strip().lower()
    if continuer != "o":
        break