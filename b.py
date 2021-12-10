import sqlite3

dbname = input("Please Enter the database Name ?")
tablename = input("Please Enter the tablename  ?")
nor = input("How many students you want to store ?")

# nor str -> not int
nor = int(nor)
print(type(nor))

database = dbname+'.sqlite3'
# Always open the file
fo = open(database,"a")



#Always open the database
con = sqlite3.connect(database)
cur = con.cursor()

#Lets the create the table
'''
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
'''
cur.execute(f"CREATE TABLE {tablename}( name text,mobile text )")

for x in range(nor):
    n = input("Enter the Student Name  ")
    m = input("Enter the Student Mobile Numb  ")
    cur.execute(f"INSERT INTO {tablename} VALUES ('{n}','{m}')")
# Save (commit) the changes
con.commit()

#Always close the database
con.close()



# Always close the file
fo.close()