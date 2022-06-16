from jamo import h2j, j2hcj
from test_sub import convert_to_morse_code


def separate_string(string_string):
    separated_consonant_vowel = j2hcj(h2j(string_string))
    separated_consonant_vowel_list = list(separated_consonant_vowel)
    return separated_consonant_vowel_list
    
def converted_morse_code_list_output(separated_string_list):
    converted_morse_code_list = []
    for separated_string_list_element in separated_string_list:
        converted_morse_code = convert_to_morse_code(separated_string_list_element)
        converted_morse_code_list.append(converted_morse_code)
    return converted_morse_code_list

def translate_string_to_morse_code(input_string):
    separated_string = separate_string(input_string)
    output_morse_code = converted_morse_code_list_output(separated_string)
    return output_morse_code


print(translate_string_to_morse_code('2022년 abc'))

