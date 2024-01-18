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

def abrir_cofre(zona):
    if zona in ["HYRULE", "Geruldo"]:
        opciones_espadas = ["espada_madera", "espada_generica"]
        objeto_obtenido = random.choice(opciones_espadas)
    elif zona in ["DeathMountain", "Neucalda"]:
        opciones_escudos = ["escudo_generico", "escudo_madera"]
        objeto_obtenido = random.choice(opciones_escudos)
    else:
        objeto_obtenido = None  # Manejar el caso de una zona no válida

    return objeto_obtenido

"""
zona_hyrule = "HYRULE"
zona_death_mountain = "DeathMountain"

objeto_en_hyrule = abrir_cofre(zona_hyrule)
objeto_en_death_mountain = abrir_cofre(zona_death_mountain)

print(f"Objeto en Hyrule: {objeto_en_hyrule}")
print(f"Objeto en Death Mountain: {objeto_en_death_mountain}")

"""
