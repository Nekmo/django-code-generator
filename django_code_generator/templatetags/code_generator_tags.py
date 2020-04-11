from django import template
from django.utils.safestring import mark_safe
register = template.Library()


#: Maximum length of the lines.
MAX_LENGTH = 115


def format_indent_line(items, spaces, indent, backslash, is_last):
    """Returns elements separated by commas. The line can be indented. This function is for
    internal use and is not available in templates.

    :param list items: a list of items.
    :param int spaces: indentation spaces
    :param bool indent: indent the line
    :param bool backslash: Add backlash (``\``) to the end
    :param bool is_last: is the last line. If it is True, a comma is not put after
                         the last element. Backlash is also not added
    :return: Items separated by commas
    """
    line = (' ' * spaces) if indent else ''
    line += ', '.join(items) + (',' if not backslash or not is_last else '')
    if backslash and not is_last:
        line += ' \\'
    return line


@register.simple_tag
def indent_items(items, spaces, backslash=False, quote=False):
    """Prints elements of a list separated by commas. If the line length exceeds :const:`MAX_LENGTH` it
    breaks to another line. The new line is indented. The first line is not indented.

    :param items: items to print.
    :param spaces: indentation of the new lines.
    :param backslash: Add backlash (``\``) to the end of each line except the last one.
    :param quote: use quotes with each element. Options: ``False``, ``"double"`` or ``"simple"``.
    :return: Items separated by commas and indented if necessary.
    """
    items = map(str, items)
    if quote:
        quote = '"' if quote == 'double' else "'"
        items = map(lambda x: '{quote}{value}{quote}'
                    .format(quote=quote, value=x.replace(quote, '\\{}'.format(quote))), items)
    line_items = []
    lines = []
    items = list(items)
    for i, item in enumerate(items):
        is_last = i >= len(items) - 1
        line = ', '.join(line_items + [item])
        if len(line) > (MAX_LENGTH - spaces):
            lines.append(format_indent_line(line_items, spaces, lines, backslash, is_last and not line_items))
            line_items = [item]
        else:
            line_items.append(item)
        if is_last and line_items:
            lines.append(format_indent_line(line_items, spaces, lines, backslash, is_last))
    return mark_safe('\n'.join(lines))


@register.simple_tag
def from_module_import(module, items):
    """Print "from <module> import <items>". Elements are separated by commas (``,``). If the line length
    exceeds :const:`MAX_LENGTH` it breaks to another line.
    """
    return mark_safe('from {} import {}'.format(module, indent_items(items, 4, True)))


@register.filter(is_safe=True)
def add_to_items(items, suffix):
    """Add a suffix to the elements of a listing. For example, add "Serializer" to
    each item in the list.

    .. deprecated::
       Use :func:`suffix_to_items` instead.

    """
    return ['{}{}'.format(x, suffix) for x in items]


@register.filter(is_safe=True)
def prefix_to_items(items, prefix):
    """Add a prefix to the elements of a listing. For example, add "Base" to
    each item in the list.
    """
    return ['{}{}'.format(prefix, x) for x in items]


@register.filter(is_safe=True)
def suffix_to_items(items, suffix):
    """Add a suffix to the elements of a listing. For example, add "Serializer" to
    each item in the list.
    """
    return ['{}{}'.format(x, suffix) for x in items]
