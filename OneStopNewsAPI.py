from flask import Flask
from flask import request
import RSStoJSON

# Switch Python version
# eval "$(pyenv init -)"
# pyenv local 3.6.0

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the One Stop News API."


# CNN RSS
@app.route("/cnn/", methods=['GET'])
def CNN():
    
    category = request.args.get('category')
    
    return str(RSStoJSON.CNN( category ))

# New York Times RSS
@app.route("/new-york-times/", methods=['GET'])
def NYT():

    category = request.args.get('category')

    return str(RSStoJSON.NYT( category ))

# Huffington Post  RSS
@app.route("/huff-post/", methods=['GET'])
def Huff():

    category = request.args.get('category')

    return str(RSStoJSON.Huff( category ))


if __name__ == '__main__':
    app.run(debug=True)

