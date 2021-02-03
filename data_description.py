class data_description:
    def __init__(self,df):
        self.df=df
        print(self.df.describe())