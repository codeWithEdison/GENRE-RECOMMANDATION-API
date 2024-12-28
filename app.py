# Import necessary libraries
import os
from flask import Flask, request, jsonify
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load our trained model and encoder
try:
    model = joblib.load('music_model.joblib')
    label_encoder = joblib.load('label_encoder.joblib')
except Exception as e:
    print(f"Error loading models: {e}")

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'API is running'})

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict_genre():
    try:
        # Get data from request
        data = request.get_json()
        
        # Extract age and gender
        age = data.get('age')
        gender = data.get('gender')
        
        # Validate input
        if not age or not isinstance(age, int) or not 0 <= age <= 120:
            return jsonify({'error': 'Age must be between 0 and 120'}), 400
            
        if gender not in [0, 1]:
            return jsonify({'error': 'Gender must be 0 or 1'}), 400
            
        # Make prediction
        features = [[age, gender]]
        prediction = model.predict(features)
        
        # Convert prediction to genre name
        predicted_genre = label_encoder.inverse_transform(prediction)[0]
        
        # Return result
        return jsonify({
            'predicted_genre': predicted_genre,
            'age': age,
            'gender': gender
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)