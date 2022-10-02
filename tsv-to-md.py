import pandas as pd

csvFile = "NFRs.tsv"
mdFile = "NFRs.md"
df = pd.read_csv(csvFile, engine="python", sep="\t", header=0)
with open(mdFile, "w") as md:
    df.fillna("", inplace=True)
    df.to_markdown(buf=md, index=False)
