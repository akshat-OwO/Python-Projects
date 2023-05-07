import pandas

nato_data = pandas.read_csv("NATO/nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

name = input("enter your name: ").upper()
nato_list_name = [nato_dict[n] for n in name if n in nato_dict.keys()]
print(nato_list_name)