from lxml import etree

from .startup import *
from .filter import Filter
from .tools import *

GM_ROCK_KIT_FILE = Path('data/GMRockKit Instrument Names.txt')
ROCK_DRUM_KIT_FILE = Path('data/Rock Drum Kit Instrument Names.txt')

GM_ROCK_KIT = GM_ROCK_KIT_FILE.readlines()
ROCK_DRUM_KIT = ROCK_DRUM_KIT_FILE.readlines()

class Peroxide(Filter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process(self, s):
        log.info(f"Processing {s=}...")
        tree = etree.parse(s)
        root = tree.getroot()
        for elem in root.iter():
            elem.tag = etree.QName(elem).localname
        # Now, we can use XPath without worrying about the namespace
        notes = root.xpath('//note')
        for note in notes:
            # Set the id of the existing note to 
            
            pass
        log.info(f'{notes=}')



