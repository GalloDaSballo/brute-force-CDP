from random import random
from math import exp


## CSV
import csv
import os
import time

## Visualization / Formatting
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

INTEREST = 200 # 2% Yearly
MAX_BPS = 10_000
TIME = 60 * 60 * 24 * 365.25 ## Interest compounded each second

RUNS = 10000

MAX_PRINCIPAL = 10_000
MAX_DEBT = 10_000
## Price ratio
RATIO = 13

def to_csv(headers, entries):
    # Create a file with current time as name
    os.makedirs('sims/', exist_ok=True)
    filename = f'sims/{pd.Timestamp.now()}.csv'

    with open(filename, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(headers)

        # write the data
        for entry in entries:
            writer.writerow([entry[0], entry[1], entry[2]])

def main():
  print("INTEREST", INTEREST)
  print("MAX_BPS", MAX_BPS)
  print("TIME", TIME)

  headers = [
    "Debt Start",
    "Debt End",
    "Time Duration",
  ]

  entries = []

  inital_principal = random() * MAX_PRINCIPAL
  initial_debt = random() * MAX_PRINCIPAL
  
  run = 0
  found = 0

  while run < RUNS:
    principal = random() * MAX_PRINCIPAL
    debt = principal * RATIO

    ## Skip, only go for those that are below the initial
    if(debt > initial_debt):
      continue

    ## Up to 1 year
    elapsed = random() * TIME

    print("elapsed", elapsed)
    multiplier = exp(elapsed * INTEREST / MAX_BPS / TIME)

    new_debt = debt * multiplier

    print("multiplier", multiplier)

    # entries.append([debt, new_debt, elapsed])
    if(new_debt > initial_debt):
      print("")
      print("")
      print("initial_debt", initial_debt)
      print("debt", debt)
      print("elapsed", elapsed)
      print("multiplier", multiplier)
      
      found += 1

    run += 1

  print("Total Found", found)
  print("Total RUNS", RUNS)
  
  # to_csv(headers, entries)
