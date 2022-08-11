from flask import Flask, request, redirect, send_file, render_template, url_for 
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from waitress import serve
import json
import sharecode

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["4000 per day", "500 per hour"]
)

NServer = "https://api.warsey.com"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create")
@limiter.limit("5/hour", override_defaults=False)
def createsharecode():
    name = request.args.get('name')
    model = request.args.get('model')
    if name == None or model == None:
        return render_template("error.html", errorcode = "1000 (Non-HTTP)", errormsg = "Missing Values/Parameters.")
    modeljson = '{"name": "' + name + '", "model": "' + model + '"}'
    code = sharecode.generatecode(str(modeljson))
    if code == None:
        return render_template("error.html", errorcode = "None", errormsg = "No Share codes available to assign at the moment, please try again later.")
    return redirect(f"/sharecode/{code['sharecode']}")

@app.route("/sharecode/<code>")
def sharecodes(code):
    try: 
        int(code)
    except:
        return render_template("error.html", errorcode = "1001 (Non-HTTP)", errormsg = "Invalid Share Code.")
    if len(code) > 8:
        return render_template("error.html", errorcode = "1002 (Non-HTTP)", errormsg = "Invalid Share Code.")
    modelnonjson = sharecode.pullsharecodedata(code)
    if modelnonjson == False: 
        return render_template("sharecode.html", modelurl = "/content/none-sharecode.webp", code = code, name = "Does Not Exist", model = "Does Not Exist")
    modeljson = json.loads(modelnonjson)
    name = str(modeljson["name"])
    model = str(modeljson["model"])
    return render_template("sharecode.html", modelurl = f"{NServer}/api/design/tshirt?text={name}&template={model}", code = code, name = name, model = model)

@app.route("/s/<code>")
def redirectsc(code):
    return redirect(f"/sharecode/{code}")

@app.route("/content/<file>")
def content(file):
    return send_file(f"files/{file}")
    
@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", errorcode = "404", errormsg = "The Page You Are Trying To Access Does Not Exist.")

@app.errorhandler(429)
def not_found(e):
    return render_template("error.html", errorcode = "429 | Too Many Requests", errormsg = "You have made too many requests in the past hour, please try again later.")

@app.errorhandler(500)
def internal_error(error):
    return render_template("error.html", errorcode = "500", errormsg = "Internal Server Error.")

if __name__ == "__main__":
    print("Started T-shirt API Front-end")
    serve(app, host='0.0.0.0', port=7000)