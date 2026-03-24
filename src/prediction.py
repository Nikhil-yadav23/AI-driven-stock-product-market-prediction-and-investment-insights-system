from preprocessing import load_data, clean_data
from model import train_model

# Load data
df = load_data('data/stock.csv')
df = clean_data(df)

# Features and target
X = df[['Open', 'High', 'Low']]
y = df['Close']

# Train model
model = train_model(X, y)

# Predict
predictions = model.predict(X)

print("Sample Predictions:", predictions[:5])
