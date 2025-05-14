
import mlipx
import pickle
import os
import zntrack
from pathlib import Path
import yaml

# Specify the file path and mode for opening the file
with open("new_model_registry.yaml", "r") as file:
	data = yaml.safe_load(file)
models = list(data.keys()) #+ ["ref-data"]

# RM GITIGNORES IN NODE FOLDERS: find nodes -name .gitignore -exec bash -c 'echo "!*" > "$0"' {} \;

import dvc.api
import json
from mlipx.cli.main import load_node_objects, load_nodes_and_ref_node_lat


from mlipx.cli.main import full_benchmark_compare

app = full_benchmark_compare(
    models=models,
    return_app=True,
    report=False,
)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print(f"Starting Dash app on port {port}...")
    app.run(host="0.0.0.0", port=port, debug=True)

