from typing import List
from connection_pool import pool
import database


class Option:
    def __init__(self, option_text: str, poll_id: int, _id: int = None):
        self.id = _id
        self.text = option_text
        self.poll_id = poll_id
    
    def __repr__(self) -> str:
        return f"Option({self.text!r}, {self.poll_id!r}, {self.id!r})"
    
    def save(self):
        connection = pool.getconn()
        new_option_id = database.add_option(self.text, self.poll_id)
        pool.putconn(connection)
        self.id = new_option_id
    
    def vote(self, username: str):
        connection = pool.getconn()
        database.add_poll_vote(connection, username, self.id)
        pool.putconn(connection)
    
    @property
    def votes(self) -> List[database.Vote]:
        connection = pool.getconn()
        votes = database.get_votes_for_option(connection, self.id)
        pool.putconn(connection)
        return votes
    
    @classmethod
    def get(cls, option_id: int) -> "Option":
        connection = pool.getconn()
        option = database.get_option(connection, option_id)
        pool.putconn(connection)
        return cls(option[1], option[2], option[0])