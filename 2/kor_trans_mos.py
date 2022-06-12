from jamo import h2j, j2hcj

def separate_hangul(hangul_string):
    separated_consonant_vowel = j2hcj(h2j(hangul_string))
    separated_consonant_vowel_list = list(separated_consonant_vowel)
    return separated_consonant_vowel_list


def convert_to_morse_code(separated_hangul_list_element):
    
    consonants = {
        'ㄱ':'·-··', 'ㄴ':'··-·', 'ㄷ':'-···', 'ㄹ':'···-', 'ㅁ':'--', 'ㅂ':'·--', 
        'ㅅ':'--·', 'ㅇ':'-·-', 'ㅈ':'·--·', 'ㅊ':'-·-·', 'ㅋ':'-··-', 'ㅌ':'--··',
        'ㅍ':'---', 'ㅎ':'·---',
        'ㄲ':'·-···-··', 'ㄸ':'-···-···', 'ㅃ':'·--·--', 'ㅆ':'--·--·', 'ㅉ':'·--··--·'
    }

    vowels = {
        'ㅏ':'·', 'ㅑ':'··', 'ㅓ':'-', 'ㅕ':'···', 'ㅗ':'·-', 'ㅛ':'-·', 'ㅜ':'····', 
        'ㅠ':'·-·', 'ㅡ':'-··', 'ㅣ':'··-', 'ㅔ':'-·--', 'ㅐ':'--·-',
        'ㅒ':'····-', 'ㅖ':'·····-', 'ㅘ':'·-·', 'ㅙ':'·---·-', 'ㅚ':'·-··-', 'ㅝ':'····-', 'ㅞ':'····-·--',
        'ㅟ':'······-', 'ㅢ':'-····-' 
    }

    last_consonants = {
        'ㄳ':'·-··--·', 'ㄵ':'··-··--·', 'ㄶ':'··-··---', 'ㄺ':'···-·-··', 'ㄻ':'···---', 'ㄼ':'···-·--', 'ㄽ':'···---·', 
        'ㄾ':'···---··', 'ㄿ':'···----', 'ㅀ':'···-·---', 'ㅄ':'·----·'
    }

    if separated_hangul_list_element in consonants :
        return consonants.get(separated_hangul_list_element)
    if separated_hangul_list_element in vowels:
        return vowels.get(separated_hangul_list_element)
    if separated_hangul_list_element in last_consonants:
        return last_consonants.get(separated_hangul_list_element)
    if separated_hangul_list_element == ' ':
        return ' '

def converted_morse_code_list_output(separated_hangul_list):
    converted_morse_code_list = []
    for separated_hangul_list_element in separated_hangul_list:
        converted_morse_code = convert_to_morse_code(separated_hangul_list_element)
        converted_morse_code_list.append(converted_morse_code)
    return converted_morse_code_list

def translate_hangul_to_morse_code(input_hangul_string):
    separated_hangul = separate_hangul(input_hangul_string)
    output_morse_code = converted_morse_code_list_output(separated_hangul)
    return output_morse_code


print(translate_hangul_to_morse_code('둠칫 둠칫'))
