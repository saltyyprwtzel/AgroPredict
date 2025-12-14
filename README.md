# 🌾 AI-Powered Crop Recommendation System

## Overview
This project implements a Machine Learning model deployed via a Flask web application to recommend the most suitable crop for cultivation based on soil and environmental parameters.

The system takes **7 key features** as input:
* **N**itrogen content in the soil.
* **P**hosphorus content in the soil.
* **K**potassium content in the soil.
* **Temperature** (in Celsius).
* **Humidity** (%).
* **pH** value of the soil.
* **Rainfall** (mm).

The trained model then predicts one of the **22 possible crops** (e.g., Rice, Maize, Apple, Coffee, etc.) that would yield the best results under the given conditions.

## 🌟 Features
* **Real-time Prediction:** Uses a lightweight Flask server to provide instant crop recommendations.
* **Web Interface:** User-friendly and responsive front-end built with HTML and Tailwind CSS.
* **Data-Driven:** Model trained on a comprehensive agricultural dataset to ensure accuracy.
* **ML Workflow:** Complete machine learning pipeline is documented in the Jupyter notebook.

## 📁 File Structure
The main components of the project are organized as follows:

| File/Folder | Description |
| :--- | :--- |
| `app.py` | The main **Flask application** file. It handles the web routes, loads the model, and performs predictions. |
| `cropRecommendSys.ipynb` | The **Jupyter Notebook** containing the entire ML workflow: Exploratory Data Analysis (EDA), Data Preprocessing (Scaling), Model Training, and Evaluation. |
| `crop_Dataset.csv` | The raw **dataset** used to train and test the model. |
| `model.pkl` | The **trained Machine Learning model** (likely a Decision Tree Classifier) serialized using `pickle`. |
| `minmaxscaler.pkl` | The **trained `MinMaxScaler` object** used for feature scaling, also serialized. Essential for preprocessing new inputs before prediction. |
| `templates/` | **(Folder to be created)** Contains the HTML templates for the web application. |
| `templates/index.html` | The main **frontend HTML** page for user input and displaying the prediction result. |
| `README.md` | This documentation file. |

## 🚀 How to Run Locally

Follow these steps to set up and run the Crop Recommendation System on your local machine.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-name>

2. Install Dependencies
The project requires Python and a few standard libraries. It is highly recommended to use a virtual environment.

# Create a virtual environment
python -m venv venv
# Activate the environment (Linux/macOS)
source venv/bin/activate
# Activate the environment (Windows)
.\venv\Scripts\activate

Install the required libraries:

pip install Flask numpy pandas scikit-learn

3. Setup HTML Template
The Flask application expects the HTML file to be within a templates folder.

mkdir templates
mv index.html templates/

4. Run the Application
Start the Flask server from the terminal:

python app.py

5. Access the Web App
Open your web browser and navigate to the displayed URL, typically: http://127.0.0.1:5000/

You can now enter the required soil and environmental parameters to get a crop recommendation!

Technology Stack
Machine Learning: scikit-learn (for model training and preprocessing)

Backend Framework: Flask (for serving the web application)

Data Handling: pandas, numpy

Frontend: HTML5, Tailwind CSS (for styling)

Deployment Assets: .pkl (for saving the model and scaler)
