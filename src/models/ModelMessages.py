from .Entities.Message import Message

class ModelMessages():
    
    @classmethod
    def getMessagesById(self,db,id):

        try:
            cursor =  db.connection.cursor()
            sql = f"""
            select id_message,id_remi,message,date_release 
            from messages m 
            where  id_dest  = {id};
            """
            cursor.execute(sql)
            rows =  cursor.fetchall()
            
            if rows != None:
                mensajes = []
                for m in rows:
                    mensajes.append(Message(m[0],None,self.getName(db,m[1]),m[2],m[3],None))
                return mensajes
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def getName(self,db,id):
        try:
            cursor = db.connection.cursor()
            sql = f"""SELECT id,username,fullname
                        from usuarios_p1 
                        WHERE id = '{id}'"""
            cursor.execute(sql)#Ejecto la consulta
            row = cursor.fetchone() #guardo el resultado
            if row !=None:
                return  row[1]            
            else:
                return  'Cuenta eliminada'   
                        
        except Exception as ex:
            raise Exception(ex) 
        
        
    @classmethod
    def clear_messages(self,db,id_dest):
        try:
            cursor = db.connection.cursor()
            sql = f"""DELETE from messages WHERE id_dest = {id_dest} """
            cursor.execute(sql)#Ejecto la consulta
            db.connection.commit()                     
        except Exception as ex:
            raise Exception(ex)
    
    
    @classmethod
    def insert_message(db,id_dest,id_remi):
        pass
                    