#  ________________
#  Import LIBRARIES
from enum import Enum
from pydantic import BaseModel, field_validator
from datetime import date
#  Import FILES
# from .data import BANDS
#  ________________


class GenreChoices(Enum):
    ROCK = "Rock"
    ELECTRONIC = "Electronic"
    METAL = "Metal"
    HIP_HOP = "Hip-hop"
    SHOEGAZE = "Shoegaze"
    REGGAE = "Reggae"
    CLASSIC = "Classical"


class GenreURLChoices(Enum):
    ROCK = "rock"
    ELECTRONIC = "electronic"
    METAL = "metal"
    HIP_HOP = "hip-hop"
    SHOEGAZE = "shoegaze"
    REGGAE = "reggae"
    CLASSIC = "classical"


class Album(BaseModel):
    title: str
    release_date: date


class BandBase(BaseModel):
    name: str
    # genre: GenreChoices
    # genre: GenreURLChoices
    genre: str
    albums: list[Album] = []


class BandCreate(BandBase):
    @field_validator("genre", mode="before")
    @classmethod
    def title_case_genre(cls, value: str) -> str:
        print(f" _____++____ cls: {cls}, value: {value}, value.title: {value.title()}")
        return value.title()  # Converts RoCK, ROCK, rock -> Rock


# class BandCreate(BandBase):
#     pass


class BandWithID(BandBase):
    id: int


# class Band(BaseModel):
#     #  "id": 1, "name": "The Kinks", "genre": "Rock"
#     id: int
#     name: str
#     genre: str
#     albums: list[Album] = []
