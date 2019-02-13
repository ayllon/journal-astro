import os.path
import IPython

from pygments import highlight
from pygments.lexers import get_lexer_for_filename, TextLexer, IniLexer
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

_custom_lexers = {
    '.config': IniLexer()
}

def _custom_guess(path):
    _, ext = os.path.splitext(path)
    if ext in _custom_lexers:
        return _custom_lexers[ext]
    return TextLexer()


def prettyprint(path):
    try:
        lexer = get_lexer_for_filename(path)
    except ClassNotFound:
        lexer = _custom_guess(path)

    content = open(path).read()
    formatter = HtmlFormatter()
    return IPython.display.HTML('<style type="text/css">{}</style>{}'.format(formatter.get_style_defs('.highlight'), highlight(content, lexer, formatter)))


def size_fmt(size):
    for unit in ['bytes','KiB','MiB','GiB','TiB','Pi','Ei','ZiB']:
        if abs(size) < 1024:
            return f'{size:.2f} {unit}'
        size /= 1024.0
    return size

