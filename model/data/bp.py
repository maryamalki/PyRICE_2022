import pandas as pd
from model.data.regions import Region


def load_bp_primary_energy_data_raw(path: str):
    bp_dataset = pd.read_excel(
        path,
        sheet_name="Primary Energy Consumption",
        header=2,
        index_col=0,
    )
    bp_dataset.index.name = None

    # TODO: Go over regions
    # Select years from base year until today
    bp_years = list(range(1990, 2022))
    bp_dataset = bp_dataset[bp_years]

    # Drop rows with all NaN
    bp_dataset_clean = bp_dataset.dropna(axis=0, how="all")

    # Conver Exajoules (from BP Dataset) to kWh: 1 EJ = 2,778e+11 kWh
    bp_dataset_clean = bp_dataset_clean * 2.778e11

    return bp_dataset_clean.transpose()


def load_bp_primary_energy_data(path: str):
    """Returns Primary Energy data in kWh from BP"""

    bp_dataset = pd.read_excel(
        path,
        sheet_name="Primary Energy Consumption",
        header=2,
        index_col=0,
    )
    bp_dataset.index.name = None

    # TODO: Go over regions
    # Select years from base year until today
    bp_years = list(range(1990, 2022))
    bp_dataset = bp_dataset[bp_years]

    # Drop rows with all NaN
    bp_dataset_clean = bp_dataset.dropna(axis=0, how="all")

    # Conver Exajoules (from BP Dataset) to kWh: 1 EJ = 2,778e+11 kWh
    bp_dataset_clean = bp_dataset_clean * 2.778e11

    # Aggregating the Primary Energy Data per region
    """
    Based on the EIA, a reference from the International Energy Outlook defines regions such as OECD-Europe, Other non-OECD Europe and Eurasia,
    Other non-OECD Asia and the Middle East. We will be using these definitions moving forward. Also, Israel is included in OECD Europe for 
    statistical reporting purposes (https://www.eia.gov/outlooks/ieo/pdf/IEO2021_ChartLibrary_References.pdf).

    For OHI, High Income Countries were based on the European Commission data
    (https://ec.europa.eu/eurostat/web/international-statistical-cooperation/higher-income-countries). Questions about whether Signapore should 
    be included in this regional category.
    """

    # Aggregates from BP Dataset based on EIO
    Latin_America_BP = ["Mexico", "Total S. & Cent. America"]
    OHI_BP = ["Canada", "Australia", "New Zealand", "South Korea", "Singapore", "Taiwan", "China Hong Kong SAR"]
    OECD_Europe_BP = [
        "Austria",
        "Belgium",
        "Czech Republic",
        "Denmark",
        "Estonia",
        "Finland",
        "France",
        "Germany",
        "Greece",
        "Hungary",
        "Iceland",
        "Ireland",
        "Israel",
        "Italy",
        "Latvia",
        "Lithuania",
        "Luxembourg",
        "Netherlands",
        "Norway",
        "Poland",
        "Portugal",
        "Slovakia",
        "Slovenia",
        "Spain",
        "Sweden",
        "Switzerland",
        "Turkey",
        "United Kingdom",
    ]
    Middle_East_BP = ["Iran", "Iraq", "Kuwait", "Oman", "Qatar", "Saudi Arabia", "United Arab Emirates", "Other Middle East", "Other Northern Africa", "Algeria", "Egypt", "Morocco"]
    Non_OECD_Asia_BP = ["Bangladesh", "Indonesia", "Malaysia", "Pakistan", "Philippines", "Sri Lanka", "Thailand", "Vietnam", "Other Asia Pacific"]
    Non_Russia_Eurasia_BP = ["Azerbaijan", "Belarus", "Bulgaria", "Croatia", "Cyprus", "Kazakhstan", "North Macedonia", "Romania", "Turkmenistan", "Ukraine", "Uzbekistan", "Other CIS"]
    Africa_BP = ["South Africa", "Eastern Africa", "Middle Africa", "Western Africa", "Other Southern Africa"]

    # Single Country Regions
    US_PE = bp_dataset_clean[bp_dataset_clean.index == Region.US.value]
    Russia_PE = bp_dataset_clean[bp_dataset_clean.index == "Russian Federation"].rename(index={"Russian Federation": Region.Russia.value})
    China_PE = bp_dataset_clean[bp_dataset_clean.index == Region.China.value]
    Japan_PE = bp_dataset_clean[bp_dataset_clean.index == Region.Japan.value]
    India_PE = bp_dataset_clean[bp_dataset_clean.index == Region.India.value]

    # Simple Grouped Regions
    Latin_America_PE = bp_dataset_clean.loc[Latin_America_BP]
    Latin_America_PE.loc[Region.Latin_America.value] = Latin_America_PE.sum()
    Latin_America_PE = Latin_America_PE.drop(index=Latin_America_BP)

    Africa_PE = bp_dataset_clean.loc[Africa_BP]
    Africa_PE.loc[Region.Africa.value] = Africa_PE.sum()
    Africa_PE = Africa_PE.drop(index=Africa_BP)

    OHI_PE = bp_dataset_clean.loc[OHI_BP]
    OHI_PE.loc[Region.OHI.value] = OHI_PE.sum()
    OHI_PE = OHI_PE.drop(index=OHI_BP)

    # Complex Grouped Regions
    OECD_Europe_PE = bp_dataset_clean.loc[OECD_Europe_BP]
    OECD_Europe_PE.loc[Region.OECD_Europe.value] = OECD_Europe_PE.sum()
    OECD_Europe_PE = OECD_Europe_PE.drop(index=OECD_Europe_BP)

    Middle_East_PE = bp_dataset_clean.loc[Middle_East_BP]
    Middle_East_PE.loc[Region.Middle_East.value] = Middle_East_PE.sum()
    Middle_East_PE = Middle_East_PE.drop(index=Middle_East_BP)

    Non_OECD_Asia_PE = bp_dataset_clean.loc[Non_OECD_Asia_BP]
    Non_OECD_Asia_PE.loc[Region.Non_OECD_Asia.value] = Non_OECD_Asia_PE.sum()
    Non_OECD_Asia_PE = Non_OECD_Asia_PE.drop(index=Non_OECD_Asia_BP)

    Non_Russia_Eurasia_PE = bp_dataset_clean.loc[Non_Russia_Eurasia_BP]
    Non_Russia_Eurasia_PE.loc[Region.Non_Russia_Eurasia.value] = Non_Russia_Eurasia_PE.sum()
    Non_Russia_Eurasia_PE = Non_Russia_Eurasia_PE.drop(index=Non_Russia_Eurasia_BP)

    # Build one Primary Energy Dataframe
    frames = [US_PE, OECD_Europe_PE, Japan_PE, Russia_PE, Non_Russia_Eurasia_PE, China_PE, India_PE, Middle_East_PE, Africa_PE, Latin_America_PE, OHI_PE, Non_OECD_Asia_PE]
    return pd.concat(frames).transpose()
