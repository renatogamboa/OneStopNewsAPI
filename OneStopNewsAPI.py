from flask import Flask
import RSStoJSON

# Switch Python version
# eval "$(pyenv init -)"
# pyenv local 3.6.0

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/CNN_topstories")
def topStories():
    return str(RSStoJSON.CNN_topstories())


if __name__ == '__main__':
    app.run(debug=True)

