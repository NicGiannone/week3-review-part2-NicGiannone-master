FileName = input("Enter the File to encrypt: ")
key = int( input("Enter the shift key: " ))
outputFileName = input("Enter the output file name: " )
Inputfile = open(FileName,'r')
OutputFile = open(outputFileName,'w')
alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
shiftedAlphabetStart = alphabet[len(alphabet) - key:]
shiftedAlphabetEnd = alphabet[:len(alphabet) - key]
shiftedAlphabet = shiftedAlphabetStart + shiftedAlphabetEnd

#print( alphabet )
#print( shiftedAlphabet )


for Message in Inputfile:
    encryptedMessage = ''
    
    for character in Message.strip():
        letterIndex = shiftedAlphabet.find( character )
        encryptedCharacter = alphabet[letterIndex]
        encryptedMessage = encryptedMessage + encryptedCharacter
    
    #print( "The encrypted message is: {0}".format( encryptedMessage ))
    print( encryptedMessage, file=outputFile )

outputFile.close()

print( "Done writing encrypted message to file {0}".format( outputFileName) )
