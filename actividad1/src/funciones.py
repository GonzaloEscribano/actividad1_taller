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
    }
}

def recorrer_columnas(rol=None):
    """
    Filtra y muestra las columnas según el rol indicado, aplicando
    criterios de ordenamiento y umbral de completitud.
    Si no se especifica un rol, muestra todas las columnas ordenadas
    por completitud de forma descendente.
    """
    if rol in roles:
        columnas_rol = roles[rol]["columnas"]
        criterio = roles[rol]["criterio"]
        forma = (roles[rol]["forma"] == "B")
        porcentaje_minimo = roles[rol].get("porcentaje_minimo")
        
        if porcentaje_minimo is not None:
            columnas_a_mostrar = list(filter(lambda col: columnas[col]["completitud"] >= porcentaje_minimo, columnas_rol))
        else:
            columnas_a_mostrar = columnas_rol
        
        if criterio == "nombre":
            columnas_ordenadas = sorted(columnas_a_mostrar, reverse=forma)
        elif criterio == "completitud":
            columnas_ordenadas = sorted(columnas_a_mostrar, key = lambda col: columnas[col]["completitud"], reverse=forma)
    else:
        columnas_ordenadas = sorted(columnas, key = lambda col: columnas[col]["completitud"], reverse=True)
    
    for col in columnas_ordenadas:
        info = columnas[col]
        print(f"{col}: tipo {info['tipo']}, completitud {info['completitud']}%")