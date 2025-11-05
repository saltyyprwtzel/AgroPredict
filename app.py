from flask import Flask, request, render_template
import numpy as np
import pickle

# Load the model and scaler
model = pickle.load(open('model.pkl', 'rb')) 
ms = pickle.load(open('minmaxscaler.pkl', 'rb')) 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Get form data
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosporus'])
        K = float(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['Ph'])
        rainfall = float(request.form['Rainfall'])

        # Create feature array
        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        # Scale and predict
        scaled_features = ms.transform(single_pred)
        prediction = model.predict(scaled_features)

        # Crop dictionary
        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 
            6: "Papaya", 7: "Orange", 8: "Apple", 9: "Muskmelon", 
            10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 
            18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans", 
            21: "Chickpea", 22: "Coffee"
        }

        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            result = f"{crop} is the best crop to be cultivated right there"
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
        
        return render_template('index.html', result=result)
    
    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)