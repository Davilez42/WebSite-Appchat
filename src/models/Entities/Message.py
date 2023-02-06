class Message():
    def __init__(self,id,id_dest,id_remi,message,date,time) -> None:
        self.id =id
        self.id_dest = id_dest
        self.id_remi = id_remi
        self.message = message
        self.date = date
        self.time = time
        self.deleted_dest = 'False'
        self.deleted_remi = 'False'
        
        
        