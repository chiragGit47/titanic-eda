import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error 
import numpy as np 


# Load the dataset

df = pd.read_csv("ML/Salary Data.csv")

#data cleaning
df["Department"] = pd.factorize(df['Department'])[0]
df["Gender"] = pd.factorize(df['Gender'])[0]
df["Education"] = pd.factorize(df['Education'])[0]

print(df.isnull())

df.dropna(inplace=True)

print(df.isnull().sum())


# Step 3: split
x= df[["Age","Gender","Education","Department","Experience"]]
print(x.shape)
y= df["Salary"]
print(y.shape)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# Step 4: train
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: evaluate
print("Score:", model.score(X_test, y_test))

mae = mean_absolute_error(y_test, model.predict(X_test)) 
rmse = np.sqrt(mean_squared_error(y_test, model.predict(X_test))) 

new_person = [[25, 1,2,2,0]]  # age 25, 2 years experience
print("Predicted salary:", model.predict(new_person))


print(f"R² Score: {model.score(X_test, y_test):.3f}") 
print(f"MAE: ₹{mae:.2f}") 
print(f"RMSE: ₹{rmse:.2f}")

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"Train R²: {train_score:.3f}")
print(f"Test R²: {test_score:.3f}")

if train_score - test_score > 0.1:
    print("⚠️ Possible overfitting detected!")
else:
    print("✓ Model generalizes well")

