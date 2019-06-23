
import matplotlib.pyplot as plt
import sys
import matplotlib
import numpy as np
from utils import parseData,processData

def drawFig(df,yx):
  # Data for plotting
  fig, ax = plt.subplots()
  ls = []
  lab = []
  for name,group in df.groupby('target_accuracy'):
    print(group)
    df = group.groupby('sigma').mean()
    t = np.log2(df.index)
    s = df[yx]
    l, = ax.plot(t, s, marker='o')
    # to annotate
    #for ts in zip(t, s):
    #  ax.annotate("(%s,%s)" % ts, xy=ts, xytext=(-20, 10), textcoords='offset points')
    ls = np.append(ls,l,)
    lab = np.append(lab,name)    

  le1 = ax.legend(ls, lab , loc='upper right')
  
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
