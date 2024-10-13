import requests
import json

# ================================
# Configuration
# ================================

# Define the Ollama REST API endpoint
# Replace 'localhost' and '11434' with your server's address and port if different
OLLAMA_API_URL = "http://localhost:11434/api/generate"

# Specify the model you want to use
# Replace 'llama2' with the actual model name available on your Ollama server
MODEL_NAME = "mistral:latest"

# Define your prompt
prompt = "What is the capital of Turkiye?"

# Optional: Define additional parameters
# Adjust these based on Ollama's API specifications
payload = {
    "model": MODEL_NAME,
    "prompt": prompt,
    "max_tokens": 150,         # Maximum number of tokens to generate
    "temperature": 0.7,        # Sampling temperature
    "top_p": 0.9,              # Nucleus sampling parameter
    "stop_sequences": ["\n"]    # Sequences where the API will stop generating further tokens
    
}

# Optional: If your Ollama server requires authentication, set the headers accordingly
# For example, using an API key
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "Bearer YOUR_API_KEY_HERE"
# }

# If no authentication is required, you can set headers like this:
headers = {
    "Content-Type": "application/json"
}

# ================================
# Function to Generate Text
# ================================

def generate_text(api_url, headers, data):
    try:
        # Send a POST request to the Ollama API
        response = requests.post(api_url, headers=headers, data=json.dumps(data))

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            response_data = response.json()

            # Extract the generated text
            generated_text = response_data.get("response", "").strip()

            return generated_text
        else:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# ================================
# Main Execution
# ================================

if __name__ == "__main__":
    print("Sending prompt to Ollama...")
    result = generate_text(OLLAMA_API_URL, headers, payload)

    if result:
        print("\n--- Generated Response ---")
        print(result)
    else:
        print("Failed to generate a response.")

