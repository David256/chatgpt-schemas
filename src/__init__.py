"""
The schemas module
"""

from typing import Literal, Union
# pylint: disable=no-name-in-module
from pydantic import BaseModel


Role = Union[Literal['user'], Literal['system'], Literal['assistant']]


class Message(BaseModel):
    """Message"""
    role: Role
    content: str

    def __repr__(self) -> str:
        return f'<Message from="{self.role}" content="{self.content}">'

    def __str__(self) -> str:
        return f'{self.role}: {self.content}'


class Choice(BaseModel):
    """Choice"""
    message: Message
    finish_reason: Union[
        Literal['stop'],
        Literal['length'],
        Literal['content_filter'],
        None,
    ]
    index: int


class Usage(BaseModel):
    """Usage"""
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class Response(BaseModel):
    """Response"""
    id: str
    object: str
    created: int
    model: str
    usage: Usage
    choices: list[Choice]


class Prompt(Message):
    """Prompt"""
    def __repr__(self) -> str:
        return f'<Prompt from="{self.role}" content="{self.content}">'
