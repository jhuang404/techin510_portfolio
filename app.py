from flask import Flask, render_template

# Create Flask app with explicit static folder path
app = Flask(__name__, 
            static_folder='static',     # Path to static folder relative to app.py
            template_folder='templates' # Path to templates folder relative to app.py
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/mobile-temple')
def mobile_temple():
    return render_template('mobile_temple.html')

if __name__ == '__main__':
    app.run(debug=True)