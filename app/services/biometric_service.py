from typing import Optional
from app.schemas.biometric import(
    BiometricCreate,
    BiometricResponse,
    BiometricMatchRequest,
    BiometricMatchResponse
)

class BiometricService:
    
    @staticmethod
    def register_biometric(data: BiometricCreate) -> BiometricMatchResponse:
        
     
     fake_id = "bio_001" # simulando um ID 
    
     return BiometricResponse(
       id=fake_id,
       user_id=data.user_id,
       biometric_type=data.biometric_type,
       message="Biometria Registrada com sucesso"
    )

    @staticmethod 
    def match_biometric(data: BiometricMatchRequest) -> BiometricMatchResponse: # aqui ira realizar uma compração biometrica (mock)
       
       match_result = True
       match_score = 0.98

       return BiometricMatchResponse(
          user_id=data.user_id,
          biometric_type=data.biometric_type,
          match=match_result,
          score=match_score
       )
