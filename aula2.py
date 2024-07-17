x = int(input())
if x > 0:
    print("positivo")
elif x < 0:
    print("negativo")

jogos = ["Crash", "Spyro", "Bioshock", "Fifa"]

for lista in jogos:
    print(lista, "\n")

k = int(input())

if k > 1:
    for i in range(2, int(k / 2) + 1):
        if (k % i) == 0:
            print("não é númerio primo")
            break
    else:
        print("é primo", k)

else:
    print("não é primo")

n1=0
n2=1
temp=0
count=0
term = int(input)
while(count != term):
    print(n2, end=" ")
    temp = n2
    n2 = n2+n1
    n1=temp
    count+=1
