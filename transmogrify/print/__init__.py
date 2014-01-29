# Based on code from: collective.transmogrifier.sections.tests.PrettyPrinter
# aimed at easier consumption.

from collective.transmogrifier.interfaces import ISection, ISectionBlueprint
from zope.interface import classProvides, implements
import pprint

class PrettyPrinter(object):
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        self.pprint = pprint.PrettyPrinter().pprint
        if 'keys' in options:
            self.keys = options['keys']
        else:
            self.keys = None

    def __iter__(self):
        def undict(source):
            """ Recurse through the structure and convert dictionaries 
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
            if not self.keys is None:
                # Create a new dict to hold our keys
                newdict={}
                for key in self.keys.split():
                    if key in item:
                        newdict[key] = item[key]

                # XXX We don't really need to 
                # re-dict then undict, but it's
                # an easy way to provide output
                # similar to what Transmogrifier
                # itself provides.
                self.pprint(undict(newdict))
            else: 
                self.pprint(undict(item))
                yield item

