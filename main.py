import sys
import pandas as pd


class main:

    def __init__(self,file=sys.argv[1]):
        print("\033[1m"+"Welcome to Machine Learning Perprocessor CLI!!!"+"\033[0m\n")

        self.file=file
        file_extension=file.split('.')[1]
        if file_extension!='csv':
            print("Give a CSV file")
            exit()
        
    def remove_target(self):
        df=pd.read_csv(self.file)
        print("Your Dataset!!!!",df.head(),sep='\n\n')
        print("\nDataset Columns")
        print("---",list(df.columns),"---\n")
        del_target=input(("\nDo you want to remove Target Variable ?(y/n) : "))
        if del_target=='y':
            for _ in range(100):
                col=str(input("\nEnter Your Target Column to remove from Dataset : "))
                if col not in df.columns:
                    print("\nEnter a Valid column name!! Try again")
                else:
                    break
            x=input("\nAre you Sure you want to remove ? (y/n) : ")
            if x=='y':
                df=df.drop(col,axis=1)
                print(f'\n\t\t\t\t After Target Column {col} removed',df.head(),sep='\n')
        return df

    def choose(self,df):
        pass



m=main()
df=m.remove_target()
m.choose(df)