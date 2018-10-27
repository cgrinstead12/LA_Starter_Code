import requests #
from bs4 import BeautifulSoup as bs #
import pymongo #
import time #
from zipfile import ZipFile #
import os #
import time #
import shutil #
import pandas as pd
import numpy as np

from datetime import datetime as dt
from pymongo import MongoClient

def get_file(url, target_path):
  response = requests.get(url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
  handle = open(target_path, "wb")
  for chunk in response.iter_content(chunk_size=512):
      if chunk:  # filter out keep-alive new chunks
          handle.write(chunk)

def scrape_metro():
    scrape_location = "C:/Users/cgrinstead12/Desktop/Scrapes/"
    unzip_location = "C:/Users/cgrinstead12/Desktop/Unzipped/"
    url = "https://bikeshare.metro.net/about/data/"
    quarters = ['Q1 (January – March)',
            'Q2 (April – June)', 
            'Q3 (July – September)',
            'Q3 (Launch, July 7 – September)', 
            'Q4 (October – December)']
    years = [2020, 2019, 2018, 2017, 2016]

    try:
        shutil.rmtree("C:/Users/cgrinstead12/Desktop/Unzipped")  
    except:
        pass
    try:
        shutil.rmtree("C:/Users/cgrinstead12/Desktop/Scrapes") 
    except:
        pass
        
    try:    
        os.mkdir("C:/Users/cgrinstead12/Desktop/Unzipped")
        os.mkdir("C:/Users/cgrinstead12/Desktop/Scrapes")
    except:
        pass
   
    url2018q3 = 'https://bikeshare.metro.net/wp-content/uploads/2018/10/metro-bike-share-trips-2018-q3.csv.zip'
    url2018q2 = 'https://bikeshare.metro.net/wp-content/uploads/2018/08/metro-bike-share-trips-2018-q2.csv.zip'
    url2018q1 = 'https://bikeshare.metro.net/wp-content/uploads/2018/04/metro-bike-share-trips-2018-q1.csv.zip'
    url2017q4 = 'https://bikeshare.metro.net/wp-content/uploads/2018/02/metro-bike-share-trips-2017-q4-v2.csv.zip'
    url2017q3 = 'https://bikeshare.metro.net/wp-content/uploads/2016/10/metro-bike-share-trips-2017-q3.csv.zip'
    url2017q2 = 'https://bikeshare.metro.net/wp-content/uploads/2017/07/la_metro_gbfs_trips_Q2_2017.csv.zip'
    url2017q1 = 'https://bikeshare.metro.net/wp-content/uploads/2017/04/la_metro_gbfs_trips_Q1_2017.zip'
    url2016q4 = 'https://bikeshare.metro.net/wp-content/uploads/2018/09/metro-bike-share-trips-2016-q4.csv.zip'
    url2016q3 = 'https://bikeshare.metro.net/wp-content/uploads/2016/10/MetroBikeShare_2016_Q3_trips.zip'
    stationzip = 'https://bikeshare.metro.net/wp-content/uploads/2018/10/metro-bike-share-stations-2018-10-19.csv'

    zip2018q3 = 'metro-bike-share-trips-2018-q3.csv.zip'
    zip2018q2 = 'metro-bike-share-trips-2018-q2.csv.zip'
    zip2018q1 = 'metro-bike-share-trips-2018-q1.csv.zip'
    zip2017q4 = 'metro-bike-share-trips-2017-q4-v2.csv.zip'
    zip2017q3 = 'metro-bike-share-trips-2017-q3.csv.zip'
    zip2017q2 = 'la_metro_gbfs_trips_Q2_2017.csv.zip'
    zip2017q1 = 'la_metro_gbfs_trips_Q1_2017.zip'
    zip2016q4 = 'metro-bike-share-trips-2016-q4.csv.zip'
    zip2016q3 = 'MetroBikeShare_2016_Q3_trips.zip'
    statzipzip = 'metro-bike-share-stations-2018-10-19.csv'

    target_path_zip ='C:/Users/cgrinstead12/Desktop/Scrapes/'

    url_list = [url2018q3, url2018q2, url2018q1, url2017q4, url2017q3, url2017q2, url2017q1, url2016q4, url2016q3]
    zip_list = [zip2018q3, zip2018q2, zip2018q1, zip2017q4, zip2017q3, zip2017q2, zip2017q1, zip2016q4, zip2016q3]

    target_zip = []

    for zippy in zip_list:
        target_zip.append(target_path_zip + zippy)
        print(target_path_zip + zippy)

    for x in range(len(url_list)):
        get_file(url_list[x], target_zip[x])
    chromeBikes = []
    for year in years:
        for quarter in quarters:
            combined = str(year) + " " + str(quarter)
            chromeBikes.append(combined)  


    time.sleep(10)

    for filename in os.listdir(scrape_location):
        print(filename)
        zf = ZipFile(scrape_location + filename, 'r')
        zf.extractall(unzip_location)

    get_file(stationzip, target_path_zip + statzipzip)

    try:
        shutil.rmtree("C:/Users/cgrinstead12/Desktop/Unzipped/__MACOSX")
    except:
        pass
    
  

    bike_2018q1=pd.read_csv("C:/Users/cgrinstead12/Desktop/Unzipped/metro-bike-share-trips-2018-q1.csv")
    bike_2018q2=pd.read_csv("C:/Users/cgrinstead12/Desktop/Unzipped/metro-bike-share-trips-2018-q2.csv")
    bike_2018q3=pd.read_csv("C:/Users/cgrinstead12/Desktop/Unzipped/metro-bike-share-trips-2018-q3.csv")

    bike_2017q1=pd.read_csv("C:/Users/cgrinstead12/Desktop/Unzipped/la_metro_gbfs_trips_Q1_2017.csv").rename(columns={"start_station_id":"start_station","end_station_id":"end_station"})
    bike_2017q2=pd.read_csv("C:/Users/cgrinstead12/Desktop/Unzipped/la_metro_gbfs_trips_Q2_2017.csv")
    bike_2017q3=pd.read_csv("C:/Users/cgrinstead12/Desktop/Unzipped/metro-bike-share-trips-2017-q3.csv")
    bike_2017q4=pd.read_csv("C:/Users/cgrinstead12/Desktop/Unzipped/metro-bike-share-trips-2017-q4-v2.csv")

    bike_2017q1["start_time"]=pd.to_datetime(bike_2017q1["start_time"],format="%m/%d/%Y %H:%M")
    bike_2017q1["end_time"]=pd.to_datetime(bike_2017q1["end_time"],format="%m/%d/%Y %H:%M")
    bike_2017q3["start_time"]=pd.to_datetime(bike_2017q3["start_time"],format="%m/%d/%Y %H:%M")
    bike_2017q3["end_time"]=pd.to_datetime(bike_2017q3["end_time"],format="%m/%d/%Y %H:%M")

    bike_2016q3=pd.read_csv("C:/Users/cgrinstead12/Desktop/Unzipped/metro-bike-share-trips-2016-q4.csv")
    bike_2016q4=pd.read_csv("C:/Users/cgrinstead12/Desktop/Unzipped/MetroBikeShare_2016_Q3_trips.csv").rename(columns={"start_station_id":"start_station","end_station_id":"end_station"})

    bike_2016q4["start_time"]=pd.to_datetime(bike_2016q4["start_time"],format="%m/%d/%Y %H:%M")
    bike_2016q4["end_time"]=pd.to_datetime(bike_2016q4["end_time"],format="%m/%d/%Y %H:%M")


    bike_2018=pd.concat([bike_2018q1,bike_2018q2,bike_2018q3])
    bike_2017=pd.concat([bike_2017q1,bike_2017q2,bike_2017q3,bike_2017q4])
    bike_2016=pd.concat([bike_2016q3,bike_2016q4])
    bike_complete=pd.concat([bike_2018,bike_2017,bike_2016])


    bike_metadata=pd.read_csv("C:/Users/cgrinstead12/Desktop/Scrapes/metro-bike-share-stations-2018-10-19.csv")
    bike_metadata=bike_metadata.iloc[1:,]

    bike_metadata["Go_live_date"]=pd.to_datetime(bike_metadata["Go_live_date"],format="%m/%d/%Y")

    start_station=bike_metadata[["Station_ID","Station_Name","Region"]]
    start_station=start_station.rename(columns={"Station_ID":"start_station"})


    bike_location_start=bike_complete[["start_station","start_lat","start_lon"]].drop_duplicates(["start_station"])
    bike_location_end=bike_complete[["end_station","end_lat","end_lon"]].drop_duplicates(["end_station"])

    start_station=bike_metadata[["Station_ID","Station_Name","Region"]]
    start_station=start_station.rename(columns={"Station_ID":"start_station"})
    start_station=start_station.rename(columns={"Station_Name":"start_station_name"})

    end_station=bike_metadata[["Station_ID","Station_Name","Region"]]
    end_station=end_station.rename(columns={"Station_ID":"end_station"})
    end_station=end_station.rename(columns={"Station_Name":"end_station_name"})

    start_station.groupby(['Region']).count().sort_values(["start_station"], ascending=False)["start_station"]
    start_station=pd.merge(start_station,bike_location_start,on="start_station",how="inner")
    start_station.to_csv("start_station.csv", index=False, header=True)

    end_station.groupby(['Region']).count().sort_values(["end_station"], ascending=False)["end_station"]
    end_station=pd.merge(end_station,bike_location_end,on="end_station",how="inner")
    end_station.to_csv("end_station.csv", index=False, header=True)


    start_station.groupby(['Region']).count().sort_values(["start_station"], ascending=False)["start_station"]
    start_station=pd.merge(start_station,bike_location_start,on="start_station",how="inner")
    start_station.to_csv("start_station.csv", index=False, header=True)

    end_station.groupby(['Region']).count().sort_values(["end_station"], ascending=False)["end_station"]
    end_station=pd.merge(end_station,bike_location_end,on="end_station",how="inner")
    end_station.to_csv("end_station.csv", index=False, header=True)

    station_region=start_station[["start_station","start_station_name","Region"]]
    station_region2=end_station[["end_station","end_station_name"]]

    bike_complete=pd.merge(bike_complete,station_region,on="start_station")
    bike_complete=pd.merge(bike_complete,station_region2,on="end_station")

    bike_complete["start_time"]=pd.to_datetime(bike_complete["start_time"])
    bike_complete["end_time"]=pd.to_datetime(bike_complete["end_time"])


    bike_complete["Day_Of_Week"]=bike_complete['start_time'].dt.weekday_name
    bike_complete["Day_Of_Week_Number"]=bike_complete['start_time'].dt.weekday

# Sort by Date
    bike_complete=bike_complete.sort_values(["start_time"], ascending=True)

# Create a new variable for Start-To-End Trip
    bike_complete["start_to_end"] = bike_complete["start_station"].astype(str)+"-"+bike_complete["end_station"].astype(str)
    bike_complete["start_to_end_name"] = bike_complete["start_station_name"]+" - "+bike_complete["end_station_name"]

# Sanity Check
    bike_complete.dtypes


# In[23]:


    bike_complete.to_csv("bike_complete.csv", index=False, header=True)


# In[24]:


    # Read Data
    bike_complete=pd.read_csv("bike_complete.csv")

# Change all start and end time to datetime datatype
    bike_complete["start_time"]=pd.to_datetime(bike_complete["start_time"])
    bike_complete["end_time"]=pd.to_datetime(bike_complete["end_time"])

#### Top 30 Popular Routes ####
    top_30_routes=bike_complete.groupby(
        ['start_to_end','start_to_end_name','Region',"start_lat","start_lon","end_lat","end_lon"]).count().sort_values(
                ["trip_id"],ascending=False)["trip_id"].reset_index()[0:30]

    top_30_routes.to_csv("top_30_routes.csv", index=False, header=True)



#### Pivot Table

# 00 Number of Bike Stations in Each Region
    bike_station_count=start_station.groupby(['Region']).count()["start_station"].reset_index()
    bike_station_count=bike_station_count.rename(columns={"start_station":"station_count"})
    bike_station_count.to_csv("bike_station_count", index=False, header=True)

# 1-1 By Day of Week
    day_of_week=bike_complete.groupby(['Day_Of_Week','Day_Of_Week_Number','Region']).count().sort_values(["trip_id"], ascending=False)["trip_id"].reset_index() #Edited Code
    day_of_week=day_of_week.rename(columns={"trip_id":"trip_count"})
    day_of_week=day_of_week.sort_values(["Day_Of_Week_Number","Region"], ascending=[True,True]) # New Code
    day_of_week.to_csv("day_of_week.csv", index=False, header=True)

# 1-2 By Day of Week (Normalized)

    day_of_week_normalized=pd.merge(day_of_week,bike_station_count,on="Region",how="inner")
    day_of_week_normalized["normalized_trip_count"]=day_of_week_normalized.trip_count/day_of_week_normalized.station_count
    day_of_week_normalized=day_of_week_normalized[["Day_Of_Week","Day_Of_Week_Number","Region","normalized_trip_count"]]
    day_of_week_normalized=day_of_week_normalized.sort_values(["Day_Of_Week_Number","Region"], ascending=[True,True])

    day_of_week_normalized.to_csv("day_of_week_normalized.csv", index=False, header=True)


# 2-1 By Passholder Type
    passholder_type=bike_complete.groupby(['passholder_type','Region']).count()["trip_id"].reset_index()
    passholder_type=passholder_type.rename(columns={"trip_id":"trip_count"})
    passholder_type=passholder_type.sort_values(["passholder_type","Region"], ascending=[False,True])

    passholder_type.to_csv("passholder_type.csv", index=False, header=True)

# 2-2 By Passholder Type (Normalized)

    passholder_type_normalized=pd.merge(passholder_type,bike_station_count,on="Region",how="inner")
    passholder_type_normalized["normalized_trip_count"]=passholder_type_normalized.trip_count/passholder_type_normalized.station_count
    passholder_type_normalized=passholder_type_normalized[["passholder_type","Region","normalized_trip_count"]]
    passholder_type_normalized=passholder_type_normalized.sort_values(["passholder_type","Region"], ascending=[False,True])

    passholder_type_normalized.to_csv("passholder_type_normalized.csv", index=False, header=True)


# 3-1 By Route Category
    route_category=bike_complete.groupby(['trip_route_category','Region']).count().sort_values(["trip_id"], ascending=False)["trip_id"].reset_index()
    route_category=route_category.rename(columns={"trip_id":"trip_count"})
    route_category=route_category.sort_values(["trip_route_category","Region"], ascending=[False,True])

    route_category.to_csv("route_category.csv", index=False, header=True)

# 3-2 By Trip Route Category (Normalized)
    route_category_normalized=pd.merge(route_category,bike_station_count,on="Region",how="inner")
    route_category_normalized["normalized_trip_count"]=route_category_normalized.trip_count/route_category_normalized.station_count
    route_category_normalized=route_category_normalized[["trip_route_category","Region","normalized_trip_count"]]
    route_category_normalized=route_category_normalized.sort_values(["trip_route_category","Region"], ascending=[False,True])

    route_category_normalized.to_csv("route_category_normalized.csv", index=False, header=True)


# 4-1 Time Series by Month
    bike_complete["Year-Month"]=bike_complete.start_time.map(lambda x: x.strftime('%Y-%m'))

    bike_complete["Year-Month"]=pd.to_datetime(bike_complete["Year-Month"])

    year_month=bike_complete.groupby(['Year-Month','Region']).count().unstack('Year-Month').stack(dropna=False).reset_index().fillna(0)
    year_month=year_month.rename(columns={"trip_id":"trip_count"})
    year_month=year_month[["Year-Month","Region","trip_count"]]
    year_month=year_month.sort_values(["Year-Month","Region"], ascending=[True,True])
    year_month["trip_count"]=year_month["trip_count"]+0.00000000000000001

    year_month.to_csv("year_month.csv", index=False, header=True)

# 4-2 Time Series by Month (Normalized)
    year_month_normalized=pd.merge(year_month,bike_station_count,on="Region",how="outer")
    year_month_normalized["normalized_trip_count"]=year_month_normalized.trip_count/year_month_normalized.station_count
    year_month_normalized=year_month_normalized[["Year-Month","Region","normalized_trip_count"]]
    year_month_normalized=year_month_normalized.sort_values(["Year-Month","Region"], ascending=[True,True])

    year_month_normalized.to_csv("year_month_normalized.csv", index=False, header=True)

    # connect to mongo and insert columns as docs in the collection
    #mongo_uri = 'mongodb://localhost:27017'
    mongo_uri = 'mongodb://adminuser:USCbootcamp2018@ds141633.mlab.com:41633/la_events'
    conn = MongoClient(mongo_uri)
    db = conn.la_events
    collection_route = db.top30


# In[27]:

    collection_route = db.routes
    #db.drop_collection(collection_route) # remove previous version of the collection.
    db.routes.drop() # remove previous version of the collection.

# create df_dict to simplify writing to mongo

    for index, row in route_category.iterrows():
    #print(str(index), list(row.values))
        collection_route.insert_one({str(index): list(row.values)})






    collection_bike_station = db.bike_station
    #db.drop_collection(collection_route) # remove previous version of the collection.
    db.bike_station.drop() # remove previous version of the collection.

# create df_dict to simplify writing to mongo

    for index, row in bike_station_count.iterrows():
    #print(str(index), list(row.values))
        collection_bike_station.insert_one({str(index): list(row.values)})

    collection_day_week_normalized = db.day_week_normalized
    #db.drop_collection(collection_route) # remove previous version of the collection.
    db.day_week_normalized.drop() # remove previous version of the collection.

# create df_dict to simplify writing to mongo

    for index, row in day_of_week_normalized.iterrows():
    #print(str(index), list(row.values))
        collection_day_week_normalized.insert_one({str(index): list(row.values)})



    collection_passholder_normalized = db.passholder_normalized
    #db.drop_collection(collection_route) # remove previous version of the collection.
    db.passholder_normalized.drop() # remove previous version of the collection.

# create df_dict to simplify writing to mongo

    for index, row in passholder_type_normalized.iterrows():
    #print(str(index), list(row.values))
        collection_passholder_normalized.insert_one({str(index): list(row.values)})


    collection_route_c_normalized = db.route_c_normalized 
    #db.drop_collection(collection_route) # remove previous version of the collection.
    db.route_c_normalized .drop() # remove previous version of the collection.

# create df_dict to simplify writing to mongo

    for index, row in route_category_normalized.iterrows():
    #print(str(index), list(row.values))
        collection_route_c_normalized.insert_one({str(index): list(row.values)})

    collection_year_month_normalized = db.year_month_normalized
    #db.drop_collection(collection_route) # remove previous version of the collection.
    db.year_month_normalized .drop() # remove previous version of the collection.

# create df_dict to simplify writing to mongo

    for index, row in year_month_normalized.iterrows():
    #print(str(index), list(row.values))
        collection_year_month_normalized.insert_one({str(index): list(row.values)})








# In[29]:


#year-month
    collection_ym = db.year_month
    db.drop_collection(collection_ym) # remove previous version of the collection.


    for index, row in year_month.iterrows():
    #print(str(index), list(row.values))
        collection_ym.insert_one({str(index): list(row.values)})


# In[30]:


#day-week
    collection_dw = db.day_week
    db.drop_collection(collection_dw) # remove previous version of the collection.

# create df_dict to simplify writing to mongo

    for index, row in day_of_week.iterrows():
    #print(str(index), list(row.values))
        collection_dw.insert_one({str(index): list(row.values)})


# In[31]:


#passholder
    collection_pass = db.passholder
    db.drop_collection(collection_pass) # remove previous version of the collection.

# create df_dict to simplify writing to mongo

    for index, row in passholder_type.iterrows():
    #print(str(index), list(row.values))
        collection_pass.insert_one({str(index): list(row.values)})


# In[32]:


#top30
    collection_30 = db.top30
    db.drop_collection(collection_30) # remove previous version of the collection.

# create df_dict to simplify writing to mongo

    for index, row in top_30_routes.iterrows():
    #print(str(index), list(row.values))
        collection_30.insert_one({str(index): list(row.values)})


# In[33]:


#start-station
    collection_ss = db.start_station
    db.drop_collection(collection_ss) # remove previous version of the collection.

# create df_dict to simplify writing to mongo

    for index, row in start_station.iterrows():
    #print(str(index), list(row.values))
        collection_ss.insert_one({str(index): list(row.values)})



# In[41]:


    route_cols = []
    for i in route_category.columns:
        route_cols.append(i)
    
    year_month_cols = []
    for i in year_month.columns:
        year_month_cols.append(i)
    
    day_of_week_cols = []
    for i in day_of_week.columns:
        day_of_week_cols.append(i)
    
    passholder_type_cols = []
    for i in passholder_type.columns:
        passholder_type_cols.append(i)
    
    top_30_routes_cols = []
    for i in top_30_routes.columns:
        top_30_routes_cols.append(i)
    
    start_station_cols = []
    for i in start_station.columns:
        start_station_cols.append(i)


#RETRIEVE!


#retrieve each column and its values - for Day of Week
    df_dw = pd.DataFrame(columns=day_of_week_cols)
    collection = db.day_week.find()

    for doc in collection:
    #thekeys  = list(doc.keys())[1] # extract column name
        thevals = list(doc.values())[1] # extract column values
        df_dw = df_dw.append(pd.DataFrame([thevals], columns=day_of_week_cols), ignore_index = True)


# In[85]:


#retrieve each column and its values - Passholder
    df_pass = pd.DataFrame(columns=passholder_type_cols)
    collection = db.passholder.find()
    for doc in collection:
    #thekeys  = list(doc.keys())[1] # extract column name
        thevals = list(doc.values())[1] # extract column values
        df_pass = df_pass.append(pd.DataFrame([thevals], columns=passholder_type_cols), ignore_index = True)


# In[86]:


#retrieve each column and its values - for Routes
    df_routes = pd.DataFrame(columns=route_cols)
    collection = db.routes.find()

    for doc in collection:
    #thekeys  = list(doc.keys())[1] # extract column name
        thevals = list(doc.values())[1] # extract column values
        df_routes = df_routes.append(pd.DataFrame([thevals], columns=route_cols), ignore_index = True)


# In[87]:


#retrieve each column and its values - for Start Station
    df_station = pd.DataFrame(columns=start_station_cols)
    collection = db.start_station.find()

    for doc in collection:
    #thekeys  = list(doc.keys())[1] # extract column name
        thevals = list(doc.values())[1] # extract column values
        df_station = df_station.append(pd.DataFrame([thevals], columns=start_station_cols), ignore_index = True)


# In[88]:


#retrieve each column and its values - for Top 30 Routes
    df_30 = pd.DataFrame(columns=top_30_routes_cols)
    collection = db.top30.find()

    for doc in collection:
    #thekeys  = list(doc.keys())[1] # extract column name
        thevals = list(doc.values())[1] # extract column values
        df_30 = df_30.append(pd.DataFrame([thevals], columns=top_30_routes_cols), ignore_index = True)


# In[89]:


#retrieve each column and its values - for Year Month
    df_ym = pd.DataFrame(columns=year_month_cols)
    collection = db.year_month.find()

    for doc in collection:
    #thekeys  = list(doc.keys())[1] # extract column name
        thevals = list(doc.values())[1] # extract column values
        df_ym = df_ym.append(pd.DataFrame([thevals], columns=year_month_cols), ignore_index = True)

if __name__ == '__main__':
    print(timeout_events())