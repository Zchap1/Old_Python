

def encrypt(plaintext,seed):
    rawstring = plaintext #get raw string
    fixedstring = rawstring.upper()#convert to uppercase
    fixedstring= fixedstring.replace(" ","")#remove the spaces
    string_array = []
    cyphertext = ""
    for character in fixedstring:
        number = ((ord(character) - 65)+seed )%26
        string_array.append(number)
        cyphertext+= chr((number % 26)+65)

#    print(fixedstring)
#    print (string_array)
    print (cyphertext)    

def decrypt(cypertext,seed):
    rawstring = cypertext #get the cyphertext
    fixedstring = rawstring.upper() #ensure that is uppercase
    #fixstring = fixedstring.replace(" ","")#remove the spaces
    string_array=[]
    plaintext = ""
    for character in fixedstring:
        if character == " ":
            plaintext += " "
            continue
        else:
            number = ((ord(character)-39) -seed)% 26
            string_array.append(number)
            plaintext+= chr((number%26)+65)
#    print (fixedstring)ng
#    print(string_array)
    print (plaintext)
    print(string_array)
    print(number)
    
print("\n\nWelcome to a demonstration of a simple ceaser shift cypher. ")
#print("\nTo continue, please press \"E\" to encrypt or \"D\" to decrpty.  ")
command= input("\nTo continue, please press \"E\" to encrypt or \"D\" to decrypt. \n ")
command = command.upper()
if command == "E":
    plaintext = str(input("Enter the plaintext you'd like to encrypt:  "))
    seed = int(input("enter the key  "))
    encrypt(plaintext,seed)
elif command=="D":
    cyphertext = str(input("Enter the cyphertext you'd like to decrypt:  "))
    seed = int(input("enter the key  "))
    decrypt(cyphertext,seed)
else :
    print ("\n\n Entry not recognized.")
    
input("\n\nPress any key to exit.")
