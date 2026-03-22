# DevelopersHub Internship — Data Science Tasks

> **Status:** Task 1 ✅ Complete | Task 2 🔜 Upcoming

---

# Task 1: Exploring and Visualizing a Simple Dataset (Iris)

## Objective
Load, inspect, and visualize the Iris dataset to understand data trends and distributions.

## Dataset
**Iris Dataset** — a classic dataset containing measurements (in cm) for 150 iris flowers across 3 species: *setosa*, *versicolor*, and *virginica*.  
Loaded directly via the `seaborn` library (no manual download needed).

## What the Script Does
- Loads the Iris dataset into a **pandas DataFrame**
- Prints:
  - Dataset shape (rows × columns)
  - Column names
  - First 5 rows using `.head()`
- Prints `.info()` and `.describe()` for summary statistics
- Generates and saves three visualizations:
  - **Scatter plot** — relationship between sepal length and petal length, colored by species
  - **Histograms** — value distribution for each numeric feature
  - **Box plots** — spread and outlier identification for each feature

## Technologies Used
- Python 3
- pandas
- seaborn
- matplotlib

## Setup & Installation

1. Clone the repository (or download the files):
   ```bash
   git clone https://github.com/IrfanKhan154/developershub-task1-iris-visualization.git
   cd developershub-task1-iris-visualization
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Run the Script

```bash
python task1_iris_analysis.py
```

## Expected Output

**Console output:**
- Dataset shape (150, 5)
- Column names: sepal_length, sepal_width, petal_length, petal_width, species
- First 5 rows of data
- Data types and non-null counts via `.info()`
- Summary statistics (mean, std, min, max, etc.) via `.describe()`

**Plot files saved in the same folder:**
- `scatter_plot.png` — scatter plot of sepal length vs petal length
- `histograms.png` — histograms for all four numeric features
- `box_plots.png` — box plots for outlier detection

## Skills Demonstrated
- Data loading and inspection with pandas
- Descriptive statistics and data exploration
- Data visualization with matplotlib and seaborn

---

# Task 2: Coming Soon 🔜

Task 2 details have not yet been provided. This section will be updated once the requirements are confirmed.

> **Note:** The repository is ready and waiting for Task 2 requirements.
