class Aircraft:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print(self.x)
        print(self.y)

    def move_left(self):
        print("Moved Left..")
        self.x = self.x-1

    def move_right(self):
        print("Moved Right..")
        self.x = self.x+1

    def move_up(self):
        self.y = self.y+1
        print("Moved Up..")

    def move_down(self):
        print("Moved Down..")
        self.y = self.y-1

    instances=["instance1", "instance2", "instance3", "instance4", "instance5"]
    def instance_create(self):
        for i in range(len(instances)):
            if i==0: instances[i] = Aircraft(0,0)
            if i==1: instances[i] = Aircraft(3,6)
            if i==2: instances[i] = Aircraft(6,12)
            if i==3: instances[i] = Aircraft(9,18)
            if i==4: instances[i] = Aircraft(12,24)

    def final_x_y_coord(self):
        for i in range(len(instances)):
            print("\nAircraft [",i,"]")
            print("Final X-Coord:", instances[i].x)
            print("Final Y-Coord:", instances[i].y)

    def initial_x_y_coord(self):
        print("Creating New Aircraft Object:",i)
        print("New Aircraft Object Has Just Been Initalized:",i)
        print("Initial X-Coord:",instances[i].x)
        print("Initial Y-Coord:",instances[i].y)

    def directions(self):
        instances[i].move_right()
        instances[i].move_right()
        instances[i].move_up()
        instances[i].move_right()
        instances[i].move_left()
        instances[i].move_up()
        instances[i].move_up()
        instances[i].move_down()
        instances[i].move_up()
        instances[i].move_down()
        instances[i].move_up()

class Boeing_747(Aircraft):

    def __init__(self,x,y,x_d,y_d):
        self.x = x
        self.y = y
        self.x_d = x_d
        self.y_d = y_d


if __name__=='__main__':

    instances=["instance1", "instance2", "instance3", "instance4", "instance5"]
    for i in range(len(instances)):
        if i==0: instances[i] = Boeing_747(11,11,51,58)
        if i==1: instances[i] = Boeing_747(11,10,59,51)
        if i==2: instances[i] = Boeing_747(11,15,56,56)
        if i==3: instances[i] = Boeing_747(5,14,64,50)
        if i==4: instances[i] = Boeing_747(7,9,69,59)

        instances[i].initial_x_y_coord()
        print("New Boeing 747 Object Has Just Been Iniitalized:", i)
        print("X-Coord:",instances[i].x_d)
        print("Y-Coord:",instances[i].y_d)
        instances[i].directions()
    instances[i].final_x_y_coord()
