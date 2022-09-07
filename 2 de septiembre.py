# e =["nombre", "Est Dat", "Prog Func", "inglés"]
# alumnos = ["Hugo", "Paco", "Luis", "Lupita"]
# m_e_d=[9,7,9,8]
# m_p_f=[10,8,7,9]
# m_i=[6,9,7,8]

# def reporte(fmt:int):
#     print(f"{e[0]:^{fmt}}{e[1]:^{fmt}}{e[2]:^{fmt}}{e[3]:^{fmt}}")
#     for i in range(len(alumnos)):
#      print(f"{alumnos[i]:*<{fmt}}{m_e_d[i]:+^{fmt}}{m_p_f[i]:#^{fmt}}{m_i[i]:-^{fmt}}")

# if __name__== "__main__": 
#     reporte(15)

# numeroBig=12342434343543
# print(f"{numeroBig: ,d}")
# #fijar cantidades decimales
# numeroPI=3.14165983920848
# print(f"{numeroPI:.3f}")
# #notaciones cientificas
# numeroPI=314.165983920848  
# print(f"{numeroBig:e}")
# print(f"{numeroPI:2e}")
# #porcentaje
# numeroPorciento=0.258478785
# print(f"{numeroPorciento:%}")
# print(f"{numeroPorciento:.2%}")

# #Numero binario
# print(f"{25:b}")
# #unicodes
# print(f"{65:c}")
# #Hexadecimal
# print(f"{255:x}")
# #Octal
# print(f"{255:o}")

#Escriba una funcion que genere una tabla de multiplicar recibiendo como argumento la cantidad de numeros 
#y la lista a generar

def tablas(m:int, n:int, t:int, fmt:int):
    for i in range(1,m+1):
        tabla(m,i,fmt)


def tabla(n:int, t:int, fmt:int):
      for i in range(1,n+1):
       print(f"{t:^{fmt}}x{i:^{fmt}}={i*t:^{fmt}}")

if __name__ == "__main__":
      tablas(3,4,6)       
               
