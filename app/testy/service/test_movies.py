import pytest

from app.service.movies_serv import MovieServise
from app.testy.coftests.movies_conf import movie_dao

class TestMovieService:

    @pytest.fixture(autouse=True)
    def director_service(self, movie_dao):
        self.movie_service = MovieServise(dao=movie_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.title is not None
        assert movie.title == "Silicon Valley"

    def test_create(self):
        movie_d = {
            "title": "Silicon Valley",
            "description": "Сериал 'Кремниевая долина', это любопытное повествование, посвященное влиянию новых технологий на жизнь планеты.",
            "trailer": "https://lordserial.fun/144-kremnievaya-dolina-72.html",
            "year": 2014,
            "rating": 9.3
        }

        movie = self.movie_service.create(movie_d)

        assert movie.title is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 4,
            "title": "Silicon Valley",
            "description": "Сериал 'Кремниевая долина', это любопытное повествование, посвященное влиянию новых технологий на жизнь планеты.",
            "trailer": "https://lordserial.fun/144-kremnievaya-dolina-72.html",
            "year": 2014,
            "rating": 9.3,
            "genre_id": 2,
            "director_id": 1
        }

        self.movie_service.update(movie_d)

    def test_get_by_genre(self):
        movies = self.movie_service.get_by_genre(1)

        assert movies is not None
        assert movies.title is not None
        assert movies.title == "Silicon Valley"
        assert movies.id == 1

    def test_get_by_director(self):
        movies = self.movie_service.get_by_director(4)

        assert movies is not None
        assert movies.title is not None
        assert movies.title == "Game of Thrones"
        assert movies.id == 2

    def test_get_by_year(self):
        movie = self.movie_service.get_by_year(2011)

        assert movie is not None
        assert movie.title is not None
        assert movie.title == "Game of Thrones"