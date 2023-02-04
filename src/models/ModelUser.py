from .Entities.User import User
from .ModelMessages import ModelMessages
class ModelUser():
    @classmethod
    def login(self,db,user):
        try:
            cursor = db.connection.cursor()
            sql = f"""SELECT id,username,password 
                    from usuarios_p1 WHERE username = '{user.username}'"""
            cursor.execute(sql)#Ejecto la consulta
            row = cursor.fetchone()#guardo el resultado
            if row !=None:
                return User(row[0],row[1],None,User.check_password_hash(row[2],user.password),None)              
            else:
                return  None    
                         
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self,db,id):
        try:
            cursor = db.connection.cursor()
            sql = f"""SELECT id,username,fullname
                        from usuarios_p1 
                        WHERE id = '{id}'"""
            cursor.execute(sql)#Ejecto la consulta
            row = cursor.fetchone() #guardo el resultado
            if row !=None:
                return User(row[0],row[1],row[2],None,ModelMessages.getMessagesById(db,row[0]) )              
            else:
                return  None    
                         
        except Exception as ex:
            raise Exception(ex)        
    
    @classmethod
    def insert_user(self,db,user):
        pass
    
    @classmethod
    def deleted_user(self,db,user):
        pass     
      
        