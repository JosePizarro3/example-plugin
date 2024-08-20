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
from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import Quantity, SchemaPackage

configuration = config.get_plugin_entry_point(
    'nomad_parser_vasp.schema_packages:vasp_schema_extensions'
)

m_package = SchemaPackage()


class MySchema(Schema):
    name = Quantity(
        type=str, default='World'
    )
    message = Quantity(type=str)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        self.message = f'Hello {self.name}!'


m_package.__init_metainfo__()
