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


#
@app.route("/cnn/", methods=['GET'])
def CNN():
    
    category = request.args.get('category')
    
    return str(RSStoJSON.CNN( category ))


if __name__ == '__main__':
    app.run()

