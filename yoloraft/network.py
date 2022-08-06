from abc import ABC, abstractmethod

from yoloraft.models import (
    AppendEntriesRequest,
    AppendEntriesResponse,
    InstallSnapshotRequest,
    InstallSnapshotResponse,
    VoteRequest,
    VoteResponse,
)


class RaftNetwork(ABC):
    @abstractmethod
    async def append_entries(
        self, target: str, request: AppendEntriesRequest
    ) -> AppendEntriesResponse:
        pass

    @abstractmethod
    async def vote(self, target: str, request: VoteRequest) -> VoteResponse:
        pass

    @abstractmethod
    async def install_snapshot(
        self, target: str, request: InstallSnapshotRequest
    ) -> InstallSnapshotResponse:
        pass
