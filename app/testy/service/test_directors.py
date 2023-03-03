import pytest

from app.service.directors_serv import DirectorServise
from app.testy.coftests.directors_conf import director_dao

class TestDirectorService:

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorServise(dao=director_dao)

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.name is not None


