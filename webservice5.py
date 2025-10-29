import requests
import json

url = "http://localhost:8080/v1/chat/completions"
headers = {"Content-Type": "application/json"}

payload = {
        "model": "Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf",    
    "messages": [
        {"role": "system", "content": "You are a very successful entrepreneur who is now doing the coach for others"},
        {"role": "user", "content": "What is the best way to build a long lasting business? Should we build for AI/ML or cybersecurity? Or other fields?"},
        {"role": "assistant", "content": (
            "As an experienced entrepreneur, I'll give you some practical advice.\n"
            "When it comes to deciding between starting with a Rapid Application Generator (RAG) or fine-tuning a Large Language Model (LLM), "
            "it depends on your goals, resources, and timeline. Let's break it down:\n\n"
            "**Rapid Application Generator (RAG):**\n"
            "Pros:\n"
            "1. **Faster time-to-market**: RAGs can generate a functional app in a matter of hours or days.\n"
            "2. **Low-code or no-code**: RAGs often require minimal coding, making it accessible to non-technical users.\n"
            "3. **Easy to experiment**: RAG"
        )},
        {"role": "user", "content": (
            "Ok. Is RAG better for entrepreneurship to start with than fine-tuning or going to ML algorithms? \n"
            "Is RAG really the first milestone, or should I look at another angle or topic in ML/Cybersecurity? \n"
            "Or a totally different field? \n"
            "propose me a few choices and tell me what would be first thing first?"
        )}
    ],
    "max_tokens":5000,
    "temperature":0.5,
    "stream":False
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
data = response.json()

# Pretty-print full JSON
print(json.dumps(data, indent=2))

# Optionally print only the assistant's text
if "choices" in data and data["choices"]:
    print("\nAssistant:\n", data["choices"][0]["message"]["content"])

