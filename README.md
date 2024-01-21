Overview
This project focuses on the comprehensive analysis of real-time electricity generation data in Northern Ireland and Ireland. Utilizing web scraping with Python and Selenium, data is extracted from the Smart Grid Dashboard (https://www.smartgriddashboard.com/#all/co2) every 15 minutes. The extracted data, including electricity demand, forecasted peak demand, and CO2 emissions and several other features, is stored in a postgreSQL Database. The repository contains two key files:

The Python script for web scraping, executed by a cron job every 15 minutes, extracts and saves data to the database.
The Jupyter notebook, which pulls data from the database, performs cleaning, and conducts visualizations using Matplotlib and Seaborn.

Key Features
Real-time data extraction and storage.
Cron job for regular extraction.
Data cleaning and imputation techniques.
Visualization with Matplotlib and Seaborn.

Note: Please do create a SQL database and also change it's details on these two files for succesfull implementation.
