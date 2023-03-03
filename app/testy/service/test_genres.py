import pytest

from app.service.genres_serv import GenreServise
from app.testy.coftests.genres_conf import genre_dao

class TestGenreService:

    @pytest.fixture(autouse=True)
    def director_service(self, genre_dao):
        self.genre_service = GenreServise(dao=genre_dao)

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.name is not None