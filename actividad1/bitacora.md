1) ¿Qué ventajas tienen las estructuras elegidas para almacenar los datos de las columnas y roles con respecto a otras de las vistas en la teoría?
Para esta actividad, usé diccionarios ya que permiten acceso mediante claves únicas (nombres de columna y nombres de rol), facilitando búsquedas directas sin tener que iterar secuencialmente como ocurriría con listas simples o tuplas.

2) ¿Qué valores elegiste para los roles y los porcentajes de completitud y por qué?
En cuanto a completitud, definí valores entre 35% y 100% para poder comprobar los filtros por umbral y el ordenamiento.
En cuanto a los roles, distribuí las columnas temáticamente, probando combinaciones de criterios ("nombre" y "completitud"), sentidos ("A" y "B") y presencia o ausencia de porcentaje_minimo.

3) ¿Cómo garantizaste que el programa pueda ser validado con diferentes roles, criterios de ordenamiento y umbrales?
Lo garantizo al haber hecho la función recorrer_columnas de forma genérica para que consuma los parámetros dinámicamente desde el diccionario roles, y testeando individualmente cada rol y el caso sin rol en celdas separadas del notebook.

4) ¿Por qué conviene separar la configuración de los roles (ROLES) de la lógica que genera el informe?
Principio de separación de responsabilidades y desacoplamiento: permite modificar, agregar o quitar roles y reglas sin necesidad de editar la función que procesa los datos.

5) ¿Qué parámetros se pueden definir con valores por defecto?
El parámetro rol en la firma de la función, permitiendo que si no se envía ningún argumento, se aplique automáticamente el reporte general por completitud descendente.

6) Si agregás una nueva columna al dataset, ¿en qué partes del código impacta? ¿Y si solo se quiere que un rol existente incluya esa nueva columna?
Si se agrega una columna, solo impacta en el diccionario columnas. Si se desea que un rol la vea, únicamente se agrega su nombre a la lista "columnas" dentro de dicho rol en roles. La función no se modifica en ningún caso.

7) ¿Qué pasaría si un rol tuviera un criterio de orden distinto a los especificados "nombre" o "completitud" (por ejemplo, "promedio")? ¿Cómo lo detectarías y qué harías para que el programa no falle?
Se puede validar con un condicional (if criterio not in ["nombre", "completitud"]:) y aplicar un criterio por defecto como ordenar por completitud descendente o lanzar un mensaje advirtiendo que el criterio no es soportado.

8) ¿Qué cambiarías si por defecto se pide el informe debiera salir según uno de los roles?
En la firma de la función se cambiaría el valor por defecto del parámetro: en lugar de def recorrer_columnas(rol=None):, se pondría def recorrer_columnas(rol="docente"): o el rol que se elija por defecto.