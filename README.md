# python-with-oracle-database
This application creates an Oracle database and inserts the data present in an excel sheet using python libraries.

An Oracle table "inventory_table" is created and the data that are available in the excel sheet"Inventory_Data" are inserted to the table with the help of SQL queries.

**Oracle Version :** Oracle 10g experss edition (10.2.1015)        
**Python Packages :** cx_Oracle (version 7.3.0),xlrd (version 1.2.0)         
                  
**Package Description:**       
The *xlrd* package will help read the excel sheet that contains the data.          
*cx_Oracle* package will help establish the connection with the Oracle database installed. With this package, all the SQL queries are executed and can write the excel data to the database.      

**Pre-requisites:**
Oracle database is installed in the local machine.          
User name and password to connect to the database.         
An Excel sheet with the data that needs to be inserted into the database.            

**Application Logic:**          
1. Reads the data present in the excel sheet.
2. Connects with the targetted Oracle database using the username password provided.
3. Creates a table in the database.
4. Inserts all the records present in the excel sheet.
5. Commits and closes the connection with the database.




