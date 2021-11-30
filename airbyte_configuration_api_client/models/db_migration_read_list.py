from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.db_migration_read import DbMigrationRead
from ..types import UNSET, Unset

T = TypeVar("T", bound="DbMigrationReadList")


@attr.s(auto_attribs=True)
class DbMigrationReadList:
    """ """

    migrations: Union[Unset, List[DbMigrationRead]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        migrations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.migrations, Unset):
            migrations = []
            for migrations_item_data in self.migrations:
                migrations_item = migrations_item_data.to_dict()

                migrations.append(migrations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if migrations is not UNSET:
            field_dict["migrations"] = migrations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        migrations = []
        _migrations = d.pop("migrations", UNSET)
        for migrations_item_data in _migrations or []:
            migrations_item = DbMigrationRead.from_dict(migrations_item_data)

            migrations.append(migrations_item)

        db_migration_read_list = cls(
            migrations=migrations,
        )

        db_migration_read_list.additional_properties = d
        return db_migration_read_list

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
