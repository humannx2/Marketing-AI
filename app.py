import pandas as pd
from transformers import pipeline

# # demo data
# data = {
#     "Campaign ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     "Impressions": [1000, 2000, 1500, 3000, 2500, 1800, 2200, 1400, 5000, 3200],
#     "Clicks": [50, 20, 10, 100, 80, 30, 55, 70, 250, 160],
#     "Conversions": [5, 1, 0, 10, 8, 3, 6, 7, 25, 15],
#     "Spend": [100, 200, 150, 300, 250, 180, 220, 140, 500, 320],
#     "Revenue": [500, 400, 0, 1000, 800, 350, 600, 700, 2500, 1500],
#     "Status": ["Active", "Active", "Paused", "Active", "Paused", "Active", "Active", "Active", "Paused", "Active"]
# }

# df=pd.DataFrame(data)
# print(df.head())
# df.to_csv("Marketing Data.csv",index=False)

# Metric Calulation
def metric(df):
    df["CTR"] = (df["Clicks"] / df["Impressions"]) * 100
    df["ROAS"] = df["Revenue"] / df["Spend"]
    df["Cost_per_Conversion"] = df["Spend"] / df["Conversions"].replace(0, float("inf"))
    return df

def calculation(file):
    df=pd.read_csv(file)
    df=metric(df)
    return df

# updated dataframe
df= calculation("Marketing Data.csv")

def analyze_ad_copy(text):
    llm = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    return llm(text)

# Example Ad Copy Analysis
insights = analyze_ad_copy("Best discounts on electronics!")
print(insights)


# def optimizaton()

