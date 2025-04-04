import itextpy
itextpy.load()

import contextlib

from iText.IO.Font.Constants import StandardFonts
from iText.Kernel.Colors import ColorConstants
from iText.Kernel.Font import PdfFontFactory
from iText.Kernel.Pdf import PdfWriter, PdfDocument
from iText.Layout import Style, Document
from iText.Layout.Element import Paragraph, Text


@contextlib.contextmanager
def itext_closing(obj):
    try:
        yield obj
    finally:
        obj.Close()


def manipulate_pdf(dest):
    code = PdfFontFactory.CreateFont(StandardFonts.COURIER)

    style = (Style()
             .SetFont(code)
             .SetFontSize(14)
             .SetFontColor(ColorConstants.RED)
             .SetBackgroundColor(ColorConstants.LIGHT_GRAY))

    paragraph = (Paragraph()
                 .Add("In this example, named ")
                 .Add(Text("HelloWorldStyles").AddStyle(style))
                 .Add(", we experiment with some text in ")
                 .Add(Text("code style").AddStyle(style))
                 .Add("."))

    with itext_closing(Document(PdfDocument(PdfWriter(dest)))) as document:
        document.Add(paragraph)


if __name__ == "__main__":
    manipulate_pdf("paragraph_text_with_style.pdf")
