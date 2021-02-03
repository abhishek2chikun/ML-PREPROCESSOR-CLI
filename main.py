import sys
import pandas as pd
import categorical
import data_description
import download
import feature_scaling
import imputation

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
        print("\033[1m","What you want to do ??? (Preprocessing)","\033[0m\n")
        x=int(input("""
                1. Data Description\n
                2. Handling NULL values\n
                3. Encoding Categorical Data\n
                4. Feature Scaling of the Dataset\n
                5. Download the modification Dataset\n"""))
        if x==1:
            data_description.data_description(df)
        elif x==2:
            imputation.imputation(df)
        elif x==3:
            categorical.categorical(df)
        elif x==4:
            feature_scaling.feature_scaling(df)
        elif x==5:
            download.download(df)
        else:
            print("Wrong Choice")
        

m=main()
df=m.remove_target()
m.choose(df)