import json

file_path = "./morse_code_data.json"

with open(file_path, 'r') as file:
    mosdata_json = json.load(file)

def convert_to_morse_code(separated_string_list_element):
    if separated_string_list_element == ' ':
        return ' '
    filtered_json = filter(lambda data: separated_string_list_element in data['word'], mosdata_json)
    return list(filtered_json)[0]['mos']
    
