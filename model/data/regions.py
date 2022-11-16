from enum import Enum

# Regional Specification

# Single country regions
US_countries = ["US"]
Japan_countries = ["Japan"]
China_countries = ["China"]
Russia_countries = ["Russia"]
India_countries = ["India"]


# Multiple countries regions
OECD_Europe_countries = [
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
    "United Kingdom"
]

# Montenegro and Serbia are also grouped as one country as this was in the case between 1996 and 2005
Non_Russia_Eurasia_countries = [
    "Albania",
    "Armenia",
    "Azerbaijan",
    "Belarus",
    "Bosnia and Herzegovina",
    "Bulgaria",
    "Croatia",
    "Cyprus",
    "Faroe Islands",
    "Georgia",
    "Gibraltar",
    "Kazakhstan",
    "Kosovo",
    "Kyrgyzstan",
    "North Macedonia",
    "Malta",
    "Moldova",
    "Montenegro",
    "Romania",
    "Serbia",
    "Serbia and Montenegro",
    "Tajikistan",
    "Turkmenistan",
    "Kyrgyzstan",
    "Ukraine",
    "Uzbekistan"
]

Middle_East_countries = [
    "Israel",
    "Bahrain",
    "Iran",
    "Iraq",
    "Jordan",
    "Kuwait",
    "Lebanon",
    "Oman",
    "Palestinian Territory",
    "Qatar",
    "Saudi Arabia",
    "Syria",
    "United Arab Emirates",
    "Yemen",
    "Egypt",
    "Algeria",
    "Tunisia",
    "Libya",
    "Morocco"
]

Latin_America_countries = [
    "Anguilla",
    "Antigua and Barbuda",
    "Argentina",
    "Aruba",
    "Bahamas",
    "Barbados",
    "Belize",
    "Bermuda",
    "Bolivia",
    "Brazil",
    "British Virgin Islands",
    "Cayman Islands",
    "Chile",
    "Colombia",
    "Costa Rica",
    "Curacao",
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
    "Mexico",
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
    "Puerto Rico",
    "Venezuela",
    "Netherlands Antilles"
]

# South Sudan, Sudan and Republic of Sudan are all present to take into account the changes in borders between both countries
Africa_countries = [
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
    "Cote d'Ivoire",
    "Djibouti",
    "Equatorial Guinea",
    "Eritrea",
    "Eswatini",
    "Ethiopia",
    "Gabon",
    "Gambia",
    "Ghana",
    "Guinea",
    "Guinea-Bissau",
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
    "Zimbabwe"
]

OHI_countries = [
    "Canada",
    "Australia",
    "New Zealand",
    "South Korea",
    "Singapore",
    "Taiwan",
    "Hong Kong",
    "Greenland",
    "Andorra"
]

Non_OECD_Asia_countries = [
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
    "Vietnam"
]

combined_regions = (
    Africa_countries
    + Non_Russia_Eurasia_countries
    + Non_OECD_Asia_countries
    + Middle_East_countries
    + OECD_Europe_countries
    + OHI_countries
    + Latin_America_countries
    + Japan_countries
    + US_countries
    + Russia_countries
    + China_countries
    + India_countries
)


class Region(str, Enum):
    Africa = "Africa"
    US = "US"
    OECD_Europe = "OECD-Europe"
    Japan = "Japan"
    Russia = "Russia"
    Non_Russia_Eurasia = "Non-Russia Eurasia"
    China = "China"
    India = "India"
    Middle_East = "Middle East"
    Latin_America = "Latin America"
    OHI = "OHI"
    Non_OECD_Asia = "Other non-OECD Asia"
