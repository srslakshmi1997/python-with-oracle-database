# python-with-oracle-database
Create an Oracle database and insert the data present in an excel sheet using python libraries

This code creates an Oracle table "inventory_table" and inserts the data that are availabe in the excel sheet "Inventory_Data" to the table with the help of SQL queries.

**Oracle Version :** Oracle 10g experss edition (10.2.1015)        
**Python Packages :** cx_Oracle (version 7.3.0),xlrd (version 1.2.0)         
				  
**Package Description:**       
The *xlrd* package wil be helpful in reading the exel sheet that contains the data.          
*cx_Oracle* package will be helpful in establishing the conection with Oracle database installed. With this package we will be able to execute all the SQL queries, write the excel data to the database.      

Make sure the oracle database is installed in your local machine.       
Please make note of the user name and password to connect to the database.     
The excel sheet should have the data that needs to be inserted to the database.       
The python code will :       
1. Read the data present in the excel sheet.
2. Connect with the targetted Oracle database using the username password provided.
3. Create a table in the database.
4. Insert all the records present in the excel sheet.
5.Commit and close the connection with the database.




