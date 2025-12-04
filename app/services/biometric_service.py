from typing import Optional
from app.Schemas.biometric import(
    BiometricCreate,
    BiometricResponse,
    BiometricMatchRequest,
    BiometricMatchResponse
)

class BiometricService:
    
    @staticmethod
    def register_biometric(data: BiometricCreate) -> BiometricMatchResponse:
        
     
     fake_id = "bio_001"
    
     return BiometricResponse(
       id=fake_id,
       user_id=data.user_id,
       biometric_type=data.biometric_type
       message="Biometria Registrada com sucesso"
    )
