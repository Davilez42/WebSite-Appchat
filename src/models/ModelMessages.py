

class ModelMessages():
    
    @classmethod
    def getMessagesById(self,db,id):

        try:
            cursor =  db.connection.cursor()
            sql = f"""
            select id_message,id_remi,message 
            from messages m 
            where  id_dest  = {id};
            """
            cursor.execute(sql)
            rows =  cursor.fetchall()
            
            if rows != None:
                
                return {x:[self.getName(db,y),z] for x,y,z in list(rows)}
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
                return  None    
                        
        except Exception as ex:
            raise Exception(ex) 