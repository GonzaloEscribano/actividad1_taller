columnas = {
    "PONDERA": {"tipo": "int", "completitud": 90},
    "ESTADO": {"tipo": "int", "completitud": 80},
    "CAT_OCUP": {"tipo": "int", "completitud": 100},
    "EDAD": {"tipo": "int", "completitud": 75},
    "REGION": {"tipo": "int", "completitud": 60},
    "AGLOMERADO": {"tipo": "int", "completitud": 40},
    "MAS_500": {"tipo": "str", "completitud": 70},
    "ANO4": {"tipo": "int", "completitud": 100},
    "TRIMESTRE": {"tipo": "int", "completitud": 35},
    "ITF": {"tipo": "int", "completitud": 85},
    "GDECCFR": {"tipo": "int", "completitud": 90}
}


roles = {
    "docente": {
        "columnas": ["EDAD", "REGION", "ANO4", "TRIMESTRE"],
        "criterio": "nombre",
        "forma": "B"
    },
    "investigador": {
        "columnas": ["PONDERA", "ESTADO", "CAT_OCUP", "EDAD", "REGION", "AGLOMERADO", "MAS_500"],
        "criterio": "completitud",
        "forma": "B",
        "porcentaje_minimo": 70
    },
    "analista": {
        "columnas": ["PONDERA", "ESTADO", "CAT_OCUP", "ITF", "GDECCFR"],
        "criterio": "completitud",
        "forma": "A",
        "porcentaje_minimo": 60
    },
    "auditor" : {
        "columnas" : ["PONDERA", "ESTADO", "CAT_OCUP", "EDAD", "REGION", "AGLOMERADO", "MAS_500", "ANO4", "TRIMESTRE", "ITF", "GDECCFR"],
        "criterio" : "nombre",
        "forma" : "B"
    }
}


def buscar_columnas_rol(rol):
    """
    Obtiene la configuración de un rol a partir del diccionario de roles.

    Parámetros:
        rol: nombre del rol a consultar (por ejemplo "docente").

    Devuelve una tupla con:
        columnas_rol: lista de columnas de interés del rol.
        criterio: criterio de ordenamiento ("nombre" o "completitud").
        forma: True si el orden es descendente (B), False si es ascendente (A).
        porcentaje_minimo: umbral de completitud, o None si el rol no lo define.
    """
    columnas_rol = roles[rol]["columnas"]
    criterio = roles[rol].get("criterio", "completitud")
    forma = (roles[rol].get("forma", "B") == "B")
    porcentaje_minimo = roles[rol].get("porcentaje_minimo")
    
    return columnas_rol, criterio, forma, porcentaje_minimo


def organizar_lista(columnas_rol, criterio="completitud", forma=True, porcentaje_minimo=None):
    """
    Filtra las columnas por porcentaje mínimo de completitud (si corresponde) y luego las ordena según el criterio y la forma indicados.

    Parámetros:
        columnas_rol: lista de nombres de columnas a organizar.
        criterio: "nombre" para orden alfabético o "completitud" para ordenar por porcentaje de completitud.
        forma: True para orden descendente, False para ascendente.
        porcentaje_minimo: solo se conservan las columnas con completitud mayor o igual a este valor. Si es None, no se filtra.

    Devuelve una lista con los nombres de columnas filtrados y ordenados.
    """
    inexistentes = list(filter(lambda col: col not in columnas, columnas_rol))
    
    if inexistentes:
        print(f"Aviso: columnas inexistentes ignoradas: {inexistentes}")
    columnas_rol = list(filter(lambda col: col in columnas, columnas_rol))
    
    if porcentaje_minimo is not None:
        columnas_a_mostrar = list(filter(lambda col: columnas[col]["completitud"] >= porcentaje_minimo, columnas_rol))
    else:
        columnas_a_mostrar = columnas_rol
            
    if criterio == "nombre":
        columnas_ordenadas = sorted(columnas_a_mostrar, reverse=forma)
    elif criterio == "completitud":
        columnas_ordenadas = sorted(columnas_a_mostrar, key = lambda col: columnas[col]["completitud"], reverse=forma)
    else:
        print(f"El criterio {criterio} no es válido. Se ordenará por completitud.")
        columnas_ordenadas = sorted(columnas_a_mostrar, key = lambda col: columnas[col]["completitud"], reverse=forma)
    
    return columnas_ordenadas


def formatear_columna(col):
    """
    Arma la línea de texto con la información de una columna.

    Parámetros:
        col: nombre de la columna.

    Devuelve un string con el nombre, el tipo y la completitud.
    """
    info = columnas[col]
    return f"{col}: tipo {info['tipo']}, completitud {info['completitud']}%"


def imprimir(columnas_ordenadas):
    """
    Muestra por pantalla la información de cada columna, una por línea, con su nombre, tipo de dato y porcentaje de completitud.

    Parámetros:
        columnas_ordenadas: lista de nombres de columnas, en el orden en que se quieren mostrar.
    """
    lineas = map(formatear_columna, columnas_ordenadas)
    print("\n".join(lineas))


def recorrer_columnas(rol=None):
    """
    Filtra y muestra las columnas según el rol indicado, aplicando
    criterios de ordenamiento y umbral de completitud.
    Si no se especifica un rol, muestra todas las columnas ordenadas
    por completitud de forma descendente.
    """
    if rol in roles:
        columnas_rol, criterio, forma, porcentaje_minimo = buscar_columnas_rol(rol)
        columnas_ordenadas = organizar_lista(columnas_rol, criterio, forma, porcentaje_minimo)
    else:
        columnas_ordenadas = organizar_lista(list(columnas))
    
    imprimir(columnas_ordenadas)