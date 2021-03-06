#!/usr/bin/env python
import pytest
import ace_magnetometer as am
from pathlib import Path
from datetime import date
import pandas as pd
import ftplib

dt = '2013-02-12'
R = Path(__file__).parent


@pytest.fixture(scope="session", autouse=True)
def test_download():
    try:
        am.download(dt, R)
    except ftplib.error_temp:
        pytest.skip('download down')


def test_load():
    dat = am.load(dt, R)

    assert isinstance(dat, pd.DataFrame)
    assert dat.index[1].date() == date(2013, 2, 12)


if __name__ == '__main__':
    pytest.main()
