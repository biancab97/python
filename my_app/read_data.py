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

def geslachtSalaris():
     # Specify the path for the salaris data file
    salaris_file = 'data/salarisdata.csv'

    # Read the CSV file into a Pandas DataFrame
    df_salaris = pd.read_csv(salaris_file, delimiter=';')

    # Select only the first 4 characters of the 'Perioden' column
    df_salaris["Jaar"] = df_salaris["Perioden"].str[:4]
    df_salaris["Jaar"] = df_salaris["Jaar"].astype('int64')

    # Mask to select only years from 2022 and 'KenmerkenBaan' equals 3000 and 4000
    salaris_mask = (df_salaris["Jaar"] == 2022) & (df_salaris["KenmerkenBaan"].isin([3000, 4000]))
    df_salaris = df_salaris[salaris_mask]
    
    # Selected columns
    df_salaris = df_salaris[["KenmerkenBaan", "BedrijfstakkenBranchesSBI2008", "MaandloonExclusiefOverwerk_6", "Perioden", "Jaar"]]

    # Drop rows with 'KenmerkenBaan' values 100460 - 100470
    df_salaris.drop(df_salaris[(df_salaris['KenmerkenBaan'] == '100460') & (df_salaris['KenmerkenBaan'] == '100470')].index, inplace=True)    

    return df_salaris


def leeftijdenSalaris():
     # Specify the path for the salaris data file
    salaris_file = 'data/salarisdata.csv'

    # Read the CSV file into a Pandas DataFrame
    df_salaris = pd.read_csv(salaris_file, delimiter=';')

    # Select only the first 4 characters of the 'Perioden' column
    df_salaris["Jaar"] = df_salaris["Perioden"].str[:4]
    df_salaris["Jaar"] = df_salaris["Jaar"].astype('int64')

    # Mask to select only years from 2022 and 'KenmerkenBaan' equals 3000 and 4000
    salaris_mask = (df_salaris["Jaar"] == 2022) & (df_salaris["KenmerkenBaan"].isin([70500, 70600, 70700, 70800, 70900, 71000, 71100, 71200, 71300]))
    df_salaris = df_salaris[salaris_mask]
    
    # Selected columns
    df_salaris = df_salaris[["KenmerkenBaan", "BedrijfstakkenBranchesSBI2008", "MaandloonExclusiefOverwerk_6", "Perioden", "Jaar"]]

    # Drop rows with 'KenmerkenBaan' values 100460 - 100470
    df_salaris.drop(df_salaris[(df_salaris['KenmerkenBaan'] == '100460') & (df_salaris['KenmerkenBaan'] == '100470')].index, inplace=True)    

    return df_salaris

def werkurenUitlezen():
    '''
    Selects rows from the DataFrame starting for the year 2022.
    Selected columns include:
    - KenmerkenBaanWerknemerBedrijf
    - BedrijfstakkenBranchesSBI2008
    - Perioden
    - PerBaanPerWeekExclusiefOverwerk_11
    - jaar
    '''
    # Specify the path for the werkuren file
    werkuren_file = 'data/werkuren.csv'

    # Read the CSV file into a Pandas DataFrame
    df_werkuren_leeftijd = pd.read_csv(werkuren_file, delimiter=';')
    
    # Drop rows with 'BedrijfstakkenBranchesSBI2008' value 800009
    df_werkuren_leeftijd.drop(df_werkuren_leeftijd[(df_werkuren_leeftijd['BedrijfstakkenBranchesSBI2008'] == '800009')].index, inplace=True)   
   
    # Mask to select only years from 2022 and 'KenmerkenBaanWerknemerBedrijf' equals 3000 and 4000
    werkuren_mask = (df_werkuren_leeftijd["KenmerkenBaanWerknemerBedrijf"] .isin(['3000', '4000']))
    df_werkuren_leeftijd = df_werkuren_leeftijd[werkuren_mask]

    # Select only the first 4 characters of the 'Perioden' column
    df_werkuren_leeftijd["Jaar"] = df_werkuren_leeftijd["Perioden"].str[:4]
    df_werkuren_leeftijd["Jaar"] = df_werkuren_leeftijd["Jaar"].astype('int64')

    # Mask to select only years from 2022 and 'KenmerkenBaanWerknemerBedrijf' equals 3000 and 4000
    werkuren_mask2 = (df_werkuren_leeftijd["Jaar"] == 2022) 
    df_werkuren_leeftijd = df_werkuren_leeftijd[werkuren_mask2]

    # Selected columns
    df_werkuren_leeftijd = df_werkuren_leeftijd[["KenmerkenBaanWerknemerBedrijf", "BedrijfstakkenBranchesSBI2008", "Uurloon_3", "Perioden", "PerBaanPerWeekExclusiefOverwerk_11", "Jaar"]]

    return df_werkuren_leeftijd

def werkurenLeeftijdUitlezen():
    # Specify the path for the werkuren file
    werkuren_file = 'data/werkuren.csv'

    # Read the CSV file into a Pandas DataFrame
    df_werkuren_leeftijd = pd.read_csv(werkuren_file, delimiter=';')
    
    # Drop rows with 'BedrijfstakkenBranchesSBI2008' value 800009
    df_werkuren_leeftijd.drop(df_werkuren_leeftijd[(df_werkuren_leeftijd['BedrijfstakkenBranchesSBI2008'] == '800009')].index, inplace=True)   
   
    # Mask to select only years from 2022 and 'KenmerkenBaanWerknemerBedrijf' equals 3000 and 4000
    werkuren_mask = (df_werkuren_leeftijd["KenmerkenBaanWerknemerBedrijf"] .isin(['70500', '70600', '70700', '70800', '70900', '71000', '71100', '71200', '71300']))
    df_werkuren_leeftijd = df_werkuren_leeftijd[werkuren_mask]

    # Select only the first 4 characters of the 'Perioden' column
    df_werkuren_leeftijd["Jaar"] = df_werkuren_leeftijd["Perioden"].str[:4]
    df_werkuren_leeftijd["Jaar"] = df_werkuren_leeftijd["Jaar"].astype('int64')


    # Mask to select only years from 2022 and 'KenmerkenBaanWerknemerBedrijf' equals 3000 and 4000
    werkuren_mask2 = (df_werkuren_leeftijd["Jaar"] == 2022) 
    df_werkuren_leeftijd = df_werkuren_leeftijd[werkuren_mask2]

    # Selected columns
    df_werkuren_leeftijd = df_werkuren_leeftijd[["KenmerkenBaanWerknemerBedrijf", "BedrijfstakkenBranchesSBI2008", "Uurloon_3", "Perioden", "PerBaanPerWeekExclusiefOverwerk_11", "Jaar"]]
    
    return df_werkuren_leeftijd
    


