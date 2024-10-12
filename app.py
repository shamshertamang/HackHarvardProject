from flask import Flask, render_template
from api.waste import waste_bp  # Import your blueprint from the API routes

# Initialize the Flask app
app = Flask(__name__)

# Register Blueprints (for your routes)
app.register_blueprint(waste_bp)

# Define a simple route to render the upload form
@app.route('/')
def home():
    return render_template('upload.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
