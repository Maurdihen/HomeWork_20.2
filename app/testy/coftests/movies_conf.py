from unittest.mock import MagicMock
import pytest

from app.dao.model.movie_model import Movie
from app.dao.movies_dao import MovieDao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDao(None)

    silicon_valley = Movie(id=1, title="Silicon Valley", description="Сериал 'Кремниевая долина', это любопытное повествование, посвященное влиянию новых технологий на жизнь планеты.",
                   trailer="https://lordserial.fun/144-kremnievaya-dolina-72.html", year=2014, rating=9.3, genre_id=1, director_id=2)
    game_of_thrones = Movie(id=2, title="Game of Thrones", description="К концу подходит время благоденствия, и лето, длившееся почти десятилетие, угасает.",
                   trailer="https://ww21.lordsfilm.win/27310-igra-prestolov-serial-17-02-21.html", year=2011, rating=9.3, genre_id=3, director_id=4)
    themazerunner = Movie(id=3, title="The Maze Runner", description="Главный герой — подросток Томас, который просыпается в лифте, но ничего не помнит, кроме своего имени.",
                   trailer="https://www.kinopoisk.ru/film/575613/", year=2014, rating=6.8, genre_id=2, director_id=1)

    movie_dao.get_all = MagicMock(return_value=[silicon_valley, game_of_thrones, themazerunner])
    movie_dao.get_one = MagicMock(return_value=silicon_valley)
    movie_dao.create = MagicMock(return_value=Movie(title="Game of Thrones"))
    movie_dao.get_by_year = MagicMock(return_value=game_of_thrones)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()
    movie_dao.get_by_genre = MagicMock(return_value=silicon_valley)
    movie_dao.get_by_director = MagicMock(return_value=game_of_thrones)

    return movie_dao