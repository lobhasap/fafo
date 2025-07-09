# 🏠 House Price Prediction ML API

A complete machine learning pipeline that trains a house price prediction model and serves it via a REST API with a beautiful frontend interface.

## 🚀 Features

- **ML Model**: Linear regression model trained on synthetic house data
- **Flask API**: RESTful API with CORS support and error handling
- **Frontend**: Modern, responsive web interface
- **Deployment Ready**: Configured for Render, Heroku, and other platforms
- **Health Checks**: API status monitoring
- **Sample Data**: Auto-generated realistic house data for training

## 📁 Project Structure

```
fafo/
├── train_model.py      # ML model training script
├── app.py             # Flask API server
├── index.html         # Frontend interface
├── requirements.txt   # Python dependencies
├── Procfile          # Deployment configuration
├── README.md         # This file
└── Generated files:
    ├── house_price_model.pkl    # Trained model
    ├── feature_names.pkl        # Feature names
    └── sample_data.csv         # Training data
```

## 🛠️ Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model

```bash
python train_model.py
```

This will:
- Generate 1000 sample houses with realistic features
- Train a linear regression model
- Save the model as `house_price_model.pkl`
- Display model performance metrics

### 3. Start the API Server

```bash
python app.py
```

The API will be available at `http://localhost:5000`

### 4. Open the Frontend

Open `index.html` in your browser or serve it with a local server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve .
```

## 🔌 API Endpoints

### Base URL: `http://localhost:5000`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information and usage |
| `/health` | GET | Health check |
| `/features` | GET | Get required features |
| `/predict` | POST | Predict house price |
| `/sample-prediction` | GET | Get a sample prediction |

### Example API Usage

```bash
# Health check
curl http://localhost:5000/health

# Get sample prediction
curl http://localhost:5000/sample-prediction

# Make a prediction
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "square_feet": 2000,
    "bedrooms": 3,
    "bathrooms": 2,
    "age": 10,
    "distance_to_city": 5
  }'
```

### JavaScript Example

```javascript
async function predictHousePrice(features) {
  const response = await fetch('http://localhost:5000/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(features)
  });
  
  const result = await response.json();
  console.log('Predicted price:', result.prediction_formatted);
  return result;
}

// Usage
predictHousePrice({
  square_feet: 2000,
  bedrooms: 3,
  bathrooms: 2,
  age: 10,
  distance_to_city: 5
});
```

## 🌐 Deployment

### Option 1: Render (Recommended - Free)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/house-price-api.git
   git push -u origin main
   ```

2. **Deploy on Render**
   - Go to [render.com](https://render.com)
   - Create account and connect GitHub
   - Create new **Web Service**
   - Select your repository
   - Set build command: `pip install -r requirements.txt && python train_model.py`
   - Set start command: `gunicorn app:app`
   - Deploy!

3. **Update Frontend**
   - Replace `localhost:5000` with your Render URL in `index.html`

### Option 2: Heroku

1. **Install Heroku CLI**
2. **Deploy**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Option 3: Railway

1. **Connect GitHub repo to Railway**
2. **Railway will auto-detect and deploy**

## 🧠 Model Details

### Features Used
- **Square Feet**: House size (500-10,000 sq ft)
- **Bedrooms**: Number of bedrooms (1-10)
- **Bathrooms**: Number of bathrooms (1-5)
- **Age**: House age in years (0-50)
- **Distance to City**: Miles from city center (0-30)

### Model Performance
- **Algorithm**: Linear Regression
- **R² Score**: ~0.85-0.90
- **Average Error**: ~$15,000-20,000

### Training Data
- 1000 synthetic houses with realistic pricing
- Generated using a formula with noise for realism
- Split: 80% training, 20% testing

## 🔧 Customization

### Change the Model
Edit `train_model.py` to:
- Use different algorithms (Random Forest, XGBoost, etc.)
- Add more features
- Use real data instead of synthetic

### Modify the API
Edit `app.py` to:
- Add authentication
- Add rate limiting
- Add more endpoints
- Change response format

### Update the Frontend
Edit `index.html` to:
- Change the design
- Add more input fields
- Add data visualization
- Add user accounts

## 🐛 Troubleshooting

### Common Issues

1. **Model not found error**
   ```bash
   python train_model.py  # Run this first
   ```

2. **Port already in use**
   ```bash
   # Change port in app.py or kill existing process
   lsof -ti:5000 | xargs kill -9
   ```

3. **CORS errors in frontend**
   - Ensure `flask-cors` is installed
   - Check that CORS is enabled in `app.py`

4. **Deployment issues**
   - Check `requirements.txt` has all dependencies
   - Ensure `Procfile` is correct
   - Check build logs on deployment platform

## 📊 API Response Format

### Success Response
```json
{
  "prediction": 325000.0,
  "prediction_formatted": "$325,000.00",
  "input_features": {
    "square_feet": 2000,
    "bedrooms": 3,
    "bathrooms": 2,
    "age": 10,
    "distance_to_city": 5
  },
  "confidence": "This is a linear regression model prediction"
}
```

### Error Response
```json
{
  "error": "Missing feature: square_feet"
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

MIT License - feel free to use this project for your own applications!

## 🆘 Support

If you encounter any issues:
1. Check the troubleshooting section
2. Review the API documentation
3. Test with the sample prediction endpoint
4. Check the deployment platform logs

---

**Happy coding! 🚀** 