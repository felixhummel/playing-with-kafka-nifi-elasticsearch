import json
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback

import sys

class ModJSON(StreamCallback):

    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        obj = json.loads(text)
        obj.update({
            'foo': 'bar',
            'pyver': sys.version
        })
        outputStream.write(bytearray(json.dumps(obj).encode('utf-8')))


flowFile = session.get()
if (flowFile != None):
    flowFile = session.write(flowFile, ModJSON())
    flowFile = session.putAttribute(flowFile, "filename", flowFile.getAttribute('filename').split('.')[0]+'_translated.json')
session.transfer(flowFile, REL_SUCCESS)
session.commit()
