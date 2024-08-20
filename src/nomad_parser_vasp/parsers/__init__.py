from nomad.config.models.plugins import ParserEntryPoint


class VasprunXMLEntryPoint(ParserEntryPoint):

    def load(self):
        from nomad_parser_vasp.parsers.parser import VasprunXMLParser

        return VasprunXMLParser(**self.dict())


vasprun_xml_entry_point = VasprunXMLEntryPoint(
    name='VasprunXMLParser',
    description='Parser for VASP output in XML format.',
    # mainfile_name_re='.*vasprun\.xml.*',
    mainfile_name_re='vasprun.xml.relax',
)