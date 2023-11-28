class ParkingSystem:
  spaces = [(0, 0), (0, 0), (0, 0)]

  def __init__(self, big: int, medium: int, small: int):
    self.spaces = [[big, 0], [medium, 0], [small, 0]]

  def addCar(self, carType: int) -> bool:
    if self.spaces[carType-1][1] + 1 > self.spaces[carType-1][0]:
      return False
    else:
      self.spaces[carType-1][1] += 1
      return True

obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))
