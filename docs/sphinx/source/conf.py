# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('../../..')) # docs/sphinx/source/conf.py 인 경우
# 만약 경로 못찾는다 나오면 아래와 같이 풀경로 넣어야함
sys.path.insert(0, os.path.abspath('/home/kspec/mingyeong/kspec-gfa'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "kspec-gfa"
copyright = "2024, mingyeong"
author = "Mingyeong Yang"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
    ]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
#on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
# only import and set the theme if we're building docs locally
#if not on_rtd:
#    import sphinx_rtd_theme
#    html_theme = 'sphinx_rtd_theme'
#    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# 출처: https://cimple.tistory.com/416 [CIMPLE - Christ Is My Personal Lord & Everything:티스토리]

html_static_path = ["_static"]
html_logo = "_static/kasi.png"
html_title = "KSPEC-GFA"
