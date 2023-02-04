from models.person import Person


class Student(Person):
    """Student class for the dbbook database."""

    def __init__(self, id: int, name: str, dept_name: str, total_creds: int) -> None:
        """Initialize a Student object."""
        self._total_creds = total_creds
        super().__init__(id, name, dept_name)

    @property
    def total_creds(self) -> int:
        """Returns the total credits."""
        return self._total_creds

    @total_creds.setter
    def total_creds(self, total_creds: int):
        """Set the student total credits."""
        self._total_creds = total_creds

    def __str__(self) -> str:
        return f"{super().__str__()}\nTotal Credits: {self._total_creds}"
