from pydantic import BaseModel, UUID4
from typing import List, Optional


class GroupBase(BaseModel):
    name: str


class GroupCreate(GroupBase):
    pass


class Group(GroupBase):
    uuid: UUID4
    users: List[str]

    class Config:
        from_attributes = True


class GroupUpdate(BaseModel):
    name: Optional[str] = None

    class Config:
        from_attributes = True
