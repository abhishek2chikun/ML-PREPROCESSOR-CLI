class data_description:
    def __init__(self,df):
        self.df=df
        print("\033[1m","\t\t\tData Description\t\t\t","\033[0m")
        for _ in range(100):
            x=int(input("""
                    1. Show the Dataset\n
                    2. Describe properties of Dataset\n
                    3. Describe specific Columns\n
                    -1 to Return back\nYou Entered:"""))
            if x==1:
                y=int(input("Enter no. of value you want to display:"))
                print("\033[1m","\t\t\tDiscription of Dataset\n","\033[0m",self.df.head(y))
            elif x==2:
                print("\033[1m","\t\t\tDiscription of Dataset\n","\033[0m",self.df.describe())
                print("\033[1m","\n\t\t\tInfo of Dataset\n","\033[0m")
                print(self.df.info())
            elif x==3:
                print(self.df.columns)
                y=str(input("Enter column to describe:"))
                print("\033[1m",f"\nDescription of coloumn {y}\n","\033[0m",self.df[y].describe())
            elif x==-1:
                return
    
        