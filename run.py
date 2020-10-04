import os
from flask import Flask, render_template #import Flask class

app = Flask (__name__)# instance of this and storing in variable called app
#single module build in varible
@app.route("/") # @ is an decorator- way of wrapping functions. / root of
def index():
    return render_template("index.html")

if __name__ == "__main__": # main is default name in python
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)