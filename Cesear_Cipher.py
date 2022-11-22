# This program is a simple Encryption-Decryption.
# Where e = encryption, d = decryption

end = 0
while end != 1:
    user_word = (input("\n1. Encrpyt\n2. Decrypt\nEnter What to do? ")).upper()
    if user_word == 'ENCRYPT' or user_word == '1':
        e_word = input("Enter word to Encrypt : ")
        for e_letter in e_word:
            e_index_letter = ord(e_letter)
            e_index_letter += 27
            e_word_enc = chr(e_index_letter)
            print(e_word_enc, end="")
        print("\tThis is your Encrypted word!")
    elif user_word == 'DECRYPT' or user_word == '2':
        d_word = input("Enter word to Decrypt : ")
        for letter in d_word:
            d_index_letter = ord(letter)
            d_index_letter -= 27
            d_word_dec = chr(d_index_letter)
            print(d_word_dec, end="")
        print("\tThis is your Decrypted word!")
    elif user_word == 'END' or user_word == 'Q':
        print("Task completed\nEnding...")
        end += 1
    else:
        print("returning null...")
