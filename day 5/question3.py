#number into alphabet
number = input("Enter any number: ")
table_of_numbers = {
"0": "Zero",
"1": "One",
"2": "Two",
"3": "Three",
"4": "Four",
"5": "Five",
"6": "Six",
"7": "Seven",
"8": "Eight",
"9": "Nine"
}
output = "" 
for ch in number:
    output += table_of_numbers.get(ch, "!") + " "
print(output)