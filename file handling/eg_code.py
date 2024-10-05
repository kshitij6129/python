try:
    with open (r"c:\Users\pc1\Desktop\New Text Document.txt","r")as file:
        for line in file:
            print(line,end="")
except FileNotFoundError:
    print("The file'New text document.txt'does not exist")
except Exception as e:
    print("an error accurred:",e)
    