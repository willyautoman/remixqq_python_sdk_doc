# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'RemixQQ Python SDK'
copyright = '2024, 404_NOT_FOUND'
author = '404_NOT_FOUND'

release = '0.1'
version = '0.0.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'


autodoc_default_options = {
    'member-order': 'bysource',  # 成员按源代码顺序排序
    'special-members': '__init__',  # 包含特殊成员，如构造函数
    'exclude-members': '__weakref__',  # 排除特定的成员，这里排除了weakref
    'undoc-members': True,  # 包括未明确标记文档的成员
    'show-inheritance': True,  # 显示类的继承关系
}
