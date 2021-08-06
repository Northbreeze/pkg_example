#!/usr/bin/env python

"""Tests for `pkg_example` package."""


import unittest
import pandas as pd
from pkg_example import pkg_example
from pytest import raises, fixture


@fixture()
def test_data():
    return {'a': pd.Categorical(["character", "hits", "your", "eyeballs"]),
            'b': pd.Categorical(["but", "integer", "where it", "counts"]),
            'c': ["but", "integer", "where it", "counts"]}


class Testpypkgs:

    def test_catbind(self, test_data):
        assert ((pkg_example.catbind(test_data['a'], test_data['b'])).codes ==
                [1, 4, 7, 3, 0, 5, 6, 2]).all()
        assert ((pkg_example.catbind(test_data['a'], test_data['b'])).categories ==
                ["but", "character", "counts", "eyeballs", "hits", "integer", "where it", "your"]).all()
