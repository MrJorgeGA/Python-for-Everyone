name = input ("Enter a file name: ")
try: 
    file = open (name)
except:
    print ("Invalid file")
    exit()

sum = 0
count = 0
for line in file:
    if line.startswith ("X-DSPAM-Confidence:"):
        start = line.find (":") + 1
        sum += float (line [start:])
        count += 1

try:
    print ("Average spam confidence:", sum/count)
except:
    print ("Wrong file")