import pandas as pd
import os 

data={"Name":["Alica","Bob","Charlie"],
      "Age":[25,30,35],
      "City":["Now-york","Itlay","Pakistan"]}

df=pd.DataFrame(data)


# Adding new row to df for v2
# new_row_low={"Name":"jowlin","Age":20,"City":"Portgal"}
# df.loc[len(df.index)]=new_row_low

# Adding new row to df for v3
# new_row_low={"Name":"jack","Age":15,"City":"austrlia"}
# df.loc[len(df.index)]=new_row_low

# Ensure the "data" directory exists at the root level
data_dir="data"
os.makedirs(data_dir,exist_ok=True)

# Define the file path 
File_path=os.path.join(data_dir,"sample_data.csv")
# Save the Dataframe to a CSV , Include column name 
df.to_csv(File_path, index=False)

print(f"CSV file saved to file path")