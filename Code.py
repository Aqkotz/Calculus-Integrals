a = float(input('Enter left endpoint'))
b = float(input('Enter right endpoint'))
n = int(input('Enter number of subintervals'))
f = input('Enter the function')
LRAM = 0.0
RRAM = 0.0
MRAM = 0.0
x = a
h = (b - a)/n
for i in range (n):
    x1 = x
    f1 = eval(f)
    LRAM = LRAM + f1*h
    x = x + h
    x2 = x
    f2 = eval(f)
    RRAM = RRAM + f2*h
    x = (x1 + x2)/2
    fm = eval(f)
    MRAM = MRAM + fm*h
    x = x2
    
print('LRAM = ',LRAM)
print('RRAM = ',RRAM)
print('MRAM = ',MRAM)
