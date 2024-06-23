import json

class Database:

    #Registration r database store korar jonno json file e
    def add_data(self,name,email,password):

        with open('db.json','r') as f:
            database = json.load(f)

        if email in database:
            return 0

        else:
            database[email]=[name,password]
            with open('db.json','w') as g:
                json.dump(database,g)
            return 1


    #login check

    def check_data(self,email,password):
        with open('db.json','r') as f:
            database = json.load(f)

        if email in database:
            if database[email][1]==password:
                return 1
            else:
                return 0
        else:
            return 0













