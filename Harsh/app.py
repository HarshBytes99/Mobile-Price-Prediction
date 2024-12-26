from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
try:
    with open("MPP4.pkl", "rb") as f:
        pipeline = pickle.load(f)
except FileNotFoundError:
    raise Exception("The model file 'MPP4.pkl' was not found. Please ensure it is in the correct directory.")

# Route to serve the index page
@app.route('/')
def home():
    return render_template('index.html')

# Route to serve the prediction form page
@app.route('/prediction')
def prediction_form():
    return render_template('prediction.html')

# Route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON request data
        data = request.get_json()

        # Check for required features
        required_features = [
            'Rating', 'No_of_sim', 'Ram', '5g_mobile', 'Battery', 'Display', 
            'Rc', 'Fc', 'External_memory', 'Android_version', 'company', 
            'Inbuilt_memory', 'fast_charging', 'Processor'
        ]
        if not all(feature in data for feature in required_features):
            return jsonify({"error": "Some features are missing in the input data."}), 400

        # Extract features in the correct order
        features = [data[feature] for feature in required_features]
        features_array = np.array([features])

        # Perform prediction
        prediction = pipeline.predict(features_array)

        # Return the prediction as JSON
        return jsonify({"predicted_price": prediction[0]})

    except Exception as e:
        # Catch any errors and return them as JSON
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
