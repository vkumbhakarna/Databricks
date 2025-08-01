# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

username = spark.sql("SELECT current_user()").first()[0]
course_dir = f"file:///dbfs/user/{username}/dbacademy/introduction_to_python_for_data_science_and_data_engineering"

print(f"Removing course directory: {course_dir}")
dbutils.fs.rm(course_dir, True)

# COMMAND ----------

# MAGIC %run "./Classroom-Setup"

# COMMAND ----------

display(dbutils.fs.ls(datasets_dir))

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
