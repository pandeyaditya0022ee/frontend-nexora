from flask import Flask, render_template
from api import api

app = Flask(__name__)
app.config.from_object('config.Config')

# Register the API Blueprint
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:page>')
def static_pages(page):
    try:
        return render_template(page)
    except:
        return "Page not found", 404

if __name__ == '__main__':
    app.run(debug=True)
