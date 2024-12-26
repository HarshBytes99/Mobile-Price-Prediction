from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)

try:
    with open("MPP.pkl", "rb") as f:
        pipeline = pickle.load(f)
except FileNotFoundError:
    raise Exception("The model file 'MPP.pkl' was not found. Please ensure it is in the correct directory.")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction')
def prediction_form():
    return render_template('prediction.html')


def convert_to_numerical(data):
    # for no of sim
    if data['No_of_sim'] == 'dual':
        data['No_of_sim'] = 0
    elif data['No_of_sim'] == 'single':
        data['No_of_sim'] = 1
    

    # for 5g mobile
    if data['5g_mobile'] == '5g': 
        data['5g_mobile'] = 1
    elif data['5g_mobile'] == 'Volte':
        data['5g_mobile'] = 2 
    

    # for company
    if data['company'] == 'Samsung':
        data['company'] = 19
    elif data['company'] == 'Vivo':
        data['company'] = 22
    elif data['company'] == 'Realme':
        data['company'] = 18  
    elif data['company'] ==  'OPPO' or data['company'] == 'Oppo':    
        data['company'] = 13
    elif data['company'] == 'OnePlus':
        data['company'] = 14
    elif data['company'] == 'Poco' or data['company'] =='POCO':
        data['company'] = 17
    elif data['company'] == 'Xiaomi':
        data['company'] = 23
    elif data['company'] == 'Tecno':
        data['company'] = 21
    elif data['company'] == 'Lava':
        data['company'] = 9
    elif data['company'] == 'Motorola':
        data['company'] = 11
    elif data['company'] == 'Nothing':
        data['company'] = 12
    elif data['company'] == 'IQOO':
        data['company'] = 24 
    elif data['company'] == 'Google':
        data['company'] = 3
    elif data['company'] == 'LG':
        data['company'] = 8
    elif data['company'] == 'Honor':
        data['company'] = 4
    elif data['company'] == 'Itel' or data['company'] =='itel':
        data['company'] = 25
    elif data['company'] == 'Huawei':
        data['company'] = 5
    elif data['company'] == 'Gionee':
        data['company'] = 2                                        
    

    # for Processor
    if data['Processor'] == 'Octa Core Processor' or data['Processor'] =='Octa Core' :
        data['Processor'] = 12
    elif data['Processor'] == 'Nine Core' or data['Processor'] =='Nine-Cores' or data['Processor'] =='Nine Cores':
        data['Processor'] = 10
    elif data['Processor'] == 'Deca Core Processor':
        data['Processor'] = 7
    elif data['Processor'] == 'Quad Core':
        data['Processor'] = 13            
    elif data['Processor'] == '2.3 GHz Processor':
        data['Processor'] = 5                              
    elif data['Processor'] == '2 GHz Processor':
        data['Processor'] = 4
    elif data['Processor'] == '1.8 GHz Processor':
        data['Processor'] = 2
    elif data['Processor'] == '1.6 GHz Processor':
        data['Processor'] = 1
    elif data['Processor'] == '1.3 GHz Processor':
        data['Processor'] = 0
    
    return data

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # for required features
        required_features = [
            'Rating', 'No_of_sim', 'Ram', '5g_mobile', 'Battery', 'Display', 
            'Rc', 'Fc', 'External_memory', 'Android_version', 'company', 
            'Inbuilt_memory', 'fast_charging', 'Processor'
        ]
        if not all(feature in data for feature in required_features):
            return jsonify({"error": "Some features are missing in the input data."}), 400

        data = convert_to_numerical(data)

        features = [data[feature] for feature in required_features]
        features_array = np.array([features])

        prediction = pipeline.predict(features_array)

        return jsonify({"predicted_price": prediction[0]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
