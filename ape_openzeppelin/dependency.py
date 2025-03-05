from pathlib import Path
from typing import TYPE_CHECKING

from ape.api import DependencyAPI
from ape_pm.dependency import GithubDependency

if TYPE_CHECKING:
    from ethpm_types import PackageManifest


class OpenZeppelinDependency(DependencyAPI):
    name: str = "openzeppelin"
    openzeppelin: str

    @property
    def github(self) -> GithubDependency:
        return GithubDependency(
            name=self.name,
            version=self.openzeppelin,
            github="OpenZeppelin/openzeppelin-contracts",
        )

    @property
    def version_id(self) -> str:
        return self.github.version_id

    @property
    def uri(self) -> str:
        return self.github.uri

    @property
    def package_id(self) -> str:
        return self.github.package_id

    def fetch(self, destination: Path) -> "PackageManifest":
        return self.github.fetch(destination)
