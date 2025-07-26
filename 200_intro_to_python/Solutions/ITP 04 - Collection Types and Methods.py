# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Collection Types and Methods
# MAGIC
# MAGIC ## ![Spark Logo Tiny](https://files.training.databricks.com/images/105/logo_spark_tiny.png) In this lesson you:<br>
# MAGIC
# MAGIC - Introduce objects and methods
# MAGIC - Create lists
# MAGIC - Use methods on new collection data types

# COMMAND ----------

# MAGIC %md ## Objects
# MAGIC
# MAGIC In this lesson we are first going to look at some new functionality provided by data types, and then see how we can use that in some new data types. But before we do that, we need to look at some terminology.
# MAGIC
# MAGIC An [**object**](https://www.w3schools.com/python/python_classes.asp) is an instance of a specific data type. 
# MAGIC
# MAGIC For example, **`1`** is an Integer, so we would call it an Integer object. **`"Hello"`** is a String, so we would call it a String object. 

# COMMAND ----------

# MAGIC %md ## Methods: More Functionality
# MAGIC
# MAGIC As a reminder, data types provide **data** of some kind and **operations** we can do on that kind of data. So far, we have actually only looked at a small fraction of the operations provided by each type. 
# MAGIC
# MAGIC Data types provide special functions called [**methods**](https://www.w3schools.com/python/gloss_python_object_methods.asp) which provide more functionality. Methods are exactly like normal functions except we call them on objects and they can edit the object they are called on. We invoke a method like this:
# MAGIC
# MAGIC **`object.method_name(arguments)`**
# MAGIC
# MAGIC This is a little tricky and we have a whole lesson on these coming up, but right now all you need to know is:
# MAGIC
# MAGIC **Methods are functions provided by a data type that we can call on objects of that type. They act on the object we call them with and allow us to use more functionality provided by that data type**

# COMMAND ----------

# MAGIC %md ### String Methods
# MAGIC
# MAGIC Let's take a look at an example of a method on a type we already know well: Strings. Strings provide a method called [**upper()**](https://www.w3schools.com/python/ref_string_upper.asp) which capitalizes a String.

# COMMAND ----------

greeting = "hello"
print(greeting.upper())
print(greeting)

# COMMAND ----------

# MAGIC %md ### In-place methods
# MAGIC
# MAGIC Methods are functions that act on objects, and can either perform operations in-place (modify the underlying object it was called upon) or return a new object.
# MAGIC
# MAGIC Notice that the method **`upper()`** was not a stateful, in-place method as it returned a new string and did not modify the **`greeting`** variable. Take a look <a href="https://www.w3schools.com/python/python_ref_string.asp" target="_blank">W3Schools</a> provides information on other string methods in Python. 

# COMMAND ----------

# MAGIC %md ### Tab Completion
# MAGIC
# MAGIC If you want to see a list of methods you can apply to an object, type **`.`** after the object, then hit tab key to see a drop down menu of available methods on that object.
# MAGIC
# MAGIC Try it below on the **`greeting`** string object. Type **`greeting.`** then hit the Tab key.

# COMMAND ----------

# Type . and hit Tab
greeting

# COMMAND ----------

# MAGIC %md ### `help()`
# MAGIC
# MAGIC While using tab completion is extremely helpful, if we use it to look through all possible methods for a given object, we might still not be certain how those methods work.
# MAGIC
# MAGIC We can look up their documentation, or we can use the [**help()**](https://www.geeksforgeeks.org/help-function-in-python/) function we saw last lesson.
# MAGIC
# MAGIC As a reminder, the **`help()`** function displays some of the documentation for the item passed into it.
# MAGIC
# MAGIC For example, when using tab completion above, we see the [**capitalize()**](https://www.w3schools.com/python/ref_string_capitalize.asp) string method, but we are not certain how it works.

# COMMAND ----------

help(greeting.capitalize)

# COMMAND ----------

greeting.capitalize()

# COMMAND ----------

# MAGIC %md ## Methods with Collection Types
# MAGIC
# MAGIC Now that we have a brief understanding of methods, let's look at some more advanced data types and the methods they provide.
# MAGIC
# MAGIC We are going to look at **collection data types** next. Like the name suggests, the data in these data types is a collection of other data types. 

# COMMAND ----------

# MAGIC %md ### Collection Type 1: Lists
# MAGIC
# MAGIC A list is just an ordered sequence of items. 
# MAGIC
# MAGIC It is defined as a sequence of comma separated items inside square brackets like this: **`[item1, item2, item3...]`**
# MAGIC
# MAGIC The items may be of any type, though in practice you'll usually create lists where all of the values are of the same type.
# MAGIC
# MAGIC Let's make a <a href="https://www.w3schools.com/python/python_lists.asp" target="_blank">list</a> of what everyone ate for breakfast this morning.
# MAGIC
# MAGIC <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Scrambed_eggs.jpg/1280px-Scrambed_eggs.jpg" width="20%" height="10%">

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles"]
breakfast_list

# COMMAND ----------

# Python can tell us breakfast_list's type
type(breakfast_list)

# COMMAND ----------

# MAGIC %md We'll use our **`breakfast_list`** as the running example, but note that the values in a list can be of any type, as shown below.

# COMMAND ----------

# any type works
["hello", True, 1, 1.5]

# COMMAND ----------

# MAGIC %md #### List Methods
# MAGIC
# MAGIC Now that we understand the **data** a list data type provides, let's look at some of its **functionality**.
# MAGIC
# MAGIC Something you will frequently want to do is add a new item to an existing list. 
# MAGIC
# MAGIC Lists provide a method called [**append()**](https://www.w3schools.com/python/ref_list_append.asp) to do just that. 
# MAGIC
# MAGIC **`append()`** takes in an argument of any type and edits the list it is called on so that the argument is stuck onto the end of the list. 
# MAGIC
# MAGIC Let's say after we ate our pancakes, eggs, and waffles, we also had yogurt.
# MAGIC
# MAGIC Here, we can use **`append()`** to add yogurt to our **`breakfast_list`**.

# COMMAND ----------

breakfast_list.append("yogurt")
breakfast_list

# COMMAND ----------

# MAGIC %md **Note:** Notice here that **`append()`** is an in-place method.
# MAGIC The method does not return a new list, but rather edits the original **`breakfast_list`** object. 
# MAGIC
# MAGIC **`+`** is also defined as concatenation for lists as shown below.

# COMMAND ----------

["pancakes", "eggs"] + ["waffles", "yogurt"]

# COMMAND ----------

# MAGIC %md While we typically use **`append()`**, it is possible to append elements to a list using **`+`**.

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles"]
breakfast_list = breakfast_list + ["yogurt"]
breakfast_list

# COMMAND ----------

# MAGIC %md A useful shortcut operation for this is **`+=`**.
# MAGIC
# MAGIC **`breakfast_list`** `+=` **`["yogurt"]`** is the same thing is **`breakfast_list`** `=` **`breakfast_list`** `+` **`["yogurt"]`**.
# MAGIC
# MAGIC The **`+=`** operator works for other types as well, using their respective **`+`** operator.

# COMMAND ----------

breakfast_list = ["pancakes", "eggs", "waffles"]
breakfast_list += ["yogurt"]
breakfast_list

# COMMAND ----------

# MAGIC %md #### List indexing
# MAGIC
# MAGIC Often, we want to reference a specific item or items in a list. This called [list indexing](https://www.w3schools.com/python/python_lists_access.asp).
# MAGIC
# MAGIC Lists provide an operation to get the item at a certain index in the list like this:
# MAGIC
# MAGIC       list_name[index]
# MAGIC
# MAGIC In Python indices start from 0, so the first element of the list is 0, the second is 1, etc. 

# COMMAND ----------

breakfast_list[0]

# COMMAND ----------

# MAGIC %md We can also use negative indexing, which starts counting from right to left, starting from -1. 
# MAGIC
# MAGIC Thus, the last element of the list is -1, the second to last is -2, etc.

# COMMAND ----------

breakfast_list[-1]

# COMMAND ----------

# MAGIC %md We can also provide a range of indices we want to access like this:
# MAGIC
# MAGIC **`list_name[start:stop]`**
# MAGIC
# MAGIC This returns a list of the values starting at **`start`** and up to but not including **`stop`**.

# COMMAND ----------

# Note the stop index is exclusive
breakfast_list[0:2]

# COMMAND ----------

# MAGIC %md If we don't provide a start index, Python assumes we start at the beginning.
# MAGIC
# MAGIC If we don't provide a stop index, Python assumes we stop at the end. 

# COMMAND ----------

print(breakfast_list[:2])
print(breakfast_list[1:])

# COMMAND ----------

# MAGIC %md We can also change the value of an index in a list to be something new like this:

# COMMAND ----------

print(breakfast_list)
breakfast_list[0] = "sausage"

print(breakfast_list)

# COMMAND ----------

# MAGIC %md We can also use **`in`** to check if an element is in a given list. This is a boolean operation:

# COMMAND ----------

"waffles" in breakfast_list

# COMMAND ----------

# MAGIC %md
# MAGIC ### Collection Type 2: Dictionaries
# MAGIC
# MAGIC A [Dictionary](https://www.w3schools.com/python/python_dictionaries.asp) is a sequence of key-value pairs. We define a dictionary as follows:
# MAGIC
# MAGIC `{key_1: value_1, key_2: value_2, ...}`
# MAGIC
# MAGIC The keys and values can all be of any type. However, because each key maps to a value, it is important that *all keys are unique*.
# MAGIC
# MAGIC Let's create a breakfast dictionary, where the keys are the type of food and the values are the number of those foods we ate for breakfast.

# COMMAND ----------

breakfast_dict = {"pancakes": 1, "eggs": 2, "waffles": 3}
breakfast_dict

# COMMAND ----------

# MAGIC %md #### Dictionary Methods
# MAGIC
# MAGIC Dictionaries provide the method [**dict_object.get()**](https://www.w3schools.com/python/ref_dictionary_get.asp) to get the value in the dictionary for the given argument. 
# MAGIC
# MAGIC Let's see how many waffles we ate.

# COMMAND ----------

breakfast_dict.get("waffles")

# COMMAND ----------

# MAGIC %md Alternatively, you can use the syntax **`dict_object[key]`**.

# COMMAND ----------

breakfast_dict["waffles"]

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC You can update a dictionary similarly to a list by assigning **`breakfast_dict[key]`** to be something. 
# MAGIC
# MAGIC If the key is present, it overwrites the current value. If not, it creates a new key-value pair. 
# MAGIC
# MAGIC Let's say we ate another waffle, bringing our total up to 4 waffles, and then ate a yogurt.

# COMMAND ----------

print(breakfast_dict)
breakfast_dict["waffles"] += 1
breakfast_dict["yogurt"] = 1
print(breakfast_dict)

# COMMAND ----------

# MAGIC %md Notice the use of **`+=`** to increment the count of waffles.
# MAGIC
# MAGIC **Question**: Why did we not use **`+=`** to increment the yogurt count?

# COMMAND ----------

# MAGIC %md In order to determine if a key is in a dictionary, we can use the method [**dict_name.keys()**](https://www.w3schools.com/python/ref_dictionary_keys.asp). This returns a list of the keys in the dictionary. 
# MAGIC
# MAGIC Similar to lists, we can use **`in`** to see if our key is in the dictionary. Let's see if we ate bacon for breakfast.

# COMMAND ----------

print(breakfast_dict.keys())
print("bacon" in breakfast_dict.keys())

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
