# json 모듈 로드
import json

mos_data = [
    {'type':'kor', 'word':'ㄱ', 'mos':'.-..'}, {'type':'kor', 'word':'ㄴ', 'mos':'..-.'}, 
    {'type':'kor', 'word':'ㄷ', 'mos':'-...'}, {'type':'kor', 'word':'ㄹ', 'mos':'...-'}, 
    {'type':'kor', 'word':'ㅁ', 'mos':'--'}, {'type':'kor', 'word':'ㅂ', 'mos':'.--'},
    {'type':'kor', 'word':'ㅅ', 'mos':'--.'}, {'type':'kor', 'word':'ㅇ', 'mos':'-.-'},
    {'type':'kor', 'word':'ㅈ', 'mos':'.--.'}, {'type':'kor', 'word':'ㅊ', 'mos':'-.-.'},
    {'type':'kor', 'word':'ㅋ', 'mos':'-..-'}, {'type':'kor', 'word':'ㅌ', 'mos':'--..'},
    {'type':'kor', 'word':'ㅍ', 'mos':'---'}, {'type':'kor', 'word':'ㅎ', 'mos':'.---'},
    {'type':'kor', 'word':'ㄲ', 'mos':'.-...-..'}, {'type':'kor', 'word':'ㄸ', 'mos':'-...-...'},
    {'type':'kor', 'word':'ㅃ', 'mos':'.--.--'}, {'type':'kor', 'word':'ㅆ', 'mos':'--.--.'},
    {'type':'kor', 'word':'ㅉ', 'mos':'.--..--.'}, {'type':'kor', 'word':'ㅏ', 'mos':'.'},
    {'type':'kor', 'word':'ㅑ', 'mos':'..'}, {'type':'kor', 'word':'ㅓ', 'mos':'-'},
    {'type':'kor', 'word':'ㅕ', 'mos':'...'}, {'type':'kor', 'word':'ㅗ', 'mos':'.-'},
    {'type':'kor', 'word':'ㅛ', 'mos':'-.'}, {'type':'kor', 'word':'ㅜ', 'mos':'....'},
    {'type':'kor', 'word':'ㅠ', 'mos':'.-.'}, {'type':'kor', 'word':'ㅡ', 'mos':'-..'},
    {'type':'kor', 'word':'ㅣ', 'mos':'..-'}, {'type':'kor', 'word':'ㅔ', 'mos':'-.--'},
    {'type':'kor', 'word':'ㅐ', 'mos':'--.-'}, {'type':'kor', 'word':'ㅒ', 'mos':'....-'},
    {'type':'kor', 'word':'ㅖ', 'mos':'.....-'}, {'type':'kor', 'word':'ㅘ', 'mos':'.-.'},
    {'type':'kor', 'word':'ㅙ', 'mos':'.---.-'}, {'type':'kor', 'word':'ㅚ', 'mos':'.-..-'},
    {'type':'kor', 'word':'ㅝ', 'mos':'....-'}, {'type':'kor', 'word':'ㅞ', 'mos':'....-.--'},
    {'type':'kor', 'word':'ㅟ', 'mos':'......-'}, {'type':'kor', 'word':'ㅢ', 'mos':'-....-'},
    {'type':'kor', 'word':'ㄳ', 'mos':'.-..--.'}, {'type':'kor', 'word':'ㄵ', 'mos':'..-..--.'},
    {'type':'kor', 'word':'ㄶ', 'mos':'..-..---'}, {'type':'kor', 'word':'ㄺ', 'mos':'...-.-..'},
    {'type':'kor', 'word':'ㄻ', 'mos':'...---'}, {'type':'kor', 'word':'ㄼ', 'mos':'...-.--'},
    {'type':'kor', 'word':'ㄽ', 'mos':'...---.'}, {'type':'kor', 'word':'ㄾ', 'mos':'...---..'},
    {'type':'kor', 'word':'ㄿ', 'mos':'...----'}, {'type':'kor', 'word':'ㅀ', 'mos':'...-.---'},
    {'type':'kor', 'word':'ㅄ', 'mos':'.----.'},

    {'type':'eng', 'word':['a','A'], 'mos':'.-'},  {'type':'eng', 'word':['b','B'], 'mos':'-...'},  
    {'type':'eng', 'word':['c','C'], 'mos':'-.-.'},  {'type':'eng', 'word':['d','D'], 'mos':'-..'},  
    {'type':'eng', 'word':['e','E'], 'mos':'.'}, {'type':'eng', 'word':['f','F'], 'mos':'..-.'}, 
    {'type':'eng', 'word':['g','G'], 'mos':'--.'},  {'type':'eng', 'word':['h','H'], 'mos':'....'}, 
    {'type':'eng', 'word':['i','I'], 'mos':'..'}, {'type':'eng', 'word':['j','J'], 'mos':'.---'},  
    {'type':'eng', 'word':['k','K'], 'mos':'-.-'}, {'type':'eng', 'word':['l','L'], 'mos':'.-..'}, 
    {'type':'eng', 'word':['m','M'], 'mos':'--'},  {'type':'eng', 'word':['n','N'], 'mos':'-.'},  
    {'type':'eng', 'word':['o','O'], 'mos':'---'},  {'type':'eng', 'word':['p','P'], 'mos':'.--.'},  
    {'type':'eng', 'word':['q','Q'], 'mos':'--.-'}, {'type':'eng', 'word':['r','R'], 'mos':'.-.'},  
    {'type':'eng', 'word':['s','S'], 'mos':'...'},  {'type':'eng', 'word':['t','T'], 'mos':'-'}, 
    {'type':'eng', 'word':['u','U'], 'mos':'..-'},  {'type':'eng', 'word':['v','V'], 'mos':'...-'},  
    {'type':'eng', 'word':['w','W'], 'mos':'.--'}, {'type':'eng', 'word':['x','X'], 'mos':'-..-'},  
    {'type':'eng', 'word':['y','Y'], 'mos':'-.--'}, {'type':'eng', 'word':['z','Z'], 'mos':'--..'}, 

    {'type':'num', 'word':'0', 'mos':'-----'}, {'type':'num', 'word':'1', 'mos':'.----'},
    {'type':'num', 'word':'2', 'mos':'..---'}, {'type':'num', 'word':'3', 'mos':'...--'},
    {'type':'num', 'word':'4', 'mos':'....-'}, {'type':'num', 'word':'5', 'mos':'.....'},
    {'type':'num', 'word':'6', 'mos':'-....'}, {'type':'num', 'word':'7', 'mos':'--...'},
    {'type':'num', 'word':'8', 'mos':'---..'}, {'type':'num', 'word':'9', 'mos':'----.'},
]

# json 파일로 저장
with open('morse_code_data.json', 'w') as f : 
	json.dump(mos_data, f, indent=4)
