sum = 0
counter = 0

while True:
    respuesta = input ("Enter a number: ")
    if respuesta == "done" :
        break
    try:
        respuesta = float (respuesta)
        sum += respuesta
        counter += 1
    except:
        print ("Invalid input")
        continue
    try: 
        if respuesta > max :
            max = respuesta
        if respuesta < min :
            min = respuesta
    except:
        max = respuesta
        min = respuesta

try:
    if sum%1 == 0.0: 
        sum = int (sum)
    if min%1 == 0.0:
        min = int (min)
    if max%1 == 0.0:
        max = int (max)
    print (sum, counter, max, min)
except:
    print ("No valid input")