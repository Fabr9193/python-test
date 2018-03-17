import  random 
import string
import cherrypy
import json

class Elevator:
    """
    nb_story
    is_broken
    """
    MAX_ELEVATOR_LVL  = 19
    def __init__(self,resistance):
        self.resistance = resistance 
        self.is_broken = False
    def crash_test(self, nb_story):
        """
        return is_broken bool
        """
        if nb_story > self.resistance:
            self.is_broken = True
        return self.is_broken


def  find_resistance_1(nb_elevator,nb_story):
    elevator = Elevator(9)
    for i in range(1, nb_story):
        if elevator.crash_test(i):
            return i - 1, i - 1

def find_resistance_2(nb_elevator, nb_story):
    




    # elevators = []
    # for i in range(0, nb_elevator):

    #     elevators.append(Elevator(9))



class MyApp(object):
    @cherrypy.expose
    def index(self):
        return "Hi to my first cherryPy App"

    @cherrypy.expose
    def tryout(self, nb_elevator, nb_story):
        resistance = random.randint(0, int(nb_story))
        result = {}
        result.update({'resistance' : resistance})
        result.update({'nbElevator' : nb_elevator})
        return json.dumps(result)
if __name__ == "__main__":
    # cherrypy.quickstart(MyApp ())
    assert  not Elevator(12).crash_test(6)
    assert  Elevator(12).crash_test(13)
    assert  find_resistance(10, 13) == (9,9)

