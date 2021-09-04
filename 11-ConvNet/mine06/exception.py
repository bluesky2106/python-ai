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

class InvalidFaceDetector(Exception):
    """Raised when an invalid face detector is encountered
    Attributes:
        message: (str) Exception message
    """

    def __init__(self) -> None:
        self.message = "Invalid Face Detector!!"

class DatabaseFileNotFound(Exception):
    """Raised when the persistent storage databse file
    doesn't exists at the given location.
    Attributes:
        message: (str) Exception message
    """

    def __init__(self) -> None:
        self.message = "Database file not found!!"

class InvalidCacheInitializationData(Exception):
    """Raised when a data structure other than
    a list is supplied for cache initialization.
    Attributes:
        message: (str) Exception message
    """

    def __init__(self) -> None:
        self.message = "Invalid data structure. Please suppply a list!!"

class NotADictionary(Exception):
    """Raised when input is not a dictionary
    Attributes:
        message: (str) Exception message
    """

    def __init__(self) -> None:
        self.message = "Invalid data structure. Please suppply a dict!!"