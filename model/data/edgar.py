import pandas as pd
from model.data.regions import (
    Africa_countries,
    Latin_America_countries,
    Middle_East_countries,
    Non_OECD_Asia_countries,
    Non_Russia_Eurasia_countries,
    OECD_Europe_countries,
    OHI_countries,
    Region,
    combined_regions,
)


def load_edgar_carbon_emissions_data(path):
    """
    Returns EDGAR carbon emissions for 2005 in kilo metric tons
    """
    xlsx = pd.ExcelFile(path)
    edgar_CO2_data = pd.read_excel(xlsx, "TOTALS BY COUNTRY")
    edgar_CO2_data = edgar_CO2_data[8:]
    edgar_CO2_data.columns = edgar_CO2_data.iloc[0]
    edgar_CO2_data = edgar_CO2_data.iloc[1:, :]

    rename = {f"Y_{k}": k for k in range(1970, 2022)}
    rename["Name"] = "Country"

    edgar_CO2_data.rename(rename, axis=1, inplace=True)
    edgar_CO2_data.drop(columns=["IPCC_annex", "C_group_IM24_sh", "Country_code_A3", "Substance"], inplace=True)

    edgar_CO2_data.reset_index(drop=True, inplace=True)
    edgar_CO2_data.set_index("Country", inplace=True)

    edgar_CO2_data.index.name = None
    edgar_CO2_data.columns.name = None

    edgar_CO2_data = edgar_CO2_data.transpose()

    rename = {
        "United States": "US",
        "Russian Federation": "Russia",
        "Virgin Islands_British": "British Virgin Islands",
        "Viet Nam": "Vietnam",
        "Ukraine": "Ukraine",
        "Tanzania_United Republic of": "Tanzania",
        "Taiwan_Province of China": "Taiwan",
        "Syrian Arab Republic": "Syria",
        "Swaziland": "Eswatini",
        "Serbia and Montenegro": "Serbia and Montenegro",
        "Saint Vincent and the Grenadines": "St. Vincent and the Grenadines",
        "Saint Pierre and Miquelon": "St. Pierre and Miquelon",
        "Saint Lucia": "St. Lucia",
        "Saint Kitts and Nevis": "St. Kitts and Nevis",
        "Saint Helena": "St. Helena",
        "Moldova, Republic of": "Moldova",
        "Macedonia, the former Yugoslav Republic of": "North Macedonia",
        "Macao": "Macau",
        "Libyan Arab Jamahiriya": "Libya",
        "Lao People's Democratic Republic": "Laos",
        "Kyrgyzstan": "Kyrgyzstan",
        "Korea, Republic of": "South Korea",
        "Korea, Democratic People's Republic of": "North Korea",
        "Iran, Islamic Republic of": "Iran",
        "Falkland Islands (Malvinas)": "Falkland Islands",
        "Brunei Darussalam": "Brunei",
        "Congo_the Democratic Republic of the": "Democratic Republic of Congo",
        "Faroe Islands": "Faeroe Islands",
    }

    edgar_CO2_data.rename(rename, axis=1, inplace=True)

    combined_lower_to_capitalized = {country.lower(): country for country in combined_regions}

    # Rename country emissions columns to all lowercase
    df_emissions = edgar_CO2_data
    countries = set(country.lower() for country in df_emissions.columns)

    df_emissions.rename({k: v for k, v in zip(df_emissions.columns, map(lambda x: x.lower(), df_emissions.columns))}, axis=1, inplace=True)

    combined_lower = list(map(lambda x: x.lower(), combined_regions))

    excluded_countries_from_ours = countries - set(combined_lower)
    excluded_countries_from_theirs = set(combined_lower) - countries

    df_emissions.drop(labels=excluded_countries_from_ours, axis=1, inplace=True)
    # Rename country emissions columns based on lower combined
    df_emissions.rename(combined_lower_to_capitalized, axis=1, inplace=True)

    # Single Country Regions
    US_emissions = df_emissions[Region.US.value]
    Russia_emissions = df_emissions[Region.Russia.value]
    China_emissions = df_emissions[Region.China.value]
    Japan_emissions = df_emissions[Region.Japan.value]
    India_emissions = df_emissions[Region.India.value]

    # Simple Grouped Regions
    Africa_cleaned = list(set(Africa_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Middle_East_cleaned = list(set(Middle_East_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Non_Russia_Eurasia_cleaned = list(set(Non_Russia_Eurasia_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Latin_America_cleaned = list(set(Latin_America_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Non_OECD_Asia_cleaned = list(set(Non_OECD_Asia_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    OECD_Europe_cleaned = list(set(OECD_Europe_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    OHI_cleaned = list(set(OHI_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))

    Africa_emissions = df_emissions.loc[:, Africa_cleaned].sum(axis=1)
    Middle_East_emissions = df_emissions.loc[:, Middle_East_cleaned].sum(axis=1)
    Non_Russia_Eurasia_emissions = df_emissions.loc[:, Non_Russia_Eurasia_cleaned].sum(axis=1)
    Latin_America_emissions = df_emissions.loc[:, Latin_America_cleaned].sum(axis=1)
    Non_OECD_Asia_emissions = df_emissions.loc[:, Non_OECD_Asia_cleaned].sum(axis=1)
    OECD_Europe_emissions = df_emissions.loc[:, OECD_Europe_cleaned].sum(axis=1)
    OHI_emissions = df_emissions.loc[:, OHI_cleaned].sum(axis=1)

    # Use common names
    Africa_emissions.name = Region.Africa.value
    Middle_East_emissions.name = Region.Middle_East.value
    Non_Russia_Eurasia_emissions.name = Region.Non_Russia_Eurasia.value
    Latin_America_emissions.name = Region.Latin_America.value
    Non_OECD_Asia_emissions.name = Region.Non_OECD_Asia.value
    OECD_Europe_emissions.name = Region.OECD_Europe.value
    OHI_emissions.name = Region.OHI.value

    return pd.DataFrame(
        data={
            Region.US.value: US_emissions,
            Region.OECD_Europe.value: OECD_Europe_emissions,
            Region.Japan.value: Japan_emissions,
            Region.Russia.value: Russia_emissions,
            Region.Non_Russia_Eurasia.value: Non_Russia_Eurasia_emissions,
            Region.China.value: China_emissions,
            Region.India.value: India_emissions,
            Region.Middle_East.value: Middle_East_emissions,
            Region.Africa.value: Africa_emissions,
            Region.Latin_America.value: Latin_America_emissions,
            Region.OHI.value: OHI_emissions,
            Region.Non_OECD_Asia.value: Non_OECD_Asia_emissions,
        },
    ) * (
        10**6
    )  # Convert from kiloton to kg
