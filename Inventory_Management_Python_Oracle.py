# import xlrd to read excel data
# import cx_Oracle to communicate with the oracle database
import xlrd
import cx_Oracle

# Open the workbook and define the worksheet
book = xlrd.open_workbook("sample.xlsx")
sheet = book.sheet_by_name("firstsheet")

# Establish a MySQL connection
#use username/password@localhostip to create a connection
connection=cx_Oracle.connect('santhu/santhu97@127.0.0.1/')

# Get the cursor, which is used to traverse the database, line by line
cursor = connection.cursor()

#Form a CREATE TABLE query to create a table in the database
query = """CREATE TABLE inventory_table (stock_item char(30),category char(30),stock_ref char(30), init_stock number, stock_in number, stock_out number, final_stock number)"""
cursor.execute(query)

# Create the INSERT INTO sql query
# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
      stock_item= sheet.cell(r,0).value
      category = sheet.cell(r,1).value
      stock_ref = sheet.cell(r,2).value
      init_stock = sheet.cell(r,3).value
      stock_in = sheet.cell(r,4).value
      stock_out = sheet.cell(r,5).value
      final_stock = sheet.cell(r,6).value
      
      # Assign values from each row
      values = (stock_item,category,stock_ref,init_stock,stock_in,stock_out,final_stock)
      query = """INSERT INTO inventory_table (stock_item,category,stock_ref,init_stock,stock_in,stock_out,final_stock) VALUES (:item,:category,:refer,:initstock,:instock,:outstock,:finalstock)"""
      # Execute sql Query
      cursor.execute(query,{"item":str(stock_item),"category":str(category),"refer":str(stock_ref),"initstock":int(init_stock),"instock":int(stock_in),"outstock":int(stock_out),"finalstock":int(final_stock)})

# Close the cursor
cursor.close()

# Commit the transaction
connection.commit()

# Close the database connection
connection.close()

# Print results
print("The data has been succesffuly inserted into the database!")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("Imported " + str(columns) + " columns and " + str(rows) +" rows to MySQL!")
