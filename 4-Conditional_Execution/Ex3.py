try:

    score = float (input ("Enter score: "))

    if score > 1: #cortocircuito
        1/0

    if score < 0.6:
        grade = "F"
    elif score < 0.7:
        grade = "D"
    elif score < 0.8:
        grade = "C"
    elif score < 0.9:
        grade = "B"
    else:
        grade = "A"
    print (grade)
    
except:
    print ("Bad score")