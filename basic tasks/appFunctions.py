#Task: Write a Python script that calculates the factorial of a given number.

def factorial_calculator(number):
    calculated_number = 1

    if (number == 0):
        return 1
    elif (number == 1):
        return 1
    else:
        for i in range(1,int(number)):
            calculated_number = calculated_number * number
            number -= 1
    return calculated_number 


# Write a Python script that counts the occurrences of each word in a given text
# text = "the quick brown fox jumps over the lazy dog. the dog barks loudly, but the fox remains calm."

def find_occurrances_in_text(text):
    checked = text.replace(".","")
    text = checked.replace(",","")
    
    char = str.split(text)
    index_number = 0
    for i in char:
        index_number = 0
        print(str(i)+": ",end="")
        for a in range(0,len(char)):
            if ( i == char[a] ):
                index_number += 1
            else:
                continue
        print(index_number)

    