import requests
import json

# Configuration
OLLAMA_API_URL = "http://localhost:11434/v1/llama/completions"  # Replace with your actual endpoint
MODEL_NAME = "llama3"  # Replace with the model you want to use
PROMPT = "Hello, how are you today?"

def query_ollama(prompt, model=MODEL_NAME, max_tokens=150, temperature=0.7):
    """
    Sends a prompt to the Ollama server and returns the generated response.

    Args:
        prompt (str): The input text to send to the model.
        model (str): The name of the model to use.
        max_tokens (int): The maximum number of tokens to generate.
        temperature (float): Sampling temperature.

    Returns:
        str: The generated text from the model.
    """
    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }

    try:
        response = requests.post(OLLAMA_API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        generated_text = data.get("choices", [{}])[0].get("text", "")
        return generated_text.strip()
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama server: {e}")
        return None
    except ValueError:
        print("Invalid JSON response received from Ollama server.")
        return None

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    response = query_ollama(user_prompt) 
    if response:
        print("Ollama Response:")
        print(response)
    else:
        print("Failed to get a response from Ollama server.")

