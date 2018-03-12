import pandas as pd
import csv

df1 = pd.read_csv("raw_data/election_data_1.csv")
df2 = pd.read_csv("raw_data/election_data_2.csv")

df = pd.concat([df1, df2])

with open("results.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    total = df.shape[0]
    print("------------------------------------------------------")
    csvwriter.writerow(["------------------------------------------------------"])
    print("The total number of votes cast: " + str(total))
    csvwriter.writerow(["The total number of votes cast: ", str(total)])


    candidates = df["Candidate"].value_counts()
    names = candidates.index.tolist()
    print("------------------------------------------------------")
    csvwriter.writerow(["------------------------------------------------------"])
    print("A complete list of candidates who received votes: " + str(candidates.index.tolist()))
    csvwriter.writerow(["A complete list of candidates who received votes: ", str(candidates.index.tolist())])
    print("------------------------------------------------------")
    csvwriter.writerow(["------------------------------------------------------"])

    for i in range(len(names)):
        # print(candidates[i]/total)
        print(names[i] + ": " + str(round(candidates[i]/total*100, 2)) + "% (" + str(candidates[i]) + ")")
        csvwriter.writerow([names[i] + ": ", str(round(candidates[i]/total*100, 2)) + "% (" + str(candidates[i]) + ")"])

    print("------------------------------------------------------")
    csvwriter.writerow(["------------------------------------------------------"])
    print("Winner: " + candidates.idxmax())
    csvwriter.writerow(["Winner: ", candidates.idxmax()])


