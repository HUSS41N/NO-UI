print("***************************WELCOME TO LETTER COUNTER APP*********************************")
userName = input("Enter your name to proceed : ")
print(f"Hello {userName}")
paragraph = input('Enter your content and press enter : ')
letter = input('Enter a letter which you want to count : ')

# * LOGIC
def letter_counter(paragraph,letter):
    count = 0
    for _ in paragraph:
        if _.lower() == letter: 
            count += 1
    return count

count = letter_counter(paragraph,letter)
print(f"Letter {letter} count is : {count}")




