# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Loops
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lab you:<br>
# MAGIC
# MAGIC Apply concepts learned in the last lesson, including:
# MAGIC - Utilizing for-loops to handle more advanced control flow
# MAGIC - Using list comprehension to filter lists

# COMMAND ----------

# MAGIC %md ## Exercise: Bart Simpson in Detention
# MAGIC
# MAGIC <img src="https://preview.redd.it/386z0p2eh5v21.jpg?auto=webp&s=383ef3536776dc3a34515e6cfd9979f363570a05" width="40%" height="20%">
# MAGIC
# MAGIC Bart Simpson got detention again... He needs to write **`I will not let my dog eat my homework`** 50 times. Of course, Bart is lazy, and needs your help to automate this in Python. 
# MAGIC
# MAGIC Write a function called **`detention_helper()`** that takes in **`detention_message`** and **`num_lines`** representing the message Bart needs to write and the number of times he needs to write it respectively. 
# MAGIC
# MAGIC Your function should print out **`detention_message`** **`num_lines`** times, but each line of **`detention_message`** should be numbered. 
# MAGIC
# MAGIC For example, if **`detention_message`** is `I will not let my dog eat my homework`, and **`num_lines`** is 50, the function should print
# MAGIC
# MAGIC `1. I will not let my dog eat my homework`
# MAGIC
# MAGIC `2. I will not let my dog eat my homework`
# MAGIC
# MAGIC `3. I will not let my dog eat my homework`
# MAGIC
# MAGIC `.
# MAGIC .
# MAGIC .`
# MAGIC
# MAGIC `50. I will not let my dog eat my homework`
# MAGIC
# MAGIC
# MAGIC Here, we are parameterizing the **`detention_message`** and **`num_lines`** in case he gets detention again.
# MAGIC
# MAGIC **Hint:** Recall the **`range()`** function, but make sure to start counting at 1, not 0. f-string formatting will also be helpful.

# COMMAND ----------

# TODO
def detention_helper(detention_message, num_lines):
    FILL_IN

# COMMAND ----------

# MAGIC %md 
# MAGIC Call your function below with the correct inputs for Bart's current detention and make sure you can see "I will not let my dog eat my homework" printed out 50 times, with the lines numbered, as shown in the problem description.

# COMMAND ----------

# TODO
detention_helper(FILL_IN, FILL_IN)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
