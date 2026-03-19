from flask import Flask, render_template, request
import pickle

app = Flask(_name_)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    prediction = model.predict([data])
    return render_template('index.html', result=prediction[0])

if _name_ == "_main_":
    app.run()
