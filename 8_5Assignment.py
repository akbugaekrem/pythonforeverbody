fname =input("Enter file name: ")
counter = 0
fh = open(fname)

for line in fh :
    line = line.rstrip()
    #print(line)
    if not line.startswith('From '): continue        
    words = line.split()
    print(words[1])
    counter +=1

print ("There were", counter, "lines in the file with From as the first word")
