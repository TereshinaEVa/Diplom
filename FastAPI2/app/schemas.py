from pydantic import BaseModel


class CreatePersons(BaseModel):
    username: str
    grade: int
    age: int
    #password: str


class UpdatePersons(BaseModel):
    firstname: str
    lastname: str
    age: int


class CreateText_and_Video(BaseModel):
    title: str
    description: str
    text_url: str
    video_url: str
    #stady


class UpdateText_and_Video(BaseModel):
    title: str
    description: str
    text_url: str
    video_url: str
