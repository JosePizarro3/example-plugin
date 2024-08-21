from nomad.config.models.plugins import ParserEntryPoint


class VasprunXMLEntryPoint(ParserEntryPoint):

    def load(self):
        from nomad_parser_vasp.parsers.parser import VasprunXMLParser

        return VasprunXMLParser(**self.dict())


vasprun_xml_parser = VasprunXMLEntryPoint(
    name='VasprunXMLParser',
    description='Parser for VASP output in XML format.',
    # mainfile_name_re='example.out',
    mainfile_contents_re=r'mysupercode',
)