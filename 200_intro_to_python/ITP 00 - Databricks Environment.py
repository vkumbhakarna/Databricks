# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # The Databricks Environment
# MAGIC   
# MAGIC References:
# MAGIC * Databricks documentation on <a href="https://docs.databricks.com/" target="_blank">AWS</a>, <a href="https://docs.microsoft.com/en-us/azure/databricks/" target="_blank">Azure</a>, and <a href="https://docs.gcp.databricks.com/" target="_blank">GCP</a>

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ## Run code
# MAGIC
# MAGIC * Each notebook specifies a default language, in this case **Python**.
# MAGIC * Run the cell below using one of the following options:
# MAGIC   * **CTRL+ENTER** or **CMD+RETURN**
# MAGIC   * **SHIFT+ENTER** or **SHIFT+RETURN** to run the cell and move to the next one
# MAGIC   * Using **Run Cell**, **Run All Above** or **Run All Below** as seen here<br/><img style="box-shadow: 5px 5px 5px 0px rgba(0,0,0,0.25); border: 1px solid rgba(0,0,0,0.25);" src="https://files.training.databricks.com/images/notebook-cell-run-cmd.png"/>
# MAGIC
# MAGIC Feel free to tweak the code below if you like:

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Mix Languages: Magic Commands
# MAGIC
# MAGIC By default, cells use the default language of the notebook. You can override the default language in a cell by clicking the language button and selecting a language from the dropdown menu.
# MAGIC
# MAGIC
# MAGIC
# MAGIC Alternately, you can use the language magic command `%` at the beginning of a cell. The supported magic commands are: 
# MAGIC - `%python` 
# MAGIC - `%r`
# MAGIC - `%scala`
# MAGIC - `%sql`
# MAGIC
# MAGIC Auxiliary magic commands:
# MAGIC - `%sh`: Allows you to run shell code in your notebook. To fail the cell if the shell command has a non-zero exit status, add the -e option. This command runs only on the Apache Spark driver, and not the workers. To run a shell command on all nodes, use an init script.
# MAGIC
# MAGIC - `%fs`: Allows you to use dbutils filesystem commands. For example, to run the dbutils.fs.ls command to list files, you can specify %fs ls instead. For more information, see Work with files on Databricks.
# MAGIC
# MAGIC - `%md`: Allows you to include various types of documentation, including text, images, and mathematical formulas and equations. See the next section.

# COMMAND ----------

print("I'm running Python!")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "I'm running SQL"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Magic Command: &percnt;md
# MAGIC
# MAGIC Our favorite Magic Command **&percnt;md** allows us to render Markdown in a cell:
# MAGIC * Double click this cell to begin editing it
# MAGIC * Then press the **`Esc`** key to stop editing
# MAGIC
# MAGIC # Title One
# MAGIC ## Title Two
# MAGIC ### Title Three
# MAGIC
# MAGIC This is a test of the emergency broadcast system. This is only a test.
# MAGIC
# MAGIC This is text with a **bold** word in it.
# MAGIC
# MAGIC This is text with an *italicized* word in it.
# MAGIC
# MAGIC This is an ordered list
# MAGIC
# MAGIC 0. once
# MAGIC 0. two
# MAGIC 0. three
# MAGIC
# MAGIC This is an unordered list
# MAGIC
# MAGIC * apples
# MAGIC * peaches
# MAGIC * bananas
# MAGIC
# MAGIC Links/Embedded HTML: <a href="http://bfy.tw/19zq" target="_blank">What is Markdown?</a>
# MAGIC
# MAGIC Images:  
# MAGIC ![Spark Engines](https://files.training.databricks.com/images/Apache-Spark-Logo_TM_200px.png)
# MAGIC
# MAGIC And of course, tables:
# MAGIC
# MAGIC | Name  | Age | Breed    |
# MAGIC |-------|-----|--------|
# MAGIC | Buddy   | 2  | Golden Retriever   |
# MAGIC | Bingo  | 10  | Border Collie |
# MAGIC | Momo  | 3  | Lab   |

# COMMAND ----------

# MAGIC %md
# MAGIC ## Learning More
# MAGIC
# MAGIC We like to encourage you to explore the documentation to learn more about the various features of the Databricks platform and notebooks.
# MAGIC * <a href="https://docs.databricks.com/user-guide/index.html" target="_blank">User Guide</a>
# MAGIC * <a href="https://docs.databricks.com/user-guide/notebooks/index.html" target="_blank">User Guide / Notebooks</a>
# MAGIC * <a href="https://docs.databricks.com/administration-guide/index.html" target="_blank">Administration Guide</a>
# MAGIC * <a href="https://docs.databricks.com/release-notes/index.html" target="_blank">Release Notes</a>
# MAGIC * <a href="https://docs.databricks.com/" target="_blank">And much more!</a>

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
