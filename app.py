from flask import Flask, render_template, request
import joblib
import numpy as np

model = joblib.load('iris_model.txt')

app= Flask(__name__)

@app.route('/')
def man():
  return render_template("home.html")

@app.route("/predict",methods=["POST"])
def home():
  data1= request.form['a']
  data2= request.form['b']
  data3= request.form['c']
  data4= request.form['d']
  arr= np.array([[float(data1), float(data2), float(data3), float(data4)]], dtype= int)
  pred= float(model.predict(arr)[0])
  return render_template("after.html", data = pred)

if __name__=='__main__':
  app.run(debug=True)
  