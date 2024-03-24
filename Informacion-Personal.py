# Dicionario
informacion_personal = {
    "nombre": "Jonathan Tandazo",
    "edad": 25,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y modificar valores
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor
informacion_personal["telefono"] = "0961330464"

# Verificar existencia de claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0961330464"

# Eliminar una clave
informacion_personal.pop("ciudad")

print(informacion_personal)
