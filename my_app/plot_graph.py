from my_app.read_data import salarisUitlezen, salarisBrancheLabels, geslachtSalaris, leeftijdenSalaris, werkurenUitlezen, werkurenLeeftijdUitlezen
import plotly.express as px
import pandas as pd


# Plot graph
def plot_line_graph():
    # Read the CSV files salaris and metadata into DataFrames
    df_salaris = salarisUitlezen()
    df_metadata = salarisBrancheLabels()
    
    # Create a mapping dictionary
    Perioden_mapping = {
        '2022MM01': 'Jan 2022',
        '2022MM02': 'Feb 2022',
        '2022MM03': 'Maa 2022',
        '2022MM04': 'Apr 2022',
        '2022MM05': 'Mei 2022',
        '2022MM06': 'Jun 2022',
        '2022MM07': 'Jul 2022',
        '2022MM08': 'Aug 2022',
        '2022MM09': 'Sep 2022',
        '2022MM10': 'Okt 2022',
        '2022MM11': 'Nov 2022',
        '2022MM12': 'Dec 2022',
        '2023MM01': 'Jan 2023',
        '2023MM02': 'Feb 2023',
        '2023MM03': 'Maa 2023',
        '2023MM04': 'Apr 2023',
        '2023MM05': 'Mei 2023',
        '2023MM06': 'Jun 2023',
        '2023MM07': 'Jul 2023',
    }
    
    # Apply the mapping to the "KenmerkenBaan" column
    df_salaris['Perioden'] = df_salaris['Perioden'].astype(str).map(Perioden_mapping)
    
    # Get unique values from both dataframes
    salaris_branches = df_salaris['BedrijfstakkenBranchesSBI2008'].unique()
    metadata_titles = df_metadata["Title"].unique()
    
    # Create options for the work branches dropdown based on unique values in the "BedrijfstakkenBranchesSBI2008" column
    # Create a list of dictionaries using zip
    work_branch_options = [{'label': title, 'value': branch} for title, branch in zip(metadata_titles, salaris_branches)]
    
    # Create an initial bar graph using Plotly Express
    fig = px.line(df_salaris, x="Perioden", y="MaandloonExclusiefOverwerk_6")
    
    return fig, work_branch_options, df_salaris


def plot_barchart_geslacht():

    # Read the CSV files salaris and metadata into DataFrames
    df_salaris_geslacht = geslachtSalaris()
    df_metadata = salarisBrancheLabels()

    # Create a mapping dictionary
    kenmerken_mapping = {
        '3000': 'Man',
        '4000': 'Vrouw'
    }
    
    # Apply the mapping to the "KenmerkenBaan" column
    df_salaris_geslacht['KenmerkenBaan'] = df_salaris_geslacht['KenmerkenBaan'].astype(str).map(kenmerken_mapping)

    # Get unique values from both dataframes
    salaris_branches = df_salaris_geslacht['BedrijfstakkenBranchesSBI2008'].unique()
    metadata_titles = df_metadata["Title"].unique()
    
    # Create options for the work branches dropdown based on unique values in the "BedrijfstakkenBranchesSBI2008" column
    # Create a list of dictionaries using zip
    work_branch_options_geslacht = [{'label': title, 'value': branch} for title, branch in zip(metadata_titles, salaris_branches)]

    # Calculate the average salary for each year and gender
    average_salary_per_year_gender = df_salaris_geslacht.groupby(['Jaar', 'KenmerkenBaan'])['MaandloonExclusiefOverwerk_6'].mean().reset_index()

    # Create a bar chart for each 'Jaar' with the average salary split by gender
    fig_geslacht = px.bar(average_salary_per_year_gender, x="Jaar", y="MaandloonExclusiefOverwerk_6", color="KenmerkenBaan",
                 barmode='group')
    
    return fig_geslacht, work_branch_options_geslacht, df_salaris_geslacht    


def plot_barchart_leeftijd():
    
    # Read the CSV files salaris and metadata into DataFrames
    df_salaris_leeftijd = leeftijdenSalaris()
    df_metadata = salarisBrancheLabels()

    # Create a mapping dictionary
    kenmerken_mapping = {
        '70500': '20 tot 25 jaar',
        '70600': '25 tot 30 jaar',
        '70700': '30 tot 35 jaar',
        '70800': '35 tot 40 jaar',
        '70900': '40 tot 45 jaar',
        '71000': '45 tot 50 jaar',
        '71100': '50 tot 55 jaar',
        '71200': '55 tot 60 jaar',
        '71300': '60 tot 65 jaar'
    }
    
    # Apply the mapping to the "KenmerkenBaan" column
    df_salaris_leeftijd['KenmerkenBaan'] = df_salaris_leeftijd['KenmerkenBaan'].astype(str).map(kenmerken_mapping)

    # Get unique values from both dataframes
    salaris_branches = df_salaris_leeftijd['BedrijfstakkenBranchesSBI2008'].unique()
    metadata_titles = df_metadata["Title"].unique()
    
    # Create options for the work branches dropdown based on unique values in the "BedrijfstakkenBranchesSBI2008" column
    # Create a list of dictionaries using zip
    work_branch_options_leeftijd = [{'label': title, 'value': branch} for title, branch in zip(metadata_titles, salaris_branches)]

    # Calculate the average salary for each year and gender
    average_salary_per_year_gender = df_salaris_leeftijd.groupby(['Jaar', 'KenmerkenBaan'])['MaandloonExclusiefOverwerk_6'].mean().reset_index()

    # Create a bar chart for each 'Jaar' with the average salary split by gender
    fig_leeftijd = px.bar(average_salary_per_year_gender, x="Jaar", y="MaandloonExclusiefOverwerk_6", color="KenmerkenBaan",
                 barmode='group')
    
    return fig_leeftijd, work_branch_options_leeftijd, df_salaris_leeftijd    

def werkuren():
    df_werkuren = werkurenUitlezen()
    df_metadata = salarisBrancheLabels()

    gender_mapping = {'3000': 'Man', '4000': 'Vrouw'}
    df_werkuren['KenmerkenBaanWerknemerBedrijf'] = df_werkuren['KenmerkenBaanWerknemerBedrijf'].map(gender_mapping)

    # Get unique values from both dataframes
    werkuren_branches = df_werkuren['BedrijfstakkenBranchesSBI2008'].unique()
    metadata_titles = df_metadata["Title"].unique()

    # Create options for the work branches dropdown based on unique values in the "BedrijfstakkenBranchesSBI2008" column
    # Create a list of dictionaries using zip
    work_branch_options_werkuren = [{'label': title, 'value': branch} for title, branch in zip(metadata_titles, werkuren_branches)]

    return work_branch_options_werkuren, df_werkuren


def werkuren_leeftijd():
    df_werkuren_leeftijd = werkurenLeeftijdUitlezen()
    df_metadata = salarisBrancheLabels()

        # Create a mapping dictionary
    leeftijd_mapping = {
        '70500': '20 tot 25 jaar',
        '70600': '25 tot 30 jaar',
        '70700': '30 tot 35 jaar',
        '70800': '35 tot 40 jaar',
        '70900': '40 tot 45 jaar',
        '71000': '45 tot 50 jaar',
        '71100': '50 tot 55 jaar',
        '71200': '55 tot 60 jaar',
        '71300': '60 tot 65 jaar'
    }
    
    # Apply the mapping to the "KenmerkenBaan" column
    df_werkuren_leeftijd['KenmerkenBaanWerknemerBedrijf'] = df_werkuren_leeftijd['KenmerkenBaanWerknemerBedrijf'].map(leeftijd_mapping)

    # Get unique values from both dataframes
    werkuren_branches = df_werkuren_leeftijd['BedrijfstakkenBranchesSBI2008'].unique()
    metadata_titles = df_metadata["Title"].unique()
    
    # Create options for the work branches dropdown based on unique values in the "BedrijfstakkenBranchesSBI2008" column
    # Create a list of dictionaries using zip
    work_branch_options_werkuren_leeftijd = [{'label': title, 'value': branch} for title, branch in zip(metadata_titles, werkuren_branches)]

    return work_branch_options_werkuren_leeftijd, df_werkuren_leeftijd