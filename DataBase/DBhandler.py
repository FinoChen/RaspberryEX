from DBoperation import TMDatabase
import SaveToDB

class DBHandler(tornado.web.RequestHandler):
    def get(self):
        database = TMDatabase()
        SaveToDB.save(database)
        self.write()



