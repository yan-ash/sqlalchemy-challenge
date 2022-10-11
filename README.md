# sqlalchemy-challenge
Introducitons
This assignment is to do a climate analysis and data exploration using sqlalchemy, Pandas and Matplotlib. 
Part 1 Precipitation Analysis and Station Analysis
  Precipitation Analysis:
        Design a query to find out the previous 12 months of data, select "date" and "prcp" values. Sort the data by 'date' and using matplotlib to show a image as below:
        image.png
  Station Analysis

        a.A query was designed to calculate the total number of stations in the dataset and viewed the result by decending the order to  find the most active station Id.
        b.find out the lowest, hignest and the average temperatures of th most active station
        c. Designed a query to find out the previous 12 months temperature observations for the most active station.
        Please see the image shown as below:
        image.png

Climate APP

After the completion of the initial analysis, a Flask API app was designed based on the queries. The following routes were created :

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
The following is the result :
image.png
