from flask import Flask, request, jsonify, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from dominate.tags import img
import numpy as np
import joblib

###############################################
#          Define flask app                   #
###############################################
winequality = Flask(__name__)
Bootstrap(winequality)

#here we define our menu items
topbar = Navbar(View('Home', 'home'),
                View('prediction', 'predict'),
                View('Documentation', 'get_docs'),
               


                )

# registers the "top" menubar
nav = Nav()
nav.register_element('top', topbar)



###############################################
#          Render Home page                   #
###############################################
@winequality.route("/")
def home():
    return render_template("home.html")

###############################################
#          Render documentation page                   #
###############################################
@winequality.route('/docs', methods=["GET"])
def get_docs():
    return(render_template('docs.html'))


# Load model
classifier = joblib.load("models/model.joblib")



###############################################
#          Render prediction page                   #
###############################################
@winequality.route("/predict", methods=["POST", "GET"])
def predict():

    print("Appel à la prédiction")
    # Check if request has a JSON content
    if request.method == "POST":
        if request.json:
            # Get the JSON as dictionnary
            params = request.get_json()
            # Predict
            X = np.array(params["input"])
            prediction = classifier.predict(X)
            # Return the result as JSON but first we need to transform the
            # result so as to be serializable by jsonify()
            return jsonify({"predict": prediction.tolist()}), 200
        else :
            print("Appel depuis formulaire")
            form = request.form
            inputs = []
            for key in form.keys() :
                inputs.append(form[key])
            print("Formulaire= ", inputs)
            X = np.array(inputs)
            #print(X.shape)
            X =  X.reshape(1, -1)
            #print(X.shape)
            prediction = classifier.predict(X)
            #print(prediction.tolist())
            return f"<h1>Votre vin est de classe : {prediction.tolist()}</h1>"
            #return render_template("predict.html")
    else :
        return render_template("predict.html")
    #return jsonify({"msg": "Error: "})


nav.init_app(winequality)
#server = winequality.server
if __name__ == "__main__":
    winequality.run(debug=True)