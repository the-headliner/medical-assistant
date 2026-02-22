import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# 1️⃣ Load dataset
data_path = os.path.join(os.path.dirname(__file__), "dataset.csv")
df = pd.read_csv(data_path)

# 2️⃣ Split features and target
X = df.drop("disease", axis=1)
y = df["disease"]

# 3️⃣ Train-test split (real engineering practice)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4️⃣ Initialize model
model = RandomForestClassifier()

# 5️⃣ Train model
model.fit(X_train, y_train)

# 6️⃣ Quick evaluation
accuracy = model.score(X_test, y_test)
print(f"Model trained successfully.")
print(f"Validation Accuracy: {accuracy:.2f}")

# 7️⃣ Save trained model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
joblib.dump(model, model_path)

# 8️⃣ Save feature columns (VERY IMPORTANT)
features_path = os.path.join(os.path.dirname(__file__), "features.pkl")
joblib.dump(X.columns.tolist(), features_path)

print("Model and features saved successfully.")