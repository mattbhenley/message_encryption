alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ''

message = input('Please enter a message: ')

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        #print(position) -taking out so the user only sees the new character assignment.
        newPosition = (position + key) % 26
        #print(newPosition) - taking out so the user only sees the new character assignment.
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character

print('Your new message is', newMessage)

# Testing key reconigniton 
# print(alphabet[2])
# print(alphabet[18])
# print(alphabet[25])