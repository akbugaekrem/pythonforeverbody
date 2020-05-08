text = "X-DSPAM-Confidence:    0.8475";
aa = text.find ('0')
bb = text.find ('', aa)
number = text[aa:]
n = float(number)
print(n)
