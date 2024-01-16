import random

class Espada:
    def espada(self, usos_totales=5, danio_por_uso=1):
        self.usos_totales = usos_totales
        self.usos_restantes = usos_totales
        self.danio_por_uso = danio_por_uso

    def usar(self):
        if self.usos_restantes > 0:
            print(f"La espada ha infligido {self.danio_por_uso} de daño.")
            self.usos_restantes -= 1
            print(f"Usos restantes: {self.usos_restantes}")
        else:
            print("La espada está rota. No puedes usarla más.")

class Escudo:
    def escudoo(self, usos_totales=5, danio_por_uso=1):
        self.usos_totales = usos_totales
        self.usos_restantes = usos_totales
        self.danio_por_uso = danio_por_uso

    def bloquear(self):
        if self.usos_restantes > 0:
            print(f"El escudo ha bloqueado {self.danio_por_uso} de daño.")
            self.usos_restantes -= 1
            print(f"Usos restantes: {self.usos_restantes}")
        else:
            print("El escudo está demasiado dañado. No puedes bloquear más.")

# Crear instancias de las espadas y escudos
espada_madera = Espada(usos_totales=5, danio_por_uso=1)
escudo_madera = Escudo(usos_totales=5, danio_por_uso=1)
escudo_generico = Escudo(usos_totales=9, danio_por_uso=1)
espada_generica = Espada(usos_totales=9, danio_por_uso=1)

# Usar y bloquear algunas veces para demostrar su funcionamiento
for _ in range(3):
    espada_madera.usar()

for _ in range(3):
    escudo_madera.bloquear()

for _ in range(3):
    escudo_generico.bloquear()



import random

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
