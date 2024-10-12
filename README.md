#sd sd rag-samples

**LLMA vs Mistral**

LLAMA 3.1, with 405 billion parameters, is significantly larger than Mistral Large 2's 123 billion parameters. The larger parameter count of LLAMA 3.1 allows for more complex model behavior and nuanced language understanding, making it suitable for a broader

# sample rest

```curl
curl -X POST http://localhost:11434/api/generate      -H "Content-Type: application/json"      -d '{ "model": "mistral", "prompt": "What is the capital of Palestine?"}'
```

Model do not want to answer correctly. So it should be updated with correct ones .Correct  answer is **Kudus**.


## Ollama Sample Commands

> ollama run llama:latest
> ollama list
> ollama ps
