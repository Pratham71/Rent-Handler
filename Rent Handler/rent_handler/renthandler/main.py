from flask import Flask,request,url_for,redirect
from agreements import Agreements_Generator
import os
app = Flask(__name__)



@app.route("/data",methods=["POST","GET"])
def Get_Form_Data():
    data = request.form
    Agreements_Generator(data).Generate_Agreement()
    return redirect("/")

@app.route("/")
def submission():
    with open(r"C:\Users\Pratham\Desktop\Rent Handler\rent_handler\templates\submitted.html") as html:
        content = html.read()

    return content

if __name__=="__main__":
    app.run(debug=True)