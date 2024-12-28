from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load models
model = joblib.load('music_model.joblib')
label_encoder = joblib.load('label_encoder.joblib')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'API is running'})

@app.route('/predict', methods=['POST'])
def predict_genre():
    try:
        data = request.get_json()
        age = data.get('age')
        gender = data.get('gender')
        
        if not age or not isinstance(age, int) or not 0 <= age <= 120:
            return jsonify({'error': 'Age must be between 0 and 120'}), 400
            
        if gender not in [0, 1]:
            return jsonify({'error': 'Gender must be 0 or 1'}), 400
            
        features = [[age, gender]]
        prediction = model.predict(features)
        predicted_genre = label_encoder.inverse_transform(prediction)[0]
        
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