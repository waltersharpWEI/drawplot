
import matplotlib.pyplot as plt
import os
import sys
import matplotlib
import numpy as np
import pandas as pd
import re


def parseData(logPath=None):
  dataset = []
  sigma = []
  iter = []
  time = []
  seed = []
  numlabel = []
  target_accuracy = []
  with open(logPath,'rt') as f:
    for line in f:
      if re.match(r"^Dataset",line):
        dsi = line.split()[-1]
        dataset = np.append(dataset,re.search(r"^[a-z]+[0-9]+",dsi).group(0))
        seed = np.append(seed,re.search(r"\.[0-9]",dsi).group(0).strip('.'))
        numlabel = np.append(numlabel,re.search(r"\@[0-9]+",dsi).group(0).strip('@'))
      if re.match(r"^targetAccuracy",line):
        target_accuracy = np.append(target_accuracy,line.split("=")[-1].strip('\n'))
      if re.match(r"^sigma",line):
        sigma = np.append(sigma,line.split("=")[-1].strip('\n'))
      if re.match(r"^iter",line):
        iter = np.append(iter,line.split("=")[-1].strip('\n'))
      if re.match(r"^time",line):
        time = np.append(time,line.split("=")[-1].strip('\n')) 
#  print(target_accuracy,dataset,sigma,iter,time,seed,numlabel)
  frame = {
    'dataset':dataset,
    'target_accuracy':target_accuracy,
    'seed':seed,
    'numlabel':numlabel,
    'time':time,
    'iter':iter,
    'sigma':sigma
  }
  df = pd.DataFrame(frame)
  return df

def processData(df):
  df['sigma']=df['sigma'].astype('int32')
  df['iter']=df['iter'].astype('int64')
  df['time']=df['time'].astype('float')
  df['numlabel']=df['numlabel'].astype('int32')
  df['seed']=df['seed'].astype('int32')
  df['target_accuracy']=df['target_accuracy'].astype('float')
  return df

def drawFig(df,yx):
  # Data for plotting
  df1 = df[df['target_accuracy'] == 0.40]
  df2 = df[df['target_accuracy'] == 0.45]
  print(df1)
  print(df2)

  df1 = df1.groupby('sigma').mean()
  df2 = df2.groupby('sigma').mean()

  t1 = df1.index
  t1 = np.log2(t1)
  s1 = df1[yx]
  
  t2 = df2.index
  t2 = np.log2(t2)
  s2 = df2[yx]
  
  fig, ax = plt.subplots()
  l1, = ax.plot(t1, s1)
  l2, = ax.plot(t2, s2)
  le1 = ax.legend([l2, l1], ["target accuracy 0.45", "target accuracy 0.40"], loc='upper right')
  
  ax.set(xlabel='log2(sigma)', ylabel='second (s)',
         title='sigma ' + yx + ' curve')
  ax.grid()
  plt.gca().add_artist(le1)
  
  fig.savefig("test.png")
  plt.show()
  
df=parseData(sys.argv[1])
#print(df)
df=processData(df)
#print(df)
drawFig(df,'time')
#drawFig(df,'iter')

