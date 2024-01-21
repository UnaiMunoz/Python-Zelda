import random

# Función para usar una espada
def usar_espada(espada):
    if espada["usos_restantes"] > 0:
        print(f"La espada ha infligido {espada['danio_por_uso']} de daño.")
        espada["usos_restantes"] -= 1
        print(f"Usos restantes: {espada['usos_restantes']}")
    else:
        print("La espada está rota. No puedes usarla más.")

# Función para bloquear con un escudo
def bloquear_escudo(escudo):
    if escudo["usos_restantes"] > 0:
        print(f"El escudo ha bloqueado {escudo['danio_por_uso']} de daño.")
        escudo["usos_restantes"] -= 1
        print(f"Usos restantes: {escudo['usos_restantes']}")
    else:
        print("El escudo está demasiado dañado. No puedes bloquear más.")

# Crear instancias de las espadas y escudos
espada_madera = {"usos_totales": 5, "usos_restantes": 5, "danio_por_uso": 1}
escudo_madera = {"usos_totales": 5, "usos_restantes": 5, "danio_por_uso": 1}
escudo_generico = {"usos_totales": 9, "usos_restantes": 9, "danio_por_uso": 1}
espada_generica = {"usos_totales": 9, "usos_restantes": 9, "danio_por_uso": 1}

# Usar y bloquear algunas veces para demostrar su funcionamiento
for _ in range(6):
    usar_espada(espada_madera)

for _ in range(3):
    bloquear_escudo(escudo_madera)

for _ in range(3):
    bloquear_escudo(escudo_generico)

#Abrir cofres por zonas

cofres_abiertos = set()

def abrir_cofre(zona):
    global cofres_abiertos

    if zona not in ["hyrule", "Geruldo", "DeathMountain", "Neucalda"]:
        print("Zona no válida")
        return None

    if zona in cofres_abiertos:
        print("El cofre en esta zona ya está abierto.")
        return None

    if zona in ["hyrule", "Geruldo"]:
        opciones_espadas = ["espada_madera", "espada"]
        objeto_obtenido = random.choice(opciones_espadas)
    elif zona in ["DeathMountain", "Neucalda"]:
        opciones_escudos = ["escudo", "escudo_madera"]
        objeto_obtenido = random.choice(opciones_escudos)
    else:
        objeto_obtenido = None  # Manejar el caso de una zona no válida

    cofres_abiertos.add(zona)
    print(f"Has abierto el cofre en {zona}. ¡Obtuviste: {objeto_obtenido}!")
    return objeto_obtenido

def resetear_cofres():
    global cofres_abiertos
    cofres_abiertos = set()
    print("Todos los cofres han sido reseteados. ¡Puedes abrirlos de nuevo!")

def cheats():
    global sword_usos
    global lives_character

    cheat_input = input("Enter cheat command: ")

    if cheat_input.startswith("cheat rename player to "):
        new_name = cheat_input[len("cheat rename player to "):]
        if 3 <= len(new_name) <= 10 and all(c.isalnum() or c.isspace() for c in new_name):
            addText(f"Player's name changed to: {new_name}")
        else:
            addText("Invalid name. Must be between 3 and 10 characters, and can only contain letters, numbers, and spaces.")

    elif cheat_input == "cheat add vegetable":
        cursor.execute("UPDATE game_food SET quantity_remaining = quantity_remaining + 1 WHERE food_name = 'Vegetable';")
        conexion.commit()
        addText("Added a vegetable to food.")

    elif cheat_input == "cheat add fish":
        cursor.execute("UPDATE game_food SET quantity_remaining = quantity_remaining + 1 WHERE food_name = 'Fish';")
        conexion.commit()
        addText("Added a fish to food.")

    elif cheat_input == "cheat add meat":
        cursor.execute("UPDATE game_food SET quantity_remaining = quantity_remaining + 1 WHERE food_name = 'Meat';")
        conexion.commit()
        addText("Added meat to food.")

    elif cheat_input == "cheat cook salad":
        cursor.execute("UPDATE game_food SET quantity_remaining = quantity_remaining - 2 WHERE food_name = 'Vegetable' AND quantity_remaining >= 2;")
        if cursor.rowcount > 0:
            cursor.execute("UPDATE game_food SET quantity_remaining = quantity_remaining + 1 WHERE food_name = 'Salad';")
            addText("Cooked a salad.")
        else:
            addText("Not enough vegetables to cook a salad.")

    # Add similar blocks for other food-related cheats

    elif cheat_input == "cheat add wood sword":
        cursor.execute("UPDATE game_weapons SET quantity_remaining = quantity_remaining + 1 WHERE weapon_name = 'Wood Sword';")
        conexion.commit()
        addText("Added a wood sword.")

    # Add similar blocks for other weapon-related cheats
    elif cheat_input == "cheat open sanctuaries":
        cursor.execute()



        
    else:
        addText("Unknown cheat command.")

