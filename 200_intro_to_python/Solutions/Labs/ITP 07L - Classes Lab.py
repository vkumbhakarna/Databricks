# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Classes
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lab you:<br>
# MAGIC
# MAGIC Apply concepts learned in the last lesson, including:
# MAGIC - Utilizing instance attributes to define data for new data types
# MAGIC - Using methods to add functionality to new data types

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ## Exercise: Simpson
# MAGIC
# MAGIC <img src="https://i.pinimg.com/originals/13/63/37/13633734d116fe188af57fe9da7d095e.jpg" style="height:400">
# MAGIC
# MAGIC Define a class **`Simpson`** representing members of the Simpson's family that has the following attributes and methods:
# MAGIC
# MAGIC * Each Simpson has a **`first_name`**, **`age`**, and **`favorite_food`**. 
# MAGIC   * Define the **`__init__()`** method to initialize these attributes. 
# MAGIC   
# MAGIC * Define a method called **`simpson_summary()`** which returns a string in this format: `{first_name} Simpson is {age} years old and their favorite food is {favorite_food}`
# MAGIC   * For example, if `first_name="Homer"`, `age=39`, and `favorite_food="donuts"`, this should return: `Homer Simpson is 39 years old and their favorite food is donuts`
# MAGIC   
# MAGIC * Define a method called **`older()`** which takes in another **`Simpson`** object and returns **`True`** if the person that called the method is older than the other one, **`False`** otherwise.

# COMMAND ----------

# ANSWER
class Simpson():
    
    def __init__(self, first_name, age, favorite_food):
        self.first_name = first_name
        self.age = age
        self.favorite_food = favorite_food
        
    def simpson_summary(self):
        return f"{self.first_name} Simpson is {self.age} years old and their favorite food is {self.favorite_food}"
        
    def older(self, other_simpson):
        return self.age > other_simpson.age

# COMMAND ----------

# MAGIC %md **Check your work:**

# COMMAND ----------

homer = Simpson("Homer", 39, "Donuts")
bart = Simpson("Bart", 10, "Hamburgers")
assert homer.first_name == "Homer", "first_name is not set properly"
assert homer.favorite_food == "Donuts", "favorite_food is not set properly"
assert bart.age == 10, "Age is not set properly"
assert homer.simpson_summary() == "Homer Simpson is 39 years old and their favorite food is Donuts", "simpson_summary is incorrect"
assert bart.simpson_summary() == "Bart Simpson is 10 years old and their favorite food is Hamburgers", "simpson_summary is incorrect"
assert homer.older(bart) == True, "Homer is older than Bart"
assert bart.older(homer) == False, "Bart is not older than Homer"
print("Test passed!")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
