from .Entities.Message import Message


class ModelMessages():

    @classmethod
    def getMessagesById(self, db, id):

        try:
            cursor = db.connection.cursor()
            sql = f"""
            select id_message,id_remi,message,date_release,date_time
            from messages m 
            where id_dest  = {id} and deleted_dest = 'False'
            order by   date_release,date_time desc;
            """
            cursor.execute(sql)
            rows = cursor.fetchall()

            if rows != None:
                mensajes = []
                for m in rows:
                    inf = self.getInfoRemitent(db, m[1])
                    mensajes.append(
                        Message(m[0], None, inf if  inf[0]!=tuple() else inf[0], m[2], m[3], m[4],inf[1]))
                    
                return mensajes
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def getInfoRemitent(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = f"""SELECT id,username,fullname,sesion
                        from usuarios_p1 
                        WHERE id = '{id}'"""
            cursor.execute(sql)  # Ejecto la consulta
            row = cursor.fetchone()  # guardo el resultado
            if row != None:
                return row[1],row[3]
            else:
                return 'Cuenta eliminada'

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def clear_messages(self, db, id_dest):
        try:
            cursor = db.connection.cursor()

            sql = f"""
            UPDATE messages
            SET  deleted_dest='True'
            WHERE id_dest = {id_dest};
            """
            
            cursor.execute(sql) 
            db.connection.commit()
            
            sql_ = """
            DELETE 
            from messages
            where deleted_dest = 'True' and deleted_remi = 'True';
            """
            cursor.execute(sql_) 
            db.connection.commit()
            
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def insert_message(self, db, message):
        try:
            cursor = db.connection.cursor()
            sql_id = f"""
            SELECT id
            from usuarios_p1
            where username = '{message.id_dest}';
            """
            cursor.execute(sql_id)
            dest = cursor.fetchone()
            print(message.time)
            if dest != None:
                sql_insert = """
                INSERT INTO messages (id_dest,id_remi,message,date_release,date_time,deleted_dest,deleted_remi)
                VALUES(%s,%s,%s,%s,%s,%s,%s)
                """
                cursor.execute(sql_insert, (dest[0],
                                            message.id_remi,
                                            message.message,
                                            message.date,
                                            message.time,
                                            message.deleted_dest,
                                            message.deleted_remi))
                db.connection.commit()
                return True
            return None

        except Exception as ex:
            raise (ex)
        pass

