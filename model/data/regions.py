from enum import Enum

# Regional Specification

# Single country regions
China_countries = ["China"]
Russia_countries = ["Russia"]
Japan_countries = ["Japan"]
US_countries = ["US"]
India_countries = ["India"]

# Multiple countries regions
Latin_America_countries = [
    "Mexico",
    "Anguilla",
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
    "Puerto Rico",
    "Venezuela",
    "Netherlands Antilles",
    "Curacao",
    "British Virgin Islands",
    "Faroe Islands",
    "Bahamas",
    "Aruba",
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
    "Andorra",
    "British Virgin Islands",
    "Faeroe Islands",
    "Bermuda",
    "Bahamas",
]

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
    "United Kingdom",
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
    "Yemen" "Egypt",
    "Algeria",
    "Tunisia",
    "Libya",
    "Morocco",
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
    "Vietnam",
]

Non_Russia_Eurasia_countries = [
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
    "Malta",
    "Moldova",
    "Serbia and Montenegro",
    "Romania",
    "Tajikistan",
    "Turkmenistan",
    "Kyrgyzstan",
    "Ukraine",
    "Uzbekistan",
]

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
    "Zimbabwe",
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
