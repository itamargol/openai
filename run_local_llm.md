## Run an Local LLM in 6 CLI commands
    
### #1

     git clone https://github.com/togethercomputer/redpajama.cpp.git
     
### #2
    
     cd redpajama.cpp
     
### #3
     
     make redpajama-chat quantize-gptneox
     
### #4
     bash ./examples/redpajama/scripts/install-RedPajama-INCITE-Chat-3B-v1.sh
     
### #5
     python ./examples/redpajama/scripts/quantize-gptneox.py \
       --quantize-output-type q4_1 \
       ./examples/redpajama/models/pythia/ggml-RedPajama-INCITE-Chat-3B-v1-f16.bin
       
### #5

    ./redpajama-chat -m ./examples/redpajama/models/pythia/ggml-RedPajama-INCITE-Chat-3B-v1-q4_1.bin \
       -c 2048 \
       -b 128 \
       -n 1 \
       -t 8 \
       --instruct \
       --color \
       --top_k 30 \
       --top_p 0.95 \
       --temp 0.8 \
       --repeat_last_n 3 \
       --repeat_penalty 1.1 \
       --seed 0

### [Full Guide](https://www.together.xyz/blog/redpajama-3b-updates)
