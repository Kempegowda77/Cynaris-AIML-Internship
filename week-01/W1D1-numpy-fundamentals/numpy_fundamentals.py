import numpy as np
import pandas as pd

print("=" * 60)
print("W1D1 - NumPy Fundamentals")
print("=" * 60)

# Task 1: Arrays and Shapes
array_1d = np.array([10, 20, 30, 40, 50])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

assert array_1d.shape == (5,)
assert array_2d.shape == (2, 3)
assert array_3d.shape == (2, 2, 2)

print("\n--- Task 1: Arrays and Shapes ---")
print("1D:", array_1d, "Shape:", array_1d.shape)
print("2D:\n", array_2d, "Shape:", array_2d.shape)
print("3D:\n", array_3d, "Shape:", array_3d.shape)

# Task 2: Broadcasting
print("\n--- Task 2: Broadcasting ---")
prices = np.array([100, 200, 300])
tax_rate = 0.18
prices_with_tax = prices + (prices * tax_rate)

print("Original prices:", prices)
print("Prices with tax:", prices_with_tax)

# Vectorized operations
print("\n--- Vectorised Operations ---")
numbers = np.array([1, 2, 3, 4, 5])
print("Squared:", numbers ** 2)
print("Doubled:", numbers * 2)
print("Plus 10:", numbers + 10)

# Matrix multiplication
print("\n--- Matrix Multiplication ---")
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

assert matrix_a.shape[1] == matrix_b.shape[0]

matrix_result = matrix_a @ matrix_b
print("A @ B:")
print(matrix_result)

# Task 3: Statistics
print("\n--- Task 3: Dataset Statistics ---")
dataset = pd.read_csv("data/student_scores.csv")

hours_studied = dataset["Hours_Studied"].to_numpy()
exam_scores = dataset["Exam_Score"].to_numpy()

mean_score = np.mean(exam_scores)
standard_deviation = np.std(exam_scores)
correlation = np.corrcoef(hours_studied, exam_scores)[0, 1]

print(dataset)
print("\nMean Exam Score:", mean_score)
print("Standard Deviation:", standard_deviation)
print("Correlation:", correlation)

print("\n" + "=" * 60)
print("W1D1 COMPLETED SUCCESSFULLY")
print("=" * 60)
