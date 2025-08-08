from datetime import datetime
from flask import jsonify
import requests

from . import api_bp
from ..models import AboutText


@api_bp.get('/rules/us_population_data')
@api_bp.get('/rules/us_population')
def us_population_data():
    # Retrieve and transform data from external API
    url = 'https://raw.githubusercontent.com/molipet/full-stack-test/main/data.json'
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        payload = r.json()
    except Exception as e:
        return jsonify({"error": "Failed to fetch population data", "detail": str(e)}), 502

    # Expect payload to include list of entries with year and population fields; transform
    transformed = []
    # Support a couple common payload variants defensively
    if isinstance(payload, dict) and 'data' in payload:
        items = payload['data']
    else:
        items = payload

    for item in items:
        try:
            # Handle keys from the GitHub JSON ("Year", "Population") and fallback keys
            if 'Year' in item and 'Population' in item:
                year_raw = item['Year']
                pop_raw = item['Population']
            else:
                year_raw = item.get('year')
                pop_raw = item.get('population')
            year = int(year_raw)
            population = int(pop_raw)
            transformed.append({"year": year, "population": population})
        except Exception:
            # Skip malformed items
            continue

    # Sort by year descending or leave as-is? Keep original order if provided.
    return jsonify(transformed)


@api_bp.get('/rules/about')
def about():
    row = AboutText.query.first()
    content = row.content if row else ''
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({
        "text": f"{content} Last update: {now}",
    })
