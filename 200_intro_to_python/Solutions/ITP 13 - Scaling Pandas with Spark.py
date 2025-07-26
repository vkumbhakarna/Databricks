# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Scaling Pandas with Spark
# MAGIC
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br>
# MAGIC - Demonstrate the similarities of the pandas API on Spark API with the pandas API
# MAGIC - Understand the differences in syntax for the same DataFrame operations in pandas API on Spark vs PySpark

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Recall from the cloud computing lesson the open source technology [Apache Spark](https://spark.apache.org/), which is an open-source data processing engine that manages distributed processing of large data sets. 
# MAGIC
# MAGIC In this course, we have been using Pandas, which is a great library for data analysis, but it only runs on one machine, it is not distributed. Luckily, we can use Spark just like traditional Pandas with the Pandas API on Spark. 
# MAGIC
# MAGIC The pandas API on Spark project makes data scientists more productive when interacting with big data, by implementing the pandas DataFrame API on top of Apache Spark. By unifying the two ecosystems with a familiar API, pandas API on Spark offers a seamless transition between small and large data. 
# MAGIC
# MAGIC See this <a href="https://databricks.com/blog/2021/10/04/pandas-api-on-upcoming-apache-spark-3-2.html" target="_blank">blog post</a> for more information on using Pandas syntax on Spark.

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC <div style="img align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://files.training.databricks.com/images/301/31gb.png" width="900"/>
# MAGIC </div>
# MAGIC
# MAGIC <div style="img align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://files.training.databricks.com/images/301/95gb.png" width="900"/>
# MAGIC </div>
# MAGIC
# MAGIC **Pandas** DataFrames are mutable, eagerily evaluated, and maintain row order. They are restricted to a single machine, and are very performant when the data sets are small, as shown in a).
# MAGIC
# MAGIC **Spark** DataFrames are distributed, lazily evaluated, immutable, and do not maintain row order. They are very performant when working at scale, as shown in b) and c).
# MAGIC
# MAGIC **pandas API on Spark** provides the best of both worlds: pandas API with the performance benefits of Spark. However, it is not as fast as implementing your solution natively in Spark, and let's see why below.

# COMMAND ----------

# MAGIC %md ## InternalFrame
# MAGIC
# MAGIC The InternalFrame holds the current Spark DataFrame and internal immutable metadata.
# MAGIC
# MAGIC It manages mappings from pandas API on Spark column names to Spark column names, as well as from pandas API on Spark index names to Spark column names. 
# MAGIC
# MAGIC If a user calls some API, the pandas API on Spark DataFrame updates the Spark DataFrame and metadata in InternalFrame. It creates or copies the current InternalFrame with the new states, and returns a new pandas API on Spark DataFrame.
# MAGIC
# MAGIC <div style="img align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://files.training.databricks.com/images/301/InternalFramePs.png" width="900"/>
# MAGIC </div>

# COMMAND ----------

# MAGIC %md ### Read in the dataset
# MAGIC
# MAGIC * PySpark
# MAGIC * pandas
# MAGIC * pandas API on Spark

# COMMAND ----------

# MAGIC %run "./Includes/Classroom-Setup"

# COMMAND ----------

# MAGIC %md Just like how we can read in data from a CSV file in pandas, we can read in data from a file in spark. 

# COMMAND ----------

spark_df = spark.read.csv(f"{datasets_dir}/sf-airbnb/sf-airbnb.csv", header="true", inferSchema="true", multiLine="true", escape='"')
display(spark_df)

# COMMAND ----------

# MAGIC %md Read in CSV with pandas

# COMMAND ----------

import pandas as pd

pandas_df = pd.read_csv(f"{datasets_dir}/sf-airbnb/sf-airbnb.csv".replace("dbfs:", "/dbfs"))
pandas_df.head()

# COMMAND ----------

# MAGIC %md Read in CSV with pandas API on Spark. You'll notice pandas API on Spark generates an index column for you, like in pandas.

# COMMAND ----------

import pyspark.pandas as ps

df = ps.read_csv(f"{datasets_dir}/sf-airbnb/sf-airbnb.csv", inferSchema="true", multiLine="true", escape='"')
df.head()

# COMMAND ----------

# MAGIC %md ### <a href="https://koalas.readthedocs.io/en/latest/user_guide/options.html#default-index-type" target="_blank">Index Types</a>
# MAGIC
# MAGIC ![](https://files.training.databricks.com/images/301/koalas_index.png)

# COMMAND ----------

ps.set_option("compute.default_index_type", "distributed-sequence")
df_dist_sequence = ps.read_csv(f"{datasets_dir}/sf-airbnb/sf-airbnb.csv", inferSchema="true", multiLine="true", escape='"')
df_dist_sequence.head()

# COMMAND ----------

# MAGIC %md ### Converting to pandas API on Spark DataFrame to/from Spark DataFrame

# COMMAND ----------

# MAGIC %md Creating a pandas API on Spark DataFrame from PySpark DataFrame

# COMMAND ----------

df = ps.DataFrame(spark_df)
display(df)

# COMMAND ----------

# MAGIC %md Alternative way of creating a pandas API on Spark DataFrame from PySpark DataFrame

# COMMAND ----------

df = spark_df.to_pandas_on_spark()
display(df)

# COMMAND ----------

# MAGIC %md Go from a pandas API on Spark DataFrame to a Spark DataFrame

# COMMAND ----------

display(df.to_spark())

# COMMAND ----------

# MAGIC %md ### Value Counts

# COMMAND ----------

# MAGIC %md Get value counts of the different property types with PySpark

# COMMAND ----------

display(spark_df.groupby("property_type").count().orderBy("count", ascending=False))

# COMMAND ----------

# MAGIC %md Get value counts of the different property types with pandas API on Spark

# COMMAND ----------

df["property_type"].value_counts()

# COMMAND ----------

# MAGIC %md ### Visualizations
# MAGIC
# MAGIC Based on the type of visualization, the pandas API on Spark has optimized ways to execute the plotting.
# MAGIC <br><br>
# MAGIC
# MAGIC ![](https://files.training.databricks.com/images/301/ps_plotting.png)

# COMMAND ----------

df["bedrooms"].hist(bins=20)

# COMMAND ----------

# MAGIC %md ### SQL on pandas API on Spark DataFrames

# COMMAND ----------

ps.sql("SELECT distinct(property_type) FROM {df}")

# COMMAND ----------

# MAGIC %md ### Interesting Facts
# MAGIC
# MAGIC * With pandas API on Spark you can read from Delta Tables and read in a directory of files
# MAGIC * If you use apply on a pandas API on Spark DF and that DF is <1000 (by default), pandas API on Spark will use pandas as a shortcut - this can be adjusted using **`compute.shortcut_limit`**
# MAGIC * When you create bar plots, the top n rows are only used - this can be adjusted using **`plotting.max_rows`**
# MAGIC * How to utilize **`.apply`** <a href="https://koalas.readthedocs.io/en/latest/reference/api/databricks.koalas.DataFrame.apply.html#databricks.koalas.DataFrame.apply" target="_blank">docs</a> with its use of return type hints similar to pandas UDFs
# MAGIC * How to check the execution plan, as well as caching a pandas API on Spark DF (which aren't immediately intuitive)
# MAGIC * Koalas are marsupials whose max speed is 30 kph (20 mph)

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
