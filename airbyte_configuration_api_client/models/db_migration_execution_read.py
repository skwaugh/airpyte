from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.db_migration_read import DbMigrationRead
from ..types import UNSET, Unset

T = TypeVar("T", bound="DbMigrationExecutionRead")


@attr.s(auto_attribs=True)
class DbMigrationExecutionRead:
    """ """

    initial_version: Union[Unset, str] = UNSET
    target_version: Union[Unset, str] = UNSET
    executed_migrations: Union[Unset, List[DbMigrationRead]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        initial_version = self.initial_version
        target_version = self.target_version
        executed_migrations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.executed_migrations, Unset):
            executed_migrations = []
            for executed_migrations_item_data in self.executed_migrations:
                executed_migrations_item = executed_migrations_item_data.to_dict()

                executed_migrations.append(executed_migrations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if initial_version is not UNSET:
            field_dict["initialVersion"] = initial_version
        if target_version is not UNSET:
            field_dict["targetVersion"] = target_version
        if executed_migrations is not UNSET:
            field_dict["executedMigrations"] = executed_migrations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        initial_version = d.pop("initialVersion", UNSET)

        target_version = d.pop("targetVersion", UNSET)

        executed_migrations = []
        _executed_migrations = d.pop("executedMigrations", UNSET)
        for executed_migrations_item_data in _executed_migrations or []:
            executed_migrations_item = DbMigrationRead.from_dict(executed_migrations_item_data)

            executed_migrations.append(executed_migrations_item)

        db_migration_execution_read = cls(
            initial_version=initial_version,
            target_version=target_version,
            executed_migrations=executed_migrations,
        )

        db_migration_execution_read.additional_properties = d
        return db_migration_execution_read

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
