#!/usr/bin/python3
# Tim H 2023
# Problem: 1603
# https://leetcode.com/problems/design-parking-system/description/
# Runtime:
# Memory:
"""docstring"""


class ParkingSystem:
    """docstring"""
    spaces = [(0, 0), (0, 0), (0, 0)]

    def __init__(self, big: int, medium: int, small: int):
        """docstring"""
        self.spaces = [[big, 0], [medium, 0], [small, 0]]

    def addCar(self, carType: int) -> bool:
        """docstring"""
        if self.spaces[carType-1][1] + 1 > self.spaces[carType-1][0]:
            return False

        self.spaces[carType-1][1] += 1
        return True


###############################################################################
#       MAIN
###############################################################################
obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))
