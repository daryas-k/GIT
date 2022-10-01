import random
n=int(input('Введіть кількість автомобільних номерів'))
buk="CM "
ABC="ABCEHIKMOPTX"
first=' '
second=' '
third=" "
probil=' '
number=' '
i=0
while i<9:
    first=random.choice(ABC)
    second=random.choice(ABC)
    third=random.choice(ABC)
    x=random.randint(10000,99999)
    cifr=str(x)
    number=first+second+third+probil+cifr
    print(number)
    i=i+1
