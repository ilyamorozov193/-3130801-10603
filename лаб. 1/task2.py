# TODO Найдите количество книг, которое можно разместить на дискете
code1b = 4
symbols1 = 25
stroki1 = 50
stran1 = 100
amountmb = 1.44
a = code1b * symbols1
b = a * stroki1
c = b * stran1
bait = amountmb * 1024 * 1024
knig = bait // c
knig1 = round(knig)
print("Количество книг, помещающихся на дискету:", knig1)
