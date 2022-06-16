from jamo import h2j, j2hcj
from mos_dict import convert_to_morse_code

def separate_string(undetermined_string):                                     # 한글 / 숫자/영어 나누고 if로
    separated_string = j2hcj(h2j(undetermined_string))
    separated_string_list = list(separated_string)
    return separated_string_list

def converted_morse_code_list_output(separated_string_list):
    converted_morse_code_list = []
    for separated_string_list_element in separated_string_list:
        converted_morse_code = convert_to_morse_code(separated_string_list_element)     # if 문으로 클래스 객체로 한글/영어/숫자 모스부호
        converted_morse_code_list.append(converted_morse_code)
    return converted_morse_code_list

def translate_string_to_morse_code(input_string):
    separated_string = separate_string(input_string)
    output_morse_code = converted_morse_code_list_output(separated_string)
    return output_morse_code


print(translate_string_to_morse_code('abfgdgd 12312312312'))
# print(separate_string('안녕하세요'))
# print(converted_morse_code_list_output(['ㅇ', 'ㅏ', 'ㄴ']))

