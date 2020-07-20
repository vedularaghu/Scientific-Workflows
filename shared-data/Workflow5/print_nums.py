#!/usr/bin/env python3
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3
import sys
import argparse
import os
import signal
import sys
import time
import traceback

from pathlib import Path

def parse_args(args):
    parser = argparse.ArgumentParser(
            description="A")
    parser.add_argument(
        "num_iterations",
        type=int,
        help="number of iterations (seconds to run for)"
    )
    return parser.parse_args()

if __name__=="__main__":
    args = parse_args(sys.argv[1:])
    CHECKPOINT_FILE = "saved_stated.txt"
    NUM_ITERATIONS = args.num_iterations
    
    i = 0
    try:
        try:
            with open(CHECKPOINT_FILE, mode="r") as f:
                i = int(f.read())
                if i == 0:
                    i = 1
                    print("placed holder file: {} found, starting with i = 0".format(CHECKPOINT_FILE))
                else:
                    print("{} found, starting with i = {}".format(CHECKPOINT_FILE, i))
        except FileNotFoundError as e:
            print("{} not found, starting with i = 0".format(CHECKPOINT_FILE))

        def SIGTERM_handler(signum, frame):
            print("Signal: {} received, writing checkpoint file with state {} to {}".format(
                    signum, i, CHECKPOINT_FILE
                ))

            with open(CHECKPOINT_FILE, mode="w") as f:
                f.write(str(i))

        # set handler
        signal.signal(signal.SIGTERM, SIGTERM_handler)

        # start computation 
        print("pid: {}".format(os.getpid()))
        for _ in range(NUM_ITERATIONS+1):
            print(i)

            if i == NUM_ITERATIONS:
                break

            i += 1
            time.sleep(1)
    except Exception as e:
        traceback.print_exc()
    finally:
        with open(CHECKPOINT_FILE, mode="w") as f:
            f.write(str(i))
            
        print("writing checkpoint file: {} with state {}".format(CHECKPOINT_FILE, i))
    

