from unittest.mock import MagicMock
import pytest

from app.dao.model.director_model import Director
from app.dao.directors_dao import DirectorDao


@pytest.fixture()
def director_dao():
    director_dao = DirectorDao(None)

    egor = Director(name="egor")
    roma = Director(name="roma")
    misha = Director(name="misha")

    director_dao.get_all = MagicMock(return_value=[egor, roma, misha])
    director_dao.get_one = MagicMock(return_value=egor)
    director_dao.create = MagicMock(return_value=Director(name="egor"))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao