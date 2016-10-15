from flask import Flask, render_template
import event, profile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/prototype")
def prototype():
    event1 = Event("Rec courts(Indoor)")
    event2 = Event("Rec fields(South)")
    event3 = Event("Rec center building")
    event_list = [event1,event2,event3]
    # return flask.render_template(index.html, events=event_list);

if __name__ == "__main__":
    app.run()
