from knowledge_base import PRECIOS, DISPONIBILIDAD
import json
import os


def consultar_precio(programa: str) -> str:
    programa = programa.lower()
    if programa in PRECIOS:
        return f"el precio de {programa} es de RD${PRECIOS[programa]}."
    return f"No se encontro precio para {programa}"

def verificar_disponibilidad(programa: str) -> str:
    programa = programa.lower()
    if programa in DISPONIBILIDAD:
        cupos = DISPONIBILIDAD[programa]
        if cupos > 0:
            return f"si, hay {cupos} disponibles para {programa}."
        return f"Lo sentimos no hay cupos disponibles para {programa} en este caso."
    return f"No encontro disponibilidad para {programa}"

def registrar_contacto(nombre: str, telefono: str) -> str:
    contacto = {
        "nombre": nombre,
        "telefono": telefono
    }

    archivo = "contactos.json"

    contactos = []
    if os.path.exists(archivo):
        try:
            with open(archivo, "r") as f:
                contactos = json.load(f)
        except json.JSONDecodeError:
            contactos = []

    for contactos_existente in contactos:
        if contactos_existente["telefono"] == telefono:
            return f"el contacto con el telefono {telefono} ya esta registrado"

    contactos.append(contacto)

    with open(archivo, "w") as f:
        json.dump(contactos, f, indent=2, ensure_ascii=False)

    return f"Listo {nombre}, registramos tu contacto"

