import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------------------------
# Task 1: Load and Inspect the Iris Dataset
# ----------------------------------------

# Load Iris dataset via seaborn into a pandas DataFrame
iris = sns.load_dataset("iris")

print("=== Dataset Shape ===")
print(iris.shape)

print("\n=== Column Names ===")
print(list(iris.columns))

print("\n=== First 5 Rows ===")
print(iris.head())

print("\n=== Dataset Info ===")
iris.info()

print("\n=== Descriptive Statistics ===")
print(iris.describe(include="all"))

# ----------------------------------------
# Visualizations
# ----------------------------------------

sns.set(style="whitegrid")

# 1) Scatter plot: relationship between sepal length and petal length, colored by species
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=iris,
    x="sepal_length",
    y="petal_length",
    hue="species",
    palette="deep",
    s=80
)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()

# 2) Histograms: value distributions for all numeric features
numeric_cols = iris.select_dtypes(include="number").columns
iris[numeric_cols].hist(figsize=(10, 8), bins=15, edgecolor="black", color="steelblue")
plt.suptitle("Histograms of Iris Features", y=1.02, fontsize=14)
plt.tight_layout()
plt.savefig("histograms.png")
plt.show()

# 3) Box plots: identify outliers across all numeric features
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris[numeric_cols], palette="Set2")
plt.title("Box Plots of Iris Features")
plt.xlabel("Features")
plt.ylabel("Values (cm)")
plt.tight_layout()
plt.savefig("box_plots.png")
plt.show()

print("\nAll plots saved: scatter_plot.png, histograms.png, box_plots.png")
