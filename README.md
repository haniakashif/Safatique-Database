# Safatique-Database

## Overview
Safatique-Database is a project aimed at creating a comprehensive database for the online store Safatique. This project is part of our DBMS course in Semester 5 at Habib University.

## Languages and Software Used
- Python (PyQt6)
- SQL (MSSQL)
- QtDesigner

## Installation and Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Safatique-Database.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Safatique-Database
    ```
3. Install the required dependencies:
    ```bash
    pip install PyQt6
    ```
4. Start the database server Safatique which can be made by running `new database script.sql` in the `Populate Data` folder.

5. For each working part, we have `WorkingAdmin.zip`, `workingCart.zip` and the current folder, where we were unable to integrate all modules together but they are working independently. `modifiedmain.py` and `final_main.py` in the main folder show the working customer side and items being added to the cart. `workingCart.zip` correctly shows the placement of the order and removal of ordered items from the CartItems and inserting into Orders table. `WorkingAdmin.zip` shows the correct implementation of the admin side of the database.