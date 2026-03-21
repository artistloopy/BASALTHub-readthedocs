# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'BASALTHub'
copyright = '2021, BASAL'
author = 'BASAL'

release = ''
version = ''

# -- General configuration

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
myst_enable_extensions = [
    'colon_fence',
]

# -- Options for HTML output

try:
    import sphinx_rtd_theme  # noqa: F401

    html_theme = 'sphinx_rtd_theme'
    # RTD theme primary/header color
    html_theme_options = {
        'style_nav_header_background': '#0077B6',
    }
except ImportError:
    html_theme = 'alabaster'
    # Alabaster fallback options
    html_theme_options = {
        'accent_color': '#0077B6',
        'sidebar_collapse': True,
    }

# Use a custom title and include a small custom stylesheet to ensure the
# ocean-blue branding works even if the RTD theme isn't available.
html_title = 'BASALTHub — Documentation'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
html_logo = '_static/logo.png'
html_show_sourcelink = False

# -- Options for EPUB output
epub_show_urls = 'footnote'
