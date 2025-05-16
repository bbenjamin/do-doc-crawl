def write_json_to_file(data, file_path):
    import json
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def create_hierarchical_json_tree(links):
    tree = {}
    for link in links:
        current_level = tree
        for part in link['path']:
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]
        current_level['text'] = link['text']
        current_level['href'] = link['href']
    return tree