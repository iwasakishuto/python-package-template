# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import re
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = '{{ PACKAGE_NAME }}'
copyright = '2021, {{ AUTHOR }}'
author = '{{ AUTHOR }}'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# import matplotlib
# import IPython

extensions = [
    'sphinxext.opengraph',         # pip install sphinxext-opengraph
    'sphinx.ext.autodoc',          # Include documentation from docstrings.
    'sphinx.ext.autosummary',      # Generate autodoc summaries.
    'sphinx.ext.viewcode',         # Add links to highlighted source code.
    'sphinx.ext.todo',             # Support for todo items.
    'sphinx.ext.napoleon',         # Support for NumPy and Google style docstrings
    'sphinx.ext.githubpages',      # Publish HTML docs in GitHub Pages
    'sphinx.ext.graphviz',         # Enable Graphvis
    'sphinx.ext.autosectionlabel', # Allow reference sections using its title
    'sphinxemoji.sphinxemoji',     # Emoji
    'sphinx_fontawesome',          # FontAwsome
    'sphinx_togglebutton',         # Add a "toggle button"
    # 'IPython.sphinxext.ipython_console_highlighting', # 
    # 'IPython.sphinxext.ipython_directive',            # Additional directive for ipython::
    # 'matplotlib.sphinxext.plot_directive',            # Additional directive for plot::
    # 'sphinx_plotly_directive',                        # Additional directive for plotly::
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# html_favicon = logo = "../images/favicon.png"
html_show_sphinx = False

# How to sort.
autodoc_member_order = "bysource"

# -- Options for extension ----------------------------------------------

# [todo]
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# [autosammary]
autosummary_generate = True

# [opengraph]
ogp_site_url = "https://iwasakishuto.github.io/{{ REPOSITORY_NAME }}/"
ogp_image = ""
ogp_description_length = 200
ogp_type = "article"
ogp_custom_meta_tags = [
    '<meta property="og:site_name" content="{{ PACKAGE_NAME }}" />',
    '<meta name="twitter:site" content="@{{ TWITTER_USERNAME }}" />',
    '<meta name="twitter:card" content="summary">',
    f'<meta name="twitter:image:src" content="{ogp_image}">',
]