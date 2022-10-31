import numpy as np
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


def load_owd_carbon_intensity_data(path):
    "Returns dataframe of carbon intensity calculated from OWD dataset"
    df = pd.read_csv(path, header=0)
    country_ci = df.pivot(index="Year", columns="Entity", values="Annual CO2 emissions per unit energy (kg per kilowatt-hour)")

    # Reconcile countries' names between datasets
    rename = {
        "Saint Lucia": "St. Lucia",
        "Palestine": "Palestinian Territory",
        "United States": "US",
        "Czechia": "Czech Republic",
    }

    country_ci.rename(rename, axis=1, inplace=True)

    country_ci.columns.name = None

    # Get set of countries for validation
    countries = set(country.lower() for country in country_ci.columns)

    # Convert names to lowercase for simpler comparison
    combined_lower_to_capitalized = {country.lower(): country for country in combined_regions}

    # Rename country emissions columns to all lowercase
    country_ci.rename({k: v for k, v in zip(country_ci.columns, map(lambda x: x.lower(), country_ci.columns))}, axis=1, inplace=True)

    # Check for differences between datasets
    combined_lower = list(map(lambda x: x.lower(), combined_regions))
    excluded_countries_from_ours = countries - set(combined_lower)
    excluded_countries_from_theirs = set(combined_lower) - countries

    # Drop exlcuded countries
    country_ci.drop(labels=excluded_countries_from_ours, axis=1, inplace=True)

    # Rename country emissions columns based on lower combined
    country_ci.rename(combined_lower_to_capitalized, axis=1, inplace=True)

    # Single country regions
    US_CI = country_ci[Region.US.value]
    Russia_CI = country_ci[Region.Russia.value]
    China_CI = country_ci[Region.China.value]
    Japan_CI = country_ci[Region.Japan.value]
    India_CI = country_ci[Region.India.value]

    # Multiple countries regions
    Africa_cleaned = list(set(Africa_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Middle_East_cleaned = list(set(Middle_East_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Non_Russia_Eurasia_cleaned = list(set(Non_Russia_Eurasia_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Latin_America_cleaned = list(set(Latin_America_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Non_OECD_Asia_cleaned = list(set(Non_OECD_Asia_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    OECD_Europe_cleaned = list(set(OECD_Europe_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    OHI_cleaned = list(set(OHI_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))

    Africa_CI = country_ci.loc[:, Africa_cleaned].sum(axis=1)
    Middle_East_CI = country_ci.loc[:, Middle_East_cleaned].sum(axis=1)
    Non_Russia_Eurasia_CI = country_ci.loc[:, Non_Russia_Eurasia_cleaned].sum(axis=1)
    Latin_America_CI = country_ci.loc[:, Latin_America_cleaned].sum(axis=1)
    Non_OECD_Asia_CI = country_ci.loc[:, Non_OECD_Asia_cleaned].sum(axis=1)
    OECD_Europe_CI = country_ci.loc[:, OECD_Europe_cleaned].sum(axis=1)
    OHI_CI = country_ci.loc[:, OHI_cleaned].sum(axis=1)

    # Create a CI dataframe
    return pd.DataFrame(
        data={
            Region.US.value: US_CI,
            Region.OECD_Europe.value: OECD_Europe_CI,
            Region.Japan.value: Japan_CI,
            Region.Russia.value: Russia_CI,
            Region.Non_Russia_Eurasia.value: Non_Russia_Eurasia_CI,
            Region.China.value: China_CI,
            Region.India.value: India_CI,
            Region.Middle_East.value: Middle_East_CI,
            Region.Africa.value: Africa_CI,
            Region.Latin_America.value: Latin_America_CI,
            Region.OHI.value: OHI_CI,
            Region.Non_OECD_Asia.value: Non_OECD_Asia_CI,
        }
    )


def load_owd_energy_intensity_data(path):
    "Returns dataframe of energy intensity calculated from OWD dataset"

    df = pd.read_csv(path + "model/inputdata/energy_intensity.csv", header=0)
    country_ei = df.pivot(index="Year", columns="Entity", values="Primary energy consumption per GDP (kWh/$)")

    # Reconcile countries' names between datasets
    rename = {
        "Saint Lucia": "St. Lucia",
        "Palestine": "Palestinian Territory",
        "United States": "US",
        "Czechia": "Czech Republic",
    }

    country_ei.rename(rename, axis=1, inplace=True)
    country_ei.columns.name = None

    # Get set of countries for validation
    countries = set(country.lower() for country in country_ei.columns)

    # Convert names to lowercase for simpler comparison
    combined_lower_to_capitalized = {country.lower(): country for country in combined_regions}

    # Rename country emissions columns to all lowercase
    country_ei.rename({k: v for k, v in zip(country_ei.columns, map(lambda x: x.lower(), country_ei.columns))}, axis=1, inplace=True)

    # Check for differences between datasets
    combined_lower = list(map(lambda x: x.lower(), combined_regions))
    excluded_countries_from_ours = countries - set(combined_lower)
    excluded_countries_from_theirs = set(combined_lower) - countries

    # Drop exlcuded countries
    country_ei.drop(labels=excluded_countries_from_ours, axis=1, inplace=True)

    # Rename country emissions columns based on lower combined
    country_ei.rename(combined_lower_to_capitalized, axis=1, inplace=True)

    # Setting up EI dataset

    # Single country regions
    US_EI = country_ei[Region.US.value]
    Russia_EI = country_ei[Region.Russia.value]
    China_EI = country_ei[Region.China.value]
    Japan_EI = country_ei[Region.Japan.value]
    India_EI = country_ei[Region.India.value]

    # Multiple countries regions
    Africa_cleaned = list(set(Africa_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Middle_East_cleaned = list(set(Middle_East_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Non_Russia_Eurasia_cleaned = list(set(Non_Russia_Eurasia_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Latin_America_cleaned = list(set(Latin_America_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Non_OECD_Asia_cleaned = list(set(Non_OECD_Asia_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    OECD_Europe_cleaned = list(set(OECD_Europe_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    OHI_cleaned = list(set(OHI_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))

    Africa_EI = country_ei.loc[:, Africa_cleaned].sum(axis=1)
    Middle_East_EI = country_ei.loc[:, Middle_East_cleaned].sum(axis=1)
    Non_Russia_Eurasia_EI = country_ei.loc[:, Non_Russia_Eurasia_cleaned].sum(axis=1)
    Latin_America_EI = country_ei.loc[:, Latin_America_cleaned].sum(axis=1)
    Non_OECD_Asia_EI = country_ei.loc[:, Non_OECD_Asia_cleaned].sum(axis=1)
    OECD_Europe_EI = country_ei.loc[:, OECD_Europe_cleaned].sum(axis=1)
    OHI_EI = country_ei.loc[:, OHI_cleaned].sum(axis=1)

    # Create a EI dataframe
    return pd.DataFrame(
        data={
            Region.US.value: US_EI,
            Region.OECD_Europe.value: OECD_Europe_EI,
            Region.Japan.value: Japan_EI,
            Region.Russia.value: Russia_EI,
            Region.Non_Russia_Eurasia.value: Non_Russia_Eurasia_EI,
            Region.China.value: China_EI,
            Region.India.value: India_EI,
            Region.Middle_East.value: Middle_East_EI,
            Region.Africa.value: Africa_EI,
            Region.Latin_America.value: Latin_America_EI,
            Region.OHI.value: OHI_EI,
            Region.Non_OECD_Asia.value: Non_OECD_Asia_EI,
        },
    )


def load_owd_energy_intensity_per_country(path):
    df_EI = pd.read_csv("/Users/maryamalki/Desktop/PyRICE_2022/model/inputdata/energy_intensity.csv", header=0)
    country_ei = df_EI.pivot(index="Year", columns="Entity", values="Primary energy consumption per GDP (kWh/$)")

    # Reconcile countries' names between datasets
    rename = {
        "Saint Lucia": "St. Lucia",
        "Palestine": "Palestinian Territory",
        "United States": "US",
        "Czechia": "Czech Republic",
    }

    country_ei.rename(rename, axis=1, inplace=True)
    country_ei.columns.name = None
    return country_ei
