from flask import Flask
from views import product_bp

app = Flask(__name__)

app.register_blueprint(product_bp)

@app.route('/')
def index():
    return "<h1>Home</h1>"



if __name__=="__main__":
    app.run(debug=True)