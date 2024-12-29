##Para muchas aplicaciones matemáticas, conocer la potencia de 2 más grande que es menor o igual a cierto
# número, es muy útil. Escribe una función exponente, que dado un número n, retorne el exponente de dicha 
# potencia de 2 más grande. Por ejemplo, si el número es 65, tu programa debe retornar 6, ya que 2⁶  = 64.

def exponente(n):
    i = 0
    while 2**i <= n: 
        i+=1
    
    return i-1

i = exponente(150)
print("Donde 2^",i, 2**i) 
