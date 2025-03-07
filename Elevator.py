#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This code is built to simulate an elevator during operation.
It is based on the following project criteria:
- Simulate an elevator using any language you choose
- Inputs: a list of floors to visit (e.g. elevator start=12 floor=2,9,1,32)
- Outputs: total travel time, floors visited (e.g. 560 12,2,9,1,32)
- Document all Assumptions and features not implemented

Filename: Elevator.py
Created: 2025-03-05
Author: Michael Martin
Contact: michael.martin2255@gmail.com
License: MIT License
Dependencies: time
"""

import time

__version__ = "1.0.0"
__status__ = "Development"

# Time it takes toi travel 1 floor
TRAVEL_TIME = 10   # Unitless according to the project instructions
BUILDING_FLOOR_COUNT = 31

class ElevatorSimulator():
    """ A simple class to simulate a passenger ride on an elevator.

        Parameters
        ----------
        num_floors : int
            The total number of floors travelable in this elevator instance

        Attributes
        ----------
        num_floors (public): int
            the total number of floors the elevator can reach
        _current_floor (private): int
            the current floor the elevator is on
        request_queue (public): dictionary
            the queue used by the elevator to travel up and down

    """
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self._current_floor = 1
        self.request_queue = {}

    def process_queue(self):
        """ Process the first elevator request in the request_queue.

            Assumptions:
                - The floor list should not be empty as no calls would be made

            Returns:
                elapsed_travel_time (int): The total time it takes to travel to
                                           all floors in the request queue
                floors_visited (list): A list of the floors visited in total
        """
        if not self.request_queue:
            return 0, []

        floors_visited = []
        elapsed_travel_time = 0

        # Retrieve the first key from queue dictionary
        calling_floor = list(self.request_queue.keys())[0]

        # Retrieves the first key,value pair from queue dictionary (FIFO)
        floor_list = self.request_queue.pop(calling_floor)

        print(f"\nTraveling to floor {calling_floor} for passenger pickup.")

        self._current_floor = calling_floor

        for floor in floor_list:
            # Check to see that the floor exists
            if floor < 1 or floor > self.num_floors: continue

            # Inform the passenger of the next stop
            print(f"Traveling to floor {floor} from floor {self._current_floor}")

            # Move to the next floor and get the distance traveled
            distance_traveled = self.move_to_next_floor(floor)

            floors_visited.append(floor)

            # Calculate the new elapsed travel time based on the travel time constant
            elapsed_travel_time = elapsed_travel_time + (distance_traveled * TRAVEL_TIME)

            time.sleep(0.20)

        return elapsed_travel_time, floors_visited

    def move_to_next_floor(self, new_floor_num: int):
        """ This function determines the absolute difference between the current
            floor and their new requested floor.

            Parameters:
                new_floor_num (integer): An Integer representing the next floor
                                         to travel to.

            Returns:
                diff_in_floor_num (int): The absolute value of the difference
                                         between the current and new floor.

        """
        diff_in_floor_num = abs(self._current_floor - new_floor_num)
        self._current_floor = new_floor_num

        return diff_in_floor_num

    def add_passenger_request(self, starting_floor: int, travel_floors: list):
        """ Adds a new entry into the request_queue.

            Assumptions:
                - the starting_floor should only be an integer since floors
                  are only integer based
                - the travel_floors should be a list of integers denoting
                  the different floors requested to visit.

            Parameters:
                starting_floor (integer): An Integer representing the starting floor
                                          to travel to.
                travel_floors (list): A List of Integers representing the floors
                                      to travel to.

        """
        self.request_queue[starting_floor] = travel_floors



if __name__ == '__main__':

    # Create ElevatorSimulator Instance
    elevator = ElevatorSimulator(num_floors=BUILDING_FLOOR_COUNT)

    # Simulate Passenger Calls to Elevator
    elevator.add_passenger_request(starting_floor=6, travel_floors=[2,9,1,31])
    elevator.add_passenger_request(starting_floor=13, travel_floors=[3,6,9,30,17])

    # Elevator Simulation Loop
    while elevator.request_queue:

        # Proces the request_queue (FIFO)
        travel_time, floors_visited = elevator.process_queue()

        if travel_time != 0:
            floor_string = ", ".join([str(floor) for floor in floors_visited])

            # Inform the passenger of the floors traveled and time it took
            print(f"You traveled to floors {floor_string} with an elapsed time of {travel_time}\n")

