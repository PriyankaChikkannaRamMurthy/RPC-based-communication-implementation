import os
import sys
import socket
import numpy as np

def Calculate_PI(s):
    print("Calculate_PI Operation")
    s.send("1".encode('utf-8'))
    pi_data = s.recv(1024).decode('utf-8')
    print(pi_data)


def ADD(s):
    print("ADD Operation:")
    s.send("2".encode('utf-8'))
    serv1=s.recv(1024).decode('utf-8')
    if(serv1 == "OK"):
        in1 = raw_input("Enter the first input parameter: ")
        in2 = raw_input("Enter the second input parameter: ")
        add_opr=str("add"+" ("+in1+ "," + in2+")")
        print(add_opr)
        s.send(add_opr.encode('utf-8'))
        add_data = s.recv(1024).decode('utf-8')
        print("Addition operation computation result received from server :")
        print(add_data)
    else:
        print("Error!")


def Sort(s):
    print("Sort Operation")
    s.send("3".encode('utf-8'))
    serv1 = s.recv(1024)
    if (serv1 == "OK"):
        n = raw_input("Enter the no of elements to be sorted: ")
        arr = []
        for i in range(int(n)):
            arr.append(raw_input("Enter the elements to be sorted: "))
        print(arr)
        arr_str = "sort" + "("+",".join([str(i) for i in arr])+")"
        print(arr_str)
        print("Array elements passing to the server for computation...")
        s.send(arr_str.encode())
        arr_data = s.recv(1024).decode()
        print("Sorted Array computation result received from server :")
        print(arr_data)
    else:
        print("Error!")



def Matrix_Multiply(s):
    print("Matrix_Multiply Operation")
    s.send("4".encode('utf-8'))
    serv1 = s.recv(1024)
    print("Matrix_A")
    mra = int(raw_input("Enter the number of rows in a matrix: "))
    mca = int(raw_input("Enter the number of cols in a matrix: "))
    sa = [[0 for i in range(mca)]for j in range(mra)]
    print(sa)
    #sa = [[0] * mca for i in range(mca)]
    for i in range(0,mra):
        for j in range(0,mca):
            sa[i][j] = raw_input()
    matrix_a=np.matrix(sa)
    print(matrix_a)
    str_a=np.array2string(matrix_a, precision=0, separator=',', suppress_small = True)
    print(str_a)
    s.send(str_a)

    print("Matrix_B")
    mrb = int(raw_input("Enter the number of rows in a matrix: "))
    mcb = int(raw_input("Enter the number of cols in a matrix: "))
    sb = [[0 for i in range(mcb)] for j in range(mrb)]
    print(sb)
    # sa = [[0] * mca for i in range(mca)]
    for i in range(0, mrb):
        for j in range(0, mcb):
            sb[i][j] = raw_input()
    matrix_b = np.matrix(sb)
    print(matrix_b)
    str_b = np.array2string(matrix_b, precision=0, separator=',', suppress_small=True)
    print(str_b)
    s.send(str_b)

    print("Matrix_C")
    mrc = int(raw_input("Enter the number of rows in a matrix: "))
    mcc = int(raw_input("Enter the number of cols in a matrix: "))
    sc = [[0 for i in range(mcc)] for j in range(mrc)]
    print(sc)
    # sa = [[0] * mca for i in range(mca)]
    for i in range(0, mrc):
        for j in range(0, mcc):
            sc[i][j] = raw_input()
    matrix_c = np.matrix(sc)
    print(matrix_c)
    str_c = np.array2string(matrix_c, precision=0, separator=',', suppress_small=True)
    print(str_c)
    s.send(str_c)
    matrix_data = s.recv(1024)
    print("Matrix Multiplication computation result received from server: ")
    print(matrix_data)


def Main():
    host = '127.0.0.1'
    port = 5050

    # Creating a socket
    s = socket.socket()
    s.connect((host,port))
    print("RPC based Communication System\n")
    option = raw_input("Select an option to perform one of the following:\n 1.Calculate_PI\n 2.ADD\n 3.Sort\n 4.Matrix_Multiply\n")
    if option == '1':
        Calculate_PI(s)
    elif option == '2':
        ADD(s)
    elif option == '3':
        Sort(s)
    elif option == '4':
        Matrix_Multiply(s)
    else:
        s.close()
        sys.exit(0)

if __name__ == '__main__':
    Main()