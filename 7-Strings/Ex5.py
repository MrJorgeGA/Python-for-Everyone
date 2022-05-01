def confidence (str):
    start = str.find(":")+1
    confidence = float (str[start:])
    return confidence

str = input ("message: ")
print (confidence(str))