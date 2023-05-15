import numpy as np
from flask import Flask ,request,jsonify,render_template
import pickle

#Create Flask APP
app = Flask(__name__)

#Load Pickle model
model = pickle.load(open("RFmodel.pkl","rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods =["POST"])
def predict():
    features = [int(x) for x in request.form.values()]
    featuresArr = [np.array(features)]
    prediction = model.predict(featuresArr)
    
    if(prediction == 2):
        pred = "Die"
    elif(prediction == 1):
        pred = "Live"

    return render_template("index.html",prediction_text = "The Patient will {}".format(pred))

if __name__ == "__main__":
    app.run(debug = True)