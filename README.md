# **``PHASE-3 CAR-CONNECT PROJECT``**


### Created By ``GAITANO GEORGE`` 7-9-2023

___

## INTRODUCTION
The Car-Connect project is a versatile and user-friendly command-line tool for managing and tracking information related to cars, garages, and owners. This project leverages the power of SQLAlchemy and Click to provide a seamless and efficient way to interact with a database that stores crucial information about these entities.

___

## KEY FEATURES

- Garage Management: Easily add, update, delete and list garages where cars are stored.

- Owner Management: Manage the owners of the cars,including adding, updating, and listing all their details.

- Car Information: Track detailed information about each car, such as; make, model, year, and its association with a specific owner and garage.

- Search and Listing: Conveniently search and list garages, owners and cars based on a certain criteria 

- Data Integrity: Maintain data integrity by enforcing relationships between cars, owners, and garages through SQLAlchemy ORM.

___

## TECHNOLOGIES USED
The following have been used in this project:

- Python
- SQLAlchemy

___


## SETUP REQUIREMENTS
- Github
- Git
- Code editor of choice

___

## GETTING STARTED
To start using the Car-Connect project, follow the instructions:

1. Installation: Clone the project repository and install the required dependencies. Refer to the project's README for detailed instructions.

2. Database Setup: Configure the database connection in the main.py script to point to your preferred database system (e.g., SQLite, PostgreSQL).

3. Run the CLI: Execute the main.py script to access the command-line interface (CLI) for managing cars, garages, and owners.

___

## COMMANDS

```
gaitano@gaitano-HP-EliteBook-Revolve-810-G3:~/car-connect-project/models$ python3 main.py
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add-car                 ADD A NEW CAR
  add-garage              ADD'S A NEW GARAGE TO THE DATABASE
  add-owner               ADD A NEW OWNER
  delete-car              DELETE A CAR
  delete-garage           DELETES A GARAGE FROM THE DATABASE
  delete-owner            DELETE OWNER'S DETAILS
  list-all                LIST ALL CARS INCLUDING THEIR OWNER AND GARAGE...
  list-cars               LIST ALL CARS
  list-garage             LIST ALL THE GARAGES IN THE TABLE
  list-owners             LIST ALL THE OWNERS
  search-garage           SEARCH FOR A GARAGE BY THE NAME
  search-garage-car       SEARCH FOR CARS THAT ARE SERVICED BY A CERTAIN...
  search-garage-location  SEARCH FOR GARAGES IN DESIRED LOCATION
  search-owner            SEARCH FOR AN OWNER WITH SPECIFIC NAME
  search-owner-car        SEARCH FOR CARS THAT BELONG TO AN INDIVIDUAL OWNER
  update-car-garage       UPDATE GARAGE SERVICING THE CAR
  update-car-owner        UPDATE CAR OWNER
  update-garage-name      UPDATE NAME OF A GARAGE USING IT'S ID
  update-owner            UPDATE ANOWNER'S NAME

```
___

## KNOWN BUGS
There are no known bugs at the moment

___

## SUPPORT DETAILS

To make a contribution to the code used or any suggestions you can click on the contact link and email me your suggestions

- Email: gaitano.george@student.moringaschool.com

___

## LICENSE 

Copyright (c) {{ 2023 }}, {{ GAITANO GEORGE }}

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.