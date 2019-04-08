import os
import socket
import threading
import re
import numpy as np
import ast

userResponse = 0

def retrFile(name,s):
    userResponse = s.recv(1024).decode('utf-8')
    if userResponse[:2] == '1':
        print("Calculate_pi operation :")
        pi_value = 22.0/7.0
        str_pi=str(pi_value)
        s.send(str_pi.encode('utf-8'))

    elif userResponse[:2] == '2':
        print("Add operation for 2 input parameters :")
        s.send("OK".encode('utf-8'))
        print("Addition Parameters received :")
        recv1 = s.recv(1024).decode('utf-8')
        print(recv1)
        inp1 = recv1.split(" (")
        #print(inp1)
        inp2=inp1[1].split(",")
        #print(inp2)sort (4,2,1)
        inp3=inp2[1].split(")")
        #print(inp3)
        add=int(inp2[0])+int(inp3[0])
        print(add)
        add_no = str(add)
        print("Addition operation is completed!!!")
        s.send(add_no.encode('utf-8'))

    elif userResponse[:2] == '3':
        print("Sort operation for input array :")
        s.send("OK".encode('utf-8'))
        print("Array of elements received :")
        recv2 = s.recv(1024).decode()
        print(recv2)
        inp4=re.split('[( )]',recv2)
        print(inp4)
        inp5 = inp4[1].split(",")
        print(inp5)
        str1=" ".join(str(x) for x in inp5)
        arr_list = str1.split(' ')
        print(arr_list)
        arr_list.sort()
        print(arr_list)
        arr_new = str(arr_list)
        print("Sorted array is completed!!!")
        s.send(arr_new.encode())

    elif userResponse[:2] == '4':
        print("Matrix operation on Server :")
        s.send("OK".encode('utf-8'))
        recva = s.recv(1024)
        print("Matrix_A received"+recva)
        inp4 = recva.replace("'", "")
        print(inp4)
        print(type(inp4))
        recvb = s.recv(1024)
        print("Matrix_B received" + recvb)
        inp5 = recvb.replace("'", "")
        print(inp5)
        print(type(inp5))
        recvc = s.recv(1024)
        print("Matrix_C received" + recvc)
        inp6 = recvc.replace("'", "")
        print(inp6)
        print(type(inp6))
        mat_a= ast.literal_eval(inp4)
        mat_b = ast.literal_eval(inp5)
        mat_c = ast.literal_eval(inp6)
        print("Matrix multiplication result : ")
        print(np.matmul(np.matmul(mat_a,mat_b),mat_c))
        mat_new = str(np.matmul(np.matmul(mat_a,mat_b),mat_c))
        print("Matrix multiplication is completed!!!")
        s.send(mat_new)


def Main():
    host = '127.0.0.1'
    port = 5050

    # Creating a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))

    # Server listening for connections
    s.listen(5)
    print("Server started, waiting for client to accept request")
    while True:
        # Get the connection socket
        c, addr = s.accept()
        print ("Client connected to ip:<", str(addr), ">")
        t = threading.Thread(target=retrFile, args=("retrThread", c))
        # Starting thread
        t.start()

    s.close()

if __name__ == '__main__':
    Main()