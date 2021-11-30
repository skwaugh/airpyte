from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.operator_dbt import OperatorDbt
from ..models.operator_normalization import OperatorNormalization
from ..models.operator_type import OperatorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OperatorConfiguration")


@attr.s(auto_attribs=True)
class OperatorConfiguration:
    """ """

    operator_type: OperatorType
    normalization: Union[Unset, OperatorNormalization] = UNSET
    dbt: Union[Unset, OperatorDbt] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operator_type = self.operator_type.value

        normalization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.normalization, Unset):
            normalization = self.normalization.to_dict()

        dbt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dbt, Unset):
            dbt = self.dbt.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operatorType": operator_type,
            }
        )
        if normalization is not UNSET:
            field_dict["normalization"] = normalization
        if dbt is not UNSET:
            field_dict["dbt"] = dbt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operator_type = OperatorType(d.pop("operatorType"))

        _normalization = d.pop("normalization", UNSET)
        normalization: Union[Unset, OperatorNormalization]
        if isinstance(_normalization, Unset):
            normalization = UNSET
        else:
            normalization = OperatorNormalization.from_dict(_normalization)

        _dbt = d.pop("dbt", UNSET)
        dbt: Union[Unset, OperatorDbt]
        if isinstance(_dbt, Unset):
            dbt = UNSET
        else:
            dbt = OperatorDbt.from_dict(_dbt)

        operator_configuration = cls(
            operator_type=operator_type,
            normalization=normalization,
            dbt=dbt,
        )

        operator_configuration.additional_properties = d
        return operator_configuration

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
