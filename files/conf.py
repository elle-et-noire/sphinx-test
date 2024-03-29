# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx-Test'
copyright = '2024, Lomega'
author = 'Lomega'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_css_files = ['header.css', 'table.css']

mathjax3_config = {
    "loader": {"load": ["[tex]/physics"]},
    "tex": {
      "packages": {"[+]": ["physics"]},
      "physics": {
        "italicdiff": True,
        "arrowdel": False,
      },
      "tags": 'ams',
      "tagSide": 'right',
      "tagIndent": '0.8em',
      "processRefs": True,
    },
}

latex_elements = {
    "extrapackages": "\\usepackage{physics}"
}

latex_docclass = {'mydocument': 'jsbook'}
