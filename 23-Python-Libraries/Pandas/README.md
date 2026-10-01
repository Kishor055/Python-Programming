# 🐼 Pandas — Data Analysis with Python

> A structured learning module for mastering **Pandas**, a powerful Python library for data manipulation, cleaning, analysis, transformation, and exploratory data analysis.

---

## 📌 Overview

**Pandas** is an open-source Python library designed for working with structured and tabular data.

It provides powerful data structures and tools for:

* 📋 Working with tabular datasets
* 🧹 Cleaning messy data
* 🔍 Filtering and selecting records
* 🔄 Transforming data
* 📊 Aggregating and summarizing data
* 🔗 Combining multiple datasets
* 📅 Working with dates and time-series data
* 📈 Exploratory Data Analysis (EDA)
* 💾 Reading and writing common data formats

The two fundamental Pandas data structures are:

* **Series** — one-dimensional labeled data
* **DataFrame** — two-dimensional labeled tabular data

Pandas is widely used in **Data Science, Machine Learning, Business Analytics, Data Engineering, and AI workflows**.

---

# 🎯 Learning Objectives

By completing this module, you will learn how to:

* Understand Pandas and its role in data analysis
* Create Series and DataFrames
* Load datasets from different file formats
* Inspect and understand datasets
* Select rows and columns
* Filter data using conditions
* Handle missing values
* Remove duplicate records
* Rename columns
* Change data types
* Sort and rank data
* Apply functions to columns
* Group and aggregate data
* Merge and join datasets
* Concatenate datasets
* Work with dates and time
* Perform basic statistical analysis
* Create pivot tables
* Export cleaned datasets
* Perform Exploratory Data Analysis
* Combine Pandas with NumPy and Matplotlib

---

# 🧰 Installation

Install Pandas using `pip`:

```bash
pip install pandas
```

Verify the installation:

```python
import pandas as pd

print(pd.__version__)
```

The official Pandas documentation provides installation instructions and guides for getting started with the library.

---

# 📦 Import Convention

The standard Pandas import convention is:

```python
import pandas as pd
```

---

# 🧠 Pandas Architecture

A simplified view of Pandas:

```text
Pandas
│
├── Series
│
├── DataFrame
│
├── Data Input / Output
│
├── Data Selection
│
├── Data Cleaning
│
├── Data Transformation
│
├── Grouping & Aggregation
│
├── Merge / Join / Concatenate
│
├── Time Series
│
├── Statistics
│
└── Data Visualization
```

---

# 🧩 Core Data Structures

## 1. Series

A **Series** is a one-dimensional labeled array.

```python
import pandas as pd

scores = pd.Series([85, 90, 78, 92])

print(scores)
```

Output:

```text
0    85
1    90
2    78
3    92
dtype: int64
```

A Series contains:

```text
Values + Index
```

---

## 2. DataFrame

A **DataFrame** is a two-dimensional labeled data structure consisting of rows and columns.

```python
data = {
    "Name": ["Amit", "Priya", "Rahul"],
    "Age": [21, 22, 20],
    "Score": [85, 92, 78]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    Name  Age  Score
0   Amit   21     85
1  Priya   22     92
2  Rahul   20     78
```

---

# 🏗️ DataFrame Structure

A DataFrame can be visualized as:

```text
              Columns
          ↓      ↓      ↓
       Name     Age    Score
       ─────────────────────
Row 0   Amit     21      85
Row 1   Priya    22      92
Row 2   Rahul    20      78
```

Each row has an index, while each column has a label.

---

# 🚀 Creating DataFrames

## From Dictionary

```python
data = {
    "Product": ["Laptop", "Phone", "Tablet"],
    "Price": [70000, 30000, 20000]
}

df = pd.DataFrame(data)
```

---

## From List

```python
data = [
    ["Amit", 21, 85],
    ["Priya", 22, 92],
    ["Rahul", 20, 78]
]

df = pd.DataFrame(
    data,
    columns=["Name", "Age", "Score"]
)
```

---

## From NumPy Array

```python
import numpy as np
import pandas as pd

array = np.array([
    [1, 80],
    [2, 90],
    [3, 75]
])

df = pd.DataFrame(
    array,
    columns=["Student", "Score"]
)
```

---

# 📂 Reading Data

Pandas can read data from many common sources and formats.

## CSV

```python
df = pd.read_csv("data.csv")
```

## Excel

```python
df = pd.read_excel("data.xlsx")
```

## JSON

```python
df = pd.read_json("data.json")
```

## SQL

```python
df = pd.read_sql(
    "SELECT * FROM students",
    connection
)
```

---

# 💾 Writing Data

## Save to CSV

```python
df.to_csv(
    "cleaned_data.csv",
    index=False
)
```

## Save to Excel

```python
df.to_excel(
    "cleaned_data.xlsx",
    index=False
)
```

## Save to JSON

```python
df.to_json(
    "data.json",
    orient="records"
)
```

---

# 🔍 Inspecting a Dataset

After loading a dataset, the first step should be understanding its structure.

## First Rows

```python
df.head()
```

## Last Rows

```python
df.tail()
```

## Random Samples

```python
df.sample(5)
```

## Dataset Shape

```python
df.shape
```

Example:

```text
(1000, 8)
```

This means:

```text
1000 rows
8 columns
```

---

# 📋 Dataset Information

Use `info()` to inspect column types and missing values.

```python
df.info()
```

---

# 📊 Statistical Summary

```python
df.describe()
```

For all columns:

```python
df.describe(include="all")
```

---

# 🏷️ Column Names

Get all column names:

```python
print(df.columns)
```

Convert them into a list:

```python
columns = df.columns.tolist()
```

---

# 🔎 Selecting Columns

## Single Column

```python
df["Name"]
```

## Multiple Columns

```python
df[
    ["Name", "Score"]
]
```

---

# 📍 Selecting Rows

## Using `loc`

`loc` is label-based selection.

```python
df.loc[0]
```

Select specific rows and columns:

```python
df.loc[
    0:2,
    ["Name", "Score"]
]
```

---

## Using `iloc`

`iloc` is integer-position based selection.

```python
df.iloc[0]
```

Select the first three rows:

```python
df.iloc[0:3]
```

Select rows and columns by position:

```python
df.iloc[
    0:3,
    0:2
]
```

---

# 🔍 Filtering Data

Filtering is one of the most important Pandas operations.

```python
df[df["Score"] > 80]
```

Multiple conditions:

```python
df[
    (df["Age"] > 20) &
    (df["Score"] > 80)
]
```

Using OR:

```python
df[
    (df["Score"] > 90) |
    (df["Age"] < 21)
]
```

---

# 🔎 `isin()`

Check whether values belong to a specific collection.

```python
df[
    df["Name"].isin(
        ["Amit", "Priya"]
    )
]
```

---

# 🔍 `query()`

Pandas also supports query-style filtering.

```python
df.query(
    "Age > 20 and Score > 80"
)
```

---

# 🧹 Handling Missing Values

Real-world datasets frequently contain missing values.

Check missing values:

```python
df.isnull().sum()
```

Alternative:

```python
df.isna().sum()
```

---

## Remove Missing Rows

```python
df.dropna()
```

---

## Fill Missing Values

```python
df.fillna(0)
```

Fill a specific column:

```python
df["Score"] = df["Score"].fillna(
    df["Score"].mean()
)
```

---

# ♻️ Removing Duplicates

Find duplicate rows:

```python
df.duplicated()
```

Count duplicates:

```python
df.duplicated().sum()
```

Remove duplicates:

```python
df = df.drop_duplicates()
```

---

# ✏️ Renaming Columns

```python
df = df.rename(
    columns={
        "Score": "Marks"
    }
)
```

Rename multiple columns:

```python
df = df.rename(
    columns={
        "Name": "Student_Name",
        "Age": "Student_Age"
    }
)
```

---

# 🔤 Changing Data Types

Check data types:

```python
df.dtypes
```

Convert a column:

```python
df["Age"] = df["Age"].astype(int)
```

Convert safely using `to_numeric()`:

```python
df["Score"] = pd.to_numeric(
    df["Score"],
    errors="coerce"
)
```

---

# 🔠 String Operations

Pandas provides vectorized string operations through `.str`.

Convert text to lowercase:

```python
df["Name"] = df["Name"].str.lower()
```

Convert to uppercase:

```python
df["Name"] = df["Name"].str.upper()
```

Remove extra whitespace:

```python
df["Name"] = df["Name"].str.strip()
```

Check whether text contains a value:

```python
df[
    df["Name"].str.contains(
        "Amit",
        case=False,
        na=False
    )
]
```

---

# 🔢 Sorting Data

Sort by one column:

```python
df.sort_values(
    "Score"
)
```

Descending order:

```python
df.sort_values(
    "Score",
    ascending=False
)
```

Sort by multiple columns:

```python
df.sort_values(
    ["Age", "Score"],
    ascending=[True, False]
)
```

---

# ➕ Adding Columns

Create a new column:

```python
df["Passed"] = df["Score"] >= 40
```

Create a calculated column:

```python
df["Bonus"] = df["Score"] * 0.10
```

---

# ✏️ Updating Values

Update a specific value:

```python
df.loc[0, "Score"] = 95
```

Conditional update:

```python
df.loc[
    df["Score"] < 40,
    "Passed"
] = False
```

---

# 🧮 Applying Functions

Use `apply()` to apply a function to a Series.

```python
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Score"].apply(grade)
```

---

# 📊 Aggregation

Pandas supports many aggregation functions.

```python
df["Score"].mean()
```

Other common functions:

```python
df["Score"].sum()
df["Score"].median()
df["Score"].min()
df["Score"].max()
df["Score"].std()
df["Score"].count()
```

---

# 🗂️ GroupBy

`groupby()` is one of the most important Pandas tools for analyzing groups of data.

Example:

```python
data = {
    "Department": [
        "IT",
        "IT",
        "HR",
        "HR",
        "Finance"
    ],
    "Salary": [
        50000,
        60000,
        45000,
        55000,
        70000
    ]
}

df = pd.DataFrame(data)
```

Calculate average salary by department:

```python
df.groupby(
    "Department"
)["Salary"].mean()
```

---

## Multiple Aggregations

```python
df.groupby(
    "Department"
)["Salary"].agg(
    ["mean", "min", "max", "count"]
)
```

---

# 🔗 Combining DataFrames

Pandas provides several ways to combine datasets.

```text
Concatenate
     │
     ├── Vertical
     └── Horizontal

Merge
     │
     ├── Inner
     ├── Left
     ├── Right
     └── Outer

Join
```

---

# 🔗 Concatenation

Combine rows:

```python
result = pd.concat(
    [df1, df2],
    ignore_index=True
)
```

Combine columns:

```python
result = pd.concat(
    [df1, df2],
    axis=1
)
```

---

# 🔀 Merge

Create two datasets:

```python
students = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Name": ["Amit", "Priya", "Rahul"]
})

scores = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Score": [85, 92, 78]
})
```

Merge them:

```python
result = pd.merge(
    students,
    scores,
    on="Student_ID"
)
```

---

# 🔗 Merge Types

Pandas supports common relational merge strategies:

```text
Inner Join
    ↓
Only matching records

Left Join
    ↓
All records from left DataFrame

Right Join
    ↓
All records from right DataFrame

Outer Join
    ↓
All records from both DataFrames
```

Example:

```python
pd.merge(
    df1,
    df2,
    on="ID",
    how="left"
)
```

---

# 📅 Working with Dates

Convert a column to datetime:

```python
df["Date"] = pd.to_datetime(
    df["Date"]
)
```

Extract year:

```python
df["Year"] = df["Date"].dt.year
```

Extract month:

```python
df["Month"] = df["Date"].dt.month
```

Extract day:

```python
df["Day"] = df["Date"].dt.day
```

Extract day name:

```python
df["Day_Name"] = df["Date"].dt.day_name()
```

---

# 📈 Time-Series Analysis

Example:

```python
dates = pd.date_range(
    start="2026-01-01",
    periods=10,
    freq="D"
)

df = pd.DataFrame({
    "Date": dates,
    "Sales": [
        100, 120, 115, 140, 160,
        155, 170, 180, 190, 210
    ]
})
```

Set the date as the index:

```python
df = df.set_index("Date")
```

Calculate a rolling average:

```python
df["Rolling_Average"] = (
    df["Sales"]
    .rolling(3)
    .mean()
)
```

---

# 📊 Pivot Tables

Pivot tables provide a convenient way to summarize grouped data.

```python
pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Department",
    aggfunc="mean"
)
```

A pivot table can summarize large datasets into a compact analytical view.

---

# 📋 Crosstab

Use `crosstab()` to calculate frequency tables.

```python
pd.crosstab(
    df["Department"],
    df["Gender"]
)
```

---

# 📈 Basic Statistics

Pandas provides convenient descriptive statistics:

```python
df.describe()
```

Individual statistics:

```python
df["Salary"].mean()
df["Salary"].median()
df["Salary"].std()
df["Salary"].var()
df["Salary"].min()
df["Salary"].max()
```

---

# 📊 Value Counts

Count unique values:

```python
df["Department"].value_counts()
```

Normalized proportions:

```python
df["Department"].value_counts(
    normalize=True
)
```

---

# 🔍 Unique Values

Get unique values:

```python
df["Department"].unique()
```

Count unique values:

```python
df["Department"].nunique()
```

---

# 📉 Correlation

Calculate correlations between numerical columns:

```python
df.corr(
    numeric_only=True
)
```

Correlation can be useful during exploratory analysis, but it should not automatically be interpreted as causation.

---

# 📈 Pandas Visualization

Pandas provides convenient plotting methods that integrate with Matplotlib.

```python
import matplotlib.pyplot as plt

df["Sales"].plot()

plt.show()
```

Bar chart:

```python
df.groupby(
    "Department"
)["Salary"].mean().plot(
    kind="bar"
)

plt.show()
```

This creates a useful workflow:

```text
Pandas
  ↓
Data Preparation
  ↓
Aggregation
  ↓
Matplotlib
  ↓
Visualization
```

---

# 🧹 Data Cleaning Workflow

A typical real-world data-cleaning process:

```text
Raw Dataset
     ↓
Load Data
     ↓
Inspect Dataset
     ↓
Check Data Types
     ↓
Check Missing Values
     ↓
Remove Duplicates
     ↓
Handle Invalid Values
     ↓
Transform Columns
     ↓
Validate Data
     ↓
Clean Dataset
```

Example:

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.shape)
print(df.info())
print(df.isnull().sum())

df = df.drop_duplicates()

df["Age"] = pd.to_numeric(
    df["Age"],
    errors="coerce"
)

df["Age"] = df["Age"].fillna(
    df["Age"].median()
)
```

---

# 🔬 Exploratory Data Analysis

Pandas is one of the most commonly used tools for Exploratory Data Analysis (EDA).

A basic EDA workflow:

```text
Dataset
   ↓
Shape
   ↓
Columns
   ↓
Data Types
   ↓
Missing Values
   ↓
Duplicates
   ↓
Descriptive Statistics
   ↓
Unique Values
   ↓
Distribution
   ↓
Relationships
   ↓
Visualization
   ↓
Insights
```

Useful commands:

```python
df.head()
df.tail()
df.shape
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()
df.nunique()
df.value_counts()
df.corr(numeric_only=True)
```

---

# 🤖 Pandas in Machine Learning

Pandas frequently appears in the data-preparation stage of machine-learning workflows.

```text
Raw Dataset
     ↓
Pandas
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Data Analysis
     ↓
NumPy / ML Framework
     ↓
Model Training
     ↓
Evaluation
```

Common ML preparation tasks include:

* Handling missing values
* Removing duplicates
* Encoding categorical data
* Creating new features
* Filtering records
* Combining datasets
* Detecting inconsistent values
* Preparing model-ready tables

---

# 🔢 Pandas + NumPy

Pandas and NumPy work closely together.

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [40, 50, 60]
})

array = df.to_numpy()

print(array)
```

Convert a NumPy array into a DataFrame:

```python
array = np.array([
    [1, 2],
    [3, 4]
])

df = pd.DataFrame(
    array,
    columns=["A", "B"]
)
```

---

# 📊 Pandas + Matplotlib

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [100, 140, 180, 220]
})

df.plot(
    x="Month",
    y="Sales",
    kind="line"
)

plt.show()
```

---

# 🧪 Practice Exercises

## 🟢 Beginner

* [ ] Create a Pandas Series
* [ ] Create a DataFrame
* [ ] Create a DataFrame from a dictionary
* [ ] Load a CSV file
* [ ] Use `head()` and `tail()`
* [ ] Check `shape`
* [ ] Check `columns`
* [ ] Check `dtypes`
* [ ] Select rows and columns
* [ ] Filter records
* [ ] Sort a DataFrame

---

## 🟡 Intermediate

* [ ] Handle missing values
* [ ] Remove duplicate records
* [ ] Rename columns
* [ ] Convert data types
* [ ] Use `apply()`
* [ ] Use `groupby()`
* [ ] Use aggregation functions
* [ ] Merge two DataFrames
* [ ] Concatenate datasets
* [ ] Work with dates
* [ ] Create pivot tables
* [ ] Perform basic EDA

---

## 🔴 Advanced

* [ ] Clean a real-world messy dataset
* [ ] Build a complete EDA project
* [ ] Perform feature engineering
* [ ] Analyze time-series data
* [ ] Build a reusable data-cleaning pipeline
* [ ] Combine multiple datasets
* [ ] Analyze correlations
* [ ] Prepare a dataset for machine learning
* [ ] Combine Pandas + NumPy + Matplotlib
* [ ] Build an end-to-end data analysis project

---

# 📁 Suggested Directory Structure

```text
23-Python-Libraries/
│
└── Pandas/
    │
    ├── README.md
    │
    ├── 01-Introduction/
    │   └── introduction.py
    │
    ├── 02-Series/
    │   └── series.py
    │
    ├── 03-DataFrames/
    │   └── dataframe.py
    │
    ├── 04-Reading-and-Writing-Data/
    │   └── io_operations.py
    │
    ├── 05-Data-Inspection/
    │   └── inspection.py
    │
    ├── 06-Selection-and-Filtering/
    │   └── selection.py
    │
    ├── 07-Missing-Values/
    │   └── missing_values.py
    │
    ├── 08-Duplicates/
    │   └── duplicates.py
    │
    ├── 09-Data-Types/
    │   └── data_types.py
    │
    ├── 10-Sorting/
    │   └── sorting.py
    │
    ├── 11-String-Operations/
    │   └── strings.py
    │
    ├── 12-GroupBy-and-Aggregation/
    │   └── groupby.py
    │
    ├── 13-Merge-Join-Concatenate/
    │   └── combining_data.py
    │
    ├── 14-DateTime/
    │   └── datetime.py
    │
    ├── 15-Pivot-Tables/
    │   └── pivot.py
    │
    ├── 16-Statistics/
    │   └── statistics.py
    │
    ├── 17-EDA/
    │   └── exploratory_analysis.py
    │
    └── 18-Projects/
        └── data_analysis_project.py
```

---

# 🛠️ Recommended Learning Workflow

```text
Python Basics
      ↓
NumPy
      ↓
Pandas Fundamentals
      ↓
Series & DataFrames
      ↓
Data Input / Output
      ↓
Data Inspection
      ↓
Selection & Filtering
      ↓
Data Cleaning
      ↓
Transformation
      ↓
GroupBy & Aggregation
      ↓
Merge & Join
      ↓
Time Series
      ↓
Exploratory Data Analysis
      ↓
Matplotlib / Seaborn
      ↓
Machine Learning
```

---

# 💡 Important Pandas Concepts

| Concept        | Importance |
| -------------- | ---------- |
| DataFrame      | ⭐⭐⭐⭐⭐      |
| Series         | ⭐⭐⭐⭐⭐      |
| Indexing       | ⭐⭐⭐⭐⭐      |
| Filtering      | ⭐⭐⭐⭐⭐      |
| Missing Values | ⭐⭐⭐⭐⭐      |
| GroupBy        | ⭐⭐⭐⭐⭐      |
| Merge / Join   | ⭐⭐⭐⭐⭐      |
| Data Types     | ⭐⭐⭐⭐       |
| Aggregation    | ⭐⭐⭐⭐       |
| Sorting        | ⭐⭐⭐⭐       |
| DateTime       | ⭐⭐⭐⭐       |
| Pivot Tables   | ⭐⭐⭐⭐       |
| EDA            | ⭐⭐⭐⭐⭐      |

---

# ⚡ Pandas Cheat Sheet

### Import

```python
import pandas as pd
```

### Create DataFrame

```python
pd.DataFrame(data)
```

### Read CSV

```python
pd.read_csv("data.csv")
```

### Save CSV

```python
df.to_csv("data.csv", index=False)
```

### First Rows

```python
df.head()
```

### Last Rows

```python
df.tail()
```

### Shape

```python
df.shape
```

### Information

```python
df.info()
```

### Statistics

```python
df.describe()
```

### Columns

```python
df.columns
```

### Data Types

```python
df.dtypes
```

### Missing Values

```python
df.isnull().sum()
```

### Remove Missing Values

```python
df.dropna()
```

### Fill Missing Values

```python
df.fillna(value)
```

### Remove Duplicates

```python
df.drop_duplicates()
```

### Sort

```python
df.sort_values("column")
```

### Filter

```python
df[df["column"] > value]
```

### Group

```python
df.groupby("column")
```

### Merge

```python
pd.merge(df1, df2, on="ID")
```

### Concatenate

```python
pd.concat([df1, df2])
```

### Unique Values

```python
df["column"].unique()
```

### Value Counts

```python
df["column"].value_counts()
```

---

# 🧠 Key Takeaways

After completing this module, you should understand:

```text
Pandas
│
├── Series
├── DataFrame
│
├── Data Input / Output
│
├── Dataset Inspection
│
├── Selection
├── Filtering
│
├── Missing Values
├── Duplicates
├── Data Types
│
├── Sorting
├── Transformation
├── String Operations
│
├── GroupBy
├── Aggregation
│
├── Merge
├── Join
├── Concatenate
│
├── DateTime
├── Time Series
│
├── Pivot Tables
├── Statistics
│
├── Exploratory Data Analysis
│
└── Visualization
```

---

# 📚 Official Learning Resources

* **Pandas Documentation:** [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
* **Getting Started:** [https://pandas.pydata.org/docs/getting_started/](https://pandas.pydata.org/docs/getting_started/)
* **User Guide:** [https://pandas.pydata.org/docs/user_guide/](https://pandas.pydata.org/docs/user_guide/)
* **API Reference:** [https://pandas.pydata.org/docs/reference/](https://pandas.pydata.org/docs/reference/)
* **10 Minutes to Pandas:** [https://pandas.pydata.org/docs/user_guide/10min.html](https://pandas.pydata.org/docs/user_guide/10min.html)

---

# 🚀 Next Step

After completing Pandas, continue with:

```text
NumPy
  ↓
Pandas
  ↓
Matplotlib
  ↓
Seaborn
  ↓
Exploratory Data Analysis
  ↓
Feature Engineering
  ↓
Machine Learning
  ↓
Artificial Intelligence
```

Pandas is an important step toward becoming comfortable with **real-world datasets and practical data analysis**.

---

## 👨‍💻 Repository

This module is part of the **Python Programming** learning repository.

**Repository:** `Kishor055/Python-Programming`

**Module:** `23-Python-Libraries/Pandas`

---

## 📄 License

This educational material is maintained as part of the repository and is intended for **learning, practice, and educational use**.

---

⭐ **If this repository helps you learn Python and Data Science, consider giving it a star on GitHub.**
