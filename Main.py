from ProyectoYugioh import Juego


contenido_cartas = """\
# Cartas de Monstruo
Monstruo|Dragón Rojo|Un dragón imponente que destruye todo a su paso.|3000|2500|D|FUEGO
Monstruo|Guerrero Espadachín|Un maestro en el uso de la espada.|1800|1500|G|TIERRA
Monstruo|Zombi Despierto|Un no-muerto que ataca sin piedad.|1500|1200|Z|OSCURIDAD
Monstruo|Bestia Salvaje|Una criatura feroz con garras afiladas.|2000|1000|B|TIERRA
Monstruo|Demonio Siniestro|Una entidad oscura que siembra terror.|2500|2000|O|OSCURIDAD
Monstruo|Mago Arcano|Un hechicero experto en conjuros poderosos.|1700|2200|L|LUZ
Monstruo|Fénix|Un ave inmortal que resucita de sus cenizas.|2400|1800|D|FUEGO
Monstruo|Caballero de Acero|Un guerrero blindado que nunca retrocede.|2300|2000|G|TIERRA
Monstruo|Luchador Zombi|Un luchador muerto viviente.|1700|1600|Z|OSCURIDAD
Monstruo|Ogro Gigante|Un monstruo de gran tamaño y fuerza.|2800|2400|B|TIERRA
Monstruo|Halcón de Fuego|Un halcón que lanza fuego a sus enemigos.|1500|1200|B|FUEGO
Monstruo|Golem de Piedra|Un golem que protege el reino con su cuerpo de roca.|2500|3000|B|TIERRA
Monstruo|Dragón de Hielo|Un dragón con el poder del hielo.|2200|2000|D|AGUA
Monstruo|Vampiro Nocturno|Un monstruo vampiro que caza durante la noche.|2000|1800|Z|OSCURIDAD
Monstruo|León de Fuego|Un león feroz con garras de fuego.|1800|1600|B|FUEGO
Monstruo|Caballero de la Luz|Un guerrero que combate con fuerza y honor.|1900|1600|G|LUZ
Monstruo|Lince de Viento|Una criatura ágil de viento que puede esquivar ataques.|1500|1200|B|VIENTO
Monstruo|Basilisco|Una criatura mítica cuyo vistazo petrifica.|2200|2100|Z|TIERRA
Monstruo|Manticora|Un monstruo con el cuerpo de un león y la cola de un escorpión.|2300|2000|B|VIENTO
Monstruo|Dragón de Acero|Un dragón de acero imparable en combate.|2600|2300|D|TIERRA
Monstruo|Dragón sin escamas|Un dragón imponente que destruye todo a su paso.|2200|2600|D|FUEGO
Monstruo|Guerrero de esgrima|Un maestro en el uso de la esgrima.|1900|1900|G|TIERRA

# Cartas Mágicas
Magica|Espada de Arturo|Aumenta en 200 el ataque de Guerreros.|200|Guerrero
Magica|Escudo de Chamelote|Aumenta en 200 la defensa de Guerreros.|-200|Guerrero
Magica|Piedra del Guardián|Aumenta en 300 la defensa de Bestias.|-300|Bestia
Magica|Oscuridad Total|Aumenta en 400 el ataque de Demonios.|400|Demonio
# Cartas de Trampa
Trampa|Tornado de Polvo|Detiene el ataque de monstruos con atributo VIENTO.|VIENTO
Trampa|Escudo Espectral|Impide el ataque de monstruos con atributo OSCURIDAD.|OSCURIDAD
Trampa|Prisión de Luz|Bloquea el ataque de monstruos con atributo LUZ.|LUZ
Trampa|Barrera de Fuego|Anula el ataque de monstruos con atributo FUEGO.|FUEGO
Trampa|Colapso Terrestre|Detiene el ataque de monstruos con atributo TIERRA.|TIERRA

"""
nombre_archivo = "cartas.txt"
with open(nombre_archivo, "w") as archivo:
    archivo.write(contenido_cartas)

juego = Juego()
juego.cargar_cartas(nombre_archivo)
juego.jugar()