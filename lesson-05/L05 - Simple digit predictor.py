
from sklearn.datasets import fetch_openml 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

# Load Menist dataset from openMl
menist = fetch_openml("mnist_784", version=1)

# Data preprocessing 
x = menist["data"] / 255.0 # Normalise the data (pixels between 0 and 1)
y = menist["target"].astype(int) # Labels (Digits 0 until 9)

# Split the data into training and test datasets
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.2, random_state=42) 

# Create and train logistic regresssion model
model = LogisticRegression(max_iter=10000) 
model.fit(xTrain, yTrain)

# Evaluate the model
yPrediction = model.predict(xTest)
accuracy = metrics.accuracy_score(yTest, yPrediction)
print(f"Test accuracy = {accuracy}")

# Display the first five test images and their predictive labels
correctPredictions = 0
wrongPredictions = 0
for i in range(10):
    plt.imshow(xTest.iloc[i].values.reshape(28, 28), cmap=plt.cm.binary) 
    plt.title(f"Predicted = {yPrediction[i]}, actual = {yTest.iloc[i]}")

    # Check if correct
    if yPrediction[i] == yTest.iloc[i]:
        correctPredictions += 1
    else: 
        wrongPredictions += 1

    plt.show()

# Show final Score
print(f"The ai had {correctPredictions} correct predictions")
print(f"and {wrongPredictions} wrong predictions")
