import pandas as pd


def load_cdiac_carbon_emissions_data(path: str):
    df = pd.read_excel(path, header=0)
    df = df[3:]
    rename = {
        "REPUBLIC OF MOLDOVA": "Moldova",
        "SAINT HELENA": "St. Helena",
        "ITALY (INCLUDING SAN MARINO)": "Italy",
        "ANTIGUA & BARBUDA": "Antigua and Barbuda",
        "MACEDONIA": "North Macedonia",
        "TIMOR-LESTE (FORMERLY EAST TIMOR)": "Timor-Leste",
        "MACAU SPECIAL ADMINSTRATIVE REGION OF CHINA": "Macau",
        "REPUBLIC OF KOREA": "South Korea",
        "DEMOCRATIC PEOPLE S REPUBLIC OF KOREA": "North Korea",
        "COTE D IVOIRE": "Côte d’Ivoire",
        "REPUBLIC OF CAMEROON": "Cameroon",
        "SYRIAN ARAB REPUBLIC": "Syria",
        "ISLAMIC REPUBLIC OF IRAN": "Iran",
        "HONG KONG SPECIAL ADMINSTRATIVE REGION OF CHINA": "Hong Kong",
        "FRANCE (INCLUDING MONACO)": "France",
        "LIBYAN ARAB JAMAHIRIYAH": "Libya",
        "SWAZILAND": "Eswatini",
        "LAO PEOPLE S DEMOCRATIC REPUBLIC": "Laos",
        "PLURINATIONAL STATE OF BOLIVIA": "Bolivia",
        "SAINT LUCIA": "St. Lucia",
        "NETHERLAND ANTILLES": "Netherlands Antilles",
        "UNITED REPUBLIC OF TANZANIA": "Tanzania",
        "BRUNEI (DARUSSALAM)": "Brunei",
        "FALKLAND ISLANDS (MALVINAS)": "Falkland Islands",
        "ST. PIERRE & MIQUELON": "St. Pierre and Miquelon",
        "RUSSIAN FEDERATION": "Russia",
        "MYANMAR (FORMERLY BURMA)": "Myanmar",
        "ST. VINCENT & THE GRENADINES": "St. Vincent and The Grenadines",
        "OCCUPIED PALESTINIAN TERRITORY": "Occupied Palestinian Territory",
        "ST. KITTS-NEVIS": "St. Kitts and Nevis",
        "SAO TOME & PRINCIPE": "Sao Tome and Principe",
        "VIET NAM": "Vietnam",
        "DEMOCRATIC REPUBLIC OF THE CONGO (FORMERLY ZAIRE)": "Democratic Republic of Congo",
        "REPUBLIC OF SOUTH SUDAN": "South Sudan",
        "BOSNIA & HERZEGOVINA": "Bosnia and Herzegovina",
        "CHINA (MAINLAND)": "China",
        "UNITED STATES OF AMERICA": "US",
        "FAEROE ISLANDS": "Faroe Islands",
        "YUGOSLAVIA (MONTENEGRO & SERBIA)": "Yugoslavia",
    }

    country_emissions = df.pivot(index="Year", columns="Nation", values="Total CO2 emissions from fossil-fuels and cement production (thousand metric tons of C)")
    country_emissions.rename(rename, axis=1, inplace=True)

    countries = set(country_emissions.columns)
    countries = set([country.lower() for country in countries])

    # TODO: Update this data
    Latin_America_CDIAC = [
        "Mexico",
        "Antigua and Barbuda",
        "Argentina",
        "Barbados",
        "Belize",
        "Bermuda",
        "Bolivia",
        "Brazil",
        "Cayman Islands",
        "Chile",
        "Colombia",
        "Costa Rica",
        "Cuba",
        "Dominica",
        "Dominican Republic",
        "Ecuador",
        "El Salvador",
        "Falkland Islands",
        "French Guiana",
        "Grenada",
        "Guadeloupe",
        "Guatemala",
        "Guyana",
        "Haiti",
        "Honduras",
        "Jamaica",
        "Martinique",
        "Montserrat",
        "Nicaragua",
        "Panama",
        "Paraguay",
        "Peru",
        "St. Kitts and Nevis",
        "St. Lucia",
        "St. Pierre and Miquelon",
        "St. Vincent and the Grenadines",
        "Suriname",
        "Trinidad and Tobago",
        "Turks and Caicos Islands",
        "Uruguay",
        "Venezuela",
        "Netherlands Antilles",
        "Curacao",
        "British Virgin Islands",
        "Faroe Islands",
        "Bahamas",
        "Aruba",
    ]

    China_CDIAC = ["China"]
    Russia_CDIAC = ["Russia"]
    Japan_CDIAC = ["Japan"]
    US_CDIAC = ["US"]
    India_CDIAC = ["India"]

    OHI_CDIAC = ["Malta", "Canada", "Australia", "New Zealand", "South Korea", "Singapore", "Taiwan", "Hong Kong", "Greenland", "Andorra"]

    OECD_Europe_CDIAC = [
        "Austria",
        "Belgium",
        "Turkey",
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
        "United Kingdom",
    ]

    Middle_East_CDIAC = [
        "Egypt",
        "Algeria",
        "Tunisia",
        "Libya",
        "Morocco",
        "Israel",
        "Bahrain",
        "Iran",
        "Iraq",
        "Jordan",
        "Kuwait",
        "Lebanon",
        "Oman",
        "Occupied Palestinian Territory",
        "Qatar",
        "Saudi Arabia",
        "Syria",
        "United Arab Emirates",
        "Yemen",
    ]

    Non_OECD_Asia_CDIAC = [
        "Afghanistan",
        "Bangladesh",
        "Bhutan",
        "Brunei",
        "Myanmar",
        "Cambodia",
        "Cook Islands",
        "Fiji",
        "French Polynesia",
        "Indonesia",
        "Kiribati",
        "Laos",
        "Macau",
        "Malaysia",
        "Maldives",
        "Mongolia",
        "Nauru",
        "Nepal",
        "New Caledonia",
        "Niue",
        "North Korea",
        "Pakistan",
        "Papua New Guinea",
        "Philippines",
        "Samoa",
        "Solomon Islands",
        "Sri Lanka",
        "Thailand",
        "Timor-Leste",
        "Tonga",
        "Vanuatu",
        "Vietnam",
    ]

    Non_Russia_Eurasia_CDIAC = [
        "Albania",
        "Armenia",
        "Azerbaijan",
        "Belarus",
        "Bosnia and Herzegovina",
        "Bulgaria",
        "Croatia",
        "Cyprus",
        "Georgia",
        "Gibraltar",
        "Kazakhstan",
        "North Macedonia",
        "Moldova",
        "Yugoslavia",
        "Montenegro",
        "Romania",
        "Serbia",
        "Tajikistan",
        "Turkmenistan",
        "Ukraine",
        "Uzbekistan",
    ]

    Africa_CDIAC = [
        "Angola",
        "Benin",
        "Botswana",
        "Burkina Faso",
        "Burundi",
        "Cameroon",
        "Cape Verde",
        "Central African Republic",
        "Chad",
        "Comoros",
        "Congo",
        "Democratic Republic of Congo",
        "Côte d’Ivoire",
        "Djibouti",
        "Equatorial Guinea",
        "Eritrea",
        "Eswatini",
        "Ethiopia",
        "Gabon",
        "Gambia",
        "Ghana",
        "Kenya",
        "Lesotho",
        "Liberia",
        "Madagascar",
        "Malawi",
        "Mali",
        "Mauritania",
        "Mauritius",
        "Mozambique",
        "Namibia",
        "Niger",
        "Nigeria",
        "Reunion",
        "Rwanda",
        "Sao Tome and Principe",
        "Senegal",
        "Seychelles",
        "Sierra Leone",
        "Somalia",
        "South Africa",
        "South Sudan",
        "St. Helena",
        "Sudan",
        "Republic of Sudan",
        "Tanzania",
        "Togo",
        "Uganda",
        "Zambia",
        "Zimbabwe",
    ]

    combined = (
        US_CDIAC
        + OECD_Europe_CDIAC
        + Japan_CDIAC
        + Russia_CDIAC
        + Non_Russia_Eurasia_CDIAC
        + China_CDIAC
        + India_CDIAC
        + Middle_East_CDIAC
        + Africa_CDIAC
        + Latin_America_CDIAC
        + OHI_CDIAC
        + Non_OECD_Asia_CDIAC
    )

    combined_lower_to_capitalized = {country.lower(): country for country in combined}

    # Rename country emissions columns to all lowercase
    country_emissions.rename({k: v for k, v in zip(country_emissions.columns, map(lambda x: x.lower(), country_emissions.columns))}, axis=1, inplace=True)

    combined_lower = list(map(lambda x: x.lower(), combined))
    excluded_countries = countries - set(combined_lower)

    country_emissions.drop(labels=excluded_countries, axis=1, inplace=True)

    # Rename country emissions columns based on lower combined
    country_emissions.rename(combined_lower_to_capitalized, axis=1, inplace=True)
    country_emissions.columns.name = None
    country_emissions = country_emissions.loc[country_emissions.index > 1991]

    # Single Country Regions
    US_CO2 = country_emissions["US"]
    Russia_CO2 = country_emissions["Russia"]
    China_CO2 = country_emissions["China"]
    Japan_CO2 = country_emissions["Japan"]
    India_CO2 = country_emissions["India"]

    # Simple Grouped Regions
    Africa_CO2 = country_emissions.loc[:, Africa_CDIAC].sum(axis=1)
    Middle_East_CO2 = country_emissions.loc[:, Middle_East_CDIAC].sum(axis=1)
    Non_Russia_Eurasia_CO2 = country_emissions.loc[:, Non_Russia_Eurasia_CDIAC].sum(axis=1)
    Latin_America_CO2 = country_emissions.loc[:, Latin_America_CDIAC].sum(axis=1)
    Non_OECD_Asia_CO2 = country_emissions.loc[:, Non_OECD_Asia_CDIAC].sum(axis=1)
    OECD_Europe_CO2 = country_emissions.loc[:, OECD_Europe_CDIAC].sum(axis=1)
    OHI_CO2 = country_emissions.loc[:, OHI_CDIAC].sum(axis=1)

    df_CO2 = pd.DataFrame(
        data={
            "US": US_CO2,
            "OECD-Europe": OECD_Europe_CO2,
            "Japan": Japan_CO2,
            "Russia": Russia_CO2,
            "Non-Russia Eurasia": Non_Russia_Eurasia_CO2,
            "China": China_CO2,
            "India": India_CO2,
            "Middle East": Middle_East_CO2,
            "Africa": Africa_CO2,
            "Latin America": Latin_America_CO2,
            "OHI": OHI_CO2,
            "Other non-OECD Asia": Non_OECD_Asia_CO2,
        }
    )

    return df_CO2 * (10**6)
