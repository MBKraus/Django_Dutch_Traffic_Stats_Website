# Django-powered Dutch Traffic Stats Website

Django-powered website (hosted on Heroku) that focuses on analyzing Dutch traffic data acquired through the following [custom scraper](https://github.com/Weesper1985/Dutch_traffic_info_scraper).

This custom scraper written in Python scrapes traffic data from the Dutch main traffic service platform, vid.nl. Headline variables retrieved are the highway or expressway under consideration, the location of the traffic jam, the reason for the traffic jam, the date, time and day of the week etc. 

This scraper is running in the cloud (by means of Heroku) at 3 fixed point in time in the morning and the evening. The retrieved data is stored in a PostgreSQL database. This database in turn serves as the basis for this Django project (which is running on Heroku).

NB 
- Procfile and runtime files are included in the headline directory
- Please refer to requirements.txt for the required modules
- This Django project has two databases (one externally sourced existing database - and the usual 'default' database)

#### Screenshot Homepage
![alt text](https://github.com/Weesper1985/Django_Dutch_Traffic_Stats_Website/blob/master/static/img/home.png)

#### Screenshot Stats - Evening rush hour
![alt text](https://github.com/Weesper1985/Django_Dutch_Traffic_Stats_Website/blob/master/static/img/overview.png)
