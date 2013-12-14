import sys
import os
if not os.path.exists("gen-py"):
    print "gen-py does not exist. Have you run build.sh?"
    sys.exit(1)
sys.path.append("gen-py")


from stringstore import StringStore
from stringstore.ttypes import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class StringStoreServer:
    store = {}
    def getValue(self, request):
        print "GET:", request, self.store
        response = GetResponse()
        response.key = request.key

        if request.key in self.store:
            response.value = self.store[request.key]
            response.status = Status.SUCCESS
        else:
            response.status = Status.ERROR

        return response
    
    def setValue(self, request):
        print "SET:", request
        self.store[request.key] = request.value

handler = StringStoreServer()
processor = StringStore.Processor(handler)

transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
server.serve()
