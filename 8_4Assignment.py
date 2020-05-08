fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    line = line.rstrip()
    line = line.split()
    #print(line)
    for i in line: 
        #print(i)
        if i not in lst:   #tekrari engelliyor listede varsa yazmiyor
            lst.append(i)
            
lst.sort() 
print(lst)
