MODEL=./Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf
/home/lnguyen/llama.cpp/build/bin/llama-server -m "$MODEL" -c 2048 -ngl 20 --host 0.0.0.0 --port 8080
