from flask import Blueprint, request, jsonify
from services.chatgpt_service import classify_waste
from PIL import Image

waste_bp = Blueprint('waste', __name__)

@waste_bp.route('/classify', methods=['POST'])
def classify_waste_route():
    # Get the uploaded image and description
    image = request.files.get('image')
    description = request.form.get('description')

    # Basic validation
    if not image or not description:
        return jsonify({"error": "Image and description are required"}), 400

    # (Optional) You could use image recognition here to auto-describe the waste item.

    # Pass the description to ChatGPT for classification
    classification = classify_waste(description)

    # Return the classification result
    return jsonify({"classification": classification})
