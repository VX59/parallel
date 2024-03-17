from protocol import Client
import sys
import time   

import numpy as np

if __name__ == "__main__":
    args = sys.argv

    address = sys.argv[1]
    port = int(sys.argv[2])

    test = Client(address,port)

    hostname = "rsenic-750-160qe"
    test.join_network(hostname,11030)
    time.sleep(1)
    print("contact", test.contact)

    module_name = "test"

    #test.upload_module(module_name)
    test.load_module(module_name)