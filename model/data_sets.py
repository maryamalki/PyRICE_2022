"""
This module contains the class DataSets
"""
import os

import pandas as pd

from model.data.edgar import load_edgar_carbon_emissions_data
from model.data.mdp import load_mdp_gdp_data
from model.data.owd import load_owd_energy_intensity_per_country
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


def calculate_primary_energy(df_gdp, df_ei) -> pd.DataFrame:
    countries_gdp = list(df_gdp.columns)
    countries_ei = list(df_ei.columns)

    df_ei.drop(columns=list(set(countries_ei) - set(countries_gdp)), inplace=True)
    df_gdp.drop(columns=list(set(countries_gdp) - set(countries_ei)), inplace=True)

    return df_gdp * df_ei


def aggregate_per_region(df: pd.DataFrame) -> pd.DataFrame:
    """Returns a dataframe of primary energy values aggregated per region"""
    # Get set of countries for validation
    countries = set(country.lower() for country in df.columns)

    # Convert names to lowercase for simpler comparison
    combined_lower_to_capitalized = {country.lower(): country for country in combined_regions}

    # Rename country emissions columns to all lowercase
    df.rename({k: v for k, v in zip(df.columns, map(lambda x: x.lower(), df.columns))}, axis=1, inplace=True)

    # Check for differences between datasets
    combined_lower = list(map(lambda x: x.lower(), combined_regions))
    excluded_countries_from_ours = countries - set(combined_lower)
    excluded_countries_from_theirs = set(combined_lower) - countries

    # Drop exlcuded countries
    df.drop(labels=excluded_countries_from_ours, axis=1, inplace=True)

    # Rename country emissions columns based on lower combined
    df.rename(combined_lower_to_capitalized, axis=1, inplace=True)

    # Single country regions
    US_EI = df[Region.US.value]
    Russia_EI = df[Region.Russia.value]
    China_EI = df[Region.China.value]
    Japan_EI = df[Region.Japan.value]
    India_EI = df[Region.India.value]

    # Multiple countries regions
    Africa_cleaned = list(set(Africa_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Middle_East_cleaned = list(set(Middle_East_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Non_Russia_Eurasia_cleaned = list(set(Non_Russia_Eurasia_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Latin_America_cleaned = list(set(Latin_America_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    Non_OECD_Asia_cleaned = list(set(Non_OECD_Asia_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    OECD_Europe_cleaned = list(set(OECD_Europe_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))
    OHI_cleaned = list(set(OHI_countries) - set(combined_lower_to_capitalized[c] for c in excluded_countries_from_theirs))

    Africa_EI = df.loc[:, Africa_cleaned].sum(axis=1)
    Middle_East_EI = df.loc[:, Middle_East_cleaned].sum(axis=1)
    Non_Russia_Eurasia_EI = df.loc[:, Non_Russia_Eurasia_cleaned].sum(axis=1)
    Latin_America_EI = df.loc[:, Latin_America_cleaned].sum(axis=1)
    Non_OECD_Asia_EI = df.loc[:, Non_OECD_Asia_cleaned].sum(axis=1)
    OECD_Europe_EI = df.loc[:, OECD_Europe_cleaned].sum(axis=1)
    OHI_EI = df.loc[:, OHI_cleaned].sum(axis=1)

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


class DataSets:
    """
    This class loads all the relevant outcomes from the folder inputdata.
    """

    def __init__(self):

        directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "inputdata")

        # Load in RICE input parameters for all regions
        self.RICE_DATA = pd.read_excel(os.path.join(directory, "RICE_data.xlsx"))
        self.RICE_PARAMETER = pd.read_excel(os.path.join(directory, "RICE_parameter.xlsx"))
        self.RICE_input = pd.read_excel(os.path.join(directory, "input_data_RICE.xlsx"))
        self.RICE_regional_damage_factor = pd.read_csv(os.path.join(directory, "regional damage frac factor RICE.csv"))
        self.RICE_regional_damage_factor = self.RICE_regional_damage_factor.iloc[:, 1:].to_numpy()

        # import World Bank income shares
        self.RICE_income_shares = pd.read_excel(os.path.join(directory, "RICE_income_shares.xlsx"))
        self.RICE_income_shares = self.RICE_income_shares.iloc[:, 1:6].to_numpy()

        # import dataframes for SSP (IPCC) uncertainty analysis
        self.RICE_GDP_SSP = pd.read_excel(os.path.join(directory, "Y_Gross_ssp.xlsx")).to_numpy()
        self.POP_ssp = pd.read_excel(os.path.join(directory, "pop_ssp.xlsx"), header=None)
        self.GDP_ssp = pd.read_excel(os.path.join(directory, "Y_Gross_ssp.xlsx"), header=None)

        # Carbon emissions data
        self.carbon_emissions_kg = load_edgar_carbon_emissions_data(os.path.join(directory, "EDGAR_CO2.xlsx"))

        # Calculate energy intensity
        # self.energy_intensity = load_owd_energy_intensity_data(os.path.join(directory, "energy_intensity.csv"))
        self.gdp_per_country = load_mdp_gdp_data(os.path.join(directory, "mpd2020.xlsx"))
        self.energy_intensity_per_country = load_owd_energy_intensity_per_country(os.path.join(directory, "energy_intensity.csv"))
        self.primary_energy_kwh_per_country = calculate_primary_energy(df_gdp=self.gdp_per_country, df_ei=self.energy_intensity_per_country)
        self.primary_energy_kwh = aggregate_per_region(self.primary_energy_kwh_per_country)
        self.gdp = aggregate_per_region(self.gdp_per_country)
        self.energy_intensity = self.primary_energy_kwh / (self.gdp / 1.15)  # Convert GDP from 2011 $ price to 2005 $ price

        # Carbon intensity data
        self.carbon_intensity = self.carbon_emissions_kg / self.primary_energy_kwh

        # convert from kt (kilo metric tons) to gigaton (x10-6), ton (x 10^3) and kg (x10^6)
        # self.carbon_emissions_Gton = self.carbon_emissions_kg * 10**-12
        # self.carbon_emissions_ton = self.carbon_emissions_kg * 10**-3
