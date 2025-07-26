# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Customer Academy
# MAGIC There is a 12-hour, self-paced [Databricks Customer Academy Course](https://customer-academy.databricks.com/learn) associated with these notebooks. 
# MAGIC
# MAGIC - If you are interested in the FREE self-paced option, you can [view the class here](https://customer-academy.databricks.com/learn/courses/1211/introduction-to-python-for-data-science-and-data-engineering).
# MAGIC - If you are interested in the 2-day instructor-led option (same content but with a group instructor), you can [view the class here](https://customer-academy.databricks.com/learn/courses/969/introduction-to-python-for-data-science-and-data-engineering).
# MAGIC
# MAGIC > **Note:** You can login to the [Databricks Customer Academy](https://customer-academy.databricks.com/learn) using your KP email.

# COMMAND ----------

# MAGIC %md
# MAGIC # Data Types and Variables
# MAGIC
# MAGIC - Explore fundamental concepts in Python, such as: 
# MAGIC     * Data types
# MAGIC     * Variables
# MAGIC     * Print values
# MAGIC    
# MAGIC Recommended Resources:
# MAGIC * <a href="https://www.amazon.com/gp/product/1491957662/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=quantpytho-20&creative=9325&linkCode=as2&creativeASIN=1491957662&linkId=ea8de4253cce96046e8ab0383ac71b33" target="_blank">Python for Data Analysis by Wes McKinney</a>
# MAGIC * <a href="https://www.pythoncheatsheet.org/" target="_blank">Python reference sheet</a>
# MAGIC * <a href="https://docs.python.org/3/tutorial/" target="_blank">Python official tutorial</a>
# MAGIC
# MAGIC Documentation to help with <a href="https://forums.databricks.com/static/markdown/help.html" target="_blank">markdown cells</a>.

# COMMAND ----------

# MAGIC %md ### Calculation
# MAGIC
# MAGIC To get started, let's use Python to calculate some mathematical expressions. Can you guess what this will evaluate to?

# COMMAND ----------

1 + 1

# COMMAND ----------

# MAGIC %md ### Comments
# MAGIC
# MAGIC In addition to markdown cells, we can annotate our code through [comments](https://www.w3schools.com/python/python_comments.asp). Comments are optional, but can help explain a line of code in context. They are not executed.
# MAGIC
# MAGIC In Python, **`#`** is a reserved keyword to represent a comment. Any characters following it on the line are treated as part of the comment.
# MAGIC
# MAGIC > Hint: If you have lines of code selected in a notebook cell, you can press `ctrl + /` you to comment or uncomment that block of code. Try adding your own comments below.

# COMMAND ----------

# This is our first line of python code
# this is my other line of code
1 + 1

# COMMAND ----------

# MAGIC %md # Data Types
# MAGIC
# MAGIC Python provides basic [**Data Types**](https://www.w3schools.com/python/python_datatypes.asp), each with their own operations. 
# MAGIC
# MAGIC Let's look at a few of them and the operations we can apply to each of them.

# COMMAND ----------

# MAGIC %md ### Type 1: Integers
# MAGIC
# MAGIC Integers (or int) are non-decimal whole numbers. 
# MAGIC
# MAGIC **Data**: Integer values (e.g. -2, -1, 0, 1, 2 ...)
# MAGIC
# MAGIC **Example Operations**: +, -, *, /

# COMMAND ----------

 # Integer expression
2 * 3 + 5 -1

# COMMAND ----------

# MAGIC %md ### Type 2: Float
# MAGIC
# MAGIC Float (or floating point) is a number containing a decimal. 
# MAGIC
# MAGIC **Data**: Decimal Values (e.g. -2.342, -1.3, 0.45, 1.1, 2.2 ...)
# MAGIC
# MAGIC **Example Operations**: +, -, *, /

# COMMAND ----------

1.5 + 1.5

# COMMAND ----------

# MAGIC %md If you are unsure what type something is, you can pass it into **`type()`**.

# COMMAND ----------

type(1)

# COMMAND ----------

# MAGIC %md ### Type 3: Strings
# MAGIC
# MAGIC Strings (or str) are a sequence of characters surrounded by quotation marks (i.e. **`""`** or **`''`**). They are just text, but can contain numbers, punctuation, etc.
# MAGIC
# MAGIC For example, `"Hello World!"` or `'Hello World!'`.
# MAGIC
# MAGIC **Data**: Text (e.g. "Hello", "I love Python", "3.14abc")
# MAGIC
# MAGIC **Example Operations**: Concatenation (+)
# MAGIC
# MAGIC Note that when you use the `+` operator on an integer or float it adds the values, but for strings it concatenates them. The operations differ between types. 

# COMMAND ----------

# String expression
"Hello " + "World"

# COMMAND ----------

# MAGIC %md 
# MAGIC Notice that the concatenation operation does **not** insert a space. If we wanted `Hello World`, we would have to add a space in the string.

# COMMAND ----------

# String expression with a space
"Hello" + " " + "World"

# COMMAND ----------

# MAGIC %md 
# MAGIC **Question:** If you add a float and string together, what is the result? Uncomment then execute the code below to find out.

# COMMAND ----------

# concatenate a string and an integer
"Hello" + 1

# COMMAND ----------

# MAGIC %md ### Type 4: Boolean
# MAGIC
# MAGIC Boolean (or bool) is a binary data type. There are only two boolean values: **`True`** and **`False`**.
# MAGIC
# MAGIC > Python is **case-sensitive**, and these boolean values must be title-case. You will get a Python error if you try to use variants like **`true`** or **`FALSE`**.
# MAGIC
# MAGIC **Data**: True, False
# MAGIC
# MAGIC **Example Operations**: logical operators (i.e. or, and, not)

# COMMAND ----------

type(True)

# COMMAND ----------

# MAGIC %md # Variables
# MAGIC
# MAGIC We can store the result of an expression in a [variable](https://www.w3schools.com/python/python_variables.asp), which we can then use to refer to the result of that expression. It's very helpful if you plan to re-use the same value multiple times. There should be only one variable assignment per line.
# MAGIC
# MAGIC **`variable_name = expression`**
# MAGIC
# MAGIC A few things to note on Python variable names from <a href="https://www.w3schools.com/python/gloss_python_variable_names.asp#:~:text=Rules%20for%20Python%20variables%3A,0%2D9%2C%20and%20_%20" target="_blank">W3 Schools</a>:
# MAGIC * A variable name must start with a letter or the underscore character
# MAGIC * A variable name cannot start with a number
# MAGIC * A variable name can contain only alpha-numeric characters and underscores (A-z, 0-9, and _ )
# MAGIC * Variable names are case-sensitive (**`age`**, **`Age`** and **`AGE`** are three different variables)

# COMMAND ----------

a = 10
b = 2
c = a*b

print(c)

# COMMAND ----------

# MAGIC %md Question: If we update the value of **`b`**, what happens to **`c`**?

# COMMAND ----------

b = 20
print(b)
print(a)

# COMMAND ----------

# MAGIC %md ### Variable State
# MAGIC
# MAGIC Variables are accessible across cells in the same notebook. If you restart your cluster or detach your notebook from your cluster, you will not lose your code, but you will lose the state of the variables. 
# MAGIC
# MAGIC **Exercise**: Try detaching and reattaching this notebook. Are you still able to run the command above successfully?

# COMMAND ----------

a = 5
b = 2
c = a*b

print(c)

# COMMAND ----------

# MAGIC %md ### Weakly Typed Languages
# MAGIC
# MAGIC
# MAGIC Python is a *weakly typed* language. That means any variable can hold any type of value, and you can overwrite a variable to have any type of value. In other words, you can assign a new value to a variable that is of a different type than its original value.

# COMMAND ----------

#b = 4
b = "Hello World"
b

# COMMAND ----------

type(b)

# COMMAND ----------

# MAGIC %md ### Naming Conventions
# MAGIC
# MAGIC While you can name Python variables almost anything and it will work, the general convention in Python is to use **`snake_case`**. This means all of the characters should be lower case, and spaces are replaced with an `_` character.
# MAGIC
# MAGIC For example, **`my_first_variable`** is a better name than **`MyFirst_variable`**. 
# MAGIC
# MAGIC Try to avoid variable re-use. For example, you would not want to use **`address`** as a variable name referring to a house address, then later use **`address`** again referring to an IP address. You would want to use something like **`house_address`** and **`ip_address`** instead.
# MAGIC
# MAGIC Also try to use variable names that describe their contents to make your Python code easier to read and understand.
# MAGIC
# MAGIC And don't use variable names that are too long. Would you really want to type **`first_appearance_of_the_word_in_this_file`** multiple times in your program?

# COMMAND ----------

my_first_variable = 'hello'
print(my_first_variable)

# COMMAND ----------

# MAGIC %md
# MAGIC # Print Statements
# MAGIC
# MAGIC In Databricks or Jupyter notebooks, the result of last line executed in a cell is printed automatically.
# MAGIC
# MAGIC If you want to see more than just the evaluation of the last line, you need to use a **`print`** statement.
# MAGIC
# MAGIC To use it, write **`print(expression)`** to see the value of the expression displayed.

# COMMAND ----------

a = 1
b = 2

# COMMAND ----------

print(a)
print(b)

# COMMAND ----------

# MAGIC %md In addition to printing variable values, you can also print strings.

# COMMAND ----------

print("Hello world")

# COMMAND ----------

# MAGIC %md #### f-string Formatting
# MAGIC
# MAGIC You can also print out variable and strings together using [f-string](https://www.w3schools.com/python/python_string_formatting.asp) formatting. Put an **`f`** at the beginning of the quotes, and place the variable inside of curly braces. The syntax looks like **`f"optional text {insert_variable_here} optional text"`**.

# COMMAND ----------

name = 'Dan'
favorite_dog = "German Shephard"

print(f'My name is {name} and my favorite dog is a {favorite_dog}')

# COMMAND ----------

# MAGIC %md
# MAGIC # STOP
# MAGIC Try out lab `ITP 01L - Data Types and Variables Lab` located at:
# MAGIC
# MAGIC   `200_intro_to_python/Labs/01L_Data_Types_and_Variables_Lab`

# COMMAND ----------

# MAGIC %md # Next: if-statement
# MAGIC
# MAGIC Python by default evaluates every line of code from top to bottom, sequentially. But what if we want to define conditional logic to control which code should be executed? 
# MAGIC
# MAGIC The order in which Python runs our code is called **control flow**, and Python provides functionality we can use to change the control flow. 
# MAGIC
# MAGIC The first tool Python provides for us is the **if-statement**. 
# MAGIC
# MAGIC We write an [**if-statement**](https://www.w3schools.com/python/gloss_python_if_statement.asp) like this:
# MAGIC
# MAGIC
# MAGIC     if bool:
# MAGIC         code_1
# MAGIC     else:
# MAGIC         code_2
# MAGIC       
# MAGIC `bool` here is a boolean expression, evaluating to either **`True`** or **`False`**
# MAGIC
# MAGIC Think of this as a fork in the road. Python will read the boolean at the top, then if it is **`True`**, it will execute **`code_1`** not **`code_2`**
# MAGIC
# MAGIC If it is **`False`**, it will skip **`code_1`** and only execute **`code_2`**
# MAGIC
# MAGIC Let's look at some examples

# COMMAND ----------

# define a simple if statement
dog = "Lab"
name = 'Dan'

if dog == "Lab":
  print(f"A {dog} is {name}'s favorite dog")
else:
  print(f"A {dog} is NOT {name}'s favorite dog")

# COMMAND ----------

# MAGIC %md ## Operators
# MAGIC
# MAGIC Now that we can use **if-statements**, let's take a look at some boolean expressions we can use with them. 
# MAGIC
# MAGIC Recall the boolean operators **`and`**, **`or`**, and **`not`**.
# MAGIC
# MAGIC Python will evaluate the boolean expression of an **if-statement** to **`True`** or **`False`**, and then act accordingly. 
# MAGIC
# MAGIC So far we have only seen expressions composed of one type that evaluate to the same type.
# MAGIC
# MAGIC For example:
# MAGIC
# MAGIC **`True or False -> True`**
# MAGIC
# MAGIC **`1 + 2 -> 3`**
# MAGIC
# MAGIC We can also have expressions composed of one type that evaluate to a different type. 
# MAGIC
# MAGIC We'll look at the **`<`**, **`>`**, **`<=`**, **`>=`**, **`==`**, and **`!=`** operators, which are defined for multiple other types but evaluate to booleans. 
# MAGIC
# MAGIC
# MAGIC | <    | > | <= | >= | == | != |
# MAGIC | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
# MAGIC | Less than   | Greater than    | Less than or equal to     | Greater than or equal to    | Equal to     | Not equal to      |
# MAGIC | **`a < b -> bool`**    | **`a > b -> bool`**        |**`a <= b -> bool`**   | **`a >= b -> bool`**       |**`a == b -> bool`**   | **`a != b -> bool`**      |
# MAGIC
# MAGIC **Note:** **`=`** is used for variable assignment, **`==`** is used for equality comparison

# COMMAND ----------

# define a multi-part if statement
age = 2
dog = 'Lab'
name = 'Dan'

if dog == 'Lab' and age < 1:
  print(f"This IS {name}'s favorite dog")
else:
  print(f"This is NOT {name}'s favorite dog")

# COMMAND ----------

# MAGIC %md
# MAGIC %md
# MAGIC ## Functions
# MAGIC
# MAGIC In this lesson, we're going to see how we can use <a href="https://www.w3schools.com/python/python_functions.asp" target="_blank">functions</a> to make code reusable.
# MAGIC
# MAGIC We define a function like this:
# MAGIC
# MAGIC       def function_name(parameters):
# MAGIC           function_code
# MAGIC
# MAGIC
# MAGIC Notice the **`def`** keyword, followed by the name of the function, any parameters in parentheses, and a colon. 
# MAGIC
# MAGIC We've actually already been using functions: **`print()`** is a function that is pre-defined in Python.

# COMMAND ----------

# define a function
def favorite_dog(dog, age, name):
  if dog == 'Lab' and age < 1:
    print(f"This IS {name}'s favorite dog")
  else:
    print(f"This is NOT {name}'s favorite dog")

# COMMAND ----------

# call the function
dog = 'pitbull'

favorite_dog(dog, .5, name)

# COMMAND ----------

# MAGIC %md ### Built-in Functions
# MAGIC
# MAGIC Python provides some built-in <a href="https://docs.python.org/3/library/functions.html" target="_blank">functions</a> for common operations. 
# MAGIC
# MAGIC Some notable ones include **`print()`**, which we have seen, **`lower()`** converts everything to lowercase **`replace()`** which replaces characters in a string

# COMMAND ----------

# define text
text = 'hello world'

# chain together functions
text.upper()

# COMMAND ----------

# MAGIC %md
# MAGIC # STOP
# MAGIC Try out lab `ITP 03L - Functions Lab` located at:
# MAGIC
# MAGIC   `200_intro_to_python/Labs/ITP 03L - Functions Lab`

# COMMAND ----------

# MAGIC %md
# MAGIC # Dataframes
# MAGIC
# MAGIC A DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
# MAGIC
# MAGIC **Indexing:** DataFrames have both row and column labels (indexes). This makes it easy to access and manipulate specific data elements.
# MAGIC
# MAGIC **Functionality**
# MAGIC - **Creating DataFrames:** You can create DataFrames from various sources like dictionaries, lists, CSV files, Excel files, and SQL databases.
# MAGIC - **Accessing Data:** You can access specific rows, columns, or individual elements using indexing and slicing techniques.
# MAGIC - **Manipulating Data:** You can perform operations like adding, deleting, renaming columns, filtering rows based on conditions, sorting data, and merging/joining multiple DataFrames.
# MAGIC - **Cleaning Data:** Pandas provides powerful tools for handling missing data, duplicate values, and data type conversions.
# MAGIC - **Analyzing Data:** You can calculate summary statistics, group data for aggregated analysis, and perform statistical operations on DataFrame columns.
# MAGIC
# MAGIC
# MAGIC <img src="https://i.postimg.cc/mDKywPW3/structure-table.jpg" alt="drawing" width="300"/>
# MAGIC
# MAGIC
# MAGIC
# MAGIC
# MAGIC <br>
# MAGIC
# MAGIC ## Using Pandas to create DataFrames
# MAGIC Pandas is the most popular open-source Python library designed for data maniuplation and analysis. It lets you create DataFrames by reading tables or files (e.g., CSV, Excel, SQL) or by defining your own data structures, making it simple to work with tabular datasets.
# MAGIC
# MAGIC ### PLEASE NOTE
# MAGIC Pandas is the most common open-source Python library for creating DataFrames to work with tabular data. 
# MAGIC
# MAGIC However, pandas has scaling limitations, and **Databricks recommends using Spark DataFrames instead.**
# MAGIC - **PySpark:** The Python API for Spark—lets you create and manipulate Spark DataFrames at scale.
# MAGIC
# MAGIC In this lesson, we’ll demonstrate both approaches, although **Spark DataFrames are almost always preferred for their performance benefits.**
# MAGIC
# MAGIC We’ll cover Spark and its integration with Python (via PySpark) in the next lesson.
# MAGIC
# MAGIC **For the purposes of demonstration, we will demonstrate both Pandas and Spark DataFrames.**
# MAGIC

# COMMAND ----------

# import the pandas library to your python session and give it an alias so you can refer to its classes
import pandas as pd

# Create a list of dog breeds with their country of origin
data = {
    "breed": ["Labrador Retriever", 
              "German Shorthair Pointer", 
              "Golden Retriever", 
              "Bulldog", 
              "Great Dane"]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC You can find the `dog_breeds.csv` file to upload to your own volume located [here.](https://sp-cloud.kp.org/:f:/r/sites/DatabricksKP401/Shared%20Documents/General/SAS%20to%20Databricks%20Training/200_intro_to_python?csf=1&web=1&e=rUDTBP)

# COMMAND ----------

# Read in data from a CSV file to a pandas DataFrame
df = pd.read_csv('/Volumes/ae_prod/dar_stg/dar_stg_vol/dog_breeds.csv')

# render the results
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # Read a CSV using PySpark DataFrame
# MAGIC The following examples will show you how to read a csv into a DataFrame using **Spark** (PySpark is the Python API for Spark), the recommended approach for creating DataFrames and working with data in Databricks.

# COMMAND ----------

# Read in data from a CSV file to a spark DataFrame
df = spark.read.csv('/Volumes/ae_prod/dar_stg/dar_stg_vol/dog_breeds.csv')

# render the results
df.display()

# COMMAND ----------

# create a table from the dataframe using PySpark
df.write.format('delta').mode('overwrite').option('overwriteSchema', 'true').saveAsTable('ae_prod.dar_stg.dog_breeds')

# COMMAND ----------

# read in data from a table to a dataframe using PySpark
df = spark.table('ae_prod.dar_stg.dog_breeds')

# render the results
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC **Hint:** You can convert a DataFrame to a temporary view so that you can perform additional operations using SQL!

# COMMAND ----------

# create a temporary view of the dataframe so you can query it using SQL
df.createOrReplaceTempView('my_dog_breeds')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM my_dog_breeds

# COMMAND ----------

# MAGIC %md
# MAGIC # Perform Data Manipulation on the DataFrame using Spark (instead of Pandas)
# MAGIC I am demonstrating maniupulating data using Spark instead of Pandas because it is considered a best practice. 
# MAGIC
# MAGIC There are lots of examples of how to manipulate data using Pandas on the internet if you are interested. 
# MAGIC
# MAGIC If you ask AI code assistants (e.g. Co-Pilot) to write python code to do something to a DataFrame, often times it will provide that recommendation using pandas. It is impoprtant that you specify using Spark in prompt to the AI code assistants!

# COMMAND ----------

#import the col function from the module
from pyspark.sql.functions import col

# Filter the dataframe where nickname contains "retriever"
df = df.filter(col('nickname').like('%retriever%'))

# render the results
df.display()

# COMMAND ----------

# import the lit function
from pyspark.sql.functions import lit

# add a new column to the dataframe
family_friendly = 'Yes'

# rename a column
df = df.withColumn('family_friendly_dog', lit(family_friendly))

# render the results
display(df)

# COMMAND ----------

# count number of records
df.count()

# assign the value to a variable
number_of_records = df.count()

# print the number of records
print(f'There are {number_of_records} record(s) in the dataframe')

# COMMAND ----------

# create a temp view
df.createOrReplaceTempView('my_new_temp_view')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM my_new_temp_view

# COMMAND ----------

# use python and SQL TOGETHER!!
df = spark.sql('SELECT * FROM my_temp_view WHERE nickname = "Lab" ')

# render the results
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC **Congratulations! You have finished your first lesson on Python!**

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
