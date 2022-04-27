try:
    hours = (input ("Enter Hours: "))
    hours = int (hours)
    rate = input ("Enter Rate: ")
    rate = float (rate)
    if hours > 40:
        print ("Pay:", 40*rate+(hours-40)*rate*1.5)
    else: 
        print("Pay:", hours*rate)
except:
    print ("Error, please enter numeric input")