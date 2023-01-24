import csv
import datetime
import pandas as pd

def LogAction(Action):
    file = open("data.csv", "a", newline="")
    writer = csv.writer(file)
    writer.writerow([str(Action),datetime.datetime.now()])
    print("Data Logged")

def GetTodayData():
    df = pd.read_csv("data.csv")
    df["TimeStamp"] = pd.to_datetime(df["TimeStamp"])
    df_filtered = df[df.TimeStamp.dt.strftime('%Y-%m-%d')==datetime.datetime.now().strftime('%Y-%m-%d')]
    return df_filtered.copy

def GetStandTimeString():
    newdf = GetTodayData()
    newdf.loc[len(newdf.index)] = [None,None] 
    newdf["TimeDiff"] = newdf["TimeStamp"] - newdf["TimeStamp"].shift()
    newdf["IsSummation"] = (newdf["Position"].shift()=="Stand")
    totalTime = newdf['TimeDiff'].loc[newdf['IsSummation'] == True].sum()
    hours, remainder = divmod(totalTime.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours} hour(s) {minutes} minute(s) {seconds} second(s)"

