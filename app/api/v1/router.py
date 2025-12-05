from fastapi import APIRouter
from app.schemas.biometric import (
    BiometricCreate,
    BiometricResponse,
    BiometricMatchRequest,
    BiometricMatchResponse
)

from app.services.biometric_service import BiometricService

router = APIRouter()
service = BiometricService()

@router.post("/biometric/register", response_model=BiometricResponse)
def register_biometric(payload: BiometricCreate):
    service.save_biometric_data(
        user_id=payload.user_id,
        biometric_type=payload.biometric_type,
        data=payload.data
    )

    return BiometricResponse(
        message="Biometric data stored",
        status="success"
    )


@router.post("/biometric/match", response_model=BiometricMatchResponse)
def match_biometric(payload: BiometricMatchRequest):
    result = service.match_biometric_data(
        user_id=payload.user_id,
        biometric_type=payload.biometric_type,
        data=payload.data
    )

    return BiometricMatchResponse(
        match=result["match"],
        confidence=result["confidence"]
    )
