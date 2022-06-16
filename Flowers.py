days = int(input())
F1 , F2 , F3 = ("G" , "C" , "V")
for i in range(0 , days):
    F1 , F2 , F3 = (F3 , F1 , F2)
print(F1+F2+F3)