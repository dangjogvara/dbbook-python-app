class Person:
    """Person class for the dbbook database."""

    def __init__(self, id: int, name: str, dept_name: str) -> None:
        """Initialize a Person object."""
        self._id = id
        self._name = name
        self._dept_name = dept_name

    @property
    def id(self) -> int:
        """Returns the id."""
        return self._id

    @id.setter
    def id(self, id: int):
        """Set the person id."""
        self._id = id

    @property
    def name(self) -> str:
        """Returns the name."""
        return self._name

    @name.setter
    def name(self, name: str):
        """Set the name."""
        self._name = name

    @property
    def dept_name(self) -> str:
        """Get the department."""
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name: str):
        """Set the department."""
        self._dept_name = dept_name

    def __str__(self) -> str:
        """Returns an object representation."""
        return f"Id: {self.id}\nName: {self.name}\nDepartment: {self.dept_name}"
