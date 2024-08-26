import logging
import numpy as np

from nomad.datamodel import EntryArchive
from nomad_parser_pyscf.parsers.parser import PySCFParser


def test_parse_file():
    parser = PySCFParser()
    archive = EntryArchive()
    parser.parse('tests/data/glycine.log', archive, logging.getLogger())

    assert archive.data.m_def.name == 'Simulation'
    assert (
        archive.data.m_xpath('program') is not None
        and archive.data.m_xpath('model_system') is not None
    )

    # Program testing
    assert (
        archive.data.program.name == 'PySCF' and archive.data.program.version == '2.2.1'
    )

    # ModelSystem testing
    model_system = archive.data.model_system
    assert len(model_system) == 1
    # Cell testing
    assert len(model_system[0].cell) == 1
    cell = model_system[0].cell[0]
    assert cell.m_def.name == 'AtomicCell'
    assert cell.positions.shape == (3, 3)
    assert np.isclose(
        cell.positions.to('angstrom').magnitude,
        np.array(
            [
                [0.0, 0.0, 0.11779],
                [0.0, 0.755453, -0.471161],
                [0.0, -0.755453, -0.471161],
            ]
        ),
    ).all()
    # ExtendedAtomsState testing
    assert len(cell.atoms_state) == 3
    assert [atom.m_def.name == 'ExtendedAtomsState' for atom in cell.atoms_state]
    assert [atom.chemical_symbol for atom in cell.atoms_state] == ['O', 'H', 'H']
    assert [atom.magnetic_moment.magnitude for atom in cell.atoms_state] == [
        0.0,
        0.0,
        0.0,
    ]
