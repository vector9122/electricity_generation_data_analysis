Overview
This project focuses on the comprehensive analysis of real-time electricity generation data in Northern Ireland and Ireland. Utilizing web scraping with Python and Selenium, data is extracted from the Smart Grid Dashboard (https://www.smartgriddashboard.com/#all/co2) every 15 minutes. The extracted data, including electricity demand, forecasted peak demand, and CO2 emissions and several other features, is stored in a postgreSQL Database. The repository contains two key files: 
1. The Python script for web scraping, executed by a cron job every 15 minutes, extracts and saves data to the database.
2.The Jupyter notebook, which pulls data from the database, performs cleaning, and conducts visualizations using Matplotlib and Seaborn.

Key Features
1.Real-time data extraction and storage.
2.Cron job for regular extraction.
3.Data cleaning and imputation techniques.
4.Visualization with Matplotlib and Seaborn.

Note: Please do create a SQL database and also change it's details on these two files for succesfull implementation. The script needs to be run using cron job or any other scheduler for extracting data every 15 minutes.
