def Mult(Tabla):
    x = 1

    while x <=12:
        y = Tabla * x
        print("{0}*{1}={2}".format(Tabla, x, y))
        x = x + 1
        
        
Tabla = int(input("Numero que desea?: "))

Mult(Tabla)
