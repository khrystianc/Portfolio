import random
import time

if __name__ == '__main__':

    while True:                           # while true
        time.sleep(1.0)                   # sleep for one second

        f = open("PRNG_service.txt", "r") # open prng_service.txt
        line = f.readline()               # read file
        
        if not line:
            continue
        
        if line == "run\n":               # If line in file is “run”:
            print("Generating random integer...") # Generate random number 
            # Erase “run” from prng-service.txt
            f = open("PRNG_service.txt", "w") # Write random number in to prng-service.txt
            f.write(f"{random.randint(0, 99999999)}\n")
            f.close()                         # Close file 

