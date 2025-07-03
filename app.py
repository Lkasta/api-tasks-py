from flask import Flask

app = Flask(__name__)

@app.route("/")
def initial():
  return "Hello Jonas"

if __name__ == "__main__":
  app.run(debug=True)