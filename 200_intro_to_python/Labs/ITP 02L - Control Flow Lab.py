# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Control Flow
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lab you:<br>
# MAGIC
# MAGIC Apply basic control flow concepts in Python we learned last lesson, including:
# MAGIC
# MAGIC * **`if`** and **`elif`** statements
# MAGIC * More boolean operators
# MAGIC * Type checking

# COMMAND ----------

# MAGIC %md ### Food Recommender
# MAGIC
# MAGIC For this lab, write the control flow logic for the following food recommender. Users provide the following input:
# MAGIC
# MAGIC *  **`temperature`**: A float representing the temperature outside (in Fahrenheit)
# MAGIC *  **`sunny`**: A boolean set to **`True`** if it is sunny outside, **`False`** otherwise. 
# MAGIC
# MAGIC Write the system to print the following recommendations:
# MAGIC
# MAGIC * If it is at least 60 degrees outside AND it is sunny, recommend `ice cream`.
# MAGIC * If it is at least 60 degrees outside, but it is not sunny, recommend `dumplings`.
# MAGIC * If if it is less than 60 degrees, regardless of the weather, recommend `hot tea`. 

# COMMAND ----------

# TODO
temperature = TODO
sunny = TODO

# COMMAND ----------

# MAGIC %md Try changing the values of **`temperature`** and **`sunny`** and make sure it recommends the proper foods!

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
