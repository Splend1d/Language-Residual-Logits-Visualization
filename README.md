## Introduction 

https://splend1d.github.io/Language-Residual-Logits-Visualization/ 

## Experiments
#### Datasets

[hf-audio/esb-datasets-test-only-sorted](https://huggingface.co/datasets/hf-audio/esb-datasets-test-only-sorted)

#### non-LLM-based:

openai/whisper-large-v3: https://www.kaggle.com/code/a24998667/lrlv-get-next-word-logits-whisper 50 samples finished in 3h 47m 44s 

nvidia/parakeet-tdt-0.6b-v2:

nvidia/canary-1b-flash:

#### LLM-based:

ibm-granite/granite-speech-3.3-8b: https://www.kaggle.com/code/xooldude/lrlv-get-next-word-logits-granite/

microsoft/Phi-4-multimodal-instruct: https://www.kaggle.com/code/a24998667/lrlv-get-next-word-logits-phi4

microsoft/Phi-4-multimodal-instruct Ablation No Lora: https://www.kaggle.com/code/a24998667/lrlv-get-next-word-logits-phi4-no-lora

nvidia/canary-qwen-2.5b:

#### LLM-based with `microsoft/Phi-4-multimodal-instruct` as target:

microsoft/Phi-4-multimodal-instruct Ablation No Lora: https://www.kaggle.com/code/a24998667/lrlv-get-next-word-logits-from-phi4-phi4-no-lora

microsoft/Phi-4-multimodal-instruct Ablation No Audio: https://www.kaggle.com/code/a24998667/lrlv-get-next-word-logits-from-phi4-phi4-no-audi



## Analysis

Gigaspeech index3 POD1000000028_S0000030 position10 roenigk

Gigaspeech index3 POD1000000028_S0000030 position54 zmeskals

Gigaspeech index4 POD1000000028_S0000030 position10 karolyi

Gigaspeech index27 POD1000000028_S0000281 position19,20 geza pozsar

Gigaspeech index44 POD1000000028_S0000281 position16,17,18 hubert de givenchy

Gigaspeech index48 POD1000000028_S0000281 position17 riley

Gigaspeech index48 POD1000000028_S0000281 position24 harper

Gigaspeech index71 POD1000000005_S0000194 position17 shirred

Gigaspeech index74 POD1000000019_S0000063 position17 harper

Gigaspeech index89 YOU1000000141_S0000140 throwing johnson (accented)

Gigaspeech index93 POD1000000041_S0000549 nnamdi asomugha Sylvie's Love






