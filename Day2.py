from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report,precision_score,recall_score,f1_score
import pandas as pd


#Load data frame
df = pd.read_csv("ML/Titanic-Dataset.csv")

print(df.head())

#Data cleaning

print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())

df.dropna(inplace=True)

print(df.isnull().sum())

#Feature selection

df["Sex"] = pd.factorize(df['Sex'])[0]

x = df[["Pclass","Sex","Age","Fare"]]

y = df["Survived"]

#split data

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#model traning

model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(f"Precision: {precision_score(y_test, y_pred):.3f}")
print(f"Recall: {recall_score(y_test, y_pred):.3f}")
print(f"F1 Score: {f1_score(y_test, y_pred):.3f}")

# Predict on new person

new_person = [[1,0,30,200]]
print("\nPredicted:", model.predict(new_person)[0])
print("Probability:", model.predict_proba(new_person))

