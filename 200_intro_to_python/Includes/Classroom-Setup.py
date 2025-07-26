# Databricks notebook source
spark.conf.set("com.databricks.training.module-name", "introduction-to-python-for-data-science-and-data-engineering")

# COMMAND ----------

# MAGIC %run "./Class-Utility-Methods"

# COMMAND ----------

import re

username = getUsername()
cleaned_username = re.sub("[^a-zA-Z0-9]", "_", username.lower().split("@")[0])

userhome = getUserhome()
course_dir = getCourseDir()
datasets_dir = f"{course_dir}/datasets"
working_dir = getWorkingDir()

None # Suppress output

# COMMAND ----------

def path_exists(path):
  try:
    return len(dbutils.fs.ls(path)) >= 0
  except Exception:
    return False

def install_datasets(reinstall=False):
  min_time = "1 min"
  max_time = "5 min"

  # You can swap out the source_path with an alternate version during development
  # source_path = f"dbfs:/mnt/work-xxx/{course_name}"
  source_path = f"wasbs://courseware@dbacademy.blob.core.windows.net/introduction-to-python-for-data-science-and-data-engineering/v01"
  print(f"The source for this dataset is\n{source_path}/\n")
  
  # Change the final directory to another name if you like, e.g. from "datasets" to "raw"
  target_dir = f"{datasets_dir}"
  print(f"Your dataset directory is\n{target_dir}\n")
  existing = path_exists(target_dir)

  if not reinstall and existing:
    print(f"Skipping install of existing dataset.")
    return 

  # Remove old versions of the previously installed datasets
  if existing:
    print(f"Removing previously installed datasets from\n{target_dir}")
    dbutils.fs.rm(target_dir, True)
  
  print(f"""Installing the datasets to {target_dir}""")
  
  print(f"""\nNOTE: The datasets that we are installing are located in Washington, USA - depending on the
      region that your workspace is in, this operation can take as little as {min_time} and 
      upwards to {max_time}, but this is a one-time operation.""")

  dbutils.fs.cp(f"{source_path}", f"{target_dir}", True)

  print(f"""\nThe install of the datasets completed successfully.""")  

try:
  reinstall = dbutils.widgets.get("reinstall").lower() == "true"
  install_datasets(reinstall=reinstall)
except:
  install_datasets(reinstall=False)

None # Suppress output

