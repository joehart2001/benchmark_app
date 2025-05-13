
import mlipx
import pickle
import os
import zntrack
project = zntrack.Project(directory=".")

with open("lattice_const_dict.pkl", "rb") as f:
    lattice_const_dict = pickle.load(f)
with open("ref_lat_const_node.pkl", "rb") as f:
    lattice_const_ref_node = pickle.load(f)


app_lattice_const, *_ = mlipx.LatticeConstant.mae_plot_interactive(
    node_dict=lattice_const_dict,
    ref_node = lattice_const_ref_node,
    run_interactive=False,
)



if __name__ == "__main__":
    app_lattice_const.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8050)))
