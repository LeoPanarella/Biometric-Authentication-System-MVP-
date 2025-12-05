class BiometricNotFoundException(Exception):
    def __init__(self, message="Biometric data not found"):
        self.message = message
        super().__init__(self.message)


class InvalidBiometricTypeException(Exception):
    def __init__(self, message="Invalid biometric type"):
        self.message = message
        super().__init__(self.message)


class BiometricAlreadyExistsException(Exception):
    def __init__(self, message="Biometric data already exists for this user"):
        self.message = message
        super().__init__(self.message)
