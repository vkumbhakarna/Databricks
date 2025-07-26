# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Pandas Lab
# MAGIC
# MAGIC In this lab, you will use <a href="https://pandas.pydata.org/docs/" target="_blank">pandas</a> for basic data manipulation.

# COMMAND ----------

# MAGIC %md #### Problem 1: Create a `DataFrame`
# MAGIC
# MAGIC Create the a **`DataFrame`** called **`df`** representing the table below of dogs. The data is included below.
# MAGIC
# MAGIC | Name    | Age | Breed| 
# MAGIC | ----------- | ----------- | ----------- | 
# MAGIC | Buddy   | 3    | Australian Shepherd |
# MAGIC | Harley    | 10       | Labrador |
# MAGIC | Luna     | 2       | Golden Retriever | 
# MAGIC | Bailey | 8 | Chihuahua |  

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# TODO
data = [["Buddy", 3, "Australian Shepherd"], ["Harley", 10, "Labrador"], ["Luna", 2, "Golden Retriever"], ["Bailey", 8, "Chihuahua"]]]

column_names = # FILL_IN

df = # FILL_IN
df

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC <button onclick="myFunction2()" >Click for Hint</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC   Remember to specify the data and columns attributes
# MAGIC </div>
# MAGIC <script>
# MAGIC function myFunction2() {
# MAGIC   var x = document.getElementById("myDIV2");
# MAGIC   if (x.style.display === "none") {
# MAGIC     x.style.display = "block";
# MAGIC   } else {
# MAGIC     x.style.display = "none";
# MAGIC   }
# MAGIC }
# MAGIC </script>

# COMMAND ----------

# MAGIC %md **Check your work by running the cell below**

# COMMAND ----------

assert (df.columns == ["Name", "Age", "Breed"]).all(), "The columns are named incorrectly"
assert [df.iloc[0][x] for x in ["Name", "Age", "Breed"]] == ["Buddy", 3, "Australian Shepherd"], "First row defined incorrectly"
assert [df.iloc[1][x] for x in ["Name", "Age", "Breed"]] == ["Harley", 10, "Labrador"], "Second row defined incorrectly"
assert [df.iloc[2][x] for x in ["Name", "Age", "Breed"]] == ["Luna", 2, "Golden Retriever"], "Third row defined incorrectly"
assert [df.iloc[3][x] for x in ["Name", "Age", "Breed"]] == ["Bailey", 8, "Chihuahua"], "Fourth row defined incorrectly"
print("Test passed!")

# COMMAND ----------

# MAGIC %md #### Problem 2: What are the `dtypes`?
# MAGIC
# MAGIC Print out the **`dtypes`** attribute of your DataFrame to see the types of each column. 

# COMMAND ----------

# TODO

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC <button onclick="myFunction2()" >Click for Hint</button>
# MAGIC
# MAGIC <div id="myDIV2" style="display: none;">
# MAGIC   Remember we access attributes like this: object.attribute
# MAGIC </div>
# MAGIC <script>
# MAGIC function myFunction2() {
# MAGIC   var x = document.getElementById("myDIV2");
# MAGIC   if (x.style.display === "none") {
# MAGIC     x.style.display = "block";
# MAGIC   } else {
# MAGIC     x.style.display = "none";
# MAGIC   }
# MAGIC }
# MAGIC </script>

# COMMAND ----------

# MAGIC %md #### Problem 3: Subset of Columns
# MAGIC
# MAGIC Select only the **`Name`** and **`Age`** columns, assigning to the new variable **`name_age_df`**.

# COMMAND ----------

# TODO
name_age_df = TODO
name_age_df

# COMMAND ----------

# MAGIC %md **Check your work by running the cell below**
# MAGIC
# MAGIC The assert below uses [**iloc**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html) to do integer-location based indexing for selection by position.

# COMMAND ----------

assert (name_age_df.columns == ["Name", "Age"]).all(), "The columns are named incorrectly"
assert name_age_df.shape == (4, 2), "There are not the right number of rows or columns"
assert [name_age_df.iloc[0][x] for x in ["Name", "Age"]] == ["Buddy", 3], "First row defined incorrectly"
assert [name_age_df.iloc[1][x] for x in ["Name", "Age"]] == ["Harley", 10], "Second row defined incorrectly"
assert [name_age_df.iloc[2][x] for x in ["Name", "Age"]] == ["Luna", 2], "Third row defined incorrectly"
assert [name_age_df.iloc[3][x] for x in ["Name", "Age"]] == ["Bailey", 8], "Fourth row defined incorrectly"
print("Test passed!")

# COMMAND ----------

# MAGIC %md #### Problem 4: Create a New Column
# MAGIC
# MAGIC Let's assume one year in dog years is equal to 7 years in human years. Create a new column called **`Human Age`** in our **`df`** that takes the dog's age and multiples it by 7.

# COMMAND ----------

# TODO

# COMMAND ----------

# MAGIC %md **Check your work by running the cell below**

# COMMAND ----------

assert df.shape == (4, 4), "There are not the correct number of rows or columns"
assert (df.columns == ["Name", "Age", "Breed", "Human Age"]).all(), "The columns are named incorrectly"
assert [df.iloc[0][x] for x in ["Name", "Age", "Breed", "Human Age"]] == ["Buddy", 3, "Australian Shepherd", 21], "First row defined incorrectly"
assert [df.iloc[1][x] for x in ["Name", "Age", "Breed", "Human Age"]] == ["Harley", 10, "Labrador", 70], "Second row defined incorrectly"
assert [df.iloc[2][x] for x in ["Name", "Age", "Breed", "Human Age"]] == ["Luna", 2, "Golden Retriever", 14], "Third row defined incorrectly"
assert [df.iloc[3][x] for x in ["Name", "Age", "Breed", "Human Age"]] == ["Bailey", 8, "Chihuahua", 56], "Fourth row defined incorrectly"
print("Test passed!")

# COMMAND ----------

# MAGIC %md #### Problem 5: Extract a value
# MAGIC
# MAGIC Programmatically extract Buddy's **`Breed`** from the DataFrame and assign it to the given **`breed`** variable.

# COMMAND ----------

# TODO
breed = TODO
breed

# COMMAND ----------

# MAGIC %md **Check your work by running the cell below**

# COMMAND ----------

assert breed == "Australian Shepherd", "Breed is not defined correctly"
print("Test passed!")

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
