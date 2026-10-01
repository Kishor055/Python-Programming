# ⚡ 23 — Python Libraries | Striky Notes

> **Quick revision notes for Python libraries, their purpose, syntax, and real-world usage.**

---

## 🧠 Python Library Concept

```text
Python Library
      ↓
Pre-built Code
      ↓
Import
      ↓
Use Functions / Classes
      ↓
Build Applications
```

### Basic Import

```python
import library
```

```python
from library import function
```

---

# 🗺️ Library Roadmap

```text
NumPy
  ↓
Pandas
  ↓
Matplotlib
  ↓
Seaborn
  ↓
Requests
  ↓
BeautifulSoup
  ↓
Scikit-Learn
  ↓
SQLAlchemy
  ↓
Flask
```

---

# 🔢 NumPy

### Purpose

**Numerical computing + arrays + mathematical operations**

```python
import numpy as np
```

### Create Array

```python
arr = np.array([1, 2, 3, 4])
```

### 2D Array

```python
arr = np.array([
    [1, 2],
    [3, 4]
])
```

### Important

```python
arr.shape
arr.ndim
arr.size
arr.dtype
```

### Common Operations

```python
np.zeros(5)
np.ones(5)
np.arange(0, 10)
np.linspace(0, 1, 5)
```

### Math

```python
np.mean(arr)
np.median(arr)
np.std(arr)
np.min(arr)
np.max(arr)
np.sum(arr)
```

### Reshape

```python
arr.reshape(2, 2)
```

### Key Concepts

```text
Array
Shape
Dimension
Indexing
Slicing
Broadcasting
Vectorization
Aggregation
Statistics
Linear Algebra
```

---

# 🐼 Pandas

### Purpose

**Data manipulation + analysis**

```python
import pandas as pd
```

### Series

```python
s = pd.Series([10, 20, 30])
```

### DataFrame

```python
df = pd.DataFrame({
    "Name": ["A", "B"],
    "Age": [20, 21]
})
```

### Read Data

```python
pd.read_csv("data.csv")
pd.read_excel("data.xlsx")
pd.read_json("data.json")
```

### Inspect

```python
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns
```

### Select Column

```python
df["Name"]
```

### Filter

```python
df[df["Age"] > 20]
```

### Missing Values

```python
df.isnull()
df.dropna()
df.fillna(0)
```

### Duplicates

```python
df.duplicated()
df.drop_duplicates()
```

### GroupBy

```python
df.groupby("Department")["Salary"].mean()
```

### Sort

```python
df.sort_values("Age")
```

### Export

```python
df.to_csv("output.csv", index=False)
```

### Key Concepts

```text
Series
DataFrame
Selection
Filtering
Cleaning
Missing Values
Duplicates
GroupBy
Merge
Join
Aggregation
Export
```

---

# 📊 Matplotlib

### Purpose

**Data visualization**

```python
import matplotlib.pyplot as plt
```

### Line Plot

```python
plt.plot(x, y)
plt.show()
```

### Bar Chart

```python
plt.bar(x, y)
plt.show()
```

### Scatter Plot

```python
plt.scatter(x, y)
plt.show()
```

### Histogram

```python
plt.hist(data)
plt.show()
```

### Labels

```python
plt.title("Sales")
plt.xlabel("Month")
plt.ylabel("Revenue")
```

### Legend

```python
plt.legend()
```

### Save

```python
plt.savefig("chart.png")
```

### Key Concepts

```text
Figure
Axes
Plot
Labels
Title
Legend
Grid
Subplot
Save Figure
```

---

# 📈 Seaborn

### Purpose

**Statistical visualization**

```python
import seaborn as sns
```

### Common Plots

```python
sns.scatterplot(data=df, x="Age", y="Salary")
sns.barplot(data=df, x="Department", y="Salary")
sns.boxplot(data=df, x="Department", y="Salary")
sns.histplot(data=df, x="Age")
sns.heatmap(df.corr(numeric_only=True))
sns.pairplot(df)
```

### Key Concepts

```text
Distribution
Correlation
Categorical Data
Box Plot
Heatmap
Pair Plot
Regression
EDA
```

---

# 🌐 Requests

### Purpose

**HTTP requests + REST APIs**

```python
import requests
```

### GET

```python
response = requests.get(
    url,
    timeout=10
)
```

### POST

```python
response = requests.post(
    url,
    json=data,
    timeout=10
)
```

### PUT

```python
requests.put(url, json=data)
```

### PATCH

```python
requests.patch(url, json=data)
```

### DELETE

```python
requests.delete(url)
```

### Response

```python
response.status_code
response.text
response.content
response.headers
response.url
```

### JSON

```python
data = response.json()
```

### Parameters

```python
requests.get(
    url,
    params={
        "page": 1,
        "limit": 10
    }
)
```

### Headers

```python
headers = {
    "Accept": "application/json"
}
```

### Authentication

```python
headers = {
    "Authorization": f"Bearer {API_KEY}"
}
```

### Error Handling

```python
response.raise_for_status()
```

```python
try:
    response = requests.get(
        url,
        timeout=10
    )
    response.raise_for_status()

except requests.RequestException as error:
    print(error)
```

### Session

```python
session = requests.Session()
```

### Key Concepts

```text
HTTP
REST
GET
POST
PUT
PATCH
DELETE
JSON
Headers
Parameters
Authentication
Cookies
Sessions
Timeouts
Exceptions
```

---

# 🕷️ BeautifulSoup

### Purpose

**HTML parsing + web scraping**

```python
from bs4 import BeautifulSoup
```

### Basic

```python
import requests
from bs4 import BeautifulSoup

response = requests.get(
    url,
    timeout=10
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)
```

### Find Element

```python
soup.find("h1")
```

### Find All

```python
soup.find_all("a")
```

### CSS Selector

```python
soup.select(".product")
```

### Text

```python
element.get_text(strip=True)
```

### Attribute

```python
element.get("href")
```

### Workflow

```text
Website
   ↓
Requests
   ↓
HTML
   ↓
BeautifulSoup
   ↓
Extract Data
   ↓
Pandas
   ↓
CSV / Database
```

### Key Concepts

```text
HTML
Tags
Attributes
Selectors
Parsing
Text Extraction
Links
Tables
Web Scraping
```

---

# 🤖 Scikit-Learn

### Purpose

**Machine Learning**

```python
import sklearn
```

### Typical Workflow

```text
Dataset
   ↓
Cleaning
   ↓
Features / Target
   ↓
Train/Test Split
   ↓
Preprocessing
   ↓
Model
   ↓
Training
   ↓
Prediction
   ↓
Evaluation
```

### Train/Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### Linear Regression

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

predictions = model.predict(X_test)
```

### Classification

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
```

### Common Algorithms

```text
Linear Regression
Logistic Regression
Decision Tree
Random Forest
KNN
SVM
Naive Bayes
K-Means
PCA
```

### Evaluation

```text
Accuracy
Precision
Recall
F1 Score
MAE
MSE
RMSE
R²
Confusion Matrix
```

---

# 🗄️ SQLAlchemy

### Purpose

**Database interaction + ORM**

```python
from sqlalchemy import create_engine
```

### Database Connection

```python
engine = create_engine(
    "sqlite:///app.db"
)
```

### ORM Concept

```text
Python Class
     ↓
SQLAlchemy Model
     ↓
Database Table
```

### CRUD

```text
Create
Read
Update
Delete
```

### Common Concepts

```text
Engine
Connection
Session
Model
Table
Column
Primary Key
Foreign Key
Relationship
Transaction
ORM
```

---

# 🌐 Flask

### Purpose

**Web applications + REST APIs**

```python
from flask import Flask

app = Flask(__name__)
```

### Route

```python
@app.route("/")
def home():
    return "Hello World"
```

### Run

```python
if __name__ == "__main__":
    app.run(debug=True)
```

### HTTP Methods

```python
@app.route(
    "/users",
    methods=["GET", "POST"]
)
def users():
    pass
```

### JSON Response

```python
from flask import jsonify

return jsonify({
    "message": "Success"
})
```

### Typical Architecture

```text
Client
  ↓
Flask
  ↓
Route
  ↓
Business Logic
  ↓
SQLAlchemy
  ↓
Database
```

### Key Concepts

```text
Application
Routes
Views
HTTP Methods
Templates
Jinja
JSON
REST API
Error Handling
Configuration
Database
Deployment
```

---

# 🔗 Libraries Working Together

## Data Science

```text
NumPy
  ↓
Pandas
  ↓
Matplotlib
  ↓
Seaborn
```

## API Data Analysis

```text
Requests
   ↓
JSON
   ↓
Pandas
   ↓
Matplotlib
```

## Web Scraping

```text
Requests
   ↓
BeautifulSoup
   ↓
Pandas
   ↓
CSV / Database
```

## Machine Learning

```text
Pandas
   ↓
NumPy
   ↓
Scikit-Learn
   ↓
Matplotlib / Seaborn
```

## ML API

```text
Scikit-Learn
      ↓
Saved Model
      ↓
Flask
      ↓
REST API
```

## Full Stack Data Application

```text
User
 ↓
Flask
 ↓
Requests
 ↓
Pandas
 ↓
NumPy
 ↓
Scikit-Learn
 ↓
SQLAlchemy
 ↓
Database
```

---

# 🧰 Installation Cheat Sheet

```bash
pip install numpy
pip install pandas
pip install matplotlib
pip install seaborn
pip install requests
pip install beautifulsoup4
pip install scikit-learn
pip install sqlalchemy
pip install flask
```

### All-in-One

```bash
pip install numpy pandas matplotlib seaborn requests beautifulsoup4 scikit-learn sqlalchemy flask
```

---

# 🛠️ Environment

### Create

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

### Upgrade pip

```bash
python -m pip install --upgrade pip
```

### Save Dependencies

```bash
pip freeze > requirements.txt
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Security Quick Notes

### ❌ Never

```python
API_KEY = "secret"
PASSWORD = "123456"
```

### ✅ Use

```python
import os

API_KEY = os.getenv("API_KEY")
```

### Never commit

```text
.env
credentials.json
*.pem
secret_keys.txt
```

---

# ⚡ Most Important Commands

| Library       | Must Know                                                    |
| ------------- | ------------------------------------------------------------ |
| NumPy         | `array()`, `reshape()`, `mean()`, `sum()`                    |
| Pandas        | `DataFrame()`, `read_csv()`, `head()`, `info()`, `groupby()` |
| Matplotlib    | `plot()`, `bar()`, `scatter()`, `hist()`, `show()`           |
| Seaborn       | `scatterplot()`, `barplot()`, `boxplot()`, `heatmap()`       |
| Requests      | `get()`, `post()`, `json()`, `raise_for_status()`            |
| BeautifulSoup | `find()`, `find_all()`, `select()`                           |
| Scikit-Learn  | `fit()`, `predict()`, `train_test_split()`                   |
| SQLAlchemy    | `create_engine()`, `Session`, ORM                            |
| Flask         | `Flask()`, `route()`, `jsonify()`, `run()`                   |

---

# 🎯 Fast Revision

```text
NumPy
→ Numerical Computing

Pandas
→ Data Analysis

Matplotlib
→ Visualization

Seaborn
→ Statistical Visualization

Requests
→ HTTP / APIs

BeautifulSoup
→ Web Scraping

Scikit-Learn
→ Machine Learning

SQLAlchemy
→ Databases / ORM

Flask
→ Web Applications / APIs
```

---

# 🧠 Remember This

```text
NUMPY
"Calculate"

PANDAS
"Analyze"

MATPLOTLIB
"Visualize"

SEABORN
"Understand Patterns"

REQUESTS
"Communicate"

BEAUTIFULSOUP
"Extract"

SCIKIT-LEARN
"Predict"

SQLALCHEMY
"Store"

FLASK
"Serve"
```

---

# 🚀 Final Learning Flow

```text
             🐍 Python
                 │
                 ▼
             🔢 NumPy
                 │
                 ▼
             🐼 Pandas
                 │
          ┌──────┴──────┐
          ▼             ▼
     📊 Matplotlib   📈 Seaborn
          │             │
          └──────┬──────┘
                 ▼
             🌐 Requests
                 │
                 ▼
          🕷️ BeautifulSoup
                 │
                 ▼
          🤖 Scikit-Learn
                 │
                 ▼
            🗄️ SQLAlchemy
                 │
                 ▼
              🌐 Flask
                 │
                 ▼
          🚀 Real Projects
```

---

## ⭐ One-Line Revision

> **NumPy calculates → Pandas analyzes → Matplotlib/Seaborn visualizes → Requests communicates → BeautifulSoup extracts → Scikit-Learn predicts → SQLAlchemy stores → Flask serves.**
