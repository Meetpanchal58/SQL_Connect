### load_MySQL

A Python package for simplifying MySQL database operations, providing an intuitive interface for executing queries and retrieving results conveniently.

#### Installation
```bash
pip install load_MySQL
To install load_MySQL, simply use pip as shown above.

Usage Guide
Importing the Package
python
Copy code
from sql_connect.MySQL import MySQLOperation
Begin by importing the necessary module from the package.

Establishing Connection
python
Copy code
db = MySQLOperation(host="localhost", user="root", password="1234", database="meet")
db.connect()
Create an instance of MySQLOperation with your MySQL database connection details and establish a connection using the connect() method.

Executing Queries
python
Copy code
query1 = "SELECT * FROM student"
student_records_df = db.execute_query(query1)
print(student_records_df.tail())
Execute SQL queries using the execute_query() method. Results are stored in pandas DataFrame for easy manipulation.

Disconnecting from Database
python
Copy code
db.disconnect()
After performing necessary operations, disconnect from the database using the disconnect() method to release resources.

Examples
Example 1: Retrieving all records from the 'student' table.
python
Copy code
query1 = "SELECT * FROM student"
student_records_df = db.execute_query(query1)
print(student_records_df.tail())
Example 2: Filtering records based on specific criteria.
python
Copy code
query2 = """
SELECT 
    name,
    mark 
FROM student 
WHERE name LIKE 'A%' AND mark > 50;
"""
student_filtered_records_df = db.execute_query(query2)
print(student_filtered_records_df)
Example 3: Aggregating data with group by and having clauses.
python
Copy code
query3 ="""
SELECT class,
    MAX(mark) AS max_mark
FROM student
GROUP BY class
HAVING max_mark > 80;
"""
aggregated_records_df = db.execute_query(query3)
print(aggregated_records_df)



### requirements_dev.txt we use for the testing
- It makes it easier to install and manage dependencies for development and testing, separate from the dependencies required for production.

### difference between requirements_dev.txt and requirements.txt

- requirements.txt is used to specify the dependencies required to run the production code of a Python project, while requirements_dev.txt is used to specify the dependencies required for development and testing purposes.

### tox.ini
- We use if for the testing in the python package testing against different version of the python 

### how tox works tox enviornment creation
1. Install depedencies and packages 
2. Run commands
3. Its a combination of the (virtualenvwrapper and makefile)
4. It creates a .tox


#### pyproject.toml
- it is being used for configuration the python project it is a alternative of the setup.cfg file. its containts configuration related to the build system
such as the build tool used package name version author license and dependencies

#### setup.cfg
- In summary, setup.cfg is used by setuptools to configure the packaging and installation of a Python projec

#### Testing python application
*types of testing*
1. Automated testing 
2. Manual testing

#### Mode of testing
1. Unit testing
2. Integration tests

#### Testing frameworks

1. pytest
2. unittest
3. robotframework
4. selenium
5. behave
6. doctest

##### check with the code style formatting and syntax(coding standard)

1. pylint
2. flake8(it is best because it containt 3 library pylint pycodestyle mccabe)
3. pycodestyle

