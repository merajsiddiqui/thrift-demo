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

## Demo Project Description
> I am assuming that you know what Apache Thrift is and why to use it. Here my focus is on how to do it.

I am developing two micro services. One of micro-service will expose some functions or service to be used by another micro service. The two micro services can be in same or different language as well as on same or diffrent machine. For this demonstartion
  - MicroService `service-py` in Python 
  - MicroService `service-node` in Node.JS

### Thrift File
Thrift is `IDL` (Interface Definition Language) which holds the definition of exposed functions and services and their respective data types. This file will be used to generate codes. Extension of file is `.thrift`

> For this project we have defined `demo.thrift`
Compiling thrift IDL code and Generating codes in desired languages 
```
cd service-py
thrift -gen py ../demo.thrift 
cd service-node
thrift -gen js:node ../demo.thrift 
```
> All the generated codes will be in folder `gen-{language}` renamed to `gen_py` for `gen-py` other wise it will throw error in python