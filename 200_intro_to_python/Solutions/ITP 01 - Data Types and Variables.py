# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Data Types and Variables
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br>
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

1+1 

# COMMAND ----------

# MAGIC %md ### Comments
# MAGIC
# MAGIC In addition to markdown cells, we can annotate our code through [comments](https://www.w3schools.com/python/python_comments.asp). Comments are optional, but can help explain a line of code in context. They are not executed.
# MAGIC
# MAGIC In Python, **`#`** is a reserved keyword to represent a comment. Any characters following it on the line are treated as part of the comment.
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_hint_24.png" alt="Hint:"> If you have lines of code selected in a notebook cell, you can press `ctrl + /` you to comment or uncomment that block of code. Try adding your own comments below.

# COMMAND ----------

# This is our first line of Python code!
1+1 

# COMMAND ----------

# MAGIC %md ## Data Types
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
2 * 3 + 5 - 1 

# COMMAND ----------

# MAGIC %md ### Type 2: Float
# MAGIC
# MAGIC Float (or floating point) is a number containing a decimal. 
# MAGIC
# MAGIC **Data**: Decimal Values (e.g. -2.342, -1.3, 0.45, 1.1, 2.2 ...)
# MAGIC
# MAGIC **Example Operations**: +, -, *, /

# COMMAND ----------

1.2 * 2.3 + 5.5

# COMMAND ----------

# MAGIC %md If you are unsure what type something is, you can pass it into **`type()`**.

# COMMAND ----------

type(1.2)

# COMMAND ----------

# MAGIC %md Question: Is `1.` a float or an int? Let's test it by checking its type. 

# COMMAND ----------

type(1.)

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
"Hello" + "123"

# COMMAND ----------

# MAGIC %md Notice that the concatenation operation does **not** insert a space. If we wanted "Hello 123", we would have to add a space in the string.

# COMMAND ----------

# String expression with a space
"Hello" + " " + "123"

# COMMAND ----------

# MAGIC %md Question: If you add a float and string together, what is the result? Uncomment then execute the code below to find out.

# COMMAND ----------

# "Hello" + 123

# COMMAND ----------

# MAGIC %md ### Type 4: Boolean
# MAGIC
# MAGIC Boolean (or bool) is a binary data type. There are only two boolean values: **`True`** and **`False`**.
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_warn_24.png" alt="Caution"> Python is **case-sensitive**, and these boolean values must be title-case. You will get a Python error if you try to use variants like **`true`** or **`FALSE`**.
# MAGIC
# MAGIC **Data**: True, False
# MAGIC
# MAGIC **Example Operations**: logical operators (i.e. or, and, not)

# COMMAND ----------

True or False

# COMMAND ----------

True and False

# COMMAND ----------

not False

# COMMAND ----------

# MAGIC %md ## Variables
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

a = 3
b = 2
c = a*b

c

# COMMAND ----------

# MAGIC %md Question: If we update the value of **`b`**, what happens to **`c`**?

# COMMAND ----------

b = 4
c

# COMMAND ----------

# MAGIC %md ### Variable State
# MAGIC
# MAGIC Variables are accessible across cells in the same notebook. If you restart your cluster or detach your notebook from your cluster, you will not lose your code, but you will lose the state of the variables. 
# MAGIC
# MAGIC **Exercise**: Try detaching and reattaching this notebook. Are you still able to run the command above successfully?

# COMMAND ----------

# MAGIC %md ### Weakly Typed Languages
# MAGIC
# MAGIC
# MAGIC Python is a *weakly typed* language. That means any variable can hold any type of value, and you can overwrite a variable to have any type of value. In other words, you can assign a new value to a variable that is of a different type than its original value.
# MAGIC
# MAGIC In contrast, *strongly typed* languages &mdash; such as C and Java &mdash; do not allow this. 

# COMMAND ----------

b = "Hello World"
b

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

my_first_variable = 2

# COMMAND ----------

# MAGIC %md
# MAGIC ## Print Statements
# MAGIC
# MAGIC In Databricks or Jupyter notebooks, the result of last line executed in a cell is printed automatically.
# MAGIC
# MAGIC If you want to see more than just the evaluation of the last line, you need to use a **`print`** statement.
# MAGIC
# MAGIC To use it, write **`print(expression)`** to see the value of the expression displayed.

# COMMAND ----------

a = 1
b = 2

a # This line isn't printed because it's not the last line of code
b

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

name = "Robin"
age = 30

print(f"My name is {name} and I am {age} years old")

# COMMAND ----------

# MAGIC %md
# MAGIC **Congratulations! You have finished your first lesson on Python!**

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
