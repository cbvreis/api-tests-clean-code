import pytest
import requests as re


class TestAPI:
    @pytest.fixture
    def url(self):
        return 'http://localhost:5000/data'

    @pytest.fixture
    def data(self):
        return [1,2,3,4]

    @pytest.fixture
    def uuid(self,url,data):
        response = re.post(url,json={'data':data})
        return response.json()['uuid']

    def test_save_data(self,url, data):
        response = re.post(url,json={'data':data})
        assert response.ok
        assert response.json()['uuid'] is not None

    def test_get_data(self,uuid,url, data):
        response = re.get(url + f'/{uuid}')
        assert response.ok
        assert response.json()['data'] == [1,2,3,4]

    def test_calc_mean(self, url, uuid):
        response = re.get(url + f'/{uuid}/mean')
        assert response.ok
        assert response.json()['result'] == pytest.approx(2.5)

    def test_calc_max(self, url, uuid):
        response = re.get(url + f'/{uuid}/max')
        assert response.ok
        assert response.json()['result'] == pytest.approx(4)

    def test_calc_min(self, url, uuid):
        response = re.get(url + f'/{uuid}/min')
        assert response.ok
        assert response.json()['result'] == pytest.approx(1)
