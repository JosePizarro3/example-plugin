from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class MySchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_parser_vasp.schema_packages.schema import m_package

        return m_package


vasp_schema_extensions = MySchemaPackageEntryPoint(
    name='MyPackage',
    description='Schema package defined using the new plugin mechanism.',
)
