import csv
filename = "puzzle-file-2.csv"
num_list = []
sum_difference = 0
row_num = 1


with open(filename, "rt") as file:
    csvreader = csv.reader(file, delimiter=',')
    for row in csvreader:
        num_list.append(row)

#Convert all strings of numbers to integers, and sort the inner lists
for item in num_list:
    for index in range(len(item)):
        item[index] = int(item[index])
    item.sort()

#Iterate through the inner-lists and compare the lowest and highest numbers.
for item in num_list:
    lowest = item[0]
    highest = item[len(item)-1]
    difference = highest - lowest
    sum_difference += difference

    print(f"Row number {row_num}:")
    print(f"Highest number: {highest}, Lowest number: {lowest}, The difference: {difference}")
    print(f"\nSum of differences: {sum_difference}\n")

    row_num += 1

print(f"\nThe checksum for this spreadsheet is: {sum_difference}")