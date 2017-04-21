# -*- coding: utf-8 -*-
import module
import DataBase.DBhandler as DB

handlers = [
    (r'/test', module.test),
    (r'/', module.IndexHandler),
    (r'/TM', module.TMHandler),
    (r'/DB',DB.DBhandler)

]
