# ETLProject-Sleepless-in-Seattle
Contributors: Brianne Ng, Walton Tan, Daniel Bourke

# Purpose and motivation

This repository demonstrates the process of extracting 2015-2016 Seattle AirBNB and tourism data, performing ETL and then loading the data in a database which can then be queried by the analyst. 

Following this ETL process, analysts will be able to analyse and provide insight into:
 - What a prospective host should charge for their stay?
 - Which factors contribute to high review scores?
 - Where are the cheapest stays in Seattle?
 - Which is the busiest time of the year?
 - Does price impact customer satisfaction?
 - What is the average distance between the properties and Seattle's landmarks?


This code repository contains the solution to perform the ETL on a scheduled basis, and store the data in a PostgreSQL Database. 

To provide confidence over the transformations applied, unit tests have also been written. Continuous integration pipelines have also been configured to automate the testing of code prior to merging to `main`.  

# Repo structure 
```
.github/workflows                           # contains continuous integration pipelines 
Resources/                                  # contains static datasets and cleaned datasets
Docs/                                       # contains additional documentation 
images/                                     # contains images used for the README
scripts/    
    |__ credentials.py                      # (already added to .gitignore)
    |__ ddl_create_table.sql                # SQL code used to create the target tables 
    |__ etl.ipynb                           # the python ETL notebook (write your code here)
    |__ etl.py                              # an auto-generated file from the python ETL notebook (do not write your code here)
    |__ run_etl.sh                          # a shell script used to shorten the amount of code needed to be written in cron 
    |__ test_transformation_functions.py    # pytest unit tests 
    |__ transform_functions.py              # custom user-generated transformation functions 
README.md                                   # all you need to know is in here 
requirements.txt                            # python dependencies 
```

# Solution 

## Solution architecture 

The solution architecture diagram was created using: https://draw.io/ 


![Solution_architecture_diagram.drawio.png](Images/Solution_architecture_diagram.drawio.png)


The **E**xtract, **T**ransform, and **L**oad steps are explained below. 

<details>
<summary><strong> Extract </strong></summary>

#### Data sources 
Data is extracted from the following data sources. 

| No | Data Source | Description | Source Type | URL | 
| - | - | - |- | - |
| 1 | Listings.csv | Contains details of each listing | CSV | https://www.kaggle.com/airbnb/seattle?select=listings.csv | 
| 2 | Calendar.csv | Contains the availability and price of each listing for each date | CSV | https://www.kaggle.com/airbnb/seattle?select=calendar.csv |
| 3 | Reviews.csv | Contains the text commentary for each review | CSV | https://www.kaggle.com/airbnb/seattle?select=reviews.csv 
| 4 | Visit Seattle | Top 25 attractions in Seattle | HTML | https://visitseattle.org/things-to-do/sightseeing/top-25-attractions/ 
| 3 | Google Text Search | Contains coordinates of locations | API | https://developers.google.com/maps/documentation/places/web-service/search-text | 

</details>

<details>
<summary><strong> Transform </strong></summary>


The following transformation scripts are executed: 
| Script | Input | Output |  
| - | - |- |
| [Listing_ETL.ipynb](scripts/Listing_ETL.ipynb) | [1] | `something`, `something`, `something` |
| [Amenities_ETL.ipynb](scripts/Amenities_ETL.ipynb) | [1] | `something`, `something`, `something` |
| [Reviews_ETL.ipynb](scripts/Reviews_ETL.ipynb) | [3] | `something`, `something`, `something` | 
| 

The `etl.ipynb` notebook is converted to `etl.py` by running the code below: 
```sh
python -m jupyter nbconvert --to python etl.ipynb
```
</details>


<details>
<summary><strong> Load </strong></summary>


#### Loading process 
Data is loaded into the PostgreSQL using an upsert (insert/update) statement. 

1. Attempt to insert the records 
2. If fail due to records already existing, then update records 

</details>

# ERD and Data Dictionary

### Entity Relationship Diagram 

The ERD diagram was created using: https://app.quickdatabasediagrams.com/#/

![ERD.PNG](Images/ERD.PNG)

The Data Definition Language (DDL) used to create the tables can be found [here](scripts/ddl_create_table.sql). 

### Data dictionary 

Below are the data definitions for the following tables: 
<details>
<summary><strong> Property </strong></summary>


|Column name| Definition | 
|-|-|
|listing_id|The unique id for each listing| 
|host_id| The unique id for the listings host| 
|listing_url| The url of each listing |
|name| The name of each listing|
|property_type| Type of property listing|
|room_type| Whether the entire property is available to the guest or different portions of access to the property|
|accommodates| the maximum number of guests allowed to stay at the listing|
|bathrooms| number of bathrooms available|
|bedrooms| number of bedrooms available|
|beds| number of beds available|
|bed_type| bed type|
|square_feet| square feet|
|description| The description of each listing|
|notes| special comments made by the lister| 
|transit| information on the transit options nearby| 
|picture_url| url for property picture| 
|guests_included| maximum number of people allowed to visit the property|
|minimum_nights| the minimum number of nights which the guest must book|
|maximum_nights| the minimum number of nights which the guest must book|
</details>


<details>
<summary><strong> Address </strong></summary>


|Column name| Definition | 
|-|-|
|listing_id|The unique id for each listing| 
|country_code| location of the listing in terms of country abv.| 
|country| Location of the listing in terms of country| 
|state| location of the listing in terms of State abv.| 
|city| location of the listing in terms of City| 
|zipcode| location of the listing in terms of zipcode| 
|smart_location| location of the listing in terms of City, State| 
|neighborhood| location of the listing in terms of suburb| 
|street| location of the listing in terms of street adress| 
|latitude| Location of the listing in terms of latitude| 
|longitude| Location of the listing in terms of longitude| 
|is_location_exact| Boolean whether the listing has its adress exactly matched|
|distance| Average distance in Km from address to top 25 landmarks in Seattle |  
</details>


<details>
<summary><strong> Pricing </strong></summary>


|Column name| Definition | 
|-|-|
|listing_id|The unique id for each listing| 
|price| price for 1 night|
|weekly_price| price for 1 week|
|monthly_price| price for 1 month|
|security_deposit| security deposit for the listing|
|cleaning_fee| fee for cleaning for each period of stay|
|extra_people| ??The price for extra people to stay??|
|cancellation policy| how strict the listing is in terms of its cancellation policy |
</details>


<details>
<summary><strong> Review_Statistics </strong></summary>


|Column name| Definition | 
|-|-|
|listing_id|The unique id for each listing| 
|number_of_reviews|Total number of reviews | 
|reviews_per_month|Average number of reviews per month  |
|first_review| The date on which the listing recieved its first review |
|last_review| The date on which the listing recieved its latest review |
|review_scores_rating|Average rating of listing | 
|review_scores_accuracy| The average score out of 10, given by the guests in terms of how accurate the listing description and photos were|
|review_scores_cleanliness| The average score out of 10, given by the guests in terms of how clean the listing was |
|review_scores_checkin| The average score out of 10, given by the guests in terms of how pleasant the checkin process was  |
|review_scores_communication| The average score out of 10, given by the guests in terms of communication to the host |
|review_scores_location| The average score out of 10, given by the guests in terms of how good the location of the listing was |
|review_scores_value| The average score out of 10, given by the guests in terms of value (quality against price)  |
</details>


<details>
<summary><strong> Availability </strong></summary>


|Column name| Definition | 
|-|-|
|listing_id|The unique id for each listing| 
|has_availability| Boolean whether or not the listing is potentially available for booking|
|availability_30| how many days in the next 30 days is the listing available|
|availability_60| how many days in the next 60 days is the listing available|
|availability_90| how many days in the next 90 days is the listing available|
|availability_365| how many days in the next 365 days is the listing available|
|calendar_updated| When the calendar was last updated| 
</details>


<details>
<summary><strong> Amenities </strong></summary>


|Column name| Definition | 
|-|-|
|listing_id|The unique id for each listing|
|amenities|The amenity available for this listing|
</details>


<details>
<summary><strong> Host </strong></summary>


|Column name| Definition | 
|-|-|
|host_id|The unique id for each host|
|host_url| the url for each host| 
|host_name| the name of each host| 
|host_since| the date the host began hosting on Airbnb| 
|host_about| the self-description of the host| 
|host_is_superhost| boolean whether the host is classified as a superhost by AirBNB|
|host_picture_url| link to the hosts picture|
|host_listings_count| The number of listings the host has with AirBNB|
|host_identity_verified| Boolean whether the host has had their identity verified by AirBNB |
|host_location| The hosts location in terms of city, state, country | 
|host_response_time| average time it typically takes the host to respond to queries| 
|host_response_rate| percentage of the time the host responds to queries|
|host_acceptance_rate| percentage of the time the host accepts guests|
|host_neighborhood| The hosts location in terms of suburb|
</details>


<details>
<summary><strong> Host Verifications </strong></summary>
    

|Column name| Definition | 
|-|-|
|host_id|The unique id for each host|
|host_verification_method|The method in which the host is verified by AirBNB|
</details>


<details>
<summary><strong> Reviews </strong></summary>
    

|Column name| Definition | 
|-|-|
|review_id| The unique id for each review of that listing| 
|listing_id|The unique id for each listing| 
|date| The date on which the review was submitted | 
|comments| The written feedback for each review | 
|reviewer_id| The unique id for each reviewer | 
|reviewer_name|The name for each reviewer | 
</details>


<details>
<summary><strong> Calendar </strong></summary>
    

|Column name| Definition | 
|-|-|
|listing_id|The unique id for each listing| 
|date| the date | 
|available| Boolean whether the listing was vacant on that date or not| 
|price| the price to stay on that date provided the listing was available on that date| 
</details>









# Usage 

## Python dependencies 
The required python libraries and version have been specified in [requirements.txt](requirements.txt). 

Install python dependencies by performing : 

```
pip install -r requirements.txt 
```

## Credentials 
In the `script/` folder, create a `credentials.py` file with the following variables:
```py
api_key = "<your_api_key>"                  # open weather API api key 
db_user = "<your_database_user>"            # postgresql username 
db_password = "<your_database_password>"    # postgresql password 
```

These credentials will be used in the `etl.ipynb` notebook. 

The `credentials.py` file is already in .gitignore and thus your credentials will not be stored on Git. 

## Running code locally 
To run the ETL code on your computer, execute the following in your terminal: 

```
cd scripts
python -m jupyter nbconvert --to python scripts/etl.ipynb
python scripts/etl.py
```

## Run unit tests 
To run the unit tests on your computer, execute the following in your terminal: 

```
pytest scripts
```

You should see the following output: 

```
====== test session starts ======
platform darwin -- Python 3.7.11, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
collected 2 items
scripts/test_transformation_functions.py .. [100%]
====== 2 passed in 0.36s ======
```

## Continuous integration 

To ensure that code is tested prior to merging to the `main` branch, an automated Continuous Integration (CI) pipeline has been configured. 

See code [here](.github/workflows/etl-ci.yml). 

The expected output when the CI pipeline runs are: 

1. Successful execution of CI pipeline 

![ci-pipeline.png](images/ci-pipeline.png)


2. All unit tests passed 

![ci-test-output.png](images/ci-test-output.png)



## Scheduling jobs 


<details>
<summary><strong> Task Scheduler (Windows) </strong></summary>

1. Open Task Scheduler on windows 

2. Select `Create task`

![images/task-scheduler-1.png](images/task-scheduler-1.png)

3. Provide a name for the task 

![images/task-scheduler-2.png](images/task-scheduler-2.png)

4. Select `Actions` > `New` 

![images/task-scheduler-3.png](images/task-scheduler-3.png)

5. Provide the following details, and click `OK`: 
    - Program/script: `<provide path to your python.exe in your conda environment folder>`
        - Example: `C:\Users\jonat\anaconda3\envs\PythonData\python.exe`
    - Add arguments (optional): `<provide the etl file>`
        - Example: `etl.py` 
    - Start in (optional): `<provide the path to the etl file>` 
        - Example: `C:\Users\jonat\Documents\weather-etl\scripts`

![images/task-scheduler-4.png](images/task-scheduler-4.png)

6. Select `Triggers` 

![images/task-scheduler-5.png](images/task-scheduler-5.png)

7. Provide details of when you would like the job to run 

![images/task-scheduler-6.png](images/task-scheduler-6.png)

8. Click `OK` 

</details>

# Contributors
- [@jonathanneo](https://github.com/jonathanneo)