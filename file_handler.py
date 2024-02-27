import json
import os
import shutil

tipAvizMap = {
    'Aviz Initial': 'ini',
    'Aviz Modificator': 'mod',
    'Aviz Prelungire': 'pre',
    'Aviz Reducere': 'red',
    'Aviz Stingere': 'sti',
}


def copy_files(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    tip_aviz = data.get("tip")
                    output_subdir = tipAvizMap.get(tip_aviz, "")
                    if output_subdir:
                        output_subdir_path = os.path.join(output_dir, f"avize-{output_subdir}")
                        os.makedirs(output_subdir_path, exist_ok=True)
                        shutil.copy(file_path, output_subdir_path)


def process_json_files(directory):
    data_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                numar = data.get("numar")
                identificator = data.get("identificator", {}).get("v")
                data_list.append({"numar": numar, "identificator": identificator})
    return data_list
