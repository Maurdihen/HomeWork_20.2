from unittest.mock import MagicMock
import pytest

from app.dao.model.genre_model import Genre
from app.dao.genres_dao import GenreDao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDao(None)

    horror = Genre(name="horror")
    drama = Genre(name="drama")
    adventures = Genre(name="adventures")

    genre_dao.get_all = MagicMock(return_value=[horror, drama, adventures])
    genre_dao.get_one = MagicMock(return_value=horror)
    genre_dao.create = MagicMock(return_value=Genre(name="horror"))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao