import numpy as np
import copy

def get_valid_bot_choices(bots):
  out = [1,1,0,0]
  if bots[1] > 0:
    out[2] = 1
  if bots[2] > 0:
    out[3] = 1
  return out

def findmaxgeodes(blueprint,bots,max_bots,resources,time_left,num_geodes,checked):
  if (tuple(bots), tuple(resources), time_left) in checked:
    return checked[(tuple(bots),tuple(resources),time_left)]+num_geodes
  if time_left <= 0:
    return num_geodes
  if time_left == 1:
    checked[(tuple(bots),tuple(resources),time_left)] = bots[-1]
    return num_geodes + bots[-1]
  if time_left == 2:
    if np.all(resources >= blueprint[3]):
      checked[(tuple(bots),tuple(resources),time_left)] = 2*bots[-1] + 1
      return num_geodes + 2*bots[-1] + 1
    else:
      checked[(tuple(bots),tuple(resources),time_left)] = 2*bots[-1]
      return num_geodes + 2*bots[-1]
      
  bot_opts = get_valid_bot_choices(bots)
  maxval = 0
  for i, bot_opt in enumerate(bot_opts):
    if not bot_opt:
      continue
    if i < 3 and bots[i] == max_bots[i]:
      continue
    new_resources = copy.deepcopy(resources)
    new_geodes = 0
    new_time = time_left
    while np.any(new_resources < blueprint[i]):
      new_resources += bots[0:-1]
      new_geodes += bots[-1]
      new_time -= 1
      if new_time <= 0:
        break
    if new_time > 0:
      new_resources -= blueprint[i]
      new_resources += bots[0:-1]
      new_geodes += bots[-1]
      new_bots = copy.deepcopy(bots)
      new_bots[i] += 1
      new_time -= 1
      new_geodes = findmaxgeodes(blueprint,new_bots,max_bots,new_resources,new_time,new_geodes,checked)
    if new_geodes > maxval:
      maxval = new_geodes
  checked[(tuple(bots),tuple(resources),time_left)] = maxval
  return maxval + num_geodes

  

if __name__ == "__main__":
  with open("day19.txt") as f:
    data = [x for x in f.read().split('\n') if x]
  blueprints = {}
  for line in data:
    raw = line.split(' ')
    blueprints[int(raw[1][:-1])] = np.array([[int(raw[6]),0,0],[int(raw[12]),0,0],[int(raw[18]),int(raw[21]),0],[int(raw[27]),0,int(raw[30])]])
  maxtime = 24
  maxgeodes = 0
  sol1 = 0
  for blueprint in blueprints:
    max_bots = np.max(blueprints[blueprint],axis=0)
    num_geodes = 0
    num_bots = [1,0,0,0]
    resources = np.array([0,0,0])
    checked = {}
    num_geodes = findmaxgeodes(blueprints[blueprint],num_bots,max_bots,resources,maxtime,num_geodes,checked)
    sol1 += num_geodes * blueprint

  sol2 = 1
  maxtime = 32
  for blueprint in range(1,4):
    max_bots = np.max(blueprints[blueprint],axis=0)
    num_geodes = 0
    num_bots = [1,0,0,0]
    resources = np.array([0,0,0])
    checked = {}
    num_geodes = findmaxgeodes(blueprints[blueprint],num_bots,max_bots,resources,maxtime,num_geodes,checked)
    sol2 *= num_geodes


  print("Solution 1: ", sol1)
  print("Solution 2: ", sol2)
          
