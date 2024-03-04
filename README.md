## Usage of Package

### Installation of Load_MySQL Package
You can install the `load_MySQL` package via pip:

```bash
pip install load_MySQL
```

### Importing the class
MySQLOperation class from sql_connect.MySQL module:

```bash
from sql_connect.MySQL import MySQLOperation
```

### Connecting to Database
Create an instance of MySQLOperation class with your database credentials:

```bash
db = MySQLOperation(host="localhost", user=" username", password="password", database="database name")
db.connect()
```

### SELECT Queries
You can execute SQL queries using the execute_query() method of the MySQLOperation instance. Results are stored in a pandas DataFrame

```bash
query = "SELECT * FROM student"
student_records_df = db.execute_query(query)
```

#### More Examples
- Students Records that starts with A and have marks greater than 50
```bash
query2 = """
SELECT 
name,
mark 
FROM student 
WHERE name LIKE 'A%' AND mark > 50;
"""
student_records_df = db.execute_query(query2)
```

- Students's Highest Marks of only those class's with Highest Marks greater than 80 
```bash
query3 = """
SELECT class,
MAX(mark) AS max_mark
FROM student
GROUP BY class
HAVING max_mark > 80;
"""
student_records_df = db.execute_query(query3)

```
More Information
For more detailed examples and coverage of features, refer to the load_MySQL Tutorial in the experiments/load_MySQL Tutorial directory
[load_MySQL Tutorial](https://github.com/Meetpanchal58/SQL_Connect/blob/main/experiments/load_MySQL%20Tutorial.ipynb)

---

## Usage of All files 

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

