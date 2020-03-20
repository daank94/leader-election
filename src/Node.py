import time
import logging

class Node:

    def __init__(self, node_number):
        self.node_number = node_number

    def set_neighbour(self, neighbour_node):
        self.neighbour_node = neighbour_node

    def wakeup(self):
        # Delay the wakeup a bit to allow other threads to do their thing as well (to simulate network traffic)
        time.sleep(1)
        logging.info("Node %i has woken up", self.node_number)

    def receive(self, message):
        # Delay the receive a bit to allow other threads to do their thing as well (to simulate network traffic)
        time.sleep(1)
        logging.info("Node %i  received '%s'", self.node_number, message)

    def __str__(self):
        return "Node " + str(self.node_number)  + " with neighbour: " + (str(self.neighbour_node.node_number) if self.neighbour_node else None)