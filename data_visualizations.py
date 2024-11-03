
# Copyright (c) 2022 Michael Neill Hartman. All rights reserved.
# mnh_license@proton.me
# https://github.com/hartmanm

# data_visualizations.py

import numpy as np
import json
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import pandas as pd
import math
import time

generate=6
# select from 0 - 6 to generate different visualizations
# 0  cdf of zebra movement speed
# 1  scatterplot xaxis='location_x' yaxis='location_y'
# 2  scatterplot xaxis='timestamp' yaxis='location_y'
# 3  scatterplot xaxis='timestamp' yaxis='location_x'
# 4  zebras scatterplot xaxis='location_x' yaxis='location_y' zaxis='timestamp'
# 5  scatterplot xaxis='temperature' yaxis='timestamp'
# 6  zebras vs lions vs elephants scatterplot xaxis='location_x' yaxis='location_y' zaxis='timestamp'

# code from https://janakiev.com/blog/gps-points-distance-python/
def haversine(coord1, coord2):
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))
# code from https://janakiev.com/blog/gps-points-distance-python/

# import data
# import zebras
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_18?raw=true"
d1 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_19?raw=true"
d2 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_20?raw=true"
d3 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_21?raw=true"
d4 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_22?raw=true"
d5 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_23?raw=true"
d6 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_24?raw=true"
d7 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_25?raw=true"
d8 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_26?raw=true"
d9 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_27?raw=true"
d10 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_28?raw=true"
d11 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_29?raw=true"
d12 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_30?raw=true"
d13 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_31?raw=true"
d14 = pd.read_csv(dataset_url)
dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Zebra/animal_32?raw=true"
d15 = pd.read_csv(dataset_url)

if generate == 6:
   # import elephants and lions data
   # import elephants
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Elephant/animal_0?raw=true"
   e1 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Elephant/animal_1?raw=true"
   e2 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Elephant/animal_2?raw=true"
   e3 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Elephant/animal_3?raw=true"
   e4 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Elephant/animal_4?raw=true"
   e5 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Elephant/animal_5?raw=true"
   e6 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Elephant/animal_6?raw=true"
   e7 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Elephant/animal_7?raw=true"
   e8 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Elephant/animal_8?raw=true"
   e9 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Elephant/animal_9?raw=true"
   e10 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Elephant/animal_10?raw=true"
   e11 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Elephant/animal_11?raw=true"
   e12 = pd.read_csv(dataset_url)
   # import lions
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Lion/animal_12?raw=true"
   l1 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Lion/animal_13?raw=true"
   l2 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Lion/animal_14?raw=true"
   l3 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Lion/animal_15?raw=true"
   l4 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Lion/animal_16?raw=true"
   l5 = pd.read_csv(dataset_url)
   dataset_url = "https://github.com/mnhuoi/data/blob/main/generated_Lion/animal_17?raw=true"
   l6 = pd.read_csv(dataset_url)

if generate == 0:
   # generate cdf for all zebras 
   #timestamp,temperature,distance,location_x,location_y,bpm
   #70.96,30.12812,6.054238,678.4766,411.9266,60
   cdf_items=[]
   zebra_list=d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15
   for zebra in zebra_list:
      print("zebra "+str(zebra))
      #time.sleep(2)
      dfv=zebra
      df_timestamp = dfv['timestamp']
      dft_count=df_timestamp.count()
      df_location_x = dfv['location_x']
      dflx_count=df_location_x.count()
      df_location_y = dfv['location_y']
      dfly_count=df_location_y.count()

      if dft_count != dflx_count and dft_count != dfly_count:
         print("error index counts differ") 
         exit
      if dft_count % 2 != 0:
         dft_count-=1
      print("dft_count "+str(dft_count))

      dft_count-=2
      for i in range(dft_count):
         #print("i "+str(i))
         coord1=df_location_x[i],df_location_y[i]
         timestamp1=df_timestamp[i]
         coord2=df_location_x[i+1],df_location_y[i+1]
         timestamp2=df_timestamp[i+1]
         #print("haversine ")
         hav_item=haversine(coord1,coord2)
         delta_time=timestamp2-timestamp1
         if delta_time > 0:
            speed=hav_item/delta_time
            cdf_items.append(speed)
         #print("cdf_items "+str(cdf_items))

   # code modified from https://www.geeksforgeeks.org/how-to-calculate-and-plot-a-cumulative-distribution-function-with-matplotlib-in-python/
   N = len(cdf_items)
   count, bins_count = np.histogram(cdf_items, bins=10)
   pdf = count / sum(count)
   cdf = np.cumsum(pdf)
   plt.plot(bins_count[1:], cdf, label="CDF")
   plt.legend()
   plt.show()
   # code modified from https://www.geeksforgeeks.org/how-to-calculate-and-plot-a-cumulative-distribution-function-with-matplotlib-in-python/

if generate == 1:
   xaxis='location_x'
   yaxis='location_y'
   ax = plt.gca()
   color_list=[]
   color = iter(cm.rainbow(np.linspace(0, 1, 15)))
   for i in range(15):
      c = next(color)
      color_list.append(c)
   d1.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[0],ax=ax,label="zebra1")
   d2.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[9],ax=ax,label="zebra2")
   d3.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[1],ax=ax,label="zebra3")
   d4.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[10],ax=ax,label="zebra4")
   d5.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[2],ax=ax,label="zebra5")
   d6.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[11],ax=ax,label="zebra6")
   d7.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[3],ax=ax,label="zebra7")
   d8.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[12],ax=ax,label="zebra8")
   d9.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[4],ax=ax,label="zebra9")
   d10.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[13],ax=ax,label="zebra10")
   d11.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[5],ax=ax,label="zebra11")
   d12.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[14],ax=ax,label="zebra12")
   d13.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[6],ax=ax,label="zebra13")
   d14.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[7],ax=ax,label="zebra14")
   d15.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[8],ax=ax,label="zebra15")
   fig = plt.gcf()
   fig.set_size_inches(18.5, 13)
   plt.ylabel(yaxis)
   plt.xlabel(xaxis)
   plt.legend(loc="upper right")
   plt.show()

if generate == 2:
   xaxis='timestamp'
   yaxis='location_y'
   ax = plt.gca()
   color_list=[]
   color = iter(cm.rainbow(np.linspace(0, 1, 15)))
   for i in range(15):
      c = next(color)
      color_list.append(c)
   d1.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[0],ax=ax,label="zebra1")
   d2.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[9],ax=ax,label="zebra2")
   d3.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[1],ax=ax,label="zebra3")
   d4.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[10],ax=ax,label="zebra4")
   d5.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[2],ax=ax,label="zebra5")
   d6.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[11],ax=ax,label="zebra6")
   d7.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[3],ax=ax,label="zebra7")
   d8.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[12],ax=ax,label="zebra8")
   d9.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[4],ax=ax,label="zebra9")
   d10.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[13],ax=ax,label="zebra10")
   d11.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[5],ax=ax,label="zebra11")
   d12.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[14],ax=ax,label="zebra12")
   d13.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[6],ax=ax,label="zebra13")
   d14.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[7],ax=ax,label="zebra14")
   d15.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[8],ax=ax,label="zebra15")
   fig = plt.gcf()
   fig.set_size_inches(18.5, 13)
   plt.ylabel(yaxis)
   plt.xlabel(xaxis)
   plt.legend(loc="upper right")
   plt.show()

if generate == 3:
   xaxis='timestamp'
   yaxis='location_x'
   ax = plt.gca()
   color_list=[]
   color = iter(cm.rainbow(np.linspace(0, 1, 15)))
   for i in range(15):
      c = next(color)
      color_list.append(c)
   d1.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[0],ax=ax,label="zebra1")
   d2.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[9],ax=ax,label="zebra2")
   d3.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[1],ax=ax,label="zebra3")
   d4.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[10],ax=ax,label="zebra4")
   d5.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[2],ax=ax,label="zebra5")
   d6.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[11],ax=ax,label="zebra6")
   d7.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[3],ax=ax,label="zebra7")
   d8.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[12],ax=ax,label="zebra8")
   d9.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[4],ax=ax,label="zebra9")
   d10.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[13],ax=ax,label="zebra10")
   d11.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[5],ax=ax,label="zebra11")
   d12.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[14],ax=ax,label="zebra12")
   d13.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[6],ax=ax,label="zebra13")
   d14.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[7],ax=ax,label="zebra14")
   d15.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[8],ax=ax,label="zebra15")
   fig = plt.gcf()
   fig.set_size_inches(18.5, 13)
   plt.ylabel(yaxis)
   plt.xlabel(xaxis)
   plt.legend(loc="upper right")
   plt.show()

if generate == 4:
   xaxis='location_x'
   yaxis='location_y'
   zaxis='timestamp'

   fig = plt.figure()
   fig.set_size_inches(20,20)
   #ax = fig.add_subplot(111, projection='3d')
   ax = fig.add_subplot(projection='3d')

   the_linewidth=0.01

   dfv=d1
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra1",linewidth=the_linewidth)
   dfv=d2
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra2",linewidth=the_linewidth)
   dfv=d3
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra3",linewidth=the_linewidth)
   dfv=d4
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra4",linewidth=the_linewidth)
   dfv=d5
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra5",linewidth=the_linewidth)
   dfv=d6
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra6",linewidth=the_linewidth)
   dfv=d7
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra7",linewidth=the_linewidth)
   dfv=d8
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra8",linewidth=the_linewidth)
   dfv=d9
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra9",linewidth=the_linewidth)
   dfv=d10
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra10",linewidth=the_linewidth)
   dfv=d11
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra11",linewidth=the_linewidth)
   dfv=d12
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra12",linewidth=the_linewidth)
   dfv=d13
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra13",linewidth=the_linewidth)
   dfv=d14
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra14",linewidth=the_linewidth)
   dfv=d15
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra15",linewidth=the_linewidth)
   ax.set_xlabel(xaxis)
   ax.set_ylabel(yaxis)
   ax.set_zlabel(zaxis)
   ax.legend()
   plt.show()

if generate == 5:
   #timestamp,temperature,distance,location_x,location_y,bpm
   xaxis='temperature'
   yaxis='timestamp'
   ax = plt.gca()
   color_list=[]
   color = iter(cm.rainbow(np.linspace(0, 1, 15)))
   for i in range(15):
      c = next(color)
      color_list.append(c)
   d1.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[0],ax=ax,label="zebra1")
   d2.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[9],ax=ax,label="zebra2")
   d3.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[1],ax=ax,label="zebra3")
   d4.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[10],ax=ax,label="zebra4")
   d5.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[2],ax=ax,label="zebra5")
   d6.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[11],ax=ax,label="zebra6")
   d7.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[3],ax=ax,label="zebra7")
   d8.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[12],ax=ax,label="zebra8")
   d9.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[4],ax=ax,label="zebra9")
   d10.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[13],ax=ax,label="zebra10")
   d11.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[5],ax=ax,label="zebra11")
   d12.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[14],ax=ax,label="zebra12")
   d13.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[6],ax=ax,label="zebra13")
   d14.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[7],ax=ax,label="zebra14")
   d15.plot(kind='scatter',x=xaxis,y=yaxis,color=color_list[8],ax=ax,label="zebra15")
   fig = plt.gcf()
   fig.set_size_inches(18.5, 13)
   plt.ylabel(yaxis)
   plt.xlabel(xaxis)
   plt.legend(loc="upper right")
   plt.show()

if generate == 6:
   xaxis='location_x'
   yaxis='location_y'
   zaxis='timestamp'

   fig = plt.figure()
   fig.set_size_inches(20,20)
   ax = fig.add_subplot(projection='3d')

   the_linewidth=0.01

   color_list=[]
   color = iter(cm.rainbow(np.linspace(0, 1, 15)))
   for i in range(15):
      c = next(color)
      color_list.append(c)

   zebra_list=d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15
   elephant_list=e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12
   lion_list=l1,l2,l3,l4,l5,l6
   iterator=1
   for zebra in zebra_list:
      dfv=zebra
      y = dfv[yaxis]
      x = dfv[xaxis]
      z = dfv[zaxis]
      ax.scatter(x,y,z,label="zebra"+str(iterator),linewidth=the_linewidth,color=color_list[0]) 
      iterator+=1
   iterator=1
   for elephant in elephant_list:
      dfv=elephant
      y = dfv[yaxis]
      x = dfv[xaxis]
      z = dfv[zaxis]
      ax.scatter(x,y,z,label="elephant"+str(iterator),linewidth=the_linewidth,color=color_list[7]) 
      iterator+=1
   iterator=1
   for lion in lion_list:
      dfv=elephant
      y = dfv[yaxis]
      x = dfv[xaxis]
      z = dfv[zaxis]
      ax.scatter(x,y,z,label="lion"+str(iterator),linewidth=the_linewidth,color=color_list[14]) 
      iterator+=1

   ax.set_xlabel(xaxis)
   ax.set_ylabel(yaxis)
   ax.set_zlabel(zaxis)
   ax.legend()
   plt.show()

"""


#from mpl_toolkits.mplot3d import Axes3D
max0=d0.loc[d0['CO2'].idxmax()]
max1=d1.loc[d1['CO2'].idxmax()]
max2=d2.loc[d2['CO2'].idxmax()]
max3=d3.loc[d3['CO2'].idxmax()]
max4=d4.loc[d4['CO2'].idxmax()]

legend_string='CO2_maxes\n\n'+"         "+'car0: '+str(max0['CO2'])+"         "+'car1: '+str(max1['CO2'])+"         "+'car2: '+str(max2['CO2'])+"         "+'car3: '+str(max3['CO2'])+"         "+'car4: '+str(max4['CO2'])
data = {'zebra': ['zebra1','zebra2','zebra3','zebra4','zebra5','zebra6','zebra7','zebra8','zebra9','zebra10','zebra11','zebra12','zebra13','zebra14','zebra15'],
        'CO2_max': [max0['CO2'],max1['CO2'],max2['CO2'],max3['CO2'],max4['CO2']]}
all_cars = pd.DataFrame(data)
all_cars = all_cars.reset_index()
all_cars.plot(kind='bar',x='zebra',y='CO2_max',label=legend_string)
fig = plt.gcf()
fig.set_size_inches(18.5, 13)
plt.ylabel('CO2_max')
plt.xlabel('car')
plt.legend(loc="upper center", prop={'size': 22})
plt.show()

## scatter plot all data
dataset = "d0"
dataset_url = client.get_dataset_content(datasetName = dataset)['entries'][0]['dataURI']
d0 = pd.read_csv(dataset_url)

dataset = "d1"
dataset_url = client.get_dataset_content(datasetName = dataset)['entries'][0]['dataURI']
d1 = pd.read_csv(dataset_url)

dataset = "d2"
dataset_url = client.get_dataset_content(datasetName = dataset)['entries'][0]['dataURI']
d2 = pd.read_csv(dataset_url)

dataset = "d3"
dataset_url = client.get_dataset_content(datasetName = dataset)['entries'][0]['dataURI']
d3 = pd.read_csv(dataset_url)

dataset = "d4"
dataset_url = client.get_dataset_content(datasetName = dataset)['entries'][0]['dataURI']
d4 = pd.read_csv(dataset_url)

d0 = d0.rename(columns = {'CO2':'car0'})
d1 = d1.rename(columns = {'CO2':'car1'})
d2 = d2.rename(columns = {'CO2':'car2'})
d3 = d3.rename(columns = {'CO2':'car3'})
d4 = d4.rename(columns = {'CO2':'car4'})

frames = [d0,d1,d2,d3,d4]
  
all_cars = pd.concat(frames)
all_cars.reset_index(inplace=True)

ax = plt.gca()
all_cars.plot(kind='scatter',x='index',y='car0',color='red',ax=ax,label="car0")
all_cars.plot(kind='scatter',x='index',y='car1',color='blue',ax=ax,label="car1")
all_cars.plot(kind='scatter',x='index',y='car2',color='green',ax=ax,label="car2")
all_cars.plot(kind='scatter',x='index',y='car3',color='yellow',ax=ax,label="car3")
all_cars.plot(kind='scatter',x='index',y='car4',color='orange',ax=ax,label="car4")
fig = plt.gcf()
fig.set_size_inches(18.5, 13)
plt.ylabel('CO2')
plt.xlabel('sample number')
plt.legend(loc="upper right")
plt.show()
"""


"""

d0 = d0.rename(columns = {'CO2':'car0'})
d1 = d1.rename(columns = {'CO2':'car1'})
d2 = d2.rename(columns = {'CO2':'car2'})
d3 = d3.rename(columns = {'CO2':'car3'})
d4 = d4.rename(columns = {'CO2':'car4'})


frames = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15]

#all_zebras = pd.concat(frames)
#all_zebras.reset_index(inplace=True)
#'zebra': ['zebra1','zebra2','zebra3','zebra4','zebra5','zebra6','zebra7','zebra8','zebra9','zebra10','zebra11','zebra12','zebra13','zebra14','zebra15'],
       

ax = plt.gca()
#d0.plot(kind='scatter',x='location_x',y='location_y',z='timestamp',color='red',ax=ax,label="zebra1")

color_list=[]
color = iter(cm.rainbow(np.linspace(0, 1, 15)))
for i in range(15):
   c = next(color)
   color_list.append(c)
d1.plot(kind='scatter',x='location_x',y='location_y',color=color_list[0],ax=ax,label="zebra1")
d2.plot(kind='scatter',x='location_x',y='location_y',color=color_list[9],ax=ax,label="zebra2")
d3.plot(kind='scatter',x='location_x',y='location_y',color=color_list[1],ax=ax,label="zebra3")
d4.plot(kind='scatter',x='location_x',y='location_y',color=color_list[10],ax=ax,label="zebra4")
d5.plot(kind='scatter',x='location_x',y='location_y',color=color_list[2],ax=ax,label="zebra5")
d6.plot(kind='scatter',x='location_x',y='location_y',color=color_list[11],ax=ax,label="zebra6")
d7.plot(kind='scatter',x='location_x',y='location_y',color=color_list[3],ax=ax,label="zebra7")
d8.plot(kind='scatter',x='location_x',y='location_y',color=color_list[12],ax=ax,label="zebra8")
d9.plot(kind='scatter',x='location_x',y='location_y',color=color_list[4],ax=ax,label="zebra9")
d10.plot(kind='scatter',x='location_x',y='location_y',color=color_list[13],ax=ax,label="zebra10")
d11.plot(kind='scatter',x='location_x',y='location_y',color=color_list[5],ax=ax,label="zebra11")
d12.plot(kind='scatter',x='location_x',y='location_y',color=color_list[14],ax=ax,label="zebra12")
d13.plot(kind='scatter',x='location_x',y='location_y',color=color_list[6],ax=ax,label="zebra13")
d14.plot(kind='scatter',x='location_x',y='location_y',color=color_list[7],ax=ax,label="zebra14")
d15.plot(kind='scatter',x='location_x',y='location_y',color=color_list[8],ax=ax,label="zebra15")
#all_cars.plot(kind='scatter',x='index',y='car1',color='blue',ax=ax,label="car1")

fig = plt.gcf()
fig.set_size_inches(18.5, 13)
plt.ylabel('location_y')
plt.xlabel('location_x')
#plt.zlabel('timestamp')
plt.legend(loc="upper right")
plt.show()










if generate == 6:
   xaxis='distance'
   yaxis='distance'
   zaxis='timestamp'

   fig = plt.figure()
   fig.set_size_inches(20,20)
   #ax = fig.add_subplot(111, projection='3d')
   ax = fig.add_subplot(projection='3d')

   the_linewidth=0.01

   dfv=d1
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra1",linewidth=the_linewidth) 
   dfv=d2
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra2",linewidth=the_linewidth)
   dfv=d3
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra3",linewidth=the_linewidth)
   dfv=d4
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra4",linewidth=the_linewidth)
   dfv=d5
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra5",linewidth=the_linewidth)
   dfv=d6
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra6",linewidth=the_linewidth)
   dfv=d7
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra7",linewidth=the_linewidth)
   dfv=d8
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra8",linewidth=the_linewidth)
   dfv=d9
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra9",linewidth=the_linewidth)
   dfv=d10
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra10",linewidth=the_linewidth)
   dfv=d11
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra11",linewidth=the_linewidth)
   dfv=d12
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra12",linewidth=the_linewidth)
   dfv=d13
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra13",linewidth=the_linewidth)
   dfv=d14
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra14",linewidth=the_linewidth)
   dfv=d15
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra15",linewidth=the_linewidth)
   ax.set_xlabel(xaxis)
   ax.set_ylabel(yaxis)
   ax.set_zlabel(zaxis)
   ax.legend()
   plt.show()


      dfv=d2
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra2",linewidth=the_linewidth,color=color_list[0]) 
   dfv=d3
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra3",linewidth=the_linewidth,color=color_list[0]) 
   dfv=d4
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra4",linewidth=the_linewidth,color=color_list[0]) 
   dfv=d5
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra5",linewidth=the_linewidth,color=color_list[0]) 
   dfv=d6
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra6",linewidth=the_linewidth,color=color_list[0]) 
   dfv=d7
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra7",linewidth=the_linewidth,color=color_list[0]) 
   dfv=d8
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra8",linewidth=the_linewidth,color=color_list[0]) 
   dfv=d9
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra9",linewidth=the_linewidth,color=color_list[0]) 
   dfv=d10
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra10",linewidth=the_linewidth,color=color_list[0]) 
   dfv=d11
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra11",linewidth=the_linewidth,color=color_list[0]) 
   dfv=d12
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra12",linewidth=the_linewidth,color=color_list[0]) 
   dfv=d13
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra13",linewidth=the_linewidth,color=color_list[0]) 
   dfv=d14
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra14",linewidth=the_linewidth,color=color_list[0]) 
   dfv=d15
   y = dfv[yaxis]
   x = dfv[xaxis]
   z = dfv[zaxis]
   ax.scatter(x,y,z,label="zebra15",linewidth=the_linewidth,color=color_list[0]) 
"""
