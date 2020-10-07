# HowHotDB - Weather database project 
A Python program that builds a database of current weather data from OpenWeatherMap web APIs.

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#To-Do)

## General Info
HowHotDB is a Python program that retrieves current weather data with API from openweathermap.org, parses the data using pandas library and saves it in a local SQLite database. 

## Technologies
The project is created with:
* Python version: 3.8
* SQLite3 version: 3

## Setup 
The following instructions assume Python 3 and pip are already installed.

* Before running this project, you will need to install the dependencies by running the following command:
    ```
    pip install -r requirements.txt
    ```
* Signup on the OpenWeatherMap website to get your own API key. This API key has to remain private, and that's why it will be saved as an environment variable and will be hidden outside of the program. 

* Create in the project folder a file called .env

* Save your private API key in the .env file.
For example:
    ```
    api-token = "typeyourapikeyhere"
    ```
* Run main.py in order to get and save the current weather data for Tel Aviv city by default
* Optional - run main.py from the command line with a specified city id as optional argument. For example, Detroit,US:

    ```
    python main.py --city_id "4990729"
    ```
* Optional - schedule running main .py to get the current weather data.

## To-Do:
- [x] Convert json file to pandas df
- [x] ETL- Transform-Extract the desired keys from the data frame
- [x] Convert kelvin to celsius
- [x] Load- Update the database
- [x] Fetch the json from API using requests library
- [x] Setup environment variables using load_dotenv
- [x] Test each function- unittest
- [x] Put all the jsons in one folder
- [x] Explain how to setup (run manually create db, run main, env var with api token) and how to install libraries, add requirements.txt
- [x] Run main.py with argparse to get data from other cities but Tel Aviv
- [ ] Add an image
- [ ] Schedule running main.py with Airflow
- [ ] Maybe run this in the cloud
- [ ] Build ML model on data
- [ ] Add website with dashboards. Display date time not in Unix.

