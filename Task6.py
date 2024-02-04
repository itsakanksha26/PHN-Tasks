import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def generate_dataset(num):
    X = np.random.uniform(low=-10, high=10, size=(num, 2))
    m = np.random.uniform(low=-5, high=5, size=num)
    b = np.random.uniform(low=-10, high=10, size=num)
    y = m * X[:, 0] + b
    return X, y

num = 1000
X, y = generate_dataset(num)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print("Train R-squared:", train_score)
print("Test R-squared:", test_score)

new_input = np.array([[1.5, 2.7]])
new_input_scaled = scaler.transform(new_input)
pred_output = model.predict(new_input_scaled)
print("Predicted output:", pred_output)
