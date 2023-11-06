import logging
from flask import Flask, redirect, render_template
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
