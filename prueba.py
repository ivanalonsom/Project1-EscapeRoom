import re
# Cadena de texto donde buscar la contraseña
texto = "ewf@adewq20wefewfewfewf'lkjashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfklj24ashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfkljashdfkl"
# Función para extraer la contraseña usando regex
def extraer_contraseña(texto):
    # Definir el patrón regex basado en las pistas
    patron = r'\d+'

    coincidencias = re.findall(patron, texto)

    # Concatenar todas las secuencias de dígitos encontradas
    resultado = ''.join(coincidencias)

    # Mostrar el resultado
    return resultado



res = extraer_contraseña(texto)

print(res)
