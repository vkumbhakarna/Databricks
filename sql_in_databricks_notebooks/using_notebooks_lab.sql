-- Databricks notebook source
-- MAGIC %md-sandbox
-- MAGIC
-- MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
-- MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
-- MAGIC </div>

-- COMMAND ----------

-- DBTITLE 0,--i18n-4212c527-b1c1-4cce-b629-b5ffb5c57d68
-- MAGIC %md
-- MAGIC
-- MAGIC # Getting Started with the Databricks Platform
-- MAGIC
-- MAGIC This notebook provides a hands-on review of some of the basic functionality of a Databricks Notebook for SQL jobs.
-- MAGIC
-- MAGIC ## Learning Objectives
-- MAGIC By the end of this lab, you should be able to:
-- MAGIC - Rename a notebook and change the default language
-- MAGIC - Attach a SQL Warehouse
-- MAGIC - Create a Markdown cell
-- MAGIC - Run SQL and create re-usable SQL results while working
-- MAGIC - Share a notebook
-- MAGIC - Schedule a notebook
-- MAGIC - Use the Databricks Assistant to help debug

-- COMMAND ----------

-- DBTITLE 0,--i18n-eb166a05-9a22-4a74-b54e-3f9e5779f342
-- MAGIC %md
-- MAGIC
-- MAGIC # Step 1: Renaming a Notebook
-- MAGIC > ### **TO DO:** Rename the notebook to **_ReplaceWithYourName Databricks Workshop_**
-- MAGIC
-- MAGIC Changing the name of a notebook is easy. Click on the name at the top of this page, then make changes to the name. To make it easier to navigate back to this notebook later in case you need to, append a short test string to the end of the existing name.

-- COMMAND ----------

-- DBTITLE 0,--i18n-a975b60c-9871-4736-9b4f-194577d730f0
-- MAGIC %md
-- MAGIC
-- MAGIC # Step 2: Attaching to Compute (SQL Warehouse)
-- MAGIC > ###**TO DO:** Make sure the default language for your notebook is SQL
-- MAGIC > ###**TO DO:** Attach compute to this notebook now by clicking the dropdown near the top-right corner of this page and selecting the appropriate compute name.
-- MAGIC
-- MAGIC Executing cells in a notebook requires compute resources! The first time you execute a cell in a notebook, you will be prompted to attach to compute if it is not already attached.
-- MAGIC
-- MAGIC **Two types of Compute to Execute Commands in Notebooks:**
-- MAGIC - **SQL Warehouse:** On-demand elastic compute optimized to run SQL commands. Can only run SQL commands, it cannot run queries in other languages (e.g. python).
-- MAGIC
-- MAGIC - **All Purpose Compute:** General compute used for interactive development when you need to run queries or processes in python or multiple languages (e.g. r, python, SQL, etc.). We will learn more about this in later sessions.
-- MAGIC
-- MAGIC *_Note Your selected compute should say <img src="https://i.postimg.cc/c49BwXDt/2024-07-29-15-43-02.png" style="float: right" width="35px"> next to it. This means you have selected a SQL Warehouse and it is optimized to run SQL queries and thus can only execute SQL queries. Compute without <img src="https://i.postimg.cc/c49BwXDt/2024-07-29-15-43-02.png" style="float: right" width="35px">  next to the compute name can run queries and execute code in multiple languages (e.g. python)_
-- MAGIC
-- MAGIC *_Note that the dropdown menu provides the option to `detach & re-attach`. This is useful for clearing the execution state when needed._

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # Step 3: Run a SQL cell
-- MAGIC > ### **TO DO:** Add a new code cell and execute some SQL to view the results
-- MAGIC
-- MAGIC **Steps:**
-- MAGIC 1. Add a new code cell below this, and either write your own query or copy and paste the following code into the cell: 
-- MAGIC ```
-- MAGIC SELECT COUNT(*) AS no_of_customers
-- MAGIC FROM samples.tpch.customer
-- MAGIC ```
-- MAGIC 2. Run the cell to see the result

-- COMMAND ----------



-- COMMAND ----------

-- DBTITLE 0,--i18n-478faa69-6814-4725-803b-3414a1a803ae
-- MAGIC %md
-- MAGIC
-- MAGIC # Step 4: Create a Markdown Cell
-- MAGIC
-- MAGIC > #### **TO DO:** Add a new **Text** cell below this one. Populate with some Markdown that includes some of the following elements:
-- MAGIC * A header
-- MAGIC * Bullet points
-- MAGIC * Optional: A link (using your choice of HTML or Markdown conventions)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # Step 6: Temporary Views
-- MAGIC
-- MAGIC > #### **TO DO:** Create a simple temporary view using the empty code cell below
-- MAGIC > #### **TO DO:** Using the other code cell below, write a query that selects the results from the temporary view (e.g. `SELECT * FROM...`)
-- MAGIC
-- MAGIC
-- MAGIC Temporary views are the foundation for creating a multi-step program/process in a notebook when using SQL!
-- MAGIC
-- MAGIC Temporary views are virtual tables that are based on the result of a SQL query. They are not stored in the catalog and are only visible to the current session, similar to that of a `temporary table` in other databases. They are automatically dropped when the session ends or when you explicitly drop them using `DROP VIEW`. Temporary views allow you to reuse the result of a complex query without creating a permanent table!
-- MAGIC
-- MAGIC - _Note: A temporary View created in one notebook isn't accessible to others!_ Temporary views are visible only to the session that created them and are dropped when the session ends.
-- MAGIC
-- MAGIC ### Temporary Views or CTEs?
-- MAGIC Temporary views can be an excellent complement—or even substitute—for CTEs when you need to break complex logic into reusable, inspectable building blocks:
-- MAGIC
-- MAGIC **Session-wide reuse**
-- MAGIC - CTEs exist only within the single SQL statement that defines them.
-- MAGIC - Temp views persist for your entire  session, so you can reference the same intermediate result across multiple independent queries without redefining it each time.
-- MAGIC
-- MAGIC **Improved readability & modularity**
-- MAGIC - Instead of a single gigantic `WITH … SELECT …` block, you can layer logic:
-- MAGIC   1. Create step-by-step temp views (`step1_view`, `step2_view`, …)
-- MAGIC   2. Then `SELECT` or join them in your final analysis.
-- MAGIC - This makes each piece easier to develop, test, and debug in isolation.
-- MAGIC
-- MAGIC **Performance tuning & caching**
-- MAGIC - You can cache a temp view in memory (`CACHE TABLE`) so that expensive transformations run once and serve many downstream queries.
-- MAGIC - CTEs get re-evaluated each time you reference them in the same statement, which can waste work if your CTE is used multiple times.
-- MAGIC
-- MAGIC ### How do you create a temporary view?
-- MAGIC **Syntax:**
-- MAGIC <br>`CREATE OR REPLACE TEMPORARY VIEW view_name AS query`
-- MAGIC
-- MAGIC **<br>Example of a temporary view:**
-- MAGIC
-- MAGIC ```
-- MAGIC CREATE OR REPLACE TEMP VIEW daily_revenue
-- MAGIC AS (
-- MAGIC   SELECT
-- MAGIC     date_format(o_orderdate, 'yyyy-MM-dd') AS day,
-- MAGIC     SUM(o_totalprice) AS revenue
-- MAGIC   FROM samples.tpch.orders
-- MAGIC   GROUP BY ALL
-- MAGIC );
-- MAGIC ```

-- COMMAND ----------

-- create a temporary view

-- COMMAND ----------

-- select from the temporary view you created


-- COMMAND ----------

-- MAGIC %md
-- MAGIC # Step 7: Run the entire notebook
-- MAGIC > #### **TO DO:** Run all cells in this notebook using the **_Run All_** button

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # Step 8: Share the notebook
-- MAGIC
-- MAGIC > #### **TO DO:** Share a notebook with a coworker
-- MAGIC
-- MAGIC <br>To share a notebook with a coworker, click <img src="https://i.postimg.cc/PJ4ZMCrX/share.png" style="float: right" width="50px"> at the top of the notebook.
-- MAGIC <br>The Sharing dialog opens, which you can use to select who to share the notebook with and what level of access they have. Share with a colleague or a group!
-- MAGIC
-- MAGIC **Notebook permissions** <br>
-- MAGIC <img src="https://i.postimg.cc/sg8WKdyh/perms.png">

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # Step 9: Create a schedule
-- MAGIC > ###**TO DO:** create a schedule for the notebook job to run. 
-- MAGIC
-- MAGIC > **_Please Note:_** _Make sure you select a **Manual** schedule since this is a training. We don't need this to run periodically and incur additional costs!_
