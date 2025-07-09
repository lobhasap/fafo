from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model and feature names
try:
    model = joblib.load('house_price_model.pkl')
    feature_names = joblib.load('feature_names.pkl')
    print("✅ Model loaded successfully")
except FileNotFoundError:
    print("❌ Model files not found. Please run 'python train_model.py' first")
    model = None
    feature_names = None

@app.route('/')
def home():
    """Home endpoint with API information"""
    return jsonify({
        "message": "🏠 House Price Prediction API",
        "version": "1.0.0",
        "endpoints": {
            "/predict": "POST - Predict house price",
            "/health": "GET - API health check",
            "/features": "GET - Get required features"
        },
        "usage": {
            "method": "POST",
            "url": "/predict",
            "body": {
                "square_feet": 2000,
                "bedrooms": 3,
                "bathrooms": 2,
                "age": 10,
                "distance_to_city": 5
            }
        }
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None
    })

@app.route('/features')
def get_features():
    """Get the required features for prediction"""
    return jsonify({
        "features": feature_names if feature_names else [],
        "description": "House features required for price prediction"
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Predict house price based on input features"""
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Extract features in the correct order
        features = []
        for feature in feature_names:
            if feature not in data:
                return jsonify({"error": f"Missing feature: {feature}"}), 400
            features.append(float(data[feature]))
        
        # Make prediction
        input_array = np.array(features).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        
        # Format response
        response = {
            "prediction": round(prediction, 2),
            "prediction_formatted": f"${prediction:,.2f}",
            "input_features": dict(zip(feature_names, features)),
            "confidence": "This is a linear regression model prediction"
        }
        
        return jsonify(response)
        
    except ValueError as e:
        return jsonify({"error": f"Invalid input data: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

@app.route('/sample-prediction')
def sample_prediction():
    """Get a sample prediction for testing"""
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    # Sample house data
    sample_data = {
        "square_feet": 2000,
        "bedrooms": 3,
        "bathrooms": 2,
        "age": 10,
        "distance_to_city": 5
    }
    
    # Make prediction
    features = [sample_data[feature] for feature in feature_names]
    input_array = np.array(features).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    
    return jsonify({
        "sample_input": sample_data,
        "prediction": round(prediction, 2),
        "prediction_formatted": f"${prediction:,.2f}"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 