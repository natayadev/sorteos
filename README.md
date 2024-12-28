# Sorteador

🐻‍❄️ Un generador de sorteos CLI de formularios de Google (o cualquier .csv) hecho en Polars, con la opción de utilizar una palabra clave o "secreta" para que los participantes tengan doble chance de salir como ganadores.

## Requisitos

- Python 3.x
- Un archivo .csv

---

## Instalación

1. Clona el repositorio:

  ```bash
  git clone https://github.com/natayadev/sorteador.git
  cd sorteador
  ```

2. Crea un entorno virtual:

  ```bash
  python3 -m venv venv
  source venv/bin/activate  # En Linux/macOS
  venv\Scripts\activate     # En Windows
  ```

3. Instala las dependencias:
 
  ```bash
  pip install -r requirements.txt
  ```

## Instrucciones de uso:

  ```bash
  python sorteo.py --file [archivo.csv] --winners [3] --winner_col [0] --secret_word_col [1] --secret_word ["chipa"]
  ```

**Parámetros o flags**

--file: Nombre del archivo CSV (debe estar en la carpeta /data/).

--winners: Cantidad de ganadores a seleccionar.

--winner_col: Índice de la columna con los nombres de los participantes.

*--secret_word_col: Índice de la columna con las palabras secretas (opcional).*

*--secret_word: Palabra secreta a la que se asigna doble chance de ganar (opcional).*
