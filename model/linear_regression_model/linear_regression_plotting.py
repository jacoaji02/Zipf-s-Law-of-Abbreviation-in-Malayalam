import csv
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

words = []
lengths = []
freqs = []

with open("word_frequency.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
     
    for i, row in enumerate(reader):

        # if i >= 10:
        #     break
        
        words.append(row["word"])
        lengths.append(int(row["length"]))
        freqs.append(int(row["frequency"]))

X = np.array(lengths).reshape(-1, 1)
y = np.log(np.array(freqs))

model = LinearRegression()
model.fit(X, y)

print("===== Linear Regression on first 10 most frequent malayalam Words =====")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("R² Score:", model.score(X, y))

plt.figure(figsize=(10, 6))

plt.scatter(X, y, alpha=0.7, label="Data Points")

# Regression line
x_range = np.linspace(min(X), max(X), 100).reshape(-1, 1)
y_pred = model.predict(x_range)

plt.plot(x_range, y_pred, linewidth=2, label="Regression Line")

plt.title("Linear Regression on 10 most Malayalam Words", fontsize=12)
plt.xlabel("Word Length", fontsize=10)
plt.ylabel("Word Frequency", fontsize=10)
plt.grid(True)
plt.legend()

plt.show()

