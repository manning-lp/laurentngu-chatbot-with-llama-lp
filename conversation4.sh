#!/bin/bash

time wasmedge --dir .:. \
    --nn-preload default:GGML:AUTO:Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf \
    llama-chat.wasm \
    --prompt-template llama-3-chat \
    --system-prompt  "You are an experienced entrepreneur who succeeded and made real businesses. Explain like a practical mentor."
    --n-predict 300 \
    --log-enable
