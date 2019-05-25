# -*- coding: utf-8 -*-

"""Exceptions for django-code-generator."""
import os
import sys


class DjangoCodeGeneratorError(Exception):
    body = ''

    def __init__(self, extra_body=''):
        self.extra_body = extra_body

    def __str__(self):
        msg = self.__class__.__name__
        if self.body:
            msg += ': {}'.format(self.body)
        if self.extra_body:
            msg += ('. {}' if self.body else ': {}').format(self.extra_body)
        return msg


class TemplateNotFound(DjangoCodeGeneratorError):
    body = 'Template not found'

    def __init__(self, directories, template):
        directories = filter(lambda x: bool(x), directories)
        directories = map(lambda x: os.path.join(x, template), directories)
        self.extra_body = 'Template name: {}. Template directories: {}'.format(
            template, ', '.join(directories)
        )


def catch(fn):
    def wrap(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except DjangoCodeGeneratorError as e:
            sys.stderr.write('[Error] django-code-generator Exception:\n{}\n'.format(e))
    return wrap
