# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Create a dictionary in this format
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = []
def generate_dict():
    for letter in word:
        try:
            new_word = phonetic_dict[letter]
        except KeyError:
            print("Sorry, only letters in the alphabet please")
            generate_dict()
        else:
            output_list.append(new_word)

    print(output_list)

    generate_dict()
    
