import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dic = {row.letter:row.code for (index, row) in df.iterrows()}

def generate_phonetic():
    name = input('Enter a word: ').upper()
    try:
        result = [nato_dic[letter] for letter in name]
    except KeyError:
        print("Sorry, only alphabets in the letters please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()
