import re

room = ['Game Room', 'Bedroom 1', 'Bedroom 2', 'Living room', 'Outside']
gameroom_items = ['Sofa', 'Piano']
bedroom1_items = ['Queen bed', 'Bedside table']
bedroom2_items = ['Double bed', 'Mirror']
livingroom_items = ['Dining table', 'Keyboard']

def hab_list():
    print("Lista de habitaciones: ")
    for x in room:
        print(f"- {x}")


def puzle_cartas():
    carta = str(input("Al examinar más de cerca te das cuenta de que solo hay 10 cartas, una por cada valor. ¿Que carta quieres examinar?")).capitalize()
    mapa_cartas = { '1': 'Esternocleidomastoideo', 'As' : 'Esternocleidomastoideo', '2' : 'Impromtus','3' : 'Galimatías', '4': 'Anhelar','5': 'Zozobrar',
                   '6' : 'Ganzúa','7': 'Hiel','8' : 'Pedernal', 'Sota' : 'Pedernal','9' : 'Casquivano', 'Caballo' : 'Casquivano', '10' : 'Caos', 'Rey' : 'Caos'}

    mensaje = mapa_cartas.get(carta, 'Carta no encontrada')
    
    print(f"En el dorso de la carta encuentras escrita la palabra '{mensaje}'")


def extraer_contraseña(patron, texto):
    # Definir el patrón regex basado en las pistas

    coincidencias = re.findall(patron, texto)

    # Concatenar todas las secuencias de dígitos encontradas
    resultado = ''.join(coincidencias)

    # Mostrar el resultado
    return resultado


def ingresar_codigo_salida():
    try:
        # Solicitar al usuario que introduzca un código
        keyboard_code = int(input("Introduce el código en el teclado: "))
        if keyboard_code == 2024:
            return 'Llave D'
        else:
            return None
    except ValueError:
        # Capturar el error si la conversión a entero falla
        print("Código inválido.")


def moverse(actual_room, key_inv):
    hab_list()
    hab = input("¿A que habitación quiere ir?").capitalize()
    while hab not in room:
        hab = input("Elija una habitación existente").capitalize()
    if hab == 'Game Room':
        actual_room = room[0]
        return actual_room
    elif hab == 'Bedroom 1' and 'Llave A' in key_inv:            
        actual_room = room[1]
        return actual_room
    elif hab == 'Bedroom 2' and 'Llave B' in key_inv:            
        actual_room = room[2]
        return actual_room
    elif hab == 'Living room' and 'Llave C' in key_inv:         
        actual_room = room[3]
        return actual_room
    elif hab == 'Outside' and 'Llave D' in key_inv:
        actual_room = room[4]
        return actual_room
    else: 
        print(f"No puedes acceder a la {hab}")
        return actual_room



def examinar(actual_room, key_inv):

    if actual_room == 'Game room':

        print(gameroom_items)
        exam_input = input("¿Que quieres examinar?").capitalize()
        
        while exam_input not in gameroom_items:
            exam_input = input("Elija uno de los objetos disponibles.").capitalize()
        
        if exam_input == 'Sofa':
            print("Tras examinar detenidamente el sofá encuentras... que no tiene nada de especial.")
        elif exam_input == 'Piano':
            print("Tras examinar el piano encuentras una tecla que destaca sobre las demás")
            levantar = input("¿Levantas la tecla? (Si/No)").capitalize()
            if levantar == 'Si':
                print("Tras levantar la tecla no encuentras nada debajo, como es lógico, pero al mirar de frente ves una llave. *Llave A obtenida*")
                key_inv.add('Llave A')
                
            
    elif actual_room == 'Bedroom 1':

        print(bedroom1_items)

        exam_input = input("¿Que quieres examinar?").capitalize()

        while exam_input not in bedroom1_items:
            exam_input = input("Elija uno de los objetos disponibles.").capitalize()


        if exam_input == 'Bedside table':

            examine_cards = input("Encuentras una baraja de cartas. ¿Examinar? (Si/No)").capitalize()
            if examine_cards == 'Si':
                puzle_cartas()

        if exam_input == 'Queen bed':

            choice_bed = input('Encima del colchón ves una caja con un código. ¿Quieres introducir una palabra? (Si/No)').capitalize()
            if choice_bed == 'Si':
                queenbed_code = input('Introduce una palabra').capitalize()

                if queenbed_code == 'Caos':
                    print("Has encontrado otra llave. *Llave B obtenida*")
                    key_inv.add('Llave B')
                else:
                    print("No se abre...")
        
    elif actual_room == 'Bedroom 2':

        print(bedroom2_items)
        exam_input = input("¿Que quieres examinar?").capitalize()

        while exam_input not in bedroom2_items:
            exam_input = input("Elija uno de los objetos disponibles.").capitalize()

        if exam_input == 'Mirror':
            rompe_espejo = input("El mueble tiene un espejo. ¿Romper espejo?").capitalize()
            if rompe_espejo == 'Si':
                print("Enhorabuena!. Has obtenido: *7 años de mala suerte*")
            else:
                print("El espejo te mira con tristeza conforme te alejas ¿o tú le miras a él?")

        if exam_input == 'Double bed':
            print("Al examinar la cama doble encuentras el siguiente mensaje: ")
            print("En esta cama doble el César cifró la contraseña 'gpmlfyai'.")
            pass_cifr = input('Introduce el mensaje del César ').lower()
            if pass_cifr == 'ironhack':
                print("Correcto. El mismísimo César estaría orgulloso. *Llave C obtenida*")
                key_inv.add('Llave C')
            else:
                print("El mensaje es incorrecto.")

    elif actual_room == 'Living room':
        
        print(livingroom_items)
        exam_input = input("¿Que quieres examinar?").capitalize()

        while exam_input not in livingroom_items:
            exam_input = input("Elija uno de los objetos disponibles.").capitalize()
        
        if exam_input == 'Dining table':
            print("Encima de la mesa encuentras una tablet con un mensaje:")
            print("Para abrir la última puerta deberás de introducir un código. El código está oculto en un mensaje el cual deberás descifrar utilizando regex.")
            choice_dining = input("¿Que quieres hacer: leer el mensaje o intentar introducir el patrón? (Leer/Resolver)").capitalize()

            texto_pista = "ewf@adewq20wefewfewfewf'lkjashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfklj24ashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfkljashdfkljahsdfkljashdfkl"

            if choice_dining == 'Leer':
                print(f"El mensaje dice lo siguiente:\n{texto_pista}")
                choice_dining = input("¿Quieres tratar de resolverlo? (Resolver/No)").capitalize()

            if choice_dining == 'Resolver':
                user_regex = str(input("Introduce el patrón regex"))

                if user_regex == "r'\d+'":
                    result_regex = extraer_contraseña(r'\d+', texto_pista)
                    print(f"Tú resultado obtenido es {result_regex}")
                else:
                    print(f"Tú resultado obtenido es incorrecto")
            

        if exam_input == 'Keyboard':
            llave = ingresar_codigo_salida()
            if llave == 'Llave D':
                print("Correcto. Ya casi estás fuera! *Llave D obtenida*")
                key_inv.add(llave)    
            else:
                print("Código incorrecto.")            

    return key_inv



def juego():

    key_inv = set()
    actual_room = room[0]
    print("Te despiertas en una habitación extraña.")

    while not actual_room == room[4]:

        print(f"Estás en la {actual_room}")
        accion = input("¿Qué quieres hacer? (moverse/examinar): ").lower()
        if accion == "moverse":
            print("Moviendose...")
            actual_room = moverse(actual_room, key_inv)

        elif accion == "examinar":

            print("Al examinar encuentras:")
            
            key_inv = examinar(actual_room, key_inv)
        else:
            print("Acción no válida. Intenta nuevamente.")
