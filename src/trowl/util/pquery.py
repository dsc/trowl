from pyquery import PyQuery
import lxml

class PQuery(PyQuery):
    
    def iter(self):
        # Iterate by index, or face infinite recursion!
        for i in xrange(len(self)):
            el = self[i]
            # print "PyQuery: %s isinstance Element? " % el, isinstance(el, lxml.etree._Element)
            if isinstance(el, lxml.etree._Element):
                yield PQuery(el)
            else:
                yield el
        
        raise StopIteration()
    
    def eq(self, idx):
        return PQuery(self[idx])
    
    @staticmethod
    def parse(f):
        if isinstance(f, file) or hasattr(f, 'read'):
            return PQuery.from_file(f)
        elif isinstance(f, basestring):
            return PQuery.from_path(f)
        else:
            return PQuery(f)
    
    @staticmethod
    def from_file(f):
        return PQuery(lxml.html.parse(f).getroot())
    
    @staticmethod
    def from_path(path):
        return PQuery.from_file(open(path, 'rU'))
    

parse = PQuery.parse
from_file = PQuery.from_file
from_path = PQuery.from_path
