import pandas as pd
import pyarrow 
def toparquet(fx):
    def conversion(*args):
        response=fx(*args)
        response.to_parquet("new.parquet")
    return conversion
@toparquet
def csvinput(name):
    df=pd.read_csv(name)
    return df


obj=csvinput(r"D:\Advanced Python Beyond Basics\new.csv")