def computepay (hours, rate):
    if hours > 40:
        return (40+(hours-40)*1.5)*rate
    return hours*rate

hours = int (input ("Enter Hours: "))
rate = float (input ("Enter Rate: "))
pay = computepay (hours, rate)
print ("Pay:", pay)