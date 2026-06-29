# Yeh i Think last tpic for practice
import pandas as pd 
class dataextaction:
    def __init__(self,filepath:str):
        self.filepath=filepath
        
    def readcsv(self,separator:str):
        df=pd.read_csv(self.filepath,sep=separator)
        print(df.head())
    
csvread=dataextaction(r"D:\Advanced Python Beyond Basics\new.csv")
csvread.readcsv(",")