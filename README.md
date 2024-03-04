Usage Guide
===========

Installation of Load_MySQL Package
-----------------------------------

You can install the ``load_MySQL`` package via pip:

.. code-block:: bash

    pip install load_MySQL

Importing the class
--------------------

MySQLOperation class from sql_connect.MySQL module:

.. code-block:: python

    from sql_connect.MySQL import MySQLOperation

Connecting to Database
-----------------------

Create an instance of MySQLOperation class with your database credentials:

.. code-block:: python

    db = MySQLOperation(host="localhost", user="username", password="password", database="database name")
    db.connect()

SELECT Queries
---------------

You can execute SQL queries using the execute_query() method of the MySQLOperation instance. Results are stored in a pandas DataFrame:

.. code-block:: python

    query = "SELECT * FROM student"
    student_records_df = db.execute_query(query)

More Examples
-------------

- Students Records that start with 'A' and have marks greater than 50:

.. code-block:: python

    query2 = """
    SELECT 
    name,
    mark 
    FROM student 
    WHERE name LIKE 'A%' AND mark > 50;
    """
    student_records_df = db.execute_query(query2)

- Students' Highest Marks of only those classes with Highest Marks greater than 80:

.. code-block:: python

    query3 = """
    SELECT class,
    MAX(mark) AS max_mark
    FROM student
    GROUP BY class
    HAVING max_mark > 80;
    """
    student_records_df = db.execute_query(query3)

More Information
----------------

For more detailed examples and coverage of features, refer to the `load_MySQL Tutorial <https://github.com/Meetpanchal58/SQL_Connect/blob/main/experiments/load_MySQL%20Tutorial.ipynb>`_ in the experiments/load_MySQL Tutorial directory.

Usage of All files
===================

requirements_dev.txt for testing
---------------------------------

It makes it easier to install and manage dependencies for development and testing, separate from the dependencies required for production.

Difference between requirements_dev.txt and requirements.txt
------------------------------------------------------------

``requirements.txt`` is used to specify the dependencies required to run the production code of a Python project, while ``requirements_dev.txt`` is used to specify the dependencies required for development and testing purposes.

tox.ini
-------

We use it for testing the Python package against different versions of Python.

How tox works: tox environment creation
----------------------------------------

1. Install dependencies and packages 
2. Run commands
3. It's a combination of virtualenvwrapper and makefile
4. It creates a .tox directory

pyproject.toml
---------------

It is used for configuring the Python project. It's an alternative to the setup.cfg file. It contains configuration related to the build system such as the build tool used, package name, version, author, license, and dependencies.

setup.cfg
---------

In summary, setup.cfg is used by setuptools to configure the packaging and installation of a Python project.

Testing python application
---------------------------

**Types of testing**

1. Automated testing 
2. Manual testing

**Mode of testing**

1. Unit testing
2. Integration tests

**Testing frameworks**

1. pytest
2. unittest
3. robotframework
4. selenium
5. behave
6. doctest

**Check with the code style formatting and syntax (coding standard)**

1. pylint
2. flake8 (it is best because it contains 3 libraries: pylint, pycodestyle, mccabe)
3. pycodestyle
