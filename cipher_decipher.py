import os
os.system('cls')

# ----------------------------------------------CIPHERING 101-------------------------------------------

# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def cipher(start_text,shift_amount):
#     end_text = ''

#     for char in start_text:
#         if char in alphabets:

#             # Finding index of that character in alphabets
#             position = alphabets.index(char)

#             # Adding shift value to current index value 
#             new_position = position + shift_amount

#             # Adding shifted alphabet value to end_text for generating encoded text
#             end_text += alphabets[new_position]

#         # If text includes some special characters we can pass them as it is
#         else:
#             end_text += char

#     print(f'Here is your encoded text: {end_text}')


# print('Welcome to this CIPHER PROGRAM ')
# text = input("Please enter your text - ").lower()
# shift = int(input("Please enter the shift amount - "))

# shift = shift % 26

# cipher(start_text = text, shift_amount = shift)





# --------------------------------------------DECIPHERING 101----------------------------------------------------
# Your encoded msg above goes here. eg msg = 'hnumjw'
msg = ''

letters = 'abcdefghijklmnopqrstuvwxyz'

# To find our key to decode msg we must use for loop to loop through out letters length i.e 26
for key in range(len(letters)):
    decoded_text = ''
    for each in msg:
        if each in letters:
            # Find position of each in letters
            num = letters.find(each)
            # Try each combination of key from 0 to 25
            num = num - key
            # Add decoded alphabet to decoded text
            decoded_text += letters[num]

        else:
            # If text includes some special characters we can pass them as it is
            decoded_text += each

    # Shows every combination with decoded text
    print(f'Hacking key {key}: {decoded_text}')
    
