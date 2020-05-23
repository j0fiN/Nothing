from flask import Flask

app = Flask(__name__)

@app.route('/')
def homie():
    return "<h3>HELL0<h3>"

@app.route('/<string:name>',methods=["GET"])
def nam(name):
    return f"<h3>your name is {name}<h3>"

if __name__=="__main__":
    app.run()

