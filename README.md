# sqlalchemy-challenge
##Introducitons

##This assignment is to do a climate analysis and data exploration using sqlalchemy, Pandas and Matplotlib. 


##Part 1 Precipitation Analysis and Station Analysis

  ##Precipitation Analysis:
  
  #Design a query to find out the previous 12 months of data, select "date" and "prcp" values. Sort the data by 'date' and using matplotlib to show a image as below:
  
  
  #![prcp](https://user-images.githubusercontent.com/109451707/194977987-1918d46c-5b9b-483e-9bf3-8888f93f26c7.png)


##Station Analysis
1. A query was designed to calculate the total number of the stations in the dataset and viewed by descending order to find the most active station ID.
2. find out the lowest, highest and the average temperatures of the most acitive station
3. desgined a query to find out the temperature observations of the most active station for the previous 12 months. 
Please see the image below:

  ![tob](https://user-images.githubusercontent.com/109451707/194979242-391d034f-85e6-4d09-989c-f03bd5e11b40.png)

##Part 2 Climate APP

#After the completion of the initial analysis, a Flask API app was designed based on the queries. The following routes were created :

Routes
/

Home page.
List of all routes that were available.
/api/v1.0/precipitation

the query results were converted to a dictionary using date as the key and prcp as the value.
Returned the JSON representation of your dictionary
/api/v1.0/stations

Returned a JSON list of stations from the dataset.
/api/v1.0/tobs

Queried the dates and temperature observations of the most active station for the last year of data.
Return a JSON list of temperature observations (TOBS) for the previous year.
/api/v1.0/<start> and /api/v1.0/<start>/<end>

Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
When given the start only, calculated TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
When given the start and the end date, calculated TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

![web](https://user-images.githubusercontent.com/109451707/194979623-fb28af44-3d91-4c95-b47d-2dcf2f503078.png)

