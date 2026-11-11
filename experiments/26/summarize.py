import csv
import json
import os

src = os.path.join(os.environ["AGENT_WINDOW_PIN"], "gold", "sample.csv")
with open(src, newline="") as f:
    scores = [float(r["score"]) for r in csv.DictReader(f)]

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
os.makedirs(out_dir, exist_ok=True)
metrics = {
    "rows": len(scores),
    "mean_score": sum(scores) / len(scores),
    "max_score": max(scores),
}
with open(os.path.join(out_dir, "metrics.json"), "w") as f:
    json.dump(metrics, f, indent=2)
    f.write("\n")
