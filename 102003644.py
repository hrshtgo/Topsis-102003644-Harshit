import sys
import pandas
import numpy
if __name__=='__main__':
  if len(sys.argv)!=5:
    sys.exit('Error: Incorrect number of parameters')
  try:
    df=pandas.DataFrame(pandas.read_csv(sys.argv[1])).copy(deep=False)
  except (FileNotFoundError, IOError):
    sys.exit('Error: File not Found')  
  try:
    weight=list(map(float,sys.argv[2].split(',')))
    impact=list(map(str,sys.argv[3].split(',')))
  except:
    sys.exit('Error: Please provide correct inputs. Impacts and weights must be separated by comma')
  c=len(df.axes[1])
  for i in range(1,c):
    if pandas.api.types.is_numeric_dtype(df.iloc[:,i])==False:
      sys.exit('Error: 2nd to last columns must contain numeric values only') 
  if c<=3:
    sys.exit('Error: Input file must contain three or more columns')
  if c-1!=len(weight) or c-1!=len(impact):
    sys.exit('Error: Number of weights, number of impacts and number of columns(from 2nd to last columns) must be the same')
  for i in impact:
    if i!='+' and i!='-':
      sys.exit('Error: Impacts must be either +ve or -ve') 
  for j in range(1,c):
    t=0
    for i in range(len(df)):
      t+=df.iloc[i,j]**2
    t**=0.5
    for i in range(len(df)):
      df.iloc[i,j]=(df.iloc[i,j]/t)*weight[j-1]
  best=df.max().values[1:]
  worst=df.min().values[1:]
  for i in range(0,c-1):
    if impact[i]=='-':
      t=best[i]
      best[i]=worst[i]
      worst[i]=t
  top=numpy.zeros(len(df))
  for i in range(len(df)):
    t1=0
    t2=0
    for j in range(1,c):
      t1+=(df.iloc[i,j]-best[j-1])**2
      t2+=(df.iloc[i,j]-worst[j-1])**2
    top[i]=t2**0.5/(t2**0.5+t1**0.5)
  data=pandas.read_csv(sys.argv[1])
  data['Topsis Score']=top
  data['Rank']=data['Topsis Score'].rank(method='max',ascending=False)
  try:
    data.to_csv(sys.argv[4],index=False)
  except:
    sys.exit('Incorrect file name')