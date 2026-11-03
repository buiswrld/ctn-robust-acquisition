# Troy data exploration of demographic data from NHANES dataset
import pandas as pd

# Loading demographic data from CDC
df_demograph = pd.read_sas('DEMO_L.xpt', format = 'xport')

# for google colab, I think that you just use from google.colab import drive, then drive.mount('/content/drive').
# I didn't run this code on colab since I was able to just run it from my vscode since I had this dataset already installed, but let me know if I should change the data to be compatible with colab.



print("Printing first few rows of dataset")
print(df_demograph.head())

print("\nInformation about the dataset: ")
print(df_demograph.info())

print("\nStatistical summary: ")
print(df_demograph.describe())

# I analyzed the demographic data (DEMO_L.xpt) and I learned that it has a lot of values that are not numbers despite each data type being a float. I'm assuming that these NaN values are empty values in the dataset.
# There are 26 columns in the dataset, each having the principle datatype of a float. 
# I noticed that certain columns tend to have specific values that are likely resulting from a yes/no answer or a range of simple answers. For example, the column labelled SDDSRVYR contains only the number 12, which is
# probably something people check off or not. Also, other columns like RIDRETH1, RIDRETH3, and DMDBORN4 seem to cintain relatively specific values from data with small variation.

