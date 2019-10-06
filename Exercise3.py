# Exercise #3: Create a small fleet of Aircraft

class Aircraft:
    x=y = 0
    acceleration = 1

    def move_left(self):
        # print("Moved Left..")
        self.x = self.x-1

    def move_right(self):
        # print("Moved Right..")
        self.x = self.x+1

    def move_up(self):
        self.y = self.y+1
        # print("Moved Up..")

    def move_down(self):
        # print("Moved Down..")
        self.y = self.y-1

print("# Exercise 3 \n")

instances=["instance1", "instance2", "instance3", "instance4", "instance5"]
for i in range(len(instances)):

    instances[i] = Aircraft()
    print("Creating New Aircraft Object:",i)
    print("New Aircraft Object Has Just Been Initalized:",i)
    print("Initial X-Coord:",instances[i].x)
    print("Initial Y-Coord:",instances[i].y)

for i in range(len(instances)):
    if i==0:
        print("Aircraft Instance",i,"has moved UP ...")
        instances[i].move_up()
        print("Aircraft Instance",i,"has moved UP ...")
        instances[i].move_up()
        print("Aircraft Instance",i,"has moved UP ...")
        instances[i].move_up()
        print("Aircraft Instance",i,"has moved RIGHT ...")
        instances[i].move_right()

    if i==1:
        print("Aircraft Instance",i,"has moved UP ...")
        instances[i].move_up()
        print("Aircraft Instance",i,"has moved RIGHT ...")
        instances[i].move_right()
        print("Aircraft Instance",i,"has moved RIGHT ...")
        instances[i].move_right()

    if i==2:
        print("Aircraft Instance",i,"has moved UP ...")
        instances[i].move_up()
        print("Aircraft Instance",i,"has moved UP ...")
        instances[i].move_up()
        print("Aircraft Instance",i,"has moved UP ...")
        instances[i].move_up()
        print("Aircraft Instance",i,"has moved RIGHT ...")
        instances[i].move_right()
        print("Aircraft Instance",i,"has moved RIGHT ...")
        instances[i].move_right()

    if i==3:
        print("Aircraft Instance",i,"has moved RIGHT ...")
        instances[i].move_right()
        print("Aircraft Instance",i,"has moved LEFT ...")
        instances[i].move_left()
        print("Aircraft Instance",i,"has moved RIGHT ...")
        instances[i].move_right()
        print("Aircraft Instance",i,"has moved UP ...")
        instances[i].move_up()

    if i==4:
        print("Aircraft Instance",i,"has moved RIGHT ...")
        instances[i].move_right()
        print("Aircraft Instance",i,"has moved RIGHT ...")
        instances[i].move_right()
        print("Aircraft Instance",i,"has moved RIGHT ...")
        instances[i].move_right()
        print("Aircraft Instance",i,"has moved RIGHT ...")
        instances[i].move_right()
        print("Aircraft Instance",i,"has moved RIGHT ...")
        instances[i].move_right()
        print("Aircraft Instance",i,"has moved UP ...")
        instances[i].move_up()
        print("Aircraft Instance",i,"has moved UP ...")
        instances[i].move_up()
        print("Aircraft Instance",i,"has moved UP ...")
        instances[i].move_up()

for i in range(len(instances)):
    print("\nAircraft [",i,"]")
    print("Final X-Coord:", instances[i].x)
    print("Final Y-Coord:", instances[i].y)
