from flask import Flask
from flask_restful import Api, Resource
from task import task

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    '''
    Home route
    '''

    def get(self):
        '''get request'''
        #delay is the key word used to do async, it puts the task in the queue
        task.delay()
        return "request made"
   

api.add_resource(Home, '/')
if __name__ == "__main__":
    app.run(debug=True)