class InvalidImage(Exception):
    """Raised when an invalid image is encountered based on array dimension
    Attributes:
        message: (str) Exception message
    """

    def __init__(self) -> None:
        self.message = "Invalid Image!!"

class NoNameProvided(Exception):
    """Raised when no name is supplied for face recognition
    Attributes:
        message: (str) Exception message
    """

    def __init__(self) -> None:
        self.message = "Please provide a name for registering face!!"

class NoFaceDetected(Exception):
    """Raised when no face is detected in an image

    Attributes:
        message: (str) Exception message
    """

    def __init__(self) -> None:
        self.message = "No face found in image!!"

class FaceMissing(Exception):
    """Raised when face is not found in an image
    Attributes:
        message: (str) Exception message
    """

    def __init__(self) -> None:
        self.message = "Face not found!!"