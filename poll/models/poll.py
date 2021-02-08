from typing import List
from connection_pool import pool
from models.option import Option
import database


class Poll:
    def __init__(self, title: str, owner: str, _id: int = None):
        self.id = _id
        self.title = title
        self.owner = owner
    
    def __repr__(self) -> str:
        return f"Poll({self.name!r}, {self.owner!r}, {self.id!r})"
    
    def add_option(self, option_text: str):
        Option(option_text, self.id).save()
    
    def save(self):
        connection = pool.getconn()
        new_poll_id = database.create_poll(connection, self.title, self.owner)
        pool.putconn(connection)
        self.id = new_poll_id
    
    @property
    def options(self) -> List[Option]:
        connection = pool.getconn()
        options = database.get_poll_options(connection, self.id)
        pool.putconn(connection)
        return [Option(option[1], option[2], option[0]) for option in options]
    
    @classmethod
    def get(cls, poll_id: int) -> "Poll":
        connection = pool.getconn()
        poll = database.get_poll(connection, poll_id)
        pool.putconn(connection)
        return cls(poll[1], poll[2], poll[0])
    
    @classmethod
    def all(cls) -> List["Poll"]:
        connection = pool.getconn()
        polls = database.get_polls(connection)
        pool.putconn(connection)
        return [cls(poll[1], poll[2], poll[0]) for poll in polls]
    
    @classmethod
    def latest(cls) -> "Poll":
        connection = pool.getconn()
        poll = database.get_latest_poll()
        pool.putconn(connection)
        return cls(poll[1], poll[2], poll[0])
