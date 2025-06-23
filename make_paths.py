import os
import json

# Folder containing the band structure files
model = "uma_sm_omat"
path = f"nodes/{model}/phonons-dispersion-pred/PhononAllBatch/phonon_pred_data"



# Get all band_structure.npz files
band_structure_files = [
    f for f in os.listdir(path) if f.endswith("_band_structure.npz")
]
print(len(band_structure_files), "band structure files found.")

# Create mapping dictionary
data = {
    f.split("_")[0]: f"{path}/{f}"
    for f in band_structure_files
}

# Save to JSON
with open(f"{path}/../phonon_band_paths.json", "w") as f:
    json.dump(data, f, indent=4)

print("Saved mapping to phonon_band_paths.json")

dos_files = [f for f in os.listdir(path) if f.endswith("_dos.npz")]

dos_paths = {
    f.split("_")[0]: f"{path}/{f}"
    for f in dos_files
}

with open(f"{path}/../phonon_dos_paths.json", "w") as f:
    json.dump(dos_paths, f, indent=4)

print("Saved mapping to phonon_dos_paths.json")



thermal_files = [f for f in os.listdir(path) if f.endswith("_thermal_properties.json")]

thermal_paths = {
    f.split("_")[0]: f"{path}/{f}"
    for f in thermal_files
}

with open(f"{path}/../thermal_properties_paths.json", "w") as f:
    json.dump(thermal_paths, f, indent=4)

print("Saved mapping to thermal_properties_paths.json")