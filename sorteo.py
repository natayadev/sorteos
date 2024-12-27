import polars as pl
import argparse
import random
import time
import os

def show_message(message):
    print(message)
    time.sleep(1)

def process_csv(file, num_winners, winner_col_idx, secret_word_col_idx, secret_word):
    show_message("⏳ Cargando datos del sorteo...")
    file_path = os.path.join("data", file)

    df = pl.read_csv(file_path)
    columns = df.columns
    show_message(f"📋 Columnas encontradas: {columns}")

    if winner_col_idx >= len(columns):
        raise ValueError("El índice de la columna de ganadores debe ser válido.")
    if secret_word_col_idx >= len(columns):
        raise ValueError("El índice de la columna de la palabra secreta debe ser válido.")

    winner_col_name = columns[winner_col_idx]
    secret_word_col_name = columns[secret_word_col_idx]

    show_message("⚙️ Calculando probabilidades...")

    column_mapping = {
        winner_col_name: "fullname",
        secret_word_col_name: "word"
    }
    df = df.rename(column_mapping)

    df = df.with_columns(df["word"].str.to_lowercase())

    # BONUS: 1 punto por participante y 2 si se encuentra la palabra secreta
    df = df.with_columns(
        pl.when(df["word"].str.contains(secret_word.lower())).then(2).otherwise(1).alias("points")
    )

    show_message("🔍 Buscando palabras secretas...")

    participants = df["fullname"].to_list()
    points = df["points"].to_list()
    
    # BONUS: lista donde los nombres aparecen varias veces según los puntos acumulados
    weighted_list = []
    for name, point in zip(participants, points):
        weighted_list.extend([name] * point)
    
    winners = random.sample(weighted_list, k=num_winners)
    show_message("🏆 Ganador en 3, 2, 1...")
    for winner in winners:
        show_message(f" • {winner}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sorteo de participantes")
    parser.add_argument("--file", type=str, help="Nombre del archivo CSV a procesar", required=True)
    parser.add_argument("--winners", type=int, help="Número de ganadores", required=True)
    parser.add_argument("--winner_col", type=int, help="Índice de la columna de ganadores", required=True)
    parser.add_argument("--secret_word_col", type=int, help="Índice de la columna de la palabra secreta", required=True)
    parser.add_argument("--secret_word", type=str, help="Palabra secreta para obtener doble chance", required=True)

    args = parser.parse_args()

    process_csv(args.file, args.winners, args.winner_col, args.secret_word_col, args.secret_word)
