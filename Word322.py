fabonaci = [1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89 , 144 , 233 , 377 ,
            610 , 987 , 1597 , 2584 , 4181 , 6765 , 10946 , 17711 , 28657 , 46368]

text = input()
for i in fabonaci:
    if i - 1 >= len(text):
        exit()
    print(text[i - 1] , end="")
