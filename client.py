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

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)

    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = StringStore.Client(protocol)

    transport.open()
    

    request = GetRequest()
    request.key = "test"
    resp = client.getValue(request)
    print resp

    request = SetRequest()
    request.key = "test"
    request.value = "exists"
    client.setValue(request)

    transport.close()
except Thrift.TException, tx:
    print tx
