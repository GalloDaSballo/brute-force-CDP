from random import random

PLCR = 103

## Change this according to MAX_LTV
MIN_CR = 125

RUNS = 10_000

## Change to w/e later
PRICE = 1

MAX_COLLATERAL = 10_000

## 125 is max ICR with 80%
MAX_LTV = 80

ONE_HUNDRED = 100

## Liquidate 50% for now
PARTIAL_LIQUIDATION_SIZE = 50

def main():  
  run = 0
  found = 0

  while run < RUNS:
    collateral = random() * MAX_COLLATERAL
    print("collateral", collateral)

    underwater_percent = random() * (ONE_HUNDRED - MAX_LTV)
    print("underwater_percent", underwater_percent)

    debt = PRICE * collateral * (MAX_LTV + underwater_percent) / ONE_HUNDRED

    print("debt", debt)

    ICR = collateral * PRICE / debt * 100
    print("ICR", ICR)


    print("Liquidate")
    debt_we_repay = PARTIAL_LIQUIDATION_SIZE * collateral / ONE_HUNDRED
    collateral_with_bonus = debt_we_repay * PRICE * PLCR / ONE_HUNDRED

    print("debt_we_repay", debt_we_repay)
    print("collateral_with_bonus", collateral_with_bonus)

    NEW_ICR = (collateral - collateral_with_bonus) * PRICE / (debt - debt_we_repay) * ONE_HUNDRED

    print("NEW_ICR", NEW_ICR)
    assert(NEW_ICR >= MIN_CR)

    run += 1
