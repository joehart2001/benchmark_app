
import mlipx
import pickle
import os
import zntrack
# project = zntrack.Project(directory=".")
# lattice_const_ref_node = project.load("LatticeConst-ref")
import yaml

# Specify the file path and mode for opening the file
with open("new_model_registry.yaml", "r") as file:
	data = yaml.safe_load(file)

models = list(data.keys())

import dvc.api
import json
from mlipx.cli.main import load_node_objects, load_nodes_and_ref_node

fs = dvc.api.DVCFileSystem()
with fs.open("zntrack.json", mode="r") as f:
    all_nodes = list(json.load(f).keys())

nodes = ["*LatticeConst*"]
glob = True

node_objects = load_node_objects(nodes, glob, models, all_nodes, split_str="_lattice-constant")

lattice_const_dict, lattice_const_ref_node = load_nodes_and_ref_node(node_objects, models, split_str="_lattice-constant")


print(f"output path {lattice_const_ref_node.output_path}")

app_lattice_const, *_ = mlipx.LatticeConstant.mae_plot_interactive(
    node_dict=lattice_const_dict,
    ref_node = lattice_const_ref_node,
    run_interactive=False,
)


if __name__ == "__main__":
    app_lattice_const.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8050)))
