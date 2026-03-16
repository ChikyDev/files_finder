# Buscador de Archivos por Extensión en Python

Script simple en Python que permite buscar archivos con una extensión específica dentro de un directorio.

## Descripción

Este proyecto permite analizar una carpeta y detectar archivos que tengan una extensión determinada, por ejemplo:

- `.exe`
- `.dll`
- `.bat`
- `.ps1`

El script recorre los archivos del directorio indicado y muestra aquellos que coinciden con la extensión buscada.

Este tipo de herramienta puede ser útil para:

- Análisis de sistemas
- Búsqueda de archivos sospechosos
- Automatización de tareas de revisión
- Aprendizaje de Python aplicado a seguridad

## Características

- Búsqueda de archivos por extensión
- Conteo total de archivos encontrados
- Salida en terminal con colores
- Script sencillo y fácil de entender

## Tecnologías utilizadas

- Python
- Librería `os`

## Uso

1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/files_finder.git
```

2. Entrar en el directorio del proyecto

```bash
cd files_finder
```

3. Ejecutar el script

```bash
python script.py
```

## Ejemplo de uso

El programa pedirá dos datos:

```
En que termina el/los archivos que buscas (.exe, .bat, .dll, etc...):
Introduce la ruta donde quieres examinar los archivos:
```

Ejemplo:

```
.exe
/home/user/Downloads
```

Salida esperada:

```
Archivo encontrado: malware.exe
Archivo encontrado: programa.exe
Se han encontrado 2 archivos totales
```

## Cómo funciona

El script utiliza la función:

```python
os.listdir()
```

para obtener los archivos de una carpeta, y luego verifica si cada archivo termina con la extensión especificada usando:

```python
files.endswith(extension)
```

## Aviso

Este proyecto está creado con fines educativos y de aprendizaje de Python y análisis de sistemas.

## Autor

Proyecto personal enfocado en aprendizaje de Python aplicado a ciberseguridad.
