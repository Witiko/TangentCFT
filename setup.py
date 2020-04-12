#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="tangentcft",
    version="0.0.1",
    description="Packaged version of BehroozMansouri/TangentCFT",
    author="Vít Novotný",
    author_email="witiko@mail.muni.cz",
    url="https://github.com/MIR-MU/TangentCFT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["gensim~=3.8.1", "matplotlib~=3.0.3", "torch~=1.4.0"],
    package_data={
        "tangentcft": [
            "Configuration/config/config_1",
            "Retrieval_Results/*",
            "TangentS/math_tan/87",
            "TangentS/math_tan/mws.sty.ltxml",
            "Visualization/formula_tsne",
        ]
    },
)
