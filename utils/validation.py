from pydantic import BaseModel
from datetime import datetime

class Token(BaseModel):
    user: str
    exp: int


    def get_expiry_time(self):
        return datetime.utcfromtimestamp(self.exp)