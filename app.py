from flask import Flask, render_template,url_for
from flask import request
import json,requests
import requests,json,time,os



app = Flask(__name__,template_folder='templates',static_folder='static')


@app.route("/")
def movie():
    user_agent = {"User-Agent":"Kaster/1.2 (mirrortv.Kaster; build:1; iOS 16.3.1) Alamofire/5.6.4",}
    url = "https://elkaster.com/ios/splash?api-key=7f8d4d6e-ppdt-7349-ikpb&v=kaster"
    sendRequest = requests.get(url, headers=user_agent)
    ss= sendRequest.json().get("ser_all")
    return render_template("index.html",id=ss)
@app.route("/show/<id>")
def show(id):
        user_agent = {"User-Agent":"Kaster/1.2 (mirrortv.Kaster; build:1; iOS 16.3.1) Alamofire/5.6.4",}
        url = f"https://elkaster.com/ios/episodes?id={id}&api-tok=7f8d4d6e-ppdt-7349-ikpb"
        sendRequest = requests.get(url, headers=user_agent)
        ss = sendRequest.json().get("epiks")
        return render_template("edp.html",ebp=ss)
@app.route("/sort/<id>/")
def sort(id):
    user_agent = {"User-Agent":"Kaster/1.2 (mirrortv.Kaster; build:1; iOS 16.3.1) Alamofire/5.6.4",}
    url = f"https://elkaster.com/ios/getLink?id={id}&api_tok=7f8d4d6e-ppdt-7349-ikpb"
    sendRequest = requests.get(url, headers=user_agent)
    urlvideo = sendRequest.text
    return render_template("edp2.html",ebp2=urlvideo)

if __name__ == "__main__":
    app.run(debug=True)
