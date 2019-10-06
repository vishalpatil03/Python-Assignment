# Exercise #1:  A Basic Aircraft

# Exercise 1, part 1
print("# Exercise 1, part 1")
aircrafts = {"x": 21, "y": 41}

print(aircrafts["x"])
print(aircrafts["y"])


# Exercise 1, part 2
print("\n# Exercise 1, part 2")
Aircrafts = ["aircraft_1", "aircraft_2", "aircraft_3", "aircraft_4", "aircraft_5"]
coordinates = [50,55, 60,61, 65,66, 71,73, 74,76]

var = 0
for aircraft in Aircrafts:
    print(aircraft, "coordinates are: ", coordinates[var], coordinates[var+1])
    var+= 2
