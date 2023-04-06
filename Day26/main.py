import pandas

with open("nato_phonetic_alphabet.csv") as phonetic:
    df = pandas.read_csv(phonetic)


#Loop through rows of a data frame

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# for (index, row) in df.iterrows():
#     print(row.letter, row.code)
phonetic_dict = {row.letter:row.code for index, row in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        phonetic_list = [phonetic_dict[i] for i in user_input]
    except KeyError:
        print("oops, only alphabets allowed")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()
