from unicodedata import numeric
from flask import Flask, render_template, request
import joblib
import numpy as np

model = joblib.load('iris_model.txt')

app= Flask(__name__)

@app.route('/')
def man():
  return render_template("home0.html")

@app.route('/info')
def sec():
  return render_template("home.html")

@app.route("/predict",methods=["POST"])
def home():
  data1= request.form['a']
  data2= request.form['b']
  data3= request.form['c']
  data4= request.form['d']
  l= [data1, data2, data3, data4]
  for i in range(len(l)):
    if l[i] =='' :
      l[i]=0
    else:
      l[i]= float(l[i])
  arr= np.array([l], dtype= float)
  pred= int(model.predict(arr)[0])
  return render_template("after.html", data = pred)

if __name__=='__main__':
  app.run(debug=True)
  