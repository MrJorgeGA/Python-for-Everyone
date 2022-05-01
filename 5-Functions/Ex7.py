def computegrade (score):
    if score < 0.6:
        return "F"
    elif score < 0.7:
        return "D"
    elif score < 0.8:
        return "C"
    elif score < 0.9:
        return "B"
    else: 
        return "A"

try:

    score = float (input ("Enter score: "))

    if score > 1: #cortocircuito
        1/0

    grade = computegrade (score)
    print (grade)
    
except:
    print ("Bad score")