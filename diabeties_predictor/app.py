import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('myhtml.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    if int_features[4]==0:
        int_features.append(1)
    else:
        int_features.append(0)
    if int_features[3]==0:
        int_features.append(1)
    else:
        int_features.append(0)
    final_features = [np.array(int_features)]
    print(final_features)
    output=None;
    prediction = model.predict(final_features)

    output = prediction[0]
    if output== None:
        return render_template('myhtml.html', prediction_text="select any option  ")
    elif output==0:
        return render_template('myhtml.html', prediction_text="Person is not diabetic ")
    elif output==1:
        return render_template('myhtml.html', prediction_text="Person is diabetic ")
    
if __name__ == "__main__":
    app.run(debug=True)