import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_model():
    df = pd.read_csv("data/mvp_dataset.csv")
    X = df[['PTS_per_game', 'AST_TOV', 'PER']]
    y = df['Label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(class_weight="balanced", random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(classification_report(y_test, preds))

    with open("models/mvp_model.pkl", "wb") as f:
        pickle.dump(model, f)
        print("Model saved to models/mvp_model.pkl")

if __name__ == "__main__":
    train_model()
