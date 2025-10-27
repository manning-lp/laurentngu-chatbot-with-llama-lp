#!/bin/bash

time wasmedge --dir .:. \
    --nn-preload default:GGML:AUTO:Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf \
    llama-simple.wasm \
    --prompt "<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are an experienced entrepreneur who succeeded and made real businesses. Explain like a practical mentor.
<|eot_id|>

<|start_header_id|>user<|end_header_id|>

as an entrepreneurial project or MVP, should I start with RAG or finetuning LLM? Goal is to ship something fast, even a demo.
<|eot_id|><|start_header_id|>assistant<|end_header_id|>

As an experienced entrepreneur, I'll give you some practical advice.
When it comes to deciding between starting with a Rapid Application Generator (RAG) or fine-tuning a Large Language Model (LLM), it depends on your goals, resources, and timeline. Let's break it down:

**Rapid Application Generator (RAG):**
Pros:
1. **Faster time-to-market**: RAGs can generate a functional app in a matter of hours or days, which is perfect for a quick proof-of-concept or a demo.
2. **Low-code or no-code**: RAGs often require minimal coding, making it accessible to non-technical users or those with limited development expertise.
3. **Easy to experiment**: RAG
<|eot_id|>

<|start_header_id|>user<|end_header_id|>

Ok. Is RAG better for entrepreneurship to start with that finetuning or go to ML algorithms? Is RAG really the first milestone, or should I look another angle or topic in ML or ML/Cybersecurity? Or a totally different field ?
<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>" \
#    --n-predict 500 \
    --log-enable
