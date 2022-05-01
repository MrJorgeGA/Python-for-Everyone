sum = 0
counter = 0

while True:
    respuesta = input ("Enter a number: ")
    if respuesta == "done" :
        break
    try:
        sum += float (respuesta)
        counter += 1
    except:
        print ("Invalid input")

if sum%1 == 0.0: 
    sum = int (sum)

try:
    print (sum, counter, sum/counter)
except:
    print (0,0,0)