import logging
from typing import Dict, List, Protocol

import requests

from osint import config

log = logging.getLogger(__name__)


class Client(Protocol):

    def get_data(domain: str) -> str | None:
        ...


class TheHarvesterClient:

    def __init__(
        self,
        base_url: str
    ) -> None:
        self._sources: List[str] | None = None
        self._base_url: str = base_url

    def get_sources(self) -> str:
        if self._sources:
            return self._sources

        # TODO: perheps it's not the best idea, since some sources require API key
        try:
            sources = requests.get(f"{self._base_url}/sources").json()["sources"]
            self._sources = sources
        except requests.exceptions.RequestException:
            raise ValueError("unable to provide sources for theHarvester")
        return self._sources

    def get_data(self, domain: str) -> str | None:
        try:
            sources = self.get_sources()
            source_query = ",".join(sources)

            resp = requests.get(f"{self._base_url}/query/?domain={domain}&source={source_query}")
            resp.raise_for_status()
            return resp.content
        except requests.exceptions.RequestException:
            log.warning(f"unable to get data for {domain=} from theHarvester")
        return None


class ClientFactory:

    def __init__(self, clients: Dict[str, Client]):
        self.clients = clients

    def get_client(self, tool: str) -> Client:
        if tool not in self.clients:
            raise ValueError("unsupported api client")
        return self.clients.get(tool)


# TODO: add more APIs
DataClientFactory = ClientFactory({
    "theHarvester": TheHarvesterClient(config.THE_HARVESTER_URL)
})
