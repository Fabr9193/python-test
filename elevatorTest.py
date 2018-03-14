import  random 
import string
import cherrypy
import json

class Elevator:
    """
    nb_story
    is_broken
    """
    def __init__(self,nb_story):
        self.nb_story = nb_story
    def crash_test(resistance):
        random.randint(self.nb_story, resistance)


class MyApp(object):
    MAX_ELEVATOR_LVL  = 19
    @cherrypy.expose
    def index(self):
        return "Hi to my first cherryPy App"

    @cherrypy.expose
    def tryout(self, nb_elevator, nb_story):
        resistance = random.randint(0, nb_story)
        result = {}
        result.update({'resistance' : resistance})
        result.update({'nbElevator' : nb_elevator})
        return json.dumps(result)
if __name__ == "__main__":
    cherrypy.quickstart(MyApp ())
