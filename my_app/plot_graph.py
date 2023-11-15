from my_app.read_data import salarisUitlezen, salarisBrancheLabels, geslachtSalaris, leeftijdenSalaris
import plotly.express as px
import pandas as pd


# Plot graph
def plot_barchart():
    '''
    This function creates a bar chart and returns the object to
    be used as the layout for the salaris page!
    '''
    # Read the CSV files salaris and metadata into DataFrames
    df_salaris_leeftijd = salarisUitlezen()
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
    df_salaris_leeftijd['Perioden'] = df_salaris_leeftijd['Perioden'].astype(str).map(Perioden_mapping)
    
    # Get unique values from both dataframes
    salaris_branches = df_salaris_leeftijd['BedrijfstakkenBranchesSBI2008'].unique()
    metadata_titles = df_metadata["Title"].unique()
    
    # Create options for the work branches dropdown based on unique values in the "BedrijfstakkenBranchesSBI2008" column
    # Create a list of dictionaries using zip
    work_branch_options = [{'label': title, 'value': branch} for title, branch in zip(metadata_titles, salaris_branches)]
    
    # Create an initial bar graph using Plotly Express
    fig = px.bar(df_salaris_leeftijd, x="Jaar", y="MaandloonExclusiefOverwerk_6")
    
    return fig, work_branch_options, df_salaris_leeftijd


def plot_barchart_geslacht():
    '''
    This function creates a bar chart and returns the object to
    be used as the layout for the salaris page!
    '''
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
    
    # Use these unique values when creating your bar graph
    # fig = px.bar(df_salaris_leeftijd, x="Jaar", y="MaandloonExclusiefOverwerk_6", color="KenmerkenBaan", barmode='group', category_orders={'Year': [2022]}, labels={'MaandloonExclusiefOverwerk_6': 'Maandloon'})

    # Calculate the average salary for each year and gender
    average_salary_per_year_gender = df_salaris_geslacht.groupby(['Jaar', 'KenmerkenBaan'])['MaandloonExclusiefOverwerk_6'].mean().reset_index()

    # Create a bar chart for each 'Jaar' with the average salary split by gender
    fig_geslacht = px.bar(average_salary_per_year_gender, x="Jaar", y="MaandloonExclusiefOverwerk_6", color="KenmerkenBaan",
                 barmode='group', labels={'MaandloonExclusiefOverwerk_6': 'Average Maandloon'})
    
    return fig_geslacht, work_branch_options_geslacht, df_salaris_geslacht    


def plot_barchart_leeftijd():
    '''
    This function creates a bar chart and returns the object to
    be used as the layout for the salaris page!
    '''
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
                 barmode='group', labels={'MaandloonExclusiefOverwerk_6': 'Average Maandloon'})
    
    return fig_leeftijd, work_branch_options_leeftijd, df_salaris_leeftijd    
