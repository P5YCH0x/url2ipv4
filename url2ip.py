##!/usr/bin/env python3
import socket

def convert(url):
    ip = socket.gethostbyname(url)
    return ip

def main():
    url = str(input("input the url you want to convert(www.google.com): "))
    ip = convert(url)
    print(ip)

if __name__ == "__main__":
    main()
