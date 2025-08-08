from flask import jsonify, request

from . import api_bp


@api_bp.get('/getMenu')
def get_menu():
    # Internationalization-ready: accept locale param (default 'en')
    locale = request.args.get('locale', 'en').lower()
    # Currently only 'en' is supported; placeholder for future locales
    if locale != 'en':
        # For now we fall back to English; extend here to provide locale-specific labels.
        ...
    menu = [
        {
            "label": "US Population Table",
            "rule": "/api/rules/us_population_data",
            "type": "table",
        },
        {
            "label": "US Population Chart",
            "rule": "/api/rules/us_population_data",
            "type": "chart",
            "params": {"fill": "red"},
        },
        {
            "label": "About",
            "rule": "/api/rules/about",
            "type": "text",
            "params": {"font-size": "30px"},
        },
    ]
    return jsonify(menu)
