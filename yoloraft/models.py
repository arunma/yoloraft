from abc import ABC
from dataclasses import dataclass
from typing import List, Set


class AppData(ABC):
    pass


class AppDataResponse(ABC):
    pass


class EntryPayload(ABC):
    pass


@dataclass(unsafe_hash=True)
class EntryBlank(EntryPayload):
    pass


@dataclass(unsafe_hash=True)
class EntryNormal(EntryPayload):
    app_data: AppData


@dataclass(unsafe_hash=True)
class MembershipConfig(EntryPayload):
    members: Set[str]
    members_after_consensus: Set[str]


@dataclass(unsafe_hash=True)
class EntryConfigChange(EntryPayload):
    membership_config: MembershipConfig


@dataclass(unsafe_hash=True)
class EntrySnapshotPointer:
    id: str
    membership_config: MembershipConfig


@dataclass(unsafe_hash=True)
class Entry:
    index: int
    term: int
    command: EntryPayload


@dataclass(unsafe_hash=True)
class AppendEntriesRequest:
    term: int
    leader_id: str
    prev_log_index: int
    prev_log_term: int
    entries: List[Entry]
    leader_commit: int


# Only present when the AE response is false. This serves as the addl information for actioning the failure
@dataclass(unsafe_hash=True)
class ConflictOpt:
    term: int
    index: int


@dataclass(unsafe_hash=True)
class AppendEntriesResponse:
    term: int
    success: bool
    conflict_opt: ConflictOpt


@dataclass(unsafe_hash=True)
class VoteRequest:
    term: int
    candidate_id: str
    last_log_index: int
    last_log_term: int


@dataclass(unsafe_hash=True)
class VoteResponse:
    term: int
    vote_granted: bool


# Used to send a snapshot to a follower
@dataclass(unsafe_hash=True)
class InstallSnapshotRequest:
    term: int
    leader_id: str
    last_included_index: int  # TODO Probably consider renaming
    last_included_term: int
    offset: int
    data: bytes
    done: bool


@dataclass(unsafe_hash=True)
class InstallSnapshotResponse:
    term: int
