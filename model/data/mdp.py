import pandas as pd


def load_mdp_gdp_data(path):
    """Returns per country GDP data (in $)"""
    df_gdp_pc = pd.read_excel(path, sheet_name="GDP pc", index_col="GDP pc 2011 prices")
    df_gdp_pc = df_gdp_pc.loc[1:]
    df_gdp_pc.index.name = None
    df_gdp_pc = df_gdp_pc.loc[1990:]

    df_pop = pd.read_excel(path, sheet_name="Population", index_col="Population")
    df_pop = df_pop.loc[1:]
    df_pop.index.name = None
    df_pop = df_pop.loc[1990:]

    df_gdp = df_gdp_pc * df_pop * 1000  # Population in thousands

    # Reconcile countries' names between datasets
    rename = {
        "Bolivia (Plurinational State of)": "Bolivia",
        "Cabo Verde": "Cape Verde",
        "China, Hong Kong SAR": "Hong Kong",
        "Côte d'Ivoire": "Cote d'Ivoire",
        "D.P.R. of Korea": "North Korea",
        "D.R. of the Congo": "Democratic Republic of Congo",
        "Former USSR": "USSR",
        "Former Yugoslavia": "Yugoslavia",
        "Iran (Islamic Republic of)": "Iran",
        "Lao People's DR": "Laos",
        "Republic of Korea": "South Korea",
        "Republic of Moldova": "Moldova",
        "Russian Federation": "Russia",
        "Saint Lucia": "St. Lucia",
        "State of Palestine": "Palestinian Territory",
        "Sudan (Former)": "Sudan",
        "Swaziland": "Eswatini",
        "Syrian Arab Republic": "Syria",
        "TFYR of Macedonia": "North Macedonia",
        "Taiwan, Province of China": "Taiwan",
        "U.R. of Tanzania: Mainland": "Tanzania",
        "United States": "US",
        "Venezuela (Bolivarian Republic of)": "Venezuela",
        "Viet Nam": "Vietnam",
    }

    df_gdp.rename(rename, axis=1, inplace=True)

    return df_gdp
