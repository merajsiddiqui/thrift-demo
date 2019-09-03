# Namespace are used to craete a folder in gen-py or gen-nodejs where auto generated code will be stored
namespace py UserService
namespace js UserService

/**
* typedef is used to define data type so instead of i32 i can use integer, while i32 is the data type supported in thrift
*/
typedef i32 integer

/**
* Defining struct when I need complex data instead of single data type like integer, boolean or string
*/
struct User {
    1: string name,
    2: integer id,
    3: bool active
}

/**
* Defining exception which will be raised by  Serving Micro service
*/
exception InvalidUser {
    1: string message
}

/**
* Defined a a service MicroService1 which holds getUser method. So getUser method will be defined in one micro-service and will be called by another micro-service
* getUser method returns data of type User defined above
* It excepts 1 argument id which is integer
* It may throw exception of type InvalidUser
*/
service MicroService1 {
    User getUser(1: integer id ) throws (1:InvalidUser ouch)
}

// For more understanding of how to write thrift file visit apache thrift website https://thrift.apache.org/