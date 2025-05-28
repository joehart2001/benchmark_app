import json
import yaml

import json

def contains_r2scan(obj):
    """
    Recursively check if 'r2scan' appears anywhere in the object.
    """
    if isinstance(obj, dict):
        return any(contains_r2scan(k) or contains_r2scan(v) for k, v in obj.items())
    elif isinstance(obj, list):
        return any(contains_r2scan(item) for item in obj)
    elif isinstance(obj, str):
        return "r2scan" in obj.lower()
    return False

def remove_sections_with_r2scan_json(input_path, output_path=None):
    """
    Remove any top-level section from a JSON file if 'r2scan' appears anywhere in that section.

    Parameters:
        input_path (str): Path to the input .json file
        output_path (str or None): Path to save cleaned .json file (or overwrite original)
    """
    with open(input_path, 'r') as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError("Expected top-level JSON object to be a dictionary")

    cleaned_data = {k: v for k, v in data.items() if not contains_r2scan(v)}

    out_path = output_path or input_path
    with open(out_path, 'w') as f:
        json.dump(cleaned_data, f, indent=2)

    print(f"Removed {len(data) - len(cleaned_data)} sections containing 'r2scan'. Saved to {out_path}")


if __name__ == "__main__":
    remove_sections_with_r2scan_json("zntrack.json")