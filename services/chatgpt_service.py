import openai
import os
import sys

# Fetch OpenAI API key from the environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')

# Check if the API key exists
if openai_api_key is None:
    print("Error: OpenAI API key not found in environment variables.")
    sys.exit(1)  # Exit the program if the API key is missing
else:
    openai.api_key = openai_api_key

def classify_waste(image_description):
    """Classify waste based on the image description using ChatGPT."""
    prompt = f"The following object is described: {image_description}. Classify it as recyclable, compostable, landfill, or hazardous."

    try:
        # Call OpenAI's ChatGPT API
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Or use "gpt-3.5-turbo" if needed
            messages=[
                {"role": "system", "content": "You are an expert in waste sorting."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the model's response
        classification = response['choices'][0]['message']['content']
        return classification.strip()

    except Exception as e:
        return f"Error: {str(e)}"

