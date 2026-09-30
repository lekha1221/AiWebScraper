"""
settings.py  — flat version (no subfolders)
All files import this directly: from settings import SCRAPER_CONFIG
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent   # same folder as all other .py files

# Data folders — created automatically if missing
PATHS = {
    "raw_data":       BASE_DIR / "data_raw",
    "processed_data": BASE_DIR / "data_processed",
    "reports":        BASE_DIR / "reports",
    "logs":           BASE_DIR / "logs",
}
for p in PATHS.values():
    p.mkdir(parents=True, exist_ok=True)

SCRAPER_CONFIG = {
    "request_delay_min": 2.0,
    "request_delay_max": 5.0,
    "max_retries": 3,
    "timeout": 30,
    "max_workers": 2,
    "user_agents": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    ],
    "default_headers": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-IN,en;q=0.9,hi;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection":      "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    },
}

DATA_SOURCES = {
    "99acres": {
        "enabled":    True,
        "base_url":   "https://www.99acres.com",
        "type":       "portal",
    },
    "magicbricks": {
        "enabled":    True,
        "base_url":   "https://www.magicbricks.com",
        "type":       "portal",
    },
    "housing": {
        "enabled":    True,
        "base_url":   "https://housing.com",
        "type":       "portal",
    },
    "nominatim": {
        "enabled":    True,
        "geocode_url": "https://nominatim.openstreetmap.org/search",
        "type":       "api",
    },
    "overpass": {
        "enabled":    True,
        "api_url":    "https://overpass-api.de/api/interpreter",
        "type":       "api",
    },
    "reddit": {
        "enabled":    True,
        "search_url": "https://www.reddit.com/search.json",
        "subreddits": ["india","bangalore","mumbai","delhi","hyderabad",
                       "pune","realestateindia","personalfinanceindia"],
        "type":       "forum",
    },
}

ANALYSIS_CONFIG = {
    "infra_radius_meters": 1000,
    "min_posts_for_sentiment": 10,
    "buyer_intent_keywords": [
        "looking to buy","planning to buy","want to buy","should i buy",
        "invest in","searching for flat","2bhk","3bhk","4bhk",
        "apartment","property","builder","possession","rera",
    ],
    "amenity_tags": {
        "Metro Station": ("railway",  "station"),
        "School":        ("amenity",  "school"),
        "Hospital":      ("amenity",  "hospital"),
        "Supermarket":   ("shop",     "supermarket"),
        "Mall":          ("shop",     "mall"),
        "Restaurant":    ("amenity",  "restaurant"),
        "Park":          ("leisure",  "park"),
        "IT Park":       ("office",   "it"),
    },
}

API_KEYS = {
    "google_maps": os.environ.get("GOOGLE_MAPS_KEY", ""),
    "rapidapi":    os.environ.get("RAPIDAPI_KEY", ""),
}