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
- `rol=None` en `recorrer_columnas`: si no se indica rol, se informan todas las columnas por completitud descendente, que es lo que pide la consigna.
- `criterio="completitud"`, `forma=True` (descendente) y `porcentaje_minimo=None` (sin filtro) en `organizar_lista`. Son los mismos valores que la consigna define para el caso sin rol, por lo que el informe general se obtiene llamando a la función solo con la lista de columnas.
- En `buscar_columnas_rol`, uso `.get()` con valor por defecto para `criterio`, `forma` y `porcentaje_minimo`. Así, un rol que no los defina no rompe el programa con un `KeyError`, sino que usa los valores por defecto.

6) Si agregás una nueva columna al dataset, ¿en qué partes del código impacta? ¿Y si solo se quiere que un rol existente incluya esa nueva columna?
Si se agrega una columna, solo impacta en el diccionario columnas. Si se desea que un rol la vea, únicamente se agrega su nombre a la lista "columnas" dentro de dicho rol en roles. La función no se modifica en ningún caso.

7) ¿Qué pasaría si un rol tuviera un criterio de orden distinto a "nombre" o "completitud" (por ejemplo, "promedio")? ¿Cómo lo detectarías y qué harías para que el programa no falle?
Pasaba que `organizar_lista` daba `UnboundLocalError`: como el criterio no entraba en ningún `if`/`elif`, la variable `columnas_ordenadas` nunca se creaba y el `return` fallaba. Lo detecté probando con un rol inventado con criterio "promedio". Lo resolví agregando un `else` que avisa que el criterio no es válido y ordena por completitud. Elegí avisar y continuar, en lugar de lanzar un `ValueError`, porque el enunciado pide que el programa no falle y porque el usuario igual se entera del problema por el mensaje. La desventaja es que un error de configuración no corta la ejecución.

8) ¿Qué cambiarías si por defecto se pide el informe debiera salir según uno de los roles?
Cambiaría la firma a `def recorrer_columnas(rol="docente")`, o mejor, definiría una constante `ROL_POR_DEFECTO = "docente"` y usaría `rol=ROL_POR_DEFECTO`. Con esto, `recorrer_columnas()` ya no muestra todas las columnas, sino las de ese rol. El informe general sigue disponible pasando `None` explícitamente (`recorrer_columnas(None)`), que cae en el `else`. La lógica interna no cambia.