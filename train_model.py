import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

def generate_sample_data(n_samples=1000):
    """Generate sample house data for training"""
    np.random.seed(42)
    
    # Generate realistic house features
    square_feet = np.random.normal(2000, 500, n_samples)
    bedrooms = np.random.randint(1, 6, n_samples)
    bathrooms = np.random.randint(1, 4, n_samples)
    age = np.random.randint(0, 50, n_samples)
    distance_to_city = np.random.uniform(0, 30, n_samples)
    
    # Create a realistic price formula with some noise
    base_price = 200000
    price_per_sqft = 150
    bedroom_bonus = 25000
    bathroom_bonus = 15000
    age_penalty = 1000
    distance_penalty = 5000
    
    prices = (base_price + 
              square_feet * price_per_sqft + 
              bedrooms * bedroom_bonus + 
              bathrooms * bathroom_bonus - 
              age * age_penalty - 
              distance_to_city * distance_penalty + 
              np.random.normal(0, 20000, n_samples))
    
    # Ensure prices are positive
    prices = np.maximum(prices, 50000)
    
    data = pd.DataFrame({
        'square_feet': square_feet,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'age': age,
        'distance_to_city': distance_to_city,
        'price': prices
    })
    
    return data

def train_model():
    """Train the house price prediction model"""
    print("🚀 Generating sample house data...")
    data = generate_sample_data(1000)
    
    # Save sample data for reference
    data.to_csv('sample_data.csv', index=False)
    print(f"✅ Generated {len(data)} sample houses")
    
    # Prepare features and target
    X = data[['square_feet', 'bedrooms', 'bathrooms', 'age', 'distance_to_city']]
    y = data['price']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    print("🧠 Training Linear Regression model...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"📊 Model Performance:")
    print(f"   Mean Squared Error: ${mse:,.2f}")
    print(f"   R² Score: {r2:.3f}")
    print(f"   Average Prediction Error: ${np.sqrt(mse):,.2f}")
    
    # Save model
    joblib.dump(model, 'house_price_model.pkl')
    print("💾 Model saved as 'house_price_model.pkl'")
    
    # Save feature names for API
    feature_names = list(X.columns)
    joblib.dump(feature_names, 'feature_names.pkl')
    print("📝 Feature names saved")
    
    return model, feature_names

if __name__ == "__main__":
    train_model() 