# Socket Programming

## Introduction
A way of communication between clients in Python.

## What is a socket?
A socket is the end point of communications between processes on a computer network, such as the internet.<br>
It can be described as a programming interface allowing a program to communicate with other programs or processes,<br>
on the internet or locally.<br>
### Socket Address
A socket address the combination of an IP address and a port number.<br>
e.g.<br>
IP address # 123.132.213.231<br>
Port # 8080<br>
<b>Socket address # 123.132.213.231 : 8080</b>
### Socket in Python
```python
import socket
s = socket.socket(socketfamily.sockettype.protocol=0)
```
<b>socketfamily</b> : Represents the address (and protocol) family. It can either be AFUNIX or AFINET.<br>
<b>sockettype</b> : Represents the socket type, and can either be SOCKSTREAM or SOCKDGRAM.<br>
<b>protocol</b> : This is an optional argument and it usually defaults to 0.<br>
<i>Further code for creating and using sockets in .py files</i>

## Network & Internet
<b>Network</b> : A computer network is a group of computer systems and other computing hardware devices that are<br>
 linked together through communication channels.<br>
 <b>Network Computer</b> : A computer that is connected with one or more other computers.<br>
 <b>Network Types</b> : 
 * Local Area Network (LAN) : A network that is confined to a relatively small area. Commonly have quick transfer speeds.
 * Wide Area Network (WAN) : Covers a big geographical area such as a city or country or even the world. (Global Network)
 * Metropolitan Area Network (MAN) : A network whose range lies between LAN and WAN.
 
 <b>Hosts</b> : A computer of other device that communicates with other hosts on a network. It is a computer that is<br>
 accessible over a network. It can be a client, server, or any other type of computer. Each host has a unique identifier<br>
 called a hostname that allows other computers to access it.<br>
 <b>Server</b> : A server is a physical computer dedicated to providing services to serve the needs of other computers.<br>
 A server is also called a "remote computer".<br>
 <b>Clients</b> : A client is a computer hardware device or software that accesses a service made available by a server.<br>
 <b>End Systems</b> : The devices or the computing systems connected to the computer network are sometimes referred to as<br>
 end systems. So called because they sit at the edge of the computer network and are operated by an end user.<br>
 These are usually connected together by a network of communication links and packet switches.<br>
 End systems are things such as email servers, workstations, web servers, TVs, phones, etc.<br>
 <b>Protocol</b> : Two hosts communicate with each other over a network using a protocol. <br>
 Network protocols include mechanisms for devices to identify and make connections with each other, as well as formatting rules.<br>
 Protocols are needed for security purposes. They specify interactions between the communicating devices.<br>
 Types of protocols:<br>
 * HTTP
 * FTP 
 * Ethernet
 * Simple Mail Transfer Protocol
 * Internet Message Access Protocol
 * Post Office Protocol
 * <b>Transmission Control Protocol/Internet Protocol (TCP)
 * User Datagram Protocol (UDP)</b>
 
 <b>IP Address</b> : A way of identifying destinations and origins when sending data across a network, similar to a street address.<br>
 
 ## TCP vs UDP
<b>TCP</b> is a transport layer protocol and is used to create a connection between remote computers by transporting and ensuring the delivery of messages<br>
over supporting networks and the internet.</br>
For faster and security compromised connections we use UDP.<br>
<b>UDP</b> does not need an ACK signal (Acknowledgment signal) in many cases. Speed is considered more important that security.<br>
So UDP compromises on security but is far faster than TCP. It is an unreliable service which does not guarantee delivery and no protection.<br>
It does not retransmit lost packets like TCP does. Good for real-time performance.<br>

 
 
