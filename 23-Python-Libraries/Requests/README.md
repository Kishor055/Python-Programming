# 🌐 Requests — HTTP Requests with Python

> A structured learning module for mastering **Requests**, a popular Python HTTP library for interacting with web services, REST APIs, websites, and internet-based applications.

---

## 📌 Overview

**Requests** is a Python library that makes it easier to send HTTP requests and work with responses from web servers and APIs.

It provides a simple interface for common HTTP operations such as:

* `GET`
* `POST`
* `PUT`
* `PATCH`
* `DELETE`
* `HEAD`
* `OPTIONS`

Requests is commonly used for:

* 🌐 Consuming REST APIs
* 🔗 Connecting Python applications to web services
* 📦 Working with JSON APIs
* 🔐 Sending authentication credentials
* 🔎 Querying remote data
* 📤 Sending form and JSON data
* 📥 Downloading files
* 🍪 Managing cookies
* 🔄 Maintaining HTTP sessions
* 🧪 Testing APIs
* 🤖 Automating web-based workflows

---

# 🎯 Learning Objectives

By completing this module, you will learn how to:

* Understand HTTP and REST APIs
* Install and import Requests
* Send HTTP requests
* Work with GET, POST, PUT, PATCH, and DELETE
* Pass query parameters
* Send headers
* Send form data
* Send JSON payloads
* Process JSON responses
* Check HTTP status codes
* Handle request exceptions
* Configure request timeouts
* Download files
* Work with cookies
* Use HTTP sessions
* Understand authentication patterns
* Debug API responses
* Build API-powered Python applications

---

# 🧰 Installation

Install Requests using `pip`:

```bash
pip install requests
```

Verify the installation:

```python
import requests

print(requests.__version__)
```

---

# 📦 Import Convention

The standard import is:

```python
import requests
```

---

# 🌐 HTTP Fundamentals

Before using Requests, understand the basic HTTP workflow:

```text
Python Application
       │
       │ HTTP Request
       ▼
    Web Server
       │
       │ HTTP Response
       ▼
Python Application
```

An HTTP request commonly contains:

```text
Request
│
├── Method
├── URL
├── Headers
├── Query Parameters
├── Body
└── Authentication
```

The response commonly contains:

```text
Response
│
├── Status Code
├── Headers
├── Body
└── Cookies
```

---

# 🚀 Your First GET Request

```python
import requests

response = requests.get(
    "https://httpbin.org/get"
)

print(response.status_code)
print(response.text)
```

A successful HTTP response commonly has a `2xx` status code.

---

# 🔢 HTTP Status Codes

Common status codes:

|  Code | Meaning               |
| ----: | --------------------- |
| `200` | OK                    |
| `201` | Created               |
| `204` | No Content            |
| `301` | Permanent Redirect    |
| `302` | Temporary Redirect    |
| `400` | Bad Request           |
| `401` | Unauthorized          |
| `403` | Forbidden             |
| `404` | Not Found             |
| `429` | Too Many Requests     |
| `500` | Internal Server Error |
| `502` | Bad Gateway           |
| `503` | Service Unavailable   |

A useful first check:

```python
if response.status_code == 200:
    print("Request successful")
```

---

# 📄 Response Object

A Requests response provides access to important information.

```python
response = requests.get(
    "https://httpbin.org/get"
)

print(response.status_code)
print(response.url)
print(response.headers)
print(response.text)
```

Useful attributes include:

| Attribute     | Purpose                |
| ------------- | ---------------------- |
| `status_code` | HTTP status code       |
| `url`         | Final request URL      |
| `headers`     | Response headers       |
| `text`        | Response body as text  |
| `content`     | Response body as bytes |
| `encoding`    | Response encoding      |
| `cookies`     | Response cookies       |
| `history`     | Redirect history       |

---

# 📦 Working with JSON

Many modern APIs return JSON.

```python
response = requests.get(
    "https://httpbin.org/json"
)

data = response.json()

print(data)
```

Example:

```python
print(data["slideshow"])
```

---

# 🔍 Checking JSON Response

```python
response = requests.get(
    "https://httpbin.org/json"
)

if response.ok:
    data = response.json()
    print(data)
```

---

# 🔎 Query Parameters

Query parameters are values added to a URL.

Example URL:

```text
https://example.com/search?q=python&page=1
```

Requests allows parameters to be passed using `params`.

```python
params = {
    "q": "python",
    "page": 1
}

response = requests.get(
    "https://httpbin.org/get",
    params=params
)

print(response.url)
```

Requests handles URL encoding for the parameters.

---

# 🏷️ Request Headers

Headers provide additional information about the request.

```python
headers = {
    "Accept": "application/json"
}

response = requests.get(
    "https://httpbin.org/headers",
    headers=headers
)

print(response.json())
```

A commonly used custom header:

```python
headers = {
    "User-Agent": "MyPythonApplication/1.0"
}
```

---

# 📤 POST Requests

POST requests are commonly used to send data to a server.

```python
data = {
    "name": "Kishor",
    "course": "Python"
}

response = requests.post(
    "https://httpbin.org/post",
    data=data
)

print(response.status_code)
print(response.json())
```

---

# 📝 Sending JSON Data

For APIs that expect JSON:

```python
payload = {
    "name": "Kishor",
    "language": "Python"
}

response = requests.post(
    "https://httpbin.org/post",
    json=payload
)

print(response.json())
```

Using `json=` lets Requests handle JSON serialization for the request body.

---

# 🔄 PUT Requests

PUT is commonly used when an API supports replacing or updating a resource.

```python
payload = {
    "name": "Kishor",
    "role": "Developer"
}

response = requests.put(
    "https://httpbin.org/put",
    json=payload
)

print(response.status_code)
```

---

# ✏️ PATCH Requests

PATCH is commonly used for partial updates.

```python
payload = {
    "role": "AI Developer"
}

response = requests.patch(
    "https://httpbin.org/patch",
    json=payload
)

print(response.status_code)
```

---

# 🗑️ DELETE Requests

DELETE is commonly used to remove a resource.

```python
response = requests.delete(
    "https://httpbin.org/delete"
)

print(response.status_code)
```

---

# 🔐 Authentication

APIs commonly require authentication.

A typical API-token pattern is:

```python
headers = {
    "Authorization": "Bearer YOUR_API_TOKEN"
}

response = requests.get(
    "https://api.example.com/data",
    headers=headers
)
```

### ⚠️ Never Hardcode Secrets

Avoid:

```python
API_KEY = "my-secret-key"
```

Instead, use environment variables:

```python
import os
import requests

api_key = os.getenv("API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(
    "https://api.example.com/data",
    headers=headers
)
```

Keep credentials outside source code and avoid committing `.env` files containing secrets to GitHub.

---

# 🔑 Basic Authentication

Requests supports HTTP Basic Authentication.

```python
from requests.auth import HTTPBasicAuth

response = requests.get(
    "https://httpbin.org/basic-auth/user/pass",
    auth=HTTPBasicAuth(
        "user",
        "pass"
    )
)

print(response.status_code)
```

A shorter form is also available:

```python
response = requests.get(
    "https://example.com",
    auth=("username", "password")
)
```

---

# 🍪 Cookies

Cookies can be accessed from responses.

```python
response = requests.get(
    "https://httpbin.org/cookies/set/theme/dark"
)

print(response.cookies)
```

You can also send cookies:

```python
cookies = {
    "theme": "dark"
}

response = requests.get(
    "https://httpbin.org/cookies",
    cookies=cookies
)

print(response.json())
```

---

# 🔄 Sessions

A `Session` object allows requests to share settings such as cookies and headers across multiple requests.

```python
import requests

session = requests.Session()

session.headers.update({
    "User-Agent": "MyPythonApp/1.0"
})

response = session.get(
    "https://httpbin.org/get"
)

print(response.status_code)
```

Sessions are useful when an application makes multiple requests to the same service.

---

# ⏱️ Timeouts

Always consider using a timeout when making network requests.

```python
response = requests.get(
    "https://httpbin.org/get",
    timeout=10
)
```

Without an appropriate timeout, a network request can wait indefinitely under certain failure conditions.

---

# 🚨 Exception Handling

Requests provides exceptions for network and request-related failures.

```python
import requests

try:
    response = requests.get(
        "https://example.com",
        timeout=10
    )

    print(response.status_code)

except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
```

---

# ✅ `raise_for_status()`

A convenient way to turn unsuccessful HTTP status codes into exceptions:

```python
response = requests.get(
    "https://example.com"
)

response.raise_for_status()

print(response.text)
```

For example:

```python
try:
    response = requests.get(
        "https://example.com",
        timeout=10
    )

    response.raise_for_status()

except requests.exceptions.HTTPError as error:
    print(f"HTTP error: {error}")

except requests.exceptions.RequestException as error:
    print(f"Request error: {error}")
```

---

# 📥 Downloading Files

Requests can be used to download binary content.

```python
import requests

url = "https://example.com/file.zip"

response = requests.get(
    url,
    timeout=30
)

response.raise_for_status()

with open("file.zip", "wb") as file:
    file.write(response.content)
```

For large files, streaming can reduce memory usage:

```python
with requests.get(
    url,
    stream=True,
    timeout=30
) as response:

    response.raise_for_status()

    with open("file.zip", "wb") as file:
        for chunk in response.iter_content(
            chunk_size=8192
        ):
            if chunk:
                file.write(chunk)
```

---

# 📡 Working with REST APIs

A typical REST API workflow:

```text
Client
  │
  ├── GET    → Retrieve data
  ├── POST   → Create resource
  ├── PUT    → Replace/update resource
  ├── PATCH  → Partially update resource
  └── DELETE → Remove resource
        │
        ▼
      REST API
        │
        ▼
     JSON Response
```

Example:

```python
import requests

BASE_URL = "https://api.example.com"

response = requests.get(
    f"{BASE_URL}/users",
    timeout=10
)

response.raise_for_status()

users = response.json()

for user in users:
    print(user)
```

---

# 🧪 API Response Validation

Don't assume every successful HTTP response contains the exact JSON structure your program expects.

Example:

```python
response = requests.get(
    "https://api.example.com/users",
    timeout=10
)

response.raise_for_status()

data = response.json()

if isinstance(data, list):
    for user in data:
        print(user)
```

For production applications, validate important external data before using it.

---

# 🛠️ Building a Reusable API Function

Instead of repeating request logic:

```python
import requests


def get_users(url):
    response = requests.get(
        url,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


users = get_users(
    "https://api.example.com/users"
)
```

A more reusable version:

```python
import requests


def get_json(
    url,
    params=None,
    headers=None,
    timeout=10
):
    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=timeout
    )

    response.raise_for_status()

    return response.json()
```

---

# 🧱 Recommended API Client Pattern

For larger projects, separate API communication from business logic.

```text
Application
    │
    ▼
API Client
    │
    ├── Authentication
    ├── Headers
    ├── Parameters
    ├── Requests
    ├── Error Handling
    └── Response Parsing
    │
    ▼
External API
```

Example:

```python
import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, params=None):
        response = self.session.get(
            f"{self.base_url}{endpoint}",
            params=params,
            timeout=10
        )

        response.raise_for_status()

        return response.json()
```

Usage:

```python
client = APIClient(
    "https://api.example.com"
)

users = client.get("/users")

print(users)
```

---

# 🔍 Debugging Requests

Useful information during debugging:

```python
response = requests.get(
    "https://httpbin.org/get",
    params={"page": 1}
)

print("URL:", response.url)
print("Status:", response.status_code)
print("Headers:", response.headers)
print("Body:", response.text)
```

For JSON:

```python
print(response.json())
```

---

# 🔒 HTTPS and Security

When communicating with external APIs:

* Prefer HTTPS
* Never expose API keys
* Avoid logging sensitive credentials
* Use environment variables or a secret manager
* Set appropriate timeouts
* Validate external responses
* Handle authentication failures
* Avoid sending sensitive information unnecessarily
* Keep dependencies updated

Requests verifies TLS certificates by default for HTTPS requests. Avoid disabling certificate verification unless you have a specific, controlled reason and understand the security implications.

---

# 📊 Requests + Pandas

Requests can retrieve API data that can then be analyzed using Pandas.

```python
import requests
import pandas as pd

response = requests.get(
    "https://api.example.com/users",
    timeout=10
)

response.raise_for_status()

data = response.json()

df = pd.DataFrame(data)

print(df.head())
```

Workflow:

```text
REST API
   ↓
Requests
   ↓
JSON
   ↓
Pandas
   ↓
DataFrame
   ↓
Analysis
```

---

# 📈 Requests + Pandas + Matplotlib

A complete data workflow can look like:

```text
External API
     ↓
Requests
     ↓
JSON Data
     ↓
Pandas
     ↓
Data Cleaning
     ↓
Data Analysis
     ↓
Matplotlib
     ↓
Visualization
```

Example:

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt

response = requests.get(
    "https://api.example.com/sales",
    timeout=10
)

response.raise_for_status()

data = response.json()

df = pd.DataFrame(data)

df.plot(
    x="month",
    y="sales",
    kind="line"
)

plt.show()
```

---

# 🧪 Testing APIs

Requests is useful for manually testing API endpoints.

Example:

```python
import requests

url = "https://httpbin.org/post"

payload = {
    "name": "Kishor",
    "project": "Python Programming"
}

response = requests.post(
    url,
    json=payload,
    timeout=10
)

response.raise_for_status()

print(response.json())
```

---

# 📋 Common Request Parameters

| Parameter | Purpose                      |
| --------- | ---------------------------- |
| `params`  | URL query parameters         |
| `headers` | HTTP request headers         |
| `data`    | Form/body data               |
| `json`    | JSON request body            |
| `cookies` | Request cookies              |
| `auth`    | Authentication               |
| `timeout` | Request timeout              |
| `files`   | Multipart file upload        |
| `stream`  | Stream response content      |
| `verify`  | TLS certificate verification |

---

# 📤 File Uploads

Requests can send files using multipart form data.

```python
import requests

with open(
    "document.pdf",
    "rb"
) as file:

    response = requests.post(
        "https://httpbin.org/post",
        files={
            "file": file
        },
        timeout=30
    )

print(response.status_code)
```

---

# 📝 Form Data

Send form-encoded data using `data=`:

```python
payload = {
    "username": "kishor",
    "language": "python"
}

response = requests.post(
    "https://httpbin.org/post",
    data=payload,
    timeout=10
)
```

---

# ⚠️ Common Mistakes

### ❌ No Timeout

```python
requests.get(url)
```

### ✅ Better

```python
requests.get(
    url,
    timeout=10
)
```

---

### ❌ Hardcoded API Key

```python
API_KEY = "secret-key"
```

### ✅ Better

```python
import os

API_KEY = os.getenv("API_KEY")
```

---

### ❌ Ignoring Errors

```python
response = requests.get(url)

data = response.json()
```

### ✅ Better

```python
response = requests.get(
    url,
    timeout=10
)

response.raise_for_status()

data = response.json()
```

---

### ❌ Assuming Every Response is JSON

```python
data = response.json()
```

### ✅ Better

Validate the response and API contract before parsing it as JSON.

---

# 🧪 Practice Exercises

## 🟢 Beginner

* [ ] Install Requests
* [ ] Send a GET request
* [ ] Print the status code
* [ ] Print response text
* [ ] Access response headers
* [ ] Read JSON responses
* [ ] Pass query parameters
* [ ] Send custom headers
* [ ] Experiment with different HTTP status codes

---

## 🟡 Intermediate

* [ ] Send POST requests
* [ ] Send JSON payloads
* [ ] Send form data
* [ ] Use PUT requests
* [ ] Use PATCH requests
* [ ] Use DELETE requests
* [ ] Handle request exceptions
* [ ] Use `raise_for_status()`
* [ ] Configure timeouts
* [ ] Work with cookies
* [ ] Use sessions
* [ ] Download files

---

## 🔴 Advanced

* [ ] Build a reusable API client
* [ ] Work with authentication
* [ ] Build an API data collector
* [ ] Consume a public REST API
* [ ] Store API data using Pandas
* [ ] Create an API-powered data analysis project
* [ ] Implement robust error handling
* [ ] Add logging to API requests
* [ ] Build a small REST API client library
* [ ] Combine Requests + Pandas + Matplotlib

---

# 📁 Suggested Directory Structure

```text
23-Python-Libraries/
│
└── Requests/
    │
    ├── README.md
    │
    ├── 01-Introduction/
    │   └── first_request.py
    │
    ├── 02-GET-Requests/
    │   └── get_request.py
    │
    ├── 03-POST-Requests/
    │   └── post_request.py
    │
    ├── 04-PUT-PATCH-DELETE/
    │   └── http_methods.py
    │
    ├── 05-Parameters/
    │   └── query_parameters.py
    │
    ├── 06-Headers/
    │   └── headers.py
    │
    ├── 07-JSON/
    │   └── json_data.py
    │
    ├── 08-Authentication/
    │   └── authentication.py
    │
    ├── 09-Cookies-and-Sessions/
    │   └── sessions.py
    │
    ├── 10-Error-Handling/
    │   └── error_handling.py
    │
    ├── 11-Timeouts/
    │   └── timeouts.py
    │
    ├── 12-File-Downloads/
    │   └── download.py
    │
    ├── 13-File-Uploads/
    │   └── upload.py
    │
    ├── 14-API-Clients/
    │   └── api_client.py
    │
    ├── 15-Pandas-Integration/
    │   └── api_to_dataframe.py
    │
    └── 16-Projects/
        └── api_data_project.py
```

---

# 🛠️ Recommended Learning Workflow

```text
Python Basics
      ↓
HTTP Fundamentals
      ↓
Requests Installation
      ↓
GET Requests
      ↓
Response Handling
      ↓
Query Parameters
      ↓
Headers
      ↓
POST / PUT / PATCH / DELETE
      ↓
JSON
      ↓
Authentication
      ↓
Cookies & Sessions
      ↓
Timeouts & Error Handling
      ↓
File Transfers
      ↓
API Client Design
      ↓
Requests + Pandas
      ↓
API-Based Projects
```

---

# 💡 Important Concepts

| Concept           | Importance |
| ----------------- | ---------- |
| HTTP Methods      | ⭐⭐⭐⭐⭐      |
| GET Requests      | ⭐⭐⭐⭐⭐      |
| POST Requests     | ⭐⭐⭐⭐⭐      |
| JSON              | ⭐⭐⭐⭐⭐      |
| Status Codes      | ⭐⭐⭐⭐⭐      |
| Error Handling    | ⭐⭐⭐⭐⭐      |
| Query Parameters  | ⭐⭐⭐⭐       |
| Headers           | ⭐⭐⭐⭐       |
| Authentication    | ⭐⭐⭐⭐⭐      |
| Sessions          | ⭐⭐⭐⭐       |
| Timeouts          | ⭐⭐⭐⭐⭐      |
| File Transfers    | ⭐⭐⭐⭐       |
| API Client Design | ⭐⭐⭐⭐⭐      |

---

# ⚡ Requests Cheat Sheet

### Import

```python
import requests
```

### GET

```python
requests.get(
    url,
    timeout=10
)
```

### POST

```python
requests.post(
    url,
    json=data,
    timeout=10
)
```

### PUT

```python
requests.put(
    url,
    json=data,
    timeout=10
)
```

### PATCH

```python
requests.patch(
    url,
    json=data,
    timeout=10
)
```

### DELETE

```python
requests.delete(
    url,
    timeout=10
)
```

### Parameters

```python
requests.get(
    url,
    params=params
)
```

### Headers

```python
requests.get(
    url,
    headers=headers
)
```

### JSON

```python
response.json()
```

### Status

```python
response.status_code
```

### Raise Error

```python
response.raise_for_status()
```

### Timeout

```python
requests.get(
    url,
    timeout=10
)
```

### Session

```python
session = requests.Session()
```

### File Download

```python
response.content
```

---

# 🧠 Key Takeaways

After completing this module, you should understand:

```text
Requests
│
├── HTTP
│   ├── GET
│   ├── POST
│   ├── PUT
│   ├── PATCH
│   └── DELETE
│
├── Request
│   ├── URL
│   ├── Parameters
│   ├── Headers
│   ├── Body
│   └── Authentication
│
├── Response
│   ├── Status Code
│   ├── Headers
│   ├── Text
│   ├── JSON
│   └── Cookies
│
├── Error Handling
├── Timeouts
├── Sessions
├── File Transfers
│
└── API Integration
```

---

# 📚 Official Learning Resources

* **Requests Documentation:** [https://requests.readthedocs.io/](https://requests.readthedocs.io/)
* **Requests Quickstart:** [https://requests.readthedocs.io/en/latest/user/quickstart/](https://requests.readthedocs.io/en/latest/user/quickstart/)
* **Requests API Reference:** [https://requests.readthedocs.io/en/latest/api/](https://requests.readthedocs.io/en/latest/api/)
* **HTTP Semantics — MDN:** [https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference)
* **REST API Concepts — MDN:** [https://developer.mozilla.org/en-US/docs/Glossary/REST](https://developer.mozilla.org/en-US/docs/Glossary/REST)

---

# 🚀 Next Step

After learning Requests, continue toward API-driven applications:

```text
Python
  ↓
Requests
  ↓
REST APIs
  ↓
JSON
  ↓
Pandas
  ↓
Data Analysis
  ↓
Matplotlib / Seaborn
  ↓
API-Based Projects
  ↓
FastAPI / Flask
  ↓
Production Applications
```

Requests is especially useful when you want your Python applications to **communicate with external services and APIs**.

---

## 👨‍💻 Repository

This module is part of the **Python Programming** learning repository.

**Repository:** `Kishor055/Python-Programming`

**Module:** `23-Python-Libraries/Requests`

---

## 📄 License

This educational material is maintained as part of the repository and is intended for **learning, practice, and educational use**.

---

⭐ **If this repository helps you learn Python and API development, consider giving it a star on GitHub.**
