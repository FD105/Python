import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

data = {
    'Hours_Studied': [10,5,7,11,1,4,9,3,5,2,12,0,5,9,2,4,7,10,11,4], # Anzahl der Lernstunden
    'Score': [93,45,63,97,9,39,85,20,50,17,100,1,40,88,12,33,69,91,95,35] # Zugehörige Testergebnisse
}

df = pd.DataFrame(data) # Dictionary in ein Pandas-DataFrame umwandeln

X = df[['Hours_Studied']] # Eingabedaten
y = df['Score'] # Zielwerte

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 21)
# Daten für Testen und Trainieren aufteilen (80% Training, 20% Test)

model = LinearRegression() #Lineares Regressionsmodell erstellen
model.fit(X_train, y_train) # Modell anhand der Trainingsdaten trainieren

y_pred = model.predict(X_test) # Vorhersagen für die Testdaten erstellen
y_pred = np.clip(y_pred, 0, 100) # Wertebereich der Vorhersage auf 0 bis 100 begrenzen
print("Actual Scores:", y_test) # Tatsächliche Testergebnisse ausgeben
                                # die Ausgabe zeigt die Stelle in Hours_Studied an, 
                                # wo dann die Stundenanzahl steht
print("Predicted Scores:", y_pred) # Vorhergesagte Testergebnisse ausgeben

mse = mean_squared_error(y_test, y_pred) # Fehler bestimmen
print("Mean Squared Error:", mse) # Fehler ausgeben

X_1d = X['Hours_Studied'].values # Lernstunden als eindimensionales Numpy-Array speichern
y_pred_full = model.predict(X).flatten() # Vorhersage für alle Datenpunkte berechnen und 
                                         # in ein eindimensionales Array umwandeln


plt.scatter(X_1d, y, color = 'blue', label = 'Actual Score')
plt.plot(X_1d, y_pred_full, color = 'red', label = 'Predicted Line')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.title('Hours Studied vs. Score Prediction')
plt.legend()
plt.show()