def CountYouMe(data):
    data = f.readlines()
    count = 0
    for lines in data:
        for words in lines.split():
            #global word
            words = words.lower()
            for letter in words:
                if letter == ".":
                    words = words.replace(".", "")
                    f.write(words)
            if words == "you":
                print(words)
                count += 1
            elif words == "me":
                print(words)
                count += 1
                        
    print(f"The number of 'You' and 'Me' words is {count}.")
    return

with open("F:\\class_12\\Notes.txt", "r+") as f:
    CountYouMe(f)
                
                    
