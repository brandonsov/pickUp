from flask import Flask
import event
app = Flask(__name__)

@app.route("/")
def index():
    return flask.render_template('index.html')

@app.route("/prototype")
def prototype():
    event1 = Event("Rec courts(Indoor)")
    event2 = Event("Rec fields(South)")
    event3 = Event("Rec center building")
    return flask.render_template)

if __name__ == "__main__":
    app.run()
