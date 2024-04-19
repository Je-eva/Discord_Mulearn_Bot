from connection import DBConnection

class TaskDB():
    def __init__(self) -> None:
        self.db_queries = DBConnection()
    
    def task_insertion(self,message):
        query=f"""
                INSERT INTO message(content,message_id,is_reacted,author,karma)
                VALUES(:content,:message_id,False,:message_author,0)"""
                
        params={
            "content": message.content,
            "message_id": message.id,
            "message_author": message.author
            
        }
        self.db_queries.execute(query,params)

    def award_karma(self,message_id,author_id):
        query="""
                UPDATE message SET karma=100, reacted_by =:author, is_reacted= TRUE
                WHERE message_id =:message
                """
        params={
            "author": author_id,
            "message": message_id
        }
        self.db_queries.execute(query,params)
    def delete_message(self, message_id):
        query="DELETE FROM message WHERE message_id =:msg_id"
        params= {
            "msg_id": message_id
        }
        self.db_queries.execute(query,params)

    def get_user_karma(self,author_id):
        query="""SELECT sum(karma) FROM message
                WHERE author =:author
                """
        param={
            "author":author_id
        }
        return self.db_queries.fetch_one(query,param)
