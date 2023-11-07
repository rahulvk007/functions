import logging
from flask import Flask, request, render_template, redirect, url_for
import azure.functions as func

app = Flask(__name__)



#standard code for Azure functions
def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)

#Actual Flask code

@app.route('/')
def index():
    return "Hello World, Simple Flask API Hosted in Azure Functions"

@app.route("/form",methods=['POST','GET'])
def home():
    if request.method=='POST':
        details = request.form
        dict = {}
        dict['reg_no']=details["regno"]
        dict['name'] = details["name"]
        dict['club_dept']='FFCS'
        dict['phone_no'] = details["phoneno"]
        dict['email'] = details["email"]
        dict['score'] = 0
        dict['contributions'] = 0
        dict['expertize_in'] = details["exp"]
        dict['contribution_details'] = ''
        return "Success"
    
    return render_template("form.html")