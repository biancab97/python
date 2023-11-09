import pandas as pd


def salarisUitlezen():
    '''
    Selects rows from the DataFrame starting from the year 2022.
    Selected columns include:
    - BedrijfstakkenBranchesSBI2008
    - MaandloonExclusiefOverwerk_6
    - Perioden
    - KenmerkenBaan
    - Jaar
    '''
    # Specify the path for the salaris data file
    salaris_file = 'data/salarisdata.csv'

    # Read the CSV file into a Pandas DataFrame
    df_salaris = pd.read_csv(salaris_file, delimiter=';')
    
    # Select only the first 4 characters of the 'Perioden' column
    df_salaris["Jaar"] = df_salaris["Perioden"].str[:4]
    df_salaris["Jaar"] = df_salaris["Jaar"].astype('int64')

    # Mask to select only years from 2022 and 'KenmerkenBaan' equals 10000
    salaris_mask = (df_salaris["Jaar"] >= 2022) & (df_salaris["KenmerkenBaan"] == 10000)
    df_salaris = df_salaris[salaris_mask]
    
    # Selected columns
    df_salaris = df_salaris[["KenmerkenBaan", "BedrijfstakkenBranchesSBI2008", "MaandloonExclusiefOverwerk_6", "Perioden", "Jaar"]]

    # Drop rows with 'KenmerkenBaan' values 100460 - 100470
    df_salaris.drop(df_salaris[(df_salaris['KenmerkenBaan'] == '100460') & (df_salaris['KenmerkenBaan'] == '100470')].index, inplace=True)    
    
    return df_salaris

def salarisBrancheLabels():
     # Specify the path for the metadata file
    metadata_file = 'data/salaris_metadata_aangepast.csv'
    
    # Read the CSV file into a Pandas DataFrame
    df_metadata = pd.read_csv(metadata_file, delimiter=';')
    
    return df_metadata