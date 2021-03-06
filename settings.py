# coding=utf-8
"""Settings file"""
import re


COVERAGE_PATH = '.coverage'
IGNORED_NAME_PORTIONS = [re.compile(r'(?:^|[_.-])test.py'), re.compile(r'(?:\b|^)docs/')]
REQUIRED_NAME_PORTIONS = [re.compile(r'\.py$')]
OUTPUT_COVERAGE_DOC = 'diff_coverage_html'
COMPARE_WITH_BRANCH = 'master'
HTML_DIFF_REPORT_PATH = 'diff_coverage.html'
XML_REPORT_FILE = 'coverage.xml'
HTML_REPORT_DIR = 'coverage_html'


try:
    execfile('globalsettings')
except IOError:
    pass
