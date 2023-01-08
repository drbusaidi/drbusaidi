# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:22:04 2022

@author: جابر
"""
from SlottedALOHA import SlottedALOHA
import matplotlib.pyplot as pl

# Number of time slots in the simulation
NUM_TIME_SLOTS = 12000
# Offered load (G)
OFFERED_LOADS = [l for l in range(9)]
# Run the simulation for each offered load
simulations = [SlottedALOHA(NUM_TIME_SLOTS, offered_load) for offered_load in OFFERED_LOADS]
for simulation in simulations:
  simulation.simulation()
throughputs = [simulation.throughput() for simulation in simulations]
# Print the results
for offered_load, throughput in zip(OFFERED_LOADS, throughputs):
  print(f"Offered load = {offered_load:.1f}, Throughput = {throughput:.3f}")

# Plot the results
pl.plot(OFFERED_LOADS, throughputs,'blue')
pl.title('Slotted ALOHA', fontsize=20, fontweight='bold')
pl.xlabel('Offered load (G)')
pl.ylabel('Throughput (successs rate) ')
pl.show()
