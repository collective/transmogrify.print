# Based on code from: collective.transmogrifier.sections.tests;
# aimed at easier consumption.
from collective.transmogrifier.interfaces import ISection, ISectionBluePrint
import pprint


class PrettyPrinter(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        self.pprint = pprint.PrettyPrinter().pprint

    def __iter__(self):
        def undict(source):
            """ Recurse trough the structure and convert dictionaries 
                into sorted lists
            """
            res = list()
            if type(source) is dict:
                source = sorted(source.items())
            if type(source) in (list, tuple):
                for item in source:
                    res.append(undict(item))
            else:
                res = source
            # convert a tuple into tuple back
            if type(source) is tuple:
                res = tuple(res)
            return res

        for item in self.previous:
            self.pprint(undict(item))
            yield item

