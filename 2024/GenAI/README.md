# 2024 GenAI

As a new twist, I'm going to play around with GenAI to understand how good some of these models are.

To be clear, (a) I am not competing by any stretch of the imagination, and (b) I am solving these puzzles myself first and then comparing how GenAI generates solutions.  No, not because I'm that much of a Pythonista Bad Ass but because I am trying to understand how best to leverage AI to solve problems.

## Copyright sensitivities

I am publishing the actual outputs of the model for research/academic purposes.

However, I am NOT publishing the entire prompt or the puzzle input, as requested by [Advent of Code](https://adventofcode.com/2024/about). The "part1" and "part2" are literally just a drag and select, cut-n-paste from their website.

(If I've screwed up and accidentally published something I shouldn't have, please let me know!)

## Models of choice

### Llama 3.1 8B

Unless otherwise stated, I'll default to the Ollama provided Llama3.1 8B parameter model:

```
$ ollama show llama3.1
  Model
    architecture        llama     
    parameters          8.0B      
    context length      131072    
    embedding length    4096      
    quantization        Q4_K_M    

  Parameters
    stop    "<|start_header_id|>"    
    stop    "<|end_header_id|>"      
    stop    "<|eot_id|>"             

  License
    LLAMA 3.1 COMMUNITY LICENSE AGREEMENT            
    Llama 3.1 Version Release Date: July 23, 2024    
```

Why? Because I have a 24GB MacBook Air M2 and it's reasonably fast at inferencing GenAI token responses.
