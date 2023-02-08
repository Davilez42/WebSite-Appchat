from .Entities.User import User
from .ModelMessages import ModelMessages


class ModelUser():
    @classmethod
    def login(self, db, user):  # CONSULTAR
        try:
            cursor = db.connection.cursor()
            sql = f"""SELECT id,username,password 
                    from usuarios_p1 WHERE username = '{user.username}'"""
            cursor.execute(sql)  # Ejecto la consulta
            row = cursor.fetchone()  # guardo el resultado
            if row != None:
                return User(row[0], row[1], None, User.check_password_hash(row[2], user.password), None, None,None)
            else:
                return None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def cambiar_estado_sesion(self,db,estado,id):
        try:
            cursor = db.connection.cursor()
            sql = f""" UPDATE usuarios_p1 SET sesion = '{estado}' where id = {id} """
            cursor.execute(sql)
            db.connection.commit()
            
        except Exception as ex:
            raise(ex)
        
    @classmethod
    def get_by_id(self, db, id):  # CONSULTAR
        try:
            cursor = db.connection.cursor()
            sql = f"""SELECT id,username,fullname,email
                        from usuarios_p1 
                        WHERE id = '{id}'"""
            cursor.execute(sql)  # Ejecto la consulta
            row = cursor.fetchone()  # guardo el resultado
            if row != None:
                return User(row[0], row[1], row[2], None, row[3], ModelMessages.getMessagesById(db, row[0]),None)
            else:
                return None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def insert_user(self, db, user):  # CREATE
        try:
            cursor = db.connection.cursor()
            sql_user = f"""
                Select username
                from usuarios_p1 
                where username = '{user.username}';
            """
            sql_email = f"""
                Select email
                from usuarios_p1 
                where email = '{user.email}';
            """
            sql_insert = f""" INSERT INTO usuarios_p1 (username,fullname,password,email,sesion) VALUES (%s,%s,%s,%s,%s); """
            cursor.execute(sql_user)
            rows_username = cursor.fetchone()

            if rows_username == None:
                cursor.execute(sql_email)
                rows_email = cursor.fetchone()
                if rows_email != None:
                    return (True, False, None)
                else:
                    if len(user.password) >= 8:
                        cursor.execute(sql_insert, (user.username, user.fullname, User.transformPasswordToHash(
                            user.password), user.email,user.estado_del_usuario))  # Ejecto la consulta
                        db.connection.commit()
                        return (True, True, True)
                    else:

                        return (True, True, False)

            else:
                return (False, None, None)

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def deleted_user(self, db, username):
        try:
            cursor = db.connection.cursor()
            sql_delete = f"""
            DELETE FROM usuarios_p1 where username = '{username}';
            """
            cursor.execute(sql_delete)
            db.connection.commit()

        except Exception as ex:
            raise (ex)  # genera una excepcion
