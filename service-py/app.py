'''
Importing transport, protocols and servers from thrift
'''
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket, TTransport
'''
Importing Micro service to which the @getUser is binded
'''
from gen_py.UserService import MicroService1
'''
Importing class which has definition of getUser
'''
from ServiceHandler import UserService


user_object = UserService()
processor = MicroService1.Processor(user_object)

HOST = "localhost"
PORT = 6543

transport = TSocket.TServerSocket(host=HOST, port=PORT)

transportFactory = TTransport.TBufferedTransportFactory()
protocolFactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TThreadedServer(processor, transport, transportFactory, protocolFactory)

print("Application started listening")

server.serve()