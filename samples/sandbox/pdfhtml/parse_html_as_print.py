import itextpy
itextpy.load()

from pathlib import Path

from System.IO import FileAccess, FileMode, FileStream
from iText.Html2pdf import ConverterProperties, HtmlConverter
from iText.StyledXmlParser.Css.Media import MediaDeviceDescription, MediaType

SCRIPT_DIR = Path(__file__).parent.absolute()
RESOURCES_DIR = SCRIPT_DIR / ".." / ".." / "resources"
SRC_DIR = RESOURCES_DIR / "pdfhtml" / "media"


def manipulate_pdf(html_source, pdf_dest, resource_loc):
    # Base URI is required to resolve the path to source files
    converter_properties = ConverterProperties().SetBaseUri(resource_loc)

    # Set media device type to correctly parsing html with media handling
    converter_properties.SetMediaDeviceDescription(MediaDeviceDescription(MediaType.PRINT))

    HtmlConverter.ConvertToPdf(
        FileStream(html_source, FileMode.Open),
        FileStream(pdf_dest, FileMode.Create, FileAccess.Write),
        converter_properties
    )


if __name__ == "__main__":
    manipulate_pdf(
        html_source=str(SRC_DIR / "rainbow.html"),
        pdf_dest="parse_html_as_print.pdf",
        resource_loc=str(SRC_DIR),
    )
