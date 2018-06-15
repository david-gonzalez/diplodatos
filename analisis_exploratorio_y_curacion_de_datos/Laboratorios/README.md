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


## Acerca del proceso realizado:

Se trabajó primero en resolver el problema en un notebook python de jupyter. Luego se confeccionó una imagen de docker conteniendo las librerías necesarias para poder ejecutarlo en cualquier lugar y evitar asi problemas de dependencias.


Para poder visualizar los resultados, se requerirá que se baje la imagen de docker que contiene el notebook, que se ejecute el comando para levantar jupyter allí contenido y luego ejecutar el notebook para poder ver los resultados. 

A continuación se especifican cada uno de esos pasos.


### Descargar la imagen de Docker necesaria para correr la limpieza y curacion del dataset:

La imagen de docker preparada se descarga ejecutando el siguiente comando:

<b>```docker pull fdiazcobos/diplodatos ```</b>
<br/><br/>

### Correr la imagen de Docker y levantar Jupyter:

La imagen de docker se ejecuta mediante el siguiente comando en el presente directorio:

<b>```docker run -p 8888:8888 -v $(pwd)/datos:/home/jovyan/work/datos fdiazcobos/diplodatos ```</b>
<br/>


Una vez ejecutado, al final de la consola se presentará un link del estilo:  

<b>```http://fa1696da495a:8888/?token=d181a94eb2e06b7f33cbc85f1159cb084de032898f8b6e7d&token=d181a94eb2e06b7f33cbc85f1159cb084de032898f8b6e7d```</b>


Tengase en cuenta que el link anterior es una referencia y que tanto el Container ID (fa1696da495a) como el token (d181a94eb2e06b7f33cbc85f1159cb084de032898f8b6e7d) pueden ser distintos a los ejecutados en su equipo.  

Copie el link que aparece en su consola y pegueló en un navegados, reemplazando el Container ID que aparece en su maquina en lugar de <b>fa1696da495a</b>   por la palabra <b>localhost</b>), quedando de forma similar a:

<b>```http://localhost:8888/?token=d181a94eb2e06b7f33cbc85f1159cb084de032898f8b6e7d&token=d181a94eb2e06b7f33cbc85f1159cb084de032898f8b6e7d```</b>

Y ejecute el llamado a la página. Una vez hecho esto se presentará la consola de Jupyter conteniendo el notebook del presente laboratorio.

<br/><br/>
### Qué hace la imagen:

El script corre sobre una imagen base que levanta jupyter y contiene las librerias necesarias para correr nuestra notebook.
El volumen es necesario montarlo ya que al final genera un nuevo archivo .zip con los datos ya limpios.

Básicamente se buscará los datos en el directorio montado como volumen, se descomprimirán y se realizarán los pasos de la consigna.
Una vez que se termine la limpieza en el directorio montado se generara un nuevo archivo comprimido con los datos limpios.
Este proceso es reproducible y sirve para nuevos datasets con más o menos datos, siempre y cuando conservern la misma estructura.
<br/><br/>
### Construir la imagen:

Para ver como está construida la imagen, y si se desea poder regenerarla, se puede hacer a partir de los siguientes pasos, partiendo de la carpeta actual:

<b>``` $ cd  ./jupyter-image ```</b>

<b>```$ docker build -t diplodatos -f Dockerfile . ```</b>

<br/><br/>

### Notas finales:

Los datos fueron previamente despersonalizados, ya que contienen datos reales sobre empresas. 
Asi que para este ejercicio, se considerará como datos crudos u originales el dataset con los datos despersonalizados, ese es el único cambio
que tienen los datos originales.ginales.