import os

from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = str(os.getenv("BEARER_TOKEN"))
IDS_TECH_REG = str(os.getenv("IDS_TECH_REG"))
MIN_END_DATE = str(os.getenv("MIN_END_DATE"))
MAX_END_DATE = str(os.getenv("MAX_END_DATE"))

DOWNLOADS_DIR = "downloads"

CERT_PAGE_SIZE = 100
CERTIFICATES_DETAILS_DIR = f"{DOWNLOADS_DIR}/certificate_details"
CERT_DATA_PATH = os.path.join(DOWNLOADS_DIR, "cert_data.csv")
OUTPUT_CERTS_PATH = os.path.join(DOWNLOADS_DIR, f"certificates_{MIN_END_DATE}_{MAX_END_DATE}.csv")
CERT_TYPES_MAP_FILE_PATH = os.path.join(DOWNLOADS_DIR, "cert_types_map.json")

DECL_PAGE_SIZE = 1000
DECLARATIONS_DETAILS_DIR = f"{DOWNLOADS_DIR}/declaration_details"
DECL_DATA_PATH = os.path.join(DOWNLOADS_DIR, f"decl_data_{MIN_END_DATE}_{MAX_END_DATE}.csv")
OUTPUT_DECLS_PATH = os.path.join(DOWNLOADS_DIR, f"declarations_{MIN_END_DATE}_{MAX_END_DATE}.csv")
DECL_TYPES_MAP_FILE_PATH = os.path.join(DOWNLOADS_DIR, "decl_types_map.json")

TRTS_FILE_PATH = os.path.join(DOWNLOADS_DIR, "trts.json")
FILTER_DATE_FORMAT = "%Y-%m-%d"
OUTPUT_DATE_FORMAT = "%d/%m/%Y"
