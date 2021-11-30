from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.db_migration_state import DbMigrationState
from ..types import UNSET, Unset

T = TypeVar("T", bound="DbMigrationRead")


@attr.s(auto_attribs=True)
class DbMigrationRead:
    """ """

    migration_type: str
    migration_version: str
    migration_description: str
    migration_state: Union[Unset, DbMigrationState] = UNSET
    migrated_by: Union[Unset, str] = UNSET
    migrated_at: Union[Unset, int] = UNSET
    migration_script: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        migration_type = self.migration_type
        migration_version = self.migration_version
        migration_description = self.migration_description
        migration_state: Union[Unset, str] = UNSET
        if not isinstance(self.migration_state, Unset):
            migration_state = self.migration_state.value

        migrated_by = self.migrated_by
        migrated_at = self.migrated_at
        migration_script = self.migration_script

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "migrationType": migration_type,
                "migrationVersion": migration_version,
                "migrationDescription": migration_description,
            }
        )
        if migration_state is not UNSET:
            field_dict["migrationState"] = migration_state
        if migrated_by is not UNSET:
            field_dict["migratedBy"] = migrated_by
        if migrated_at is not UNSET:
            field_dict["migratedAt"] = migrated_at
        if migration_script is not UNSET:
            field_dict["migrationScript"] = migration_script

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        migration_type = d.pop("migrationType")

        migration_version = d.pop("migrationVersion")

        migration_description = d.pop("migrationDescription")

        _migration_state = d.pop("migrationState", UNSET)
        migration_state: Union[Unset, DbMigrationState]
        if isinstance(_migration_state, Unset):
            migration_state = UNSET
        else:
            migration_state = DbMigrationState(_migration_state)

        migrated_by = d.pop("migratedBy", UNSET)

        migrated_at = d.pop("migratedAt", UNSET)

        migration_script = d.pop("migrationScript", UNSET)

        db_migration_read = cls(
            migration_type=migration_type,
            migration_version=migration_version,
            migration_description=migration_description,
            migration_state=migration_state,
            migrated_by=migrated_by,
            migrated_at=migrated_at,
            migration_script=migration_script,
        )

        db_migration_read.additional_properties = d
        return db_migration_read

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
