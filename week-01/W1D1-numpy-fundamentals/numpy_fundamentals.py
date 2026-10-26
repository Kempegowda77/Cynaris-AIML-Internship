import numpy as np
import pandas as pd


# ============================================================
# W1D1 — Python for ML: NumPy Fundamentals
# ============================================================

print("=" * 60)
print("W1D1 — NumPy Fundamentals")
print("=" * 60)


# ------------------------------------------------------------
# Task 1: Create 1D, 2D and 3D arrays and verify shapes
# ------------------------------------------------------------

array_1d = np.array([10, 20, 30, 40, 50])

array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

array_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("\n--- Task 1: Arrays and Shapes ---")

print("1D Array:")
print(array_1d)
print("Shape:", array_1d.shape)

print("\n2D Array:")
print(array_2d)
print("Shape:", array_2d.shape)

print("\n3D Array:")
print(array_3d)
print("Shape:", array_3d.shape)


# ------------------------------------------------------------
# Task 2: Broadcasting
# ------------------------------------------------------------

print("\n--- Task 2: Broadcasting ---")

prices = np.array([100, 200, 300])
tax_rate = 0.18

tax_amount = prices * tax_rate
prices_with_tax = prices + tax_amount

print("Original prices:", prices)
print("Tax amount:", tax_amount)
print("Prices with tax:", prices_with_tax)


# ------------------------------------------------------------
# Task 2: Vectorised Operations
# ------------------------------------------------------------

print("\n--- Vectorised Operations ---")

numbers = np.array([1, 2, 3, 4, 5])

print("Original:", numbers)
print("Squared:", numbers ** 2)
print("Doubled:", numbers * 2)
print("Plus 10:", numbers + 10)


# ------------------------------------------------------------
# Task 2: Matrix Multiplication
# ------------------------------------------------------------

print("\n--- Matrix Multiplication ---")

matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])

matrix_result = matrix_a @ matrix_b

print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

print("\nA @ B:")
print(matrix_result)


# ------------------------------------------------------------
# Task 3: Statistics using a real CSV dataset
# ------------------------------------------------------------

print("\n--- Task 3: Dataset Statistics ---")

dataset = pd.read_csv("data/student_scores.csv")

hours_studied = dataset["Hours_Studied"].to_numpy()
exam_scores = dataset["Exam_Score"].to_numpy()

mean_score = np.mean(exam_scores)
standard_deviation = np.std(exam_scores)
correlation = np.corrcoef(hours_studied, exam_scores)[0, 1]

print("\nDataset:")
print(dataset)

print("\nMean Exam Score:", mean_score)
print("Standard Deviation:", standard_deviation)
print("Correlation:", correlation)


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("W1D1 COMPLETED SUCCESSFULLY")
print("=" * 60)