import csv
import pandas as pd

data = pd.read_csv("morse.csv")


alphabet = data.iloc[0:25]
alphabet_letters = alphabet.iloc[:,0]
alphabet_morse = alphabet.iloc[:,1]

alphabet_dict = dict(zip(alphabet_letters, alphabet_morse))
print(alphabet_dict)

alphabet_dict["A"] = ".-"

morse_output = ""
names = input("Please enter a letter or name: ")
for i in names:
    i = i.capitalize()
    morse_output += str(alphabet_dict[i]) + " "
print(morse_output)
