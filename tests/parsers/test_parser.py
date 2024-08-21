import logging

from nomad.datamodel import EntryArchive
from nomad_parser_vasp.parsers.parser import VasprunXMLParser


def test_parse_file():
    parser = VasprunXMLParser()
    archive = EntryArchive()
    parser.parse('tests/data/example.out', archive, logging.getLogger())
