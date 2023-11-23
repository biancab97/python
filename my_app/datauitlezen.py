import pandas as pd

# Create function for transforming CSV file into Pandas dataframe
def vacaturesUitlezen():
    # Specify path file
    vacatures = 'data/vacatures.csv'
    # Read the CSV file into a Pandas dataframe
    vacatures_df = pd.read_csv(vacatures, delimiter=';')
    # Select only year from Perioden column
    vacatures_df["Jaar"] = vacatures_df["Perioden"].str[:4]
    vacatures_df["Jaar"] = vacatures_df["Jaar"].astype('int64')
    # Mask to select only years starting from 2020 up until now
    vacatures_mask = (vacatures_df["Jaar"] >= 2020)
    vacatures_df = vacatures_df[vacatures_mask]
    # Select columns
    vacatures_df = vacatures_df[["Bedrijfskenmerken", "OpenstaandeVacatures_1", "OntstaneVacatures_2", "VervuldeVacatures_3", "Perioden", "Jaar"]]
    return vacatures_df

# Create function to define labels for different sectors
def vacatureLabels():
    # Specify path file
    sectoren_metadata = 'data/sectoren_metadata.csv'
    # Read the CSV file into a Pandas dataframe
    vacatures_metadata_df = pd.read_csv(sectoren_metadata, delimiter=',')
    return vacatures_metadata_df

# Create function for transforming CSV file into Pandas dataframe
def vacaturesRegioUitlezen():
    # Specify path file
    vacatures_regio = 'data/vacatures_regio.csv'
    #Read the CSV file into a Pandas dataframe
    vacatures_regio_df = pd.read_csv(vacatures_regio, delimiter=',')
    # Select only the year from the Perioden column
    vacatures_regio_df["Jaar"] = vacatures_regio_df["Perioden"].str[:4]
    vacatures_regio_df["Jaar"] = vacatures_regio_df["Jaar"].astype('int')
    # Mask to select only years starting from 2020 up until now
    vacatures_regio_mask = (vacatures_regio_df["Jaar"] >= 2020)
    vacatures_regio_df = vacatures_regio_df[vacatures_regio_mask]
    #Selected columns
    #print(vacatures_regio_df)
    vacatures_regio_df = vacatures_regio_df[["Regios", "OpenstaandeVacatures", "Perioden", "Jaar"]]
    return vacatures_regio_df

# Create function to define different areas/regions in The Netherlands
def regioLabels():
    #Specify path file
    regios_metadata = 'data/regios_metadata.csv'
    # Read the CSV file into a Pandas dataframe
    regios_metadata_df = pd.read_csv(regios_metadata, delimiter=',')
    return regios_metadata_df