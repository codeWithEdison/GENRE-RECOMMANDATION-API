
# Music Genre Prediction API

## Overview 🎵
This project is a machine learning-powered REST API that predicts music genre preferences based on age and gender. Built using Flask and scikit-learn, it provides fast and accurate predictions through a simple RESTful interface.

## Features 🌟
- Real-time music genre predictions
- RESTful API endpoints
- Simple deployment process
- Error handling
- Health monitoring
- API authentication

## Tech Stack 🛠️
- **Backend:** Flask
- **Machine Learning:** scikit-learn
- **Data Processing:** pandas, numpy
- **Model Storage:** joblib
- **Server:** gunicorn

## Getting Started 🚀

### Prerequisites
```bash
Python 3.8+
pip (Python package manager)
Virtual environment (recommended)
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/codeWithEdison/GENRE-RECOMMANDATION-API.git
cd GENRE-RECOMMANDATION-API
```

2. **Set up virtual environment**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

## API Documentation 📝

### Health Check
```http
GET /health
```
**Response:**
```json
{
    "status": "API is running"
}
```

### Predict Genre
```http
POST /predict
```
**Request Body:**
```json
{
    "age": 25,
    "gender": 1
}
```
**Response:**
```json
{
    "predicted_genre": "Hip-Hop",
    "age": 25,
    "gender": 1
}
```

## Usage Example 💻

```python
import requests

# Test prediction
data = {
    "age": 25,
    "gender": 1  # 1 for male, 0 for female
}
response = requests.post("http://localhost:5000/predict", json=data)
print(response.json())
```

## Deployment Guide 🚀

### Local Deployment
```bash
# Run with Flask
python app.py

# Run with Gunicorn
gunicorn app:app
```

### Deploy to Render
1. Push code to GitHub
2. Connect repository to Render
3. Configure build settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

## Model Details 📊
- Algorithm: Decision Tree Classifier
- Input Features: Age, Gender
- Output: Music Genre
- Supported Genres: Hip-Hop, Jazz, Classical, Rock, etc.

## Error Handling 🛡️
The API handles:
- Invalid inputs
- Missing parameters
- Server errors
- Prediction errors

## Contributing 🤝
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Support 📞
For support:
- Open an issue in the GitHub repository
- Email: your@email.com

---
⭐ **Star this repository if you find it helpful!**

[def]: #overview-

This README includes:
- Clear section headings
- Code blocks with syntax highlighting
- Emojis for visual appeal
- Well-structured information
- Easy-to-follow instructions