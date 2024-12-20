import os
import sys
import django
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'my_site.settings'
django.setup()

#  Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'My_Site'
copyright = '2024, EmaanIsaacsWaggie'
author = 'EmaanIsaacsWaggie'
release = '01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',      # Generates documentation from Python docstrings
    'sphinx.ext.napoleon',     # Supports Google-style and NumPy-style docstrings
    'sphinx.ext.viewcode',     # Adds links to source code
    'sphinxcontrib_django',    # Django-specific tools for documenting models, views, etc. (install separately)
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
