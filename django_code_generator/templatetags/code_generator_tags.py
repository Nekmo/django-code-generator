from django import template
from django.utils.safestring import mark_safe
register = template.Library()


MAX_LENGTH = 115


def format_indent_line(items, spaces, indent, backslash, is_last):
    line = (' ' * spaces) if indent else ''
    line += ', '.join(items) + (',' if not backslash or not is_last else '')
    if backslash and not is_last:
        line += ' \\'
    return line


@register.simple_tag
def indent_items(items, spaces, backslash=False, quote=False):
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
    return mark_safe('from {} import {}'.format(module, indent_items(items, 4, True)))


@register.filter(is_safe=True)
def add_to_items(items, suffix):
    return ['{}{}'.format(x, suffix) for x in items]
