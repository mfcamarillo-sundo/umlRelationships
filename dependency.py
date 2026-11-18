class Document:
    def __init__(self, title):
        self.title = title


class Printer:
    def print_document(self, document):
        print("Printing:", document.title)


document = Document("Science Report")
printer = Printer()

printer.print_document(document)
