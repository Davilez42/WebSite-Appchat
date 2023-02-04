from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
class User(UserMixin):
    def __init__(self,id,username,fullname,password,mensage) -> None:
        self.id = id
        self.username = username
        self.fullname = fullname
        self.password = password
        self.messages = mensage
        ()
    @classmethod    
    def check_password_hash(self,hashed_password,password)->None:
        return check_password_hash(hashed_password,password=password)   
    

