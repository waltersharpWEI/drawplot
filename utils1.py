import re
import os
import sys
import numpy as np
import pandas as pd

def parseData(logPath=None):
  dataset = []
  sigma = []
  iter = []
  time = []
  seed = []
  numlabel = []
  accuracy = []
  timeBudget = []
  with open(logPath,'rt') as f:
    for line in f:
      if re.match(r"^Dataset",line):
        dsi = line.split()[-1]
        dataset = np.append(dataset,re.search(r"^[a-z]+[0-9]+",dsi).group(0))
        seed = np.append(seed,re.search(r"\.[0-9]",dsi).group(0).strip('.'))
        numlabel = np.append(numlabel,re.search(r"\@[0-9]+",dsi).group(0).strip('@'))
      if re.match(r"^accuracy",line):
        accuracy = np.append(accuracy,line.split("=")[-1].strip('\n'))
      if re.match(r"^sigma",line):
        sigma = np.append(sigma,line.split("=")[-1].strip('\n'))
      if re.match(r"^iter",line):
        iter = np.append(iter,line.split("=")[-1].strip('\n'))
      if re.match(r"^timeBudget",line):
        timeBudget = np.append(timeBudget,line.split("=")[-1].strip('\n'))
      elif re.match(r"^time",line):
        time = np.append(time,line.split("=")[-1].strip('\n')) 
  print(timeBudget.size,accuracy.size,dataset.size,sigma.size,iter.size,time.size,seed.size,numlabel.size)
  frame = {
    'dataset':dataset,
    'accuracy':accuracy,
    'seed':seed,
    'numlabel':numlabel,
    'time':time,
    'iter':iter,
    'sigma':sigma,
    'time_budget':timeBudget
  }
  df = pd.DataFrame(frame)
  return df

def processData(df):
  df['sigma']=df['sigma'].astype('int32')
  df['iter']=df['iter'].astype('int64')
  df['time']=df['time'].astype('float')
  df['numlabel']=df['numlabel'].astype('int32')
  df['seed']=df['seed'].astype('int32')
  df['accuracy']=df['accuracy'].astype('float')
  df['time_budget']=df['time_budget'].astype('int32')
  return df

def main():
  processData(parseData(sys.argv[1]))

if __name__ == "__main__":
  main()
