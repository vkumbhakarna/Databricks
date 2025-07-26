# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Advanced Pandas
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:
# MAGIC * Explore some more advanced features pandas provides including:
# MAGIC   - Renaming columns
# MAGIC   - Filtering the DataFrame
# MAGIC   - Grouping and aggregation Functions
# MAGIC   - Sorting
# MAGIC   - Imputing columns

# COMMAND ----------

# MAGIC %md For this lesson, we are going to work with datasets. Running the cell below will define and give us access to variables defining the path to our datasets in the Databricks File System.

# COMMAND ----------

# MAGIC %run "./Includes/Classroom-Setup"

# COMMAND ----------

# MAGIC %md Remember, to access **`pandas`** functionality, we must **`import`** the library first. We do not have to **`pip install pandas`** because we already have it installed.

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# MAGIC %md ## Reading Data
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/301/sf.jpg" style="height: 200px; margin: 10px; border: 1px solid #ddd; padding: 10px"/>
# MAGIC
# MAGIC So far we have created a DataFrame by manually specifying the rows and columns. Often, we will have a dataset stored as a CSV (comma-separated-value) file. 
# MAGIC
# MAGIC **`pandas`** provides a function called [**read_csv(path)**](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html), where we provide a path to where our CSV file is stored, and it returns a DataFrame of the contents at that path.
# MAGIC
# MAGIC You'll be analyzing data from <a href="http://insideairbnb.com/get-the-data.html" target="_blank">Inside Airbnb</a> to better understand the San Francisco rental market. Let's read in the dataset.

# COMMAND ----------

file_path = f"{datasets_dir}/sf-airbnb/sf-airbnb.csv".replace("dbfs:", "/dbfs")
df = pd.read_csv(file_path)

# COMMAND ----------

# MAGIC %md To look at the first few records of the dataset, we can call [**head()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html). If you do not specify the number of rows, it defaults to 5 rows.

# COMMAND ----------

df.head(3)

# COMMAND ----------

# MAGIC %md Conversely, we can call [**tail()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html) to look at the last few records. 

# COMMAND ----------

df.tail(3)

# COMMAND ----------

# MAGIC %md ## Renaming Columns
# MAGIC
# MAGIC We can rename columns of our DataFrame using [**rename()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html). We pass into columns a dictionary containing the mappings from the old column names to the new ones to the **`columns`** parameter.
# MAGIC
# MAGIC Let's rename the **`neighbourhood`** column above to be **`neighborhood`**.

# COMMAND ----------

df = df.rename(columns={"neighbourhood": "neighborhood"})
df[["id", "neighborhood"]].head(10)

# COMMAND ----------

# MAGIC %md ## Filtering
# MAGIC
# MAGIC Often, you will want to select a subset of rows that meet a certain criteria, which can be accomplished by specifying: **`df[bool_array]`**, where **`bool_array`** is a **`Series`** of **`True`** and **`False`** values for each row. 
# MAGIC
# MAGIC The rows that evaluate to **`True`** are kept, while the ones that evaluate to **`False`** are not. 
# MAGIC
# MAGIC Let's filter for all the rows **`host_is_superhost`** is **`"t"`**, meaning the airbnb owner is a superhost.

# COMMAND ----------

filtered_df = df[df["host_is_superhost"] == "t"]
filtered_df[["id", "host_is_superhost"]].head(10)

# COMMAND ----------

# MAGIC %md Here, **`df["host_is_superhost"] == "t"]`** is our boolean array. Let's take a look at the corresponding **True/False** row indices.

# COMMAND ----------

df["host_is_superhost"] == "t"

# COMMAND ----------

# MAGIC %md We can also search for all the records where the **`host_is_superhost`** is NOT "t".

# COMMAND ----------

df["host_is_superhost"] != "t"

# COMMAND ----------

# MAGIC %md ## Pandas Boolean Operators
# MAGIC
# MAGIC Often you will want to evaluate multiple criteria to filter out records. For example, let's select all records where the host is a superhost and the airbnb has at least 150 reviews.
# MAGIC
# MAGIC Instead of the normal Boolean operators we have seen previously, we have [bitwise Boolean operators](https://www.w3schools.com/python/gloss_python_bitwise_operators.asp):
# MAGIC * **`and`** -> **`&`**
# MAGIC * **`or`** -> **`|`** 
# MAGIC * **`not`** -> **`~`**

# COMMAND ----------

filtered_df = df[(df["host_is_superhost"] == "t") & (df["number_of_reviews"] >= 150)]
filtered_df[["id", "host_is_superhost", "number_of_reviews"]].head(10)

# COMMAND ----------

# MAGIC %md ## Aggregate Functions
# MAGIC
# MAGIC Aggregate functions are functions that take in a series of inputs and return a single output. 
# MAGIC
# MAGIC The most common ones that we use in pandas are ones that take in numerical **`Series`** and return a statistic of interest, such as the mean. 
# MAGIC
# MAGIC Let's take a look at the mean, min, and max of **`number_of_reviews`**:

# COMMAND ----------

print(df["number_of_reviews"].mean())
print(df["number_of_reviews"].min())
print(df["number_of_reviews"].max())

# COMMAND ----------

# MAGIC %md Another useful method is [**describe()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) which provides a report of summary statistics on a given numerical **`Series`**:

# COMMAND ----------

df["number_of_reviews"].describe()

# COMMAND ----------

# MAGIC %md We can also use this method on a DataFrame to see it applied to every numerical column:

# COMMAND ----------

df[["number_of_reviews", "host_listings_count", "bedrooms"]].describe()

# COMMAND ----------

# MAGIC %md Many times, you won't care about the 6th value after the decimal. Let's round our results by calling [**round()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html?highlight=round#pandas.DataFrame.round).

# COMMAND ----------

df[["number_of_reviews", "host_listings_count", "bedrooms"]].describe().round(2)

# COMMAND ----------

# MAGIC %md ## Group By
# MAGIC
# MAGIC Sometimes we will want to see the results of an aggregate function per category in a non-numerical column. 
# MAGIC
# MAGIC For example, say we wanted to see the average number of bedrooms per neighborhood.
# MAGIC
# MAGIC In order to do this we first use the [**groupby([columns])**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) method and specific the category we want to group by. In this case, let's group by **`neighborhood`**.

# COMMAND ----------

df.groupby(["neighborhood"])

# COMMAND ----------

# MAGIC %md Then we apply the aggregate function of interest. In this case, **`mean()`** to the column of interest, in this case **`bedrooms`**.
# MAGIC
# MAGIC **Note:** Here we use **`[["bedrooms"]]`** to select for bedrooms because we could add other columns in addition to bedrooms.

# COMMAND ----------

grouped_df = df.groupby(["neighborhood"])[["bedrooms"]].mean().head(10)
grouped_df

# COMMAND ----------

# MAGIC %md ## Reset Index
# MAGIC Typically, row indices are numbers, but they can also be named. In the example above, **`neighborhood`** is now the row index, rather than a column. 
# MAGIC
# MAGIC We can see that if we print out the columns.

# COMMAND ----------

grouped_df.columns

# COMMAND ----------

# MAGIC %md To reset the index to be numbers, and move the current index to be a column, we use [**reset_index()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html).

# COMMAND ----------

reset_df = grouped_df.reset_index()
reset_df

# COMMAND ----------

# MAGIC %md ## Sorting
# MAGIC
# MAGIC Pandas provides a [**sort_values()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html) method to sort the rows in a **`DataFrame`** or **`Series`**.
# MAGIC
# MAGIC If called on a **`DataFrame`** you need to specify which column you are sorting by like this **`df.sort_values([col])`**

# COMMAND ----------

sorted_df = df.sort_values(["bedrooms"])
sorted_df[["id","bedrooms"]].head(10)

# COMMAND ----------

# MAGIC %md If applied to a **`Series`** there is only one column, so you don't need to specify:

# COMMAND ----------

df["bedrooms"].sort_values()

# COMMAND ----------

# MAGIC %md By default **`sort_values()`** sorts in ascending order. You can specify the **`ascending=False`** parameter to change it to descending order.

# COMMAND ----------

df["bedrooms"].sort_values(ascending=False)

# COMMAND ----------

# MAGIC %md ## NaN 
# MAGIC
# MAGIC You might have noticed that our **`DataFrame`** contains NaN values. These indicate a missing value. 
# MAGIC
# MAGIC We have a few ways we can handle missing values. Often having these values present causes problems for computational tasks.
# MAGIC
# MAGIC First, we can check using the [**isna()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html#pandas.DataFrame.isna) method, alias for [**isnull()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html#pandas.DataFrame.isnull), and the **`sum()`** method to count the number of NaN values present.

# COMMAND ----------

nan_df = df[["security_deposit", "notes"]] # subset of columns with NaNs
nan_df

# COMMAND ----------

nan_df.isna().sum()

# COMMAND ----------

# MAGIC %md ## Dropping NaN
# MAGIC
# MAGIC One way you can handle NaN is to drop all rows that have NaN values. We can use the [**dropna()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html) method to do that.

# COMMAND ----------

nan_df.dropna()

# COMMAND ----------

# MAGIC %md ### Impute Columns
# MAGIC
# MAGIC However, we are throwing away a lot of information when we drop records - in the example above, we removed over 3000 rows.
# MAGIC
# MAGIC Instead of dropping rows with missing values, we can impute the missing values using [**fillna()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html) and specifying a default value to use.

# COMMAND ----------

nan_df.fillna("Missing")

# COMMAND ----------

# MAGIC %md Oftentimes, we want to impute different values to different columns. For example, with `numeric` values, we can impute with the mean/median/etc. For `categorical` features, imputing with the mode or a special category are common.
# MAGIC
# MAGIC Let's instead specify that **`security_deposit`** is `$0.00` if it is missing. We can pass in a dictionary to **`fillna()`** that has column names as the key and the value to impute the column with as the value. 
# MAGIC
# MAGIC You can optionally specify **`inplace=True`** if you want to update the underlying DataFrame.

# COMMAND ----------

nan_df.fillna({"security_deposit": "$0.00", "notes": "Missing"}, inplace=False)

# COMMAND ----------

# MAGIC %md ## Write to CSV
# MAGIC
# MAGIC We can write a **`pandas`** DataFrame to a CSV file as shown below using the [**to_csv()**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) method.

# COMMAND ----------

file_path = working_dir.replace("dbfs:", "/dbfs") + ".csv"
df.to_csv(file_path, index=False)

# COMMAND ----------

# MAGIC %md We can then read our csv file back in with **`read_csv`**.

# COMMAND ----------

load_df = pd.read_csv(file_path)
load_df.head()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
