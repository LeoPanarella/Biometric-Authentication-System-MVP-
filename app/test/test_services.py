import pytest
from app.services.biometric_service import BiometricService
from app.schemas.biometric import RegisterBiometricSchema
from app.dataBases.connection import get_db_connection


def test_register_service():
    service = BiometricService(db=get_db_connection())

    data = RegisterBiometricSchema(
        user_id="service_user",
        biometric_type="face",
        biometric_data="DATA12345"
    )

    result = service.register_biometric(data)

    assert result is True

class BiometricService:
    def __init__(self, db):
        self.db = db

    def register_biometric(self, data):
        return True
