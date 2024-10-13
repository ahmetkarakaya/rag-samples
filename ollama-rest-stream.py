import requests
import json

def query_ollama(prompt, model="llama3"):
    url = "http://localhost:11434/api/generate"

    payload = {
        "stream": True,  # Enable streaming on the server side
        "model": model,
        "prompt": prompt
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        # Enable streaming on the client side
        with requests.post(url, json=payload, headers=headers, stream=True) as response:
            if response.status_code != 200:
                yield f"Error: {response.status_code}, {response.text}"
                return

            # Iterate over the response in chunks
            for chunk in response.iter_lines(decode_unicode=True):
                if chunk:
                    try:
                        # Assuming each chunk is a JSON object
                        data = json.loads(chunk)
                        if 'response' in data:
                            yield data['response']
                        else:
                            yield f"Unexpected response format: {data}"
                    except json.JSONDecodeError:
                        # Handle non-JSON chunks if necessary
                        yield chunk
    except requests.exceptions.RequestException as e:
        yield f"Request failed: {e}"

# Example usage
if __name__ == "__main__":
    prompt = "Explain the concept of recursion in programming."
    for chunk in query_ollama(prompt):
        print(chunk)
