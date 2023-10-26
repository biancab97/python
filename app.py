from flask import Flask
import haven
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/Bianca")
def Bianca():
    var1 = 26
    print(var1)
    var1 += 100
    return "<p>Hello, Bianca!</p>" +str(var1)


@app.route("/verzinnen/<eenvariabele>")
def ietsverzinnen(eenvariabele):
    return "<p>Hello, World!" +eenvariabele + " </p>" 

@app.route("/haven")
def havenmethode():
    return haven.demethodevandehaven()