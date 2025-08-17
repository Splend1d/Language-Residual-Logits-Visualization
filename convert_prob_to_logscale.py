import json
import math

input_path = "assets/phi4-multimodal-noaudio-from-phi4-multimodal.jsonl"           # <- change this
output_path = "assets/phi4-multimodal-noaudio-from-phi4-multimodal.logscale.jsonl"  # <- change this

def log_or_neg_inf(p):
    # Convert probability to log scale; handle zeros safely
    return math.log(p) if p > 0 else float("-inf")

data = []
with open(input_path, "r", encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        obj = json.loads(line)
        # Transform candidates -> log scale
        if "candidates" in obj and isinstance(obj["candidates"], dict):
            obj["candidates"] = {k: log_or_neg_inf(v) for k, v in obj["candidates"].items()}
        data.append(obj)

with open(output_path, "w", encoding="utf-8") as f:
    for obj in data:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")

print(f"Saved log-scale JSONL to: {output_path}")
