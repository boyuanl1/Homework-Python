import pandas as pd

budget1 = pd.read_csv('raw_data/budget_data_1.csv')
budget2 = pd.read_csv('raw_data/budget_data_2.csv')

len1 = budget1.shape[0]
len2 = budget2["Date"].shape[0]

print("The total number of months: " + str(len1 + len2))

rev1 = budget1["Revenue"].sum()
rev2 = budget2["Revenue"].sum()

print("The total amount of revenue: " + str(rev1 + rev2))

diff1 = budget1["Revenue"].diff()
diff2 = budget2["Revenue"].diff()

avgDiff = (diff1.mean() * len1 + diff2.mean() * len2)/(len1 + len2)
print("The average change in revenue: " + str(round(avgDiff, 2)))

diffMax = diff1.max() if diff1.max() > diff2.max() else diff2.max()
print("The greatest increase in revenue: " + str(diffMax))

diffMin = diff1.min() if diff1.min() < diff2.min() else diff2.min()
print("The greatest decrease in revenue: " + str(diffMin))

result = pd.DataFrame({
    "Item": ["The total number of months: ", "The total amount of revenue: ", "The average change in revenue: ", "The greatest increase in revenue: ", "The greatest decrease in revenue: "],
    "Results": [len1 + len2, rev1 + rev2, round(avgDiff, 2), diffMax, diffMin]
})


result.to_csv("result.csv", index=False, sep='\t', header=False)