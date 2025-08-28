f= open("twinkle.txt", "r")

file = f.read()

# to decode you have to write the pattern ad it automatically decodes from file

new = file
word = str()
Code = input("Enter a pattern to UnCensor it...")

if (Code in file):
    if (Code == "#####"):
        word = "twinkle"
    if (Code == "****"):
        word = "star"
    if (word != ""):
        new= file.replace(Code, word)
        with open("twinkle.txt", "w") as s:
            s.write(new)    
        print("Found \n Decoded")
else:
    print("Not Found")




f.close()
      
