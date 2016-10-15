from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return flask.render_template('fbsignin.html')

# @app.route("/fb_signin")
# def sign_in():
#     return flask.render_template('fbsignin.html')

if __name__ == "__main__":
    app.run()
