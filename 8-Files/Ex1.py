name = input ("Enter a file name: ")
try: 
    file = open (name)
except:
    print ("Invalid file")
    exit()

for line in file:
    print (line.upper())
