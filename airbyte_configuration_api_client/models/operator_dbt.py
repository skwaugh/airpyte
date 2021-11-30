from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OperatorDbt")


@attr.s(auto_attribs=True)
class OperatorDbt:
    """ """

    git_repo_url: str
    git_repo_branch: Union[Unset, str] = UNSET
    docker_image: Union[Unset, str] = UNSET
    dbt_arguments: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        git_repo_url = self.git_repo_url
        git_repo_branch = self.git_repo_branch
        docker_image = self.docker_image
        dbt_arguments = self.dbt_arguments

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gitRepoUrl": git_repo_url,
            }
        )
        if git_repo_branch is not UNSET:
            field_dict["gitRepoBranch"] = git_repo_branch
        if docker_image is not UNSET:
            field_dict["dockerImage"] = docker_image
        if dbt_arguments is not UNSET:
            field_dict["dbtArguments"] = dbt_arguments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        git_repo_url = d.pop("gitRepoUrl")

        git_repo_branch = d.pop("gitRepoBranch", UNSET)

        docker_image = d.pop("dockerImage", UNSET)

        dbt_arguments = d.pop("dbtArguments", UNSET)

        operator_dbt = cls(
            git_repo_url=git_repo_url,
            git_repo_branch=git_repo_branch,
            docker_image=docker_image,
            dbt_arguments=dbt_arguments,
        )

        operator_dbt.additional_properties = d
        return operator_dbt

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
