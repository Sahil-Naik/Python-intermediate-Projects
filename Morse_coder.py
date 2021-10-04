# This is a simple Program which converts either Words to Morse code or Morse Code to Words.

# Below is the Morse Code dictionary. The program takes letter from the given word and returns it's appropriate morse version. 
morse_code = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..',
              'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
              'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', " ":" "}
key_list = list(morse_code.keys())
val_list = list(morse_code.values())
temp_code = []
chc = int(input("Enter what to do?\n1 = Word to Morse code\n2 = Morse code to Word\nEnter choice = "))
if chc == 1:
    user1 = input("Enter to translate into morse : ").upper()
    print("Morse code is = ", end=" ")
    for i1 in user1:
        letter = morse_code.get(i1)
        print(letter, end=" ")
elif chc == 2:
    temp_word = ""
    user2 = input("Enter Morse code = ")
    user2 += " "
    for i2 in user2:
        if i2 != " ":
            temp_word += i2
        elif i2 == " ":
            temp_code.append(temp_word)
            temp_word = ""
    for i3 in temp_code:
        if i3 in val_list:
            pos = val_list.index(i3)
            print(key_list[pos], end="")
        else:
            print("Unknown Morse!")
