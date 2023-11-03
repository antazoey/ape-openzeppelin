import pytest

from ape_openzeppelin.dependency import OpenZeppelinDependency


class TestOpenZeppelinDependency:
    @pytest.fixture
    def dependency(self):
        return OpenZeppelinDependency(openzeppelin="4.0.0")

    def test_version_id(self, dependency):
        assert dependency.version_id == "4.0.0"

    def test_uri(self, dependency):
        assert (
            dependency.uri
            == "https://github.com/OpenZeppelin/openzeppelin-contracts@4.0.0/releases/tag/v4.0.0"
        )