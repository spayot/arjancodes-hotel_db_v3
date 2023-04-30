from typing import Any, Callable, Protocol

DataObject = dict[str, Any]


class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...

    def __lt__(self, other: Any) -> bool:
        ...

    def __gt__(self, other: Any) -> bool:
        ...


class DataInterface(Protocol):
    def read_by_id(self, id: int) -> DataObject:
        ...

    def read_all(self) -> list[DataObject]:
        ...

    def create(self, data: DataObject) -> DataObject:
        ...

    def update(self, id: int, data: DataObject) -> DataObject:
        ...

    def delete(self, id: int) -> DataObject:
        ...

    def filter(self, condition: Any) -> list[DataObject]:
        ...

    def field_getter(self) -> Callable[[str], Comparable]:
        """returns a function that maps field name to a comparable object."""
        ...
