import numpy as np
import copy

class Monkey():
  def __init__(self,raw):
    split = raw.split(': ')
    self.name = split[0]
    op = split[1].split(' ')
    if len(op) == 1:
      self.value = int(op[0])
    else:
      self.value = None
      self.l = op[0]
      self.op = op[1]
      self.r = op[2]
  

  def getValue(self, monkeys):
    if not self.value == None:
      return self.value
    if self.op == "*":
      return monkeys[self.l].getValue(monkeys) * monkeys[self.r].getValue(monkeys)
    if self.op == "+":
      return monkeys[self.l].getValue(monkeys) + monkeys[self.r].getValue(monkeys)
    if self.op == "-":
      return monkeys[self.l].getValue(monkeys) - monkeys[self.r].getValue(monkeys)
    if self.op == "/":
      return monkeys[self.l].getValue(monkeys) / monkeys[self.r].getValue(monkeys)
    if self.op == "=":
      return monkeys[self.l].getValue(monkeys) == monkeys[self.r].getValue(monkeys)
    
    

if __name__ == "__main__":
  with open("day21.txt") as f:
    data = [x for x in f.read().split('\n') if x]
  monkeys = {}
  for line in data:
    newmonkey = Monkey(line)
    monkeys[newmonkey.name] = newmonkey

  sol1 = monkeys['root'].getValue(monkeys)
  
  monkeys['root'].op = "="

  minval = 0
  maxval = 2**63
  monkeys['humn'].value = minval
  mincheck = monkeys[monkeys['root'].l].getValue(monkeys)-monkeys[monkeys['root'].r].getValue(monkeys)
  monkeys['humn'].value = maxval
  maxcheck = monkeys[monkeys['root'].l].getValue(monkeys)-monkeys[monkeys['root'].r].getValue(monkeys)
  while not monkeys['root'].getValue(monkeys):
    checkval = (minval + maxval)/2
    monkeys['humn'].value = checkval
    curcheck = monkeys[monkeys['root'].l].getValue(monkeys)-monkeys[monkeys['root'].r].getValue(monkeys)
    if mincheck > 0 and curcheck < 0:
      maxval = checkval
      maxcheck = curcheck
    elif mincheck < 0 and curcheck > 0:
      maxval = checkval
      maxcheck = curcheck
    elif maxcheck > 0 and curcheck < 0:
      minval = checkval
      mincheck = curcheck
    elif maxcheck < 0 and curcheck > 0:
      minval = checkval
      mincheck = curcheck

  sol2 = checkval
    
  print("Solution 1: ", sol1)
  print("Solution 2: ", sol2)
          
