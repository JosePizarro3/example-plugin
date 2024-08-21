from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config
from nomad.parsing.parser import MatchingParser
from nomad.parsing.file_parser import Quantity as ParsedQuantity, TextParser
from nomad_simulations.schema_packages.general import Simulation, Program


configuration = config.get_plugin_entry_point(
    'nomad_parser_pyscf.parsers:pyscf_entry_point'
)


class LogParser(TextParser):
    def init_quantities(self):
        self._quantities = [
            ParsedQuantity(
                'program_version', r'PySCF *version *([\d\.]+)', repeats=False
            )
        ]


class PySCFParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: 'EntryArchive',
        logger: 'BoundLogger',
        child_archives: dict[str, 'EntryArchive'] = None,
    ) -> None:

        log_parser = LogParser(mainfile=mainfile, logger=logger)

        simulation = Simulation()
        program = Program(
            name='PySCF', version=log_parser.get('program_version')
        )
        simulation.program = program

        # Add the `Simulation` activity to the `archive`
        archive.data = simulation

