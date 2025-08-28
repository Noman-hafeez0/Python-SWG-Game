f= open("twinkle.txt", "r")

file = f.read()


# To Encode a file you must have to Provide a name to censor
new = file
word = input("Enter a Word to Censor it...")
Code = str()

if (word in file):
    if (word == "twinkle"):
        Code = "#####"
    elif (word == "star"):
        Code = "****"
    if (Code != ""):
        new= file.replace(word, Code)
        with open("twinkle.txt", "w") as s:
            s.write(new)    
            print("Found \n Encoded")
else:
    print("Not Found")



f.close()
      
