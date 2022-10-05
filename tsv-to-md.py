__doc__ = """
This converts a delimited csv file to a markdown table using pandas.
Run with the -h option to see arguments
"""

import pandas as pd
import argparse

csvFileDefault = "NFRs.tsv"
mdFileDefault = "NFRs.md"
headerRowDefault = 0

parser = argparse.ArgumentParser(description="Convert tabular data to markdown tables.")
parser.add_argument(
    "--source",
    dest="csvFile",
    default=csvFileDefault,
    help="The delimited source file [" + csvFileDefault + "]",
)
parser.add_argument(
    "--dest",
    dest="mdFile",
    default=mdFileDefault,
    help="The target md file [" + mdFileDefault + "]",
)
parser.add_argument(
    "--sep",
    dest="sep",
    default="\t",
    help="Source column separator [tab]",
)
parser.add_argument(
    "--header",
    dest="header",
    default=headerRowDefault,
    help="The header row [" + str(headerRowDefault) + "]",
)

args = parser.parse_args()

df = pd.read_csv(args.csvFile, engine="python", sep=args.sep, header=args.header)
with open(args.mdFile, "w") as md:
    df.fillna("", inplace=True)
    df.to_markdown(buf=md, index=False)
