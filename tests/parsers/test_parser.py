import logging

from nomad.datamodel import EntryArchive
from nomad_parser_pyscf.parsers.parser import PySCFParser


def test_parse_file():
    parser = PySCFParser()
    archive = EntryArchive()
    parser.parse('tests/data/glycine.log', archive, logging.getLogger())

    assert archive.workflow2.name == 'test'
