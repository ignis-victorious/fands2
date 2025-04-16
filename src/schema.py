#  ________________
#  Import LIBRARIES
from enum import Enum
from pydantic import BaseModel
from datetime import date
#  Import FILES
# from .data import BANDS
#  ________________


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


class Band(BaseModel):
    #  "id": 1, "name": "The Kinks", "genre": "Rock"
    id: int
    name: str
    genre: str
    albums: list[Album] = []
