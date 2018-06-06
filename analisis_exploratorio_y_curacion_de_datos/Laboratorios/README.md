# Laboratorio: Limpiar un set de datos con pandas

<p><em>Consigna:</em></p>
<p>Limpiar un set de datos con pandas</p>
<ul>
<li>Un set de datos que tengan permisos para compartir con nosotros</li>
<li>M&aacute;s de 100000 registros</li>
<li>M&aacute;s de 20 columnas</li>
<li>Con datos con cadenas, n&uacute;meros, fechas, y categor&iacute;as</li>
</ul>
<p>

<ol>
    <li>Importando los datos</li>
        <ol>
            <li> Verificar si no hay problemas en la importación Habilitar chequeos al importar </li>
            <li> Asegurar de tener ids/claves únicas Chequear que no hay datos duplicados </li>
            <li> Despersonalizar datos y guardarlos en un nuevo archivo</li>
            <li> Nunca modificar los datos crudos u originales</li>
        </ol>
    <li>Pasos necesarios</li>
        <ol>
            <li>Etiquetas de variables/columnas: no usar caracteres especiales Verificar que no haya problemas de codificación/encoding </li>
            <li> Tratar valores faltantes Quitar o imputar</li>
            <li> Codificar variables: las variables categóricas deben ser etiquetadas como variables numéricas, no como cadenas</li>
            <li> No cambiar los nombres de las variables de la fuente de origen</li>
            <li> Verificar la consistencia de las variables
Aplicar reglas de integridad</li>
            <li> Identificar y documentar valores atípicos/outliers
Calcular estadísticos</li>
            <li> Evaluar cómo comprimir los datos para su almacenamiento más eficiente</li>
            <li> Guardar el set de datos con un nombre informativo.</li>
        </ol>
    <li> Pasos deseables</li>
    <ol>
        <li> Ordenar variables/columnas si es posible – primero ID, luego en el mismo orden que la fuente</li>
        <li> Quitar variables/columnas que no tienen información a analizar</li>
        <li> Renombrar variables de grillas</li>
        <li> Categorizar resultados en “Otros”
Si tiene un campo de texto libre asociado, codificar en nuevos valores de la variable
categórica asociada. Revisar fuzzyness.</li>
        <li> Agregar metadata a los datos: cuando y como fueron obtenidos, limpieza realizada,
asunciones, etc
Vincular con etiquetas del código fuente y los datos. Al menos incluir un README.</li>
    <ol>
</ol>
</p>




### Comandos para descargar la imagen de Docker necesaria para correr la limpieza y curacion del dataset.

La imagen de docker se puede descargar con el siguiente comando:

```docker pull fdiazcobos/diplodatos ```

Si se prefiere el imagen se puede construir con el siguiente comando.

```docker build -t diplodatos -f Dockerfile . ```

### Comandos para correr la imagen de Docker

```docker run -v <Dir_datos>:/usr/local/diplodatos/datos fdiazcobos/diplodatos ```

### Qué hace la imagen.

El script corre sobre una imagen base que posee python3 y las librerias mas comunes para trabajar con datos, estás se pueden obvservar en
el archivo requirements.txt

Básicamente se buscará los datos en el directorio montado como volumen, se descomprimirán y se realizarán los pasos de la consigna.
Una vez que se termine la limpieza en el directorio montado se generara un nuevo archivo comprimido con los datos limpios.
Este proceso es reproducible y sirve para nuevos datasets con más o menos datos, siempre y cuando conservern la misma estructura.

### NOTAS:

Los datos fueron previamente despersonalizados, ya que contienen datos reales sobre empresas. 
Asi que para este ejercicio, se considerará como datos crudos u originales el dataset con los datos despersonalizados, ese es el único cambio
que tienen los datos originales.