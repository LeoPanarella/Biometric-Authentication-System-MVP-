import sqlite3
from sqlite3 import Connection


DATABASE_PATH = "app/database/biometric.db"


def get_db_connection() -> Connection: # cria e retorna uma conexão com o banco de dados sqlite e cria o arquivo biometric.db automaticamente

    conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)  
    conn.row_factory = sqlite3.Row  # Retorna resultados como dicionários
  
    return conn
