# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:08:03 2022

@author: جابر
"""

import random
import matplotlib.pyplot as plt

class SlottedALOHA:
    
  def __init__(self, num_time_slots, offered_load):
    # Initialize the number of time slots, probability of transmission, and counters for successful transmissions and collisions
    self.num_time_slots = num_time_slots
    self.p = offered_load / 10
    self.num_successful_transmissions = 0
    self.num_collisions = 0

  def simulation(self):
      
    # Loop through each time slot
    for i in range(self.num_time_slots):
      # Check if each node wants to transmit in this time slot
      node_transmitting = [random.random() < self.p for _ in range(10)]
      # Count the number of nodes that are transmitting
      num_nodes_transmitting = sum(node_transmitting)
      # If only one node is transmitting, it is a successful transmission
      if num_nodes_transmitting == 1:
        self.num_successful_transmissions += 1
      # If more than one node is transmitting, it is a collision
      elif num_nodes_transmitting > 1:
        self.num_collisions += 1

  def throughput(self):
      
    # Calculate the throughput per frame time for this simulation
    throughput = self.num_successful_transmissions / self.num_time_slots
    return throughput
