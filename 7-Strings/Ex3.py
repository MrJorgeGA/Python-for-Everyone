def count (word, letter):
    counter = 0
    for each in word:
        if letter == each:
            counter += 1
    return counter

word = input ("Word: ")
letter = input ("Letter: ")
print (count (word, letter))