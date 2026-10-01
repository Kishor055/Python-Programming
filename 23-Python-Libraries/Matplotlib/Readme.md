# 📊 Matplotlib — Python Data Visualization

> A structured learning module for understanding **Matplotlib**, Python's foundational library for creating data visualizations, charts, plots, and graphical representations.

---

## 📌 Overview

**Matplotlib** is a powerful Python visualization library used to transform numerical and categorical data into meaningful graphical representations.

It provides APIs for creating:

* 📈 Line charts
* 📊 Bar charts
* 🥧 Pie charts
* 🔵 Scatter plots
* 📦 Histograms
* 📉 Area charts
* 🎯 Box plots
* 🌡️ Heatmaps
* 🧩 Subplots
* 🧊 3D visualizations
* 🎞️ Animations
* 🖼️ Image visualizations

Matplotlib supports both quick interactive plotting through `pyplot` and a more structured **object-oriented API** using `Figure` and `Axes`. The object-oriented approach is especially useful for reusable scripts and larger projects. ([Matplotlib][1])

---

## 🎯 Learning Objectives

By completing this module, you will learn how to:

* Understand the Matplotlib architecture
* Create and customize basic plots
* Work with `Figure` and `Axes`
* Use `matplotlib.pyplot`
* Add titles, labels, legends, and annotations
* Customize colors, markers, and line styles
* Create multiple plots using subplots
* Visualize categorical and numerical data
* Create statistical visualizations
* Work with dates and time-series data
* Create 3D plots
* Save visualizations to files
* Build publication-ready charts
* Follow reusable visualization practices

---

## 🧰 Installation

Install Matplotlib using `pip`:

```bash
pip install matplotlib
```

Verify the installation:

```python
import matplotlib

print(matplotlib.__version__)
```

The official Matplotlib documentation currently provides installation options for `pip`, Conda, Pixi, and `uv`. ([Matplotlib][2])

---

## 📦 Import Convention

The most common import for plotting is:

```python
import matplotlib.pyplot as plt
```

For numerical data, Matplotlib is frequently used together with NumPy:

```python
import numpy as np
import matplotlib.pyplot as plt
```

---

# 🏗️ Matplotlib Architecture

A useful way to understand Matplotlib is through its main building blocks:

```text
Figure
│
├── Axes
│   ├── X-Axis
│   ├── Y-Axis
│   ├── Lines
│   ├── Markers
│   ├── Labels
│   └── Legend
│
└── Other Artists
```

### Figure

The **Figure** represents the complete visualization or canvas.

```python
fig = plt.figure()
```

### Axes

An **Axes** represents the actual plotting area where data is visualized.

```python
fig, ax = plt.subplots()
```

The official documentation recommends `plt.subplots()` as a convenient way to create a Figure and one or more Axes. ([Matplotlib][1])

---

# 🚀 Your First Plot

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_title("Simple Line Plot")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

plt.show()
```

### Visualization Flow

```text
Data
 ↓
Figure
 ↓
Axes
 ↓
Plot
 ↓
Labels / Title / Legend
 ↓
Display or Save
```

---

# 📈 Core Plot Types

## 1. Line Plot

Used for showing trends and continuous data.

```python
plt.plot(x, y)
plt.show()
```

---

## 2. Bar Chart

Useful for comparing categories.

```python
categories = ["A", "B", "C", "D"]
values = [25, 40, 30, 55]

plt.bar(categories, values)

plt.title("Category Comparison")
plt.xlabel("Category")
plt.ylabel("Value")

plt.show()
```

---

## 3. Scatter Plot

Useful for examining relationships between two numerical variables.

```python
x = [1, 2, 3, 4, 5]
y = [5, 3, 6, 2, 7]

plt.scatter(x, y)

plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
```

---

## 4. Histogram

Used to understand the distribution of numerical data.

```python
data = [12, 15, 15, 18, 20, 22, 22, 23, 25, 28]

plt.hist(data, bins=5)

plt.title("Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()
```

---

## 5. Pie Chart

Useful for displaying proportions.

```python
labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [40, 25, 20, 15]

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%"
)

plt.title("Programming Language Usage")

plt.show()
```

---

## 6. Box Plot

Useful for understanding statistical distributions, spread, and potential outliers.

```python
data = [10, 12, 15, 18, 20, 22, 25, 30, 45]

plt.boxplot(data)

plt.title("Box Plot")
plt.ylabel("Values")

plt.show()
```

---

# 🎨 Plot Customization

Matplotlib provides extensive control over plot appearance, including labels, ticks, colors, markers, line styles, legends, and layout. ([Matplotlib][3])

### Line Style

```python
plt.plot(
    x,
    y,
    linestyle="--"
)
```

### Marker

```python
plt.plot(
    x,
    y,
    marker="o"
)
```

### Line Width

```python
plt.plot(
    x,
    y,
    linewidth=2
)
```

### Combining Properties

```python
plt.plot(
    x,
    y,
    marker="o",
    linestyle="--",
    linewidth=2
)
```

---

# 🏷️ Titles and Labels

Good visualizations should clearly communicate what the axes and chart represent.

```python
fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_title("Sales Growth")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue")

plt.show()
```

---

# 🗂️ Legends

Legends help distinguish multiple datasets.

```python
x = [1, 2, 3, 4, 5]

y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

fig, ax = plt.subplots()

ax.plot(x, y1, label="Dataset A")
ax.plot(x, y2, label="Dataset B")

ax.legend()

plt.show()
```

---

# 🧩 Subplots

Multiple visualizations can be placed inside a single Figure.

```python
fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, y)
axes[0, 0].set_title("Line Plot")

axes[0, 1].bar(
    ["A", "B", "C"],
    [10, 20, 15]
)
axes[0, 1].set_title("Bar Chart")

axes[1, 0].scatter(x, y)
axes[1, 0].set_title("Scatter Plot")

axes[1, 1].hist(y)
axes[1, 1].set_title("Histogram")

plt.tight_layout()
plt.show()
```

Matplotlib supports multiple Axes within a Figure and provides several layout approaches for arranging them. ([Matplotlib][3])

---

# 🧠 Object-Oriented API

For larger and reusable projects, prefer the object-oriented approach:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot(
    [1, 2, 3, 4],
    [1, 4, 2, 3]
)

ax.set_title("Object-Oriented Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")

plt.show()
```

Instead of repeatedly using global `plt` functions, you explicitly work with the `Axes` object:

```text
Figure
  │
  └── Axes
       │
       ├── plot()
       ├── set_title()
       ├── set_xlabel()
       ├── set_ylabel()
       └── legend()
```

Matplotlib's official guidance recommends the object-oriented style particularly for complicated plots, reusable functions, and larger projects. ([Matplotlib][1])

---

# 📐 Multiple Datasets

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

sales_2024 = [20, 35, 40, 55, 70]
sales_2025 = [25, 40, 50, 65, 85]

fig, ax = plt.subplots()

ax.plot(
    x,
    sales_2024,
    marker="o",
    label="2024"
)

ax.plot(
    x,
    sales_2025,
    marker="o",
    label="2025"
)

ax.set_title("Sales Comparison")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")

ax.legend()

plt.show()
```

---

# 💾 Saving Plots

Charts can be exported to image files.

```python
plt.savefig("chart.png")
```

For higher-quality output:

```python
plt.savefig(
    "chart.png",
    dpi=300,
    bbox_inches="tight"
)
```

Common output formats include:

```text
PNG
JPG
SVG
PDF
```

---

# 📊 Common Visualization Use Cases

Matplotlib can be used for:

| Use Case                 | Recommended Plot |
| ------------------------ | ---------------- |
| Trend analysis           | Line Plot        |
| Category comparison      | Bar Chart        |
| Relationship analysis    | Scatter Plot     |
| Data distribution        | Histogram        |
| Statistical spread       | Box Plot         |
| Percentage composition   | Pie Chart        |
| Multiple comparisons     | Subplots         |
| Scientific visualization | Line / Scatter   |
| Time-series analysis     | Line Plot        |
| 3D visualization         | 3D Plot          |

Matplotlib's official example gallery includes line plots, bars, markers, subplots, 3D visualizations, contours, and many other visualization patterns. ([Matplotlib][4])

---

# 🔬 Matplotlib with NumPy

Matplotlib works naturally with NumPy arrays.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_title("Sine Wave")

plt.show()
```

---

# 🐼 Matplotlib with Pandas

Matplotlib can also be used with Pandas data.

```python
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [120, 150, 180, 210]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots()

ax.plot(
    df["Month"],
    df["Sales"],
    marker="o"
)

ax.set_title("Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")

plt.show()
```

---

# 🧪 Practice Exercises

### Beginner

* [ ] Create a basic line plot
* [ ] Create a bar chart
* [ ] Create a scatter plot
* [ ] Create a histogram
* [ ] Create a pie chart
* [ ] Add titles and axis labels
* [ ] Add a legend
* [ ] Change markers and line styles

### Intermediate

* [ ] Create a 2×2 subplot layout
* [ ] Compare two datasets
* [ ] Customize tick labels
* [ ] Create a box plot
* [ ] Save plots as PNG and PDF
* [ ] Visualize a Pandas DataFrame
* [ ] Create a time-series visualization

### Advanced

* [ ] Create a multi-axis visualization
* [ ] Build a reusable plotting function
* [ ] Create a 3D visualization
* [ ] Work with annotations
* [ ] Customize Matplotlib styles
* [ ] Create an animated visualization
* [ ] Build a complete data visualization project

---

# 📁 Suggested Directory Structure

```text
23-Python-Libraries/
│
└── Matplotlib/
    │
    ├── README.md
    │
    ├── 01-Introduction/
    │   └── basics.py
    │
    ├── 02-Line-Plots/
    │   └── line_plot.py
    │
    ├── 03-Bar-Charts/
    │   └── bar_chart.py
    │
    ├── 04-Scatter-Plots/
    │   └── scatter_plot.py
    │
    ├── 05-Histograms/
    │   └── histogram.py
    │
    ├── 06-Pie-Charts/
    │   └── pie_chart.py
    │
    ├── 07-Box-Plots/
    │   └── box_plot.py
    │
    ├── 08-Subplots/
    │   └── subplots.py
    │
    ├── 09-Customization/
    │   └── customization.py
    │
    ├── 10-NumPy-Integration/
    │   └── numpy_visualization.py
    │
    ├── 11-Pandas-Integration/
    │   └── pandas_visualization.py
    │
    └── 12-Projects/
        └── data_visualization_project.py
```

---

# 🛠️ Recommended Workflow

A professional visualization workflow can follow these steps:

```text
1. Understand the Data
        ↓
2. Select the Appropriate Chart
        ↓
3. Create Figure & Axes
        ↓
4. Plot the Data
        ↓
5. Add Titles & Labels
        ↓
6. Add Legend / Annotations
        ↓
7. Improve Layout
        ↓
8. Validate the Visualization
        ↓
9. Export the Figure
```

---

# 📚 Learning Resources

### Official Documentation

* [Matplotlib Documentation](https://matplotlib.org/stable/?utm_source=chatgpt.com)
* [Matplotlib Quick Start Guide](https://matplotlib.org/stable/users/explain/quick_start.html?utm_source=chatgpt.com)
* [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/?utm_source=chatgpt.com)
* [Matplotlib Examples Gallery](https://matplotlib.org/stable/gallery/?utm_source=chatgpt.com)
* [Matplotlib API Reference](https://matplotlib.org/stable/api/?utm_source=chatgpt.com)

The official tutorials cover topics ranging from basic plotting and the plotting lifecycle to styling, legends, layouts, animations, transformations, and advanced visualization techniques. ([Matplotlib][5])

---

# 🎓 Key Takeaways

After completing this module, you should understand:

```text
Matplotlib
│
├── pyplot
│
├── Figure
│
├── Axes
│
├── Line Plots
├── Bar Charts
├── Scatter Plots
├── Histograms
├── Pie Charts
├── Box Plots
│
├── Subplots
├── Labels
├── Legends
├── Annotations
├── Styling
│
├── NumPy Integration
├── Pandas Integration
│
└── Visualization Projects
```

---

## 🚀 Next Step

Once you are comfortable with Matplotlib, continue with:

**NumPy → Pandas → Matplotlib → Seaborn → Data Analysis → Machine Learning Visualization**

This progression builds a strong foundation for **Data Science, Machine Learning, Exploratory Data Analysis (EDA), and AI projects**.

---

## 👨‍💻 Repository

This module is part of the **Python Programming** learning repository.

**Repository:**
`Kishor055/Python-Programming`

**Module:**
`23-Python-Libraries/Matplotlib`

---

## 📄 License

This educational material is maintained as part of the repository and is intended for **learning, practice, and educational use**.

---
