import pandas as pd

#Incorporate data

def vacatures_uitlezen():
    vacatures = 'data/vacatures.csv'
    vacatures_metadata = 'data/vacatures_metadata1.csv'
    vacatures_df = pd.read_csv(vacatures, delimiter=';')
    vacatures_metadata_df = pd.read_csv(vacatures_metadata, delimiter=',')
    return vacatures_df, vacatures_metadata_df

#Read data
#def zet_nummer_om_naar_bedrijfsnaam(code):
#    for key, value in vacatures_metadata_df.iterrows():
#        print(value["Title"])
#        if value["Key"] == code:
#            return value["Title"]

#def meeste_openstaande_vacatures():
#    for rij in vacatures_df:
#        print(rij)

#meeste_openstaande_vacatures()
#a = zet_nummer_om_naar_bedrijfsnaam("T001081")
#print(a, "rrr")
#Incorporate data
def vacatures_regio_uitlezen():
    vacatures_regio = 'data/vacatures_regio.csv'
    vacatures_regio_metadata = 'data/vacatures_metadata_regio1.csv'
    vacatures_regio_df = pd.read_csv(vacatures_regio, delimiter=';')
    vacatures_regio_metadata_df = pd.read_csv(vacatures_regio_metadata, delimiter=',')
    return vacatures_regio_df, vacatures_regio_metadata_df

#print(vacatures_regio_df)
#print(vacatures_regio_metadata_df)

#Read data
#def zet_nummer_om_naar_bedrijfsnaam(code):
#    for key, value in vacatures_regio_metadata_df.iterrows():
#        print(value["Title"])
#        if value["Key"] == code:
#            return value["Title"]

#def meeste_openstaande_vacatures():
#    for rij in vacatures_regio_df:
#        print(rij)

#meeste_openstaande_vacatures()
#a = zet_nummer_om_naar_bedrijfsnaam("T001081")
#print(a, "rrr")