import requests
import json
import time

url = "http://localhost:8080/v1/chat/completions"
headers = {"Content-Type": "application/json"}

messages = [
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
        "Propose me a few choices and tell me what would be first thing first?\n"
        "The goal is to startup the company so that it grows and does not stay a side business or a 1 person business"
    )}
]

# Parameters that can be tuned
max_tokens = 1024      # limit per generation round
temperature = 0.5
full_reply = ""
k=0

while True:
    payload = {
        "model": "Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf",
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()

    # print raw JSON once if needed for debugging
    print(json.dumps(data, indent=2))

    choice = data["choices"][0]
    reply = choice["message"]["content"]
    finish_reason = choice.get("finish_reason", "")

    full_reply += reply
    messages.append({"role": "assistant", "content": reply})

    print(f"\n[Chunk received — {len(reply.split())} words, finish_reason={finish_reason}]")

    if finish_reason != "length":
        break

    # small delay between requests to avoid overwhelming local server
    time.sleep(0.1)
    print ("K = " + str(k) + "\n")
    k=k+1

print("\n\nFull Assistant Reply:\n" + "-" * 40)
print(full_reply)
print("-" * 40)
