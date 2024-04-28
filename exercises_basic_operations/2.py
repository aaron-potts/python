digits = 4936

ones = digits % 10
tens = (digits % 100)// 10
hundreds = (digits % 1000)//100
thousands = (digits % 10000)//1000

print(ones)
print(tens)
print(hundreds)
print(thousands)