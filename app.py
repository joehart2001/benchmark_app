
import mlipx
import pickle



if __name__ == "__main__":
    
    with open("lattice_const_dict.pkl", "rb") as f:
        node_dict = pickle.load(f)
    with open("ref_lat_const_node.pkl", "rb") as f:
        ref_node = pickle.load(f)

    
    mlipx.LatticeConstant.mae_plot_interactive(
        node_dict=node_dict,
        ref_node=ref_node,
        ui="browser",
        run_interactive=True,
        use_render=True,
    )