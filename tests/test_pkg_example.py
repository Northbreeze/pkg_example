#!/usr/bin/env python

"""Tests for `pkg_example` package."""


import unittest
import pandas as pd
from pkg_example import pkg_example


def test_catbind():
    a = pd.Categorical(["character", "hits", "your", "eyeballs"])
    b = pd.Categorical(["but", "integer", "where it", "counts"])
    assert ((pkg_example.catbind(a, b)).codes ==
            [1, 4, 7, 3, 0, 5, 6, 2]).all()
    assert ((pkg_example.catbind(a, b)).categories == ["but", "character",
                                                       "counts", "eyeballs", "hits", "integer", "where it", "your"]).all()
