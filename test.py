# import joblib

# # Load the saved model
# rf_regressor = joblib.load('crop_yield_model.joblib')

# # Enter new data from console
# rain_fall = float(input("Enter Rain Fall (mm): "))
# fertilizer = float(input("Enter Fertilizer: "))
# temperature = float(input("Enter Temperatue: "))
# nitrogen = float(input("Enter Nitrogen (N): "))
# phosphorus = float(input("Enter Phosphorus (P): "))
# potassium = float(input("Enter Potassium (K): "))

# new_data = [rain_fall, fertilizer, temperature, nitrogen, phosphorus, potassium]

# # Make a prediction
# prediction = rf_regressor.predict([new_data])[0]

# # Print the predicted crop yield
# print("Predicted Crop Yield (Q/acre):", prediction)

from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the saved model
rf_regressor = joblib.load('crop_yield_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    rain_fall = data['rainfall']
    fertilizer = data['fertilizer']
    temperature = data['temperature']
    nitrogen = data['nitrogen']
    phosphorus = data['phosphorus']
    potassium = data['potassium']

    new_data = [rain_fall, fertilizer, temperature, nitrogen, phosphorus, potassium]

    # Make a prediction
    prediction = rf_regressor.predict([new_data])[0]

    # Return the predicted crop yield
    return jsonify({'predicted_yield': prediction})

if __name__ == '__main__':
    app.run(debug=True)