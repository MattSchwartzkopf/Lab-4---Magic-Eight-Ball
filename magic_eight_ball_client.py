"""magic_eight_client.py

TODO -- complete header docstring

Champlain College CSI-235, Spring 2018
This code builds off skeleton code written by 
Prof. Joshua Auerbach (jauerbach@champlain.edu)
"""



import socket
import argparse
import time

TEST_QUESTIONS = [b'Am I awesome?', b'Will I pass this class?', 
                  b'Will a single threaded server suffice?']

class EightBallClient:
    def __init__(self, host, port):
        self.socket = socket.getaddrinfo(host, port, flags=socket.AI_ADDRCONFIG | socket.AI_V4MAPPED)
        self.socket.connect((host, port))
        self.stored = b''
        # Not sure if getaddrinfo is working properly ATM

    def close(closer):
        closer.socket.close()

    def recv_until_delimiters(self, delimiters, buffer_size=1024) :
        words = self.stored
        
        while delimiters not in words:
            words += self.socket.recv(buffer_size)
            
        fields = words.split(byte, 1)
        self.stored = fields[1]
        # NEED TO RETURN A BYTE STRING
        return(fields[0])
        
    def ask_question(self, question):
        self.socket.send(question)
        recv_next_response(question)
        return question
    
    def recv_next_response(self):
        # Needs to call recv_until_delimiters until next response
        recv_until_delimiters(self, self.stored, 1024)


def run_interactive_client(host, port):
    userInput = raw_input("Ask a question: ")
    question_mark = userInput.split()
    question_mark_counter = 0
    
    for i in range(len(question_mark)):
        if(question_mark[i].__contains__("?"))
            question_mark_counter += 1
    while(question_mark_counter == 0 or question_mark_counter > 1):
        question_mark_counter = 0
        userInput = raw_input("Ask a question: ")
        if(question_mark_counter == 1):
            break
    ask_question(userInput)
    
def run_single_test_client(host, port):
    pass

def test(host, port, workers):
    pass
        
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example client')
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=7000,
                        help='TCP port (default 7000)')
    parser.add_argument('-t', action='store_true', help='test mode')
    parser.add_argument('-n', metavar='num threads', type=int, default=4,
                        help='Num threads for test mode')
    args = parser.parse_args()
    if args.t:
        test(args.host, args.p, args.n)
    else:
        run_interactive_client(args.host, args.p)
