from abc import ABC , abstractmethod

class PasswordGenerator(ABC):

    """
    Base class for generating passwords.
    """

    @abstractmethod
    def password_generator(self) -> str:
        
        """
        Every subclasses need to override this method to generate password.
        """
        pass



