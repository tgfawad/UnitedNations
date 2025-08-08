import json
from app import create_app, db
from app.models import AboutText


def make_client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client(), app


def test_get_menu():
    client, _ = make_client()
    resp = client.get('/api/getMenu?locale=en')
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    labels = [i['label'] for i in data]
    assert 'US Population Table' in labels
    assert 'US Population Chart' in labels
    assert 'About' in labels


def test_about_returns_text_and_timestamp():
    client, app = make_client()
    with app.app_context():
        # Ensure there is content
        if not AboutText.query.first():
            db.session.add(AboutText(content='Hello world.'))
            db.session.commit()
    resp = client.get('/api/rules/about')
    assert resp.status_code == 200
    payload = resp.get_json()
    assert 'text' in payload
    assert 'Last update:' in payload['text']


def test_us_population_data_handles_failure(monkeypatch):
    client, _ = make_client()

    class DummyResp:
        def raise_for_status(self):
            raise Exception('boom')

    def fake_get(*args, **kwargs):
        return DummyResp()

    import app.routes.rules as routes
    monkeypatch.setattr(routes.requests, 'get', fake_get)

    resp = client.get('/api/rules/us_population_data')
    assert resp.status_code == 502
    payload = resp.get_json()
    assert payload['error']


def test_us_population_data_transforms(monkeypatch):
    client, _ = make_client()

    class DummyResp:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                'data': [
                    {'year': '2022', 'population': '331097593'},
                    {'year': 2021, 'population': 329725481},
                ]
            }

    import app.routes.rules as routes
    monkeypatch.setattr(routes.requests, 'get', lambda *args, **kwargs: DummyResp())

    resp = client.get('/api/rules/us_population_data')
    assert resp.status_code == 200
    payload = resp.get_json()
    assert payload[0]['year'] == 2022
    assert payload[0]['population'] == 331097593
