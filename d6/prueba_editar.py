texto = open('texto.txt', 'w')
texto.write('Nuevo texto')
texto.close()
texto = open('texto.txt')
print(texto.read())
texto.close()

archivo = open('texto.txt', 'a')
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open('texto.txt')
texto = archivo.read()
print(texto)
archivo.close()

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open('texto.txt', 'a')
archivo.writelines([texto + '\t' for texto in registro_ultima_sesion])
archivo.close()
archivo = open('texto.txt')
print(archivo.read())
archivo.close()
