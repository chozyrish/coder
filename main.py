DICT = {'а' : '.-', 'б' : '-...' , 'в' : '.--', 'г' : '--.', 'д' : '-..', 'е' : '.', 'ж' : '...-', 'з' : '--..', 'и' : '..', 'й' : '.---', 'к' : '-.-', 'л' : '.-..', 'м' : '--',
        'н' : '-.', 'о' : '---', 'п' : '.--.', 'р' : '.-.', 'с' : '...', 'т' : '-', 'у' : '..-', 'ф' : '..-.', 'х' : '....', 'ц' : '-.-.','ч' : '---.', 'ш' : '----', 'щ' : '--.-',
        'ъ' : '.--.-.', 'ы' : '-.--', 'ь' : '-..-', 'э' : '..-..', 'ю' : '..--', 'я' : '.-.-', '1' : '.----', '2' : '..---', '3' : '...--', '4' : '....-', '5' : '.....', '6' : '....-',
        '7' : '--...', '8' : '---..', '9' : '----.', '0' : '-----', ' ': ' '}
DICT_REVERSE = {value: key for key, value in DICT.items()}

def crypt(mes):
    stroka = ""
    for symbol in mes:
        if symbol != " ":
            stroka += DICT[symbol] + " "
        else:
            stroka += " "
    return stroka

def decrypt(mes):
    stroka = ""
    sumbol = mes.split()
    for i in range(len(sumbol)):
        if sumbol[i] == ' ' and sumbol[i + 1] == ' ':
            stroka += DICT_REVERSE[sumbol[i]]
            stroka += ' '
        else:
            stroka += DICT_REVERSE[sumbol[i]]

    return stroka

do = input('Введите действие: 1 - шифровать, 2 - дешифровать ')

if do == '1':
    a = input().lower()
    print(crypt(a))
elif do == '2':
    a = input().lower()
    print(decrypt(a))

