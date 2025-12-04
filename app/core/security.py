import bcrypt
from datetime import datetime, timedelta
from typing import Optional
import  jwt

SECRET_KEY = "changeme123" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8") #transformar a senha  para bytes.
    salt = bcrypt.gensalt() # gerar um "salt" que é um valor aleatorio, para deixar cada hash unico mesmo que duas pessoas usem a mesma senha.
    hashed = bcrypt.hashpw(password_bytes, salt) # aqui ele vai juntar o salt + senha e aplica o algoritmo de hash lento do bcrypt e gera o hash final poe exemplo: "$2b$12$y2JtCag9cw1/De8R7wrLeOgPwQH3KjZJv0Y0Y4E8iZ2bUXTUiGvNe'"
    return hashed.decode("utf-8") # aqui tranforma o hash "2b$12$y2JtCag9cw1/De8R7wrLeOgPwQH3KjZJv0Y0Y4E8iZ2bUXTUiGvNe" para o texto normal 

def verify_password(plain_password: str, hashed_password: str) -> bool: # vai comparar a senha pura com a senha hash 
       return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )

def decode_acess_token(token : str) -> Optional[dict]:
     
      try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) # decodifica o Token 
            return decoded # se der certo devolve os dados que querem ser acessados 
      except jwt.ExpiredSignatureError: # se o Token estiver vencido ira retornar none 
            return None
      except jwt.InvalidTokenError: # se o Token for invalido retorna none 
            return None