# Apache Thrift Demo Application

[![N|Solid](https://www.apache.org/logos/res/thrift/thrift.png)](https://thrift.apache.org/)
Apache Thrift allows you to define data types and service interfaces in a simple definition file. Taking that file as input, the compiler generates code to be used to easily build RPC clients and servers that communicate seamlessly across programming languages. Instead of writing a load of boilerplate code to serialize and transport your objects and invoke remote methods, you can get right down to business.

## Installation of apache-thrift 
```
sudo apt-get install libboost-dev libboost-test-dev libboost-program-options-dev libevent-dev automake libtool flex bison pkg-config g++ libssl-dev
wget http://apachemirror.wuchna.com/thrift/0.12.0/thrift-0.12.0.tar.gz
tar -xvzf thrift-0.12.0.tar.gz
cd thrift-0.12.0
./configure
make
sudo make install  
```
If any error occurs solve the dependency problem and `sudo make install` again until it is solved and installed
### Thrift version
```
thrift --version
```
