
#Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break 
    try:
        inp=float(num)
    except:
        print("Invalid input")
        continue

for value in [7,2,10,4]: 
    if largest is None:
        largest = value
    elif value>largest:  
        largest=value
        print("Maximum is", largest)            
for value in [7,2,10,4]: 
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest=value          
        print("Minimum is", smallest)
