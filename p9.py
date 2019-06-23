
import matplotlib.pyplot as plt
import os
import sys
import matplotlib
import numpy as np
import pandas as pd
from utils import parseData,processData

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

def main():
  df=parseData(sys.argv[1])
  #print(df)
  df=processData(df)
  #print(df)
  drawFig(df,'time')
  #drawFig(df,'iter')


if __name__ == "__main__":
    main()
