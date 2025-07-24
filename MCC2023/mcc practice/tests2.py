#Initialize a list of lists (matrix) containing the four rows of numbers.
matrix = []
with open("C:\Users\zanyi\OneDrive\Git hub\Python\MCC\Real\innovation.txt") as f:
	for i in f:
		matrix.append(list(map(int,i.split(" "))))
#2. Calculate the sum of the first two elements in each row, store them in a list,
# and sort the rows based on this sum in ascending order, and then by the total four elements in descending order.
row_sums = [(row[0] + row[1], sum(row), row) for row in matrix]
row_sums = sorted(row_sums, key=lambda x: (x[0], sum(x[2])), reverse=True)
#3. Sum the first and second elements based on the top m-1 rows.
m = 1277
n = 2000
x = sum(row[0] + row[1] for row in row_sums[:m - 1])
#4. Keep the last m n + 1 rows from the sorted matrix.
selected_rows = row_sums[-(n - m + 1):]
# 5. Find the maximum sum of the four elements in the remaining rows.
max_sum = max([sum(row) for row in selected_rows])
# 6. Add the result from step 4 to the sum of the first two elements calculated in step 3.
result = x + max_sum
print("x -", x)
print("y-", max_sum)
print("result", result)