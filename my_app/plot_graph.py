from my_app.read_data import salarisUitlezen, salarisBrancheLabels
import plotly.express as px


# Plot graph
def plot_barchart():
    '''
    This function creates a bar chart and returns the object to
    be used as the layout for the salaris page!
    '''
    # Read the CSV files salaris and metadata into DataFrames
    df_salaris = salarisUitlezen()
    df_metadata = salarisBrancheLabels()
    
    # Get unique values from both dataframes
    salaris_branches = df_salaris['BedrijfstakkenBranchesSBI2008'].unique()
    metadata_titles = df_metadata["Title"].unique()
    
    # Create options for the work branches dropdown based on unique values in the "BedrijfstakkenBranchesSBI2008" column
    # Create a list of dictionaries using zip
    work_branch_options = [{'label': title, 'value': branch} for title, branch in zip(metadata_titles, salaris_branches)]
    
    # Create an initial bar graph using Plotly Express
    fig = px.bar(df_salaris, x="Perioden", y="MaandloonExclusiefOverwerk_6")
    
    return fig, work_branch_options, df_salaris
    
