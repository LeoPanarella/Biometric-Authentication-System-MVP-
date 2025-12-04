from pydantic import BaseModel
from typing import Optional

class BiometricsBase(BaseModel): #modelo base usado tanto para cadastro quanto no match
    user_id: int 
    biometric_type: str 
    data: str 

class BiometricCreate(BiometricsBase): #modelo usado quando o cliente manda os dados biometricos
    pass 

class BiometricResponse(BaseModel): # resposta de confirmação 
    message: str
    status : str = "success"

class biometricMathRequest(BaseModel): #Para a quando o usuario envia os dados para comparação 
    user_id : int
    biometric_type: str
    data: str 

class BiometricMatchResponse(BaseModel): #Resultado da comparação se True/False   e um percentual de confiança
    match : bool
    confidence : float

