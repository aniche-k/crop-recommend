from os import P_DETACH
from flask import Flask,request,url_for,render_template
import pandas as pd
import numpy as np
import pickle
import requests
model_path="models/RandomForest1.pkl"
model=pickle.load(open(model_path,'rb'))
def weather_city(city):
    api_key="&appid=2c87673cbe9d4eb88fe151f5de7acdc5"
    weather_link="http://api.openweathermap.org/data/2.5/weather?q="+city+api_key
    city_info=requests.get(weather_link)
    city_json=city_info.json()
    if city_json!="404":
        main=city_json["main"]
        temp=round(main["temp"]-273.15,2)
        humid=main["humidity"]
        return temp,humid
    else:
        return None
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("forest.html")
@app.route("/predict", methods=["POST"])
def crop_recommend():
    n=int(request.form["Nitrogen"])
    p=int(request.form["Phosphorous"])
    k=int(request.form["Potassium"])
    ph=float(request.form["pH"])
    rain=float(request.form["Rainfall"])
    city=request.form["City"]
    if(weather_city!=None):
        temp,humid=weather_city(city)
        features=np.array([[n,p,k,temp,humid,ph,rain]])
        prediction=model.predict(features)
        return render_template("forest.html",pred="The suitable crop to grow is {}".format(prediction[0]))
    else:
        return render_template("forest.html",pred="Sorry this application is not available for your location")

if __name__=="__main__":
    app.run(debug=True)