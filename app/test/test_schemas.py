import pytest
from app.schemas.biometric import RegisterBiometricSchema, MatchBiometricSchema


def test_register_schema_valid():
    obj = RegisterBiometricSchema(
        user_id="user1",
        biometric_type="face",
        biometric_data="XYZ123"
    )
    assert obj.user_id == "user1"


def test_register_schema_invalid():
    with pytest.raises(Exception):
        RegisterBiometricSchema(
            user_id="",
            biometric_type="fingerprint",
            biometric_data="12345"
        )


def test_match_schema_valid():
    obj = MatchBiometricSchema(
        user_id="user1",
        biometric_data="AAAA1111"
    )
    assert obj.user_id == "user1"
