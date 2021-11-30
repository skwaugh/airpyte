from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.airbyte_catalog import AirbyteCatalog
from ..models.synchronous_job_read import SynchronousJobRead
from ..types import UNSET, Unset

T = TypeVar("T", bound="SourceDiscoverSchemaRead")


@attr.s(auto_attribs=True)
class SourceDiscoverSchemaRead:
    """Returns the results of a discover catalog job. If the job was not successful, the catalog field will not be present. jobInfo will aways be present and its status be used to determine if the job was successful or not."""

    job_info: SynchronousJobRead
    catalog: Union[Unset, AirbyteCatalog] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_info = self.job_info.to_dict()

        catalog: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.catalog, Unset):
            catalog = self.catalog.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobInfo": job_info,
            }
        )
        if catalog is not UNSET:
            field_dict["catalog"] = catalog

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_info = SynchronousJobRead.from_dict(d.pop("jobInfo"))

        _catalog = d.pop("catalog", UNSET)
        catalog: Union[Unset, AirbyteCatalog]
        if isinstance(_catalog, Unset):
            catalog = UNSET
        else:
            catalog = AirbyteCatalog.from_dict(_catalog)

        source_discover_schema_read = cls(
            job_info=job_info,
            catalog=catalog,
        )

        source_discover_schema_read.additional_properties = d
        return source_discover_schema_read

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
