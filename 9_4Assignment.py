file =input("Enter file:")

if len(file) < 1:
    name = "mbox-short.txt"

fh = open(name)

from_lines = []
emails = {}

for line in fh:
    line = line.rstrip()
    if line.find('From ') == 0:
        line = line.split(' ')
        email = line[1]
        if email not in emails:
            emails[email] = 1
        else:
            emails[email] += 1

email = ''
count = 0

for key in emails:
    if emails[key] > count:
        count = emails[key]
        email = key

print ("%s %s" % (email, str(count)))
