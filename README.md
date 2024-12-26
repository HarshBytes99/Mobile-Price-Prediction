
# Mobile_Price_Prediction
This project focuses on building a machine learning-based web application to predict mobile phone prices. The application uses machine learning models tailored for various specifications like RAM, storage, battery capacity, and other parameters to provide accurate price predictions. This system is designed to assist users in making informed decisions about purchasing mobile phones.

# Features
Dataset: Curated datasets of mobile phones, including specifications and corresponding prices, were sourced from relevant platforms to ensure accurate predictions.

Machine Learning Model: Models like Linear Regression, Ridge Regression, or other ML techniques are employed to enhance feature selection and regularization, minimizing overfitting and improving prediction accuracy.

User-Friendly Interface
- **Frontend**: Built with HTML, CSS, and JavaScript to deliver an interactive and responsive user experience.
- **Backend**: Developed using Flask for robust server-side logic and secure data handling.

Database: Efficiently stores user inputs and model outputs, seamlessly integrating with the web application.

Categorical Feature Conversion: Specifications such as RAM and storage are converted into human-readable categories for user-friendly input and output.

Data Visualization: Key insights, such as trends and distributions of mobile prices, are presented through interactive graphs and charts.

# How It Works
1. Users provide mobile specifications through an intuitive form on the web application.
2. The application processes the data and passes it to the trained machine learning model.
3. The model returns the predicted mobile price, displayed in a user-friendly format.
4. Visual aids help users understand the factors influencing the prediction.

# Technology Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **Database**: SQLite
- **Machine Learning**: Regression models (e.g., Linear, Ridge Regression)

# Requirements for the Project
- **Flask Framework Version**: 2.x or higher
  - Reason: Leverages modern Flask features for better application performance.
- **Python Version**: 3.10 or higher
  - Reason: Ensures compatibility with advanced libraries and features.

# Libraries
- **NumPy**: >=1.21.0
  - For numerical operations in regression models.
- **pandas**: >=1.3.0
  - For data manipulation and preprocessing.
- **scikit-learn**: >=1.0.0
  - For implementing regression models.
- **joblib**: >=1.2.0
  - For saving and loading serialized models.

# Deployment Requirements
- **Gunicorn**: >=20.0.0
- **WhiteNoise**: >=5.3.0 (for serving static files in production).

# Steps or Commands to Run the Project
1.Download the project zip file and extract it.

2.Open the extracted folder in VSCode.

3.Open the terminal in VSCode.

4.Navigate to the project directory by running:bash

5.Copy code

6.cd Mobile Price

7.Start the Django development server by running: bash

8.Copy code

9.python manage.py runserver  

10.Open the provided URL in a browser to access the application.
