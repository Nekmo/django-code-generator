#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `django_code_generator` package."""
import os
import unittest
from os.path import expanduser
from unittest.mock import patch

from django.test import override_settings

from django_code_generator.management.commands.generator import TEMPLATES_ENVIRONMENT_VARIABLE, \
    TEMPLATES_DJANGO_SETTINGS_VARIABLE, get_template_directories, DOTTED_TEMPLATE_DIRECTORY, TEMPLATE_DIRECTORY, \
    directory


class TestGetTemplateDirectories(unittest.TestCase):

    def setUp(self):
        module = 'django_code_generator.management.commands.generator'
        self.env_mock = patch.dict('os.environ', {TEMPLATES_ENVIRONMENT_VARIABLE: '/env/'})
        self.env_mock.start()
        self.main_mock = patch('{}.main_tpl_directory'.format(module),
                             '/main/')
        self.main_mock.start()

    def tearDown(self):
        self.main_mock.stop()
        self.env_mock.stop()

    # @patch.dict('os.environ', {TEMPLATES_ENVIRONMENT_VARIABLE: '/env/'})
    @override_settings(**{TEMPLATES_DJANGO_SETTINGS_VARIABLE: ['/settings/']})
    def test_directories(self):
        """Test something."""
        directories = get_template_directories()
        self.assertListEqual(directories, [
            '/env/',
            os.path.join(os.getcwd(), DOTTED_TEMPLATE_DIRECTORY),
            '/settings/',
            '/main/',
            os.path.join(expanduser("~/.config/"), TEMPLATE_DIRECTORY),
            os.path.join(directory, 'templates'),
        ])
