text = "X-DSPAM-Confidence:    0.8475";

number=text.find('0')
a=float(text[number:number+6])
print(a)
