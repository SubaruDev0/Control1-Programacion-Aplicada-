"""
El usuario debe ingresar, a través del teclado, un valor numérico entero. [LISTO]

Luego, una función que reciba tal valor, debe calcular todos los divisores de ese numero y 
retornarlos a través de una lista. [LISTO]

Finalmente, otra función deberá imprimir el valor promedio de todos los divisores, 
en un archivo de texto (nombre a elección del grupo).[LISTO]
"""

 #JAVIER MORALES SUBARU  
def calcular_divisores(n): 
    divisores = [] 
    if n == 0: 
        print("\nTodos los números son divisores de 0") 
     
    for i in range(1, n + 1): 
        if n % i == 0: 
            divisores.append(i) 
    return divisores 
 
def promedio_divisores(divisores, archivoTXT, n): 
    with open(archivoTXT, 'w') as archivo: 
        if n == 0: 
            archivo.write("Todos los números son divisores de 0\n") 
            print(f"\nSe ha dejado constancia de esto en el archivo de texto: {archivoTXT[2:-4]}") 
        else: 
            promedio = sum(divisores) / len(divisores) 
            archivo.write(f"Los divisores de {n} son: {divisores}\n\n") 
            archivo.write(f"El promedio de los divisores es: {promedio}") 
 
while True: 
    try: 
        n = int(input("Ingresa un número entero: ")) 
        break 
    except ValueError: 
        print("\n- INGRESA UN NÚMERO VÁLIDO - \n") 
 
divisores = calcular_divisores(n) 
 
archivoTXT = "./promedio_divisores.txt" 
 
promedio_divisores(divisores, archivoTXT, n) 
 
if n != 0: 
    print(f"\nEl promedio de los divisores ha sido calculado y guardado en el archivo de texto: {archivoTXT[2:-4]}")
    


