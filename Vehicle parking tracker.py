class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class ParkingSpot:
    def __init__(self, size):
        self.size = size  # List of acceptable vehicle types
        self.occupied = False
        self.vehicle = None

    def can_fit(self, vehicle):
        return not self.occupied and vehicle.vehicle_type in self.size

    def park(self, vehicle):
        if self.can_fit(vehicle):
            self.vehicle = vehicle
            self.occupied = True
            return True
        return False

    def leave(self):
        self.vehicle = None
        self.occupied = False

    def __str__(self):
        if self.occupied:
            return f"Occupied by {self.vehicle.vehicle_type}"
        return "Empty"

class Level:
    def __init__(self, spots):
        self.spots = spots

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.park(vehicle):
                return True
        return False

    def display_parking(self):
        for i, spot in enumerate(self.spots):
            print(f"Spot {i + 1}: {spot}")


spots = [
    ParkingSpot(["car", "motorcycle"]),
    ParkingSpot(["motorcycle"]),
    ParkingSpot(["car", "motorcycle"]),
    ParkingSpot(["truck", "car"]),
    ParkingSpot(["truck"]),
    ParkingSpot(["car"]),
    ParkingSpot(["truck", "motorcycle"])
]

level = Level(spots)

vehicles = [
    Vehicle("car"),
    Vehicle("motorcycle"),
    Vehicle("truck"),
    Vehicle("motorcycle"),
    Vehicle("car"), 
    Vehicle("truck"),  
    Vehicle("car"),
    Vehicle("motorcycle")
]


for i, v in enumerate(vehicles):
    result = level.park_vehicle(v)
    print(f"Vehicle {i + 1} ({v.vehicle_type}) parked:", result)


print("\nFinal parking spot status:")
level.display_parking()
