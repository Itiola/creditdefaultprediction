from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model (replace 'credit_default_model.pkl' with your model file)
with open('smartcreditmodel.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract inputs from the form
        inputs = [
            float(request.form['gender']),
            float(request.form['married']),
            float(request.form['dependent_no']),
            float(request.form['education']),
            float(request.form['self_employed']),
            float(request.form['applicant_income']),
            float(request.form['coapplicant_income']),
            float(request.form['loan_amount']),
            float(request.form['loan_amount_term']),
            float(request.form['credit_history'])
        ]

        # Reshape inputs for the model
        inputs_array = np.array([inputs]).reshape(1, -1)

        # Predict using the model
        prediction = model.predict(inputs_array)
        prediction_proba = model.predict_proba(inputs_array)

        # Prepare the response
        result = "Approved" if prediction[0] == 1 else "Rejected"
        confidence = round(prediction_proba[0][prediction[0]] * 100, 2)

        return jsonify({
            'result': result,
            'confidence': confidence
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
