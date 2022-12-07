from pathlib import Path
from typing import List
import re
from collections import deque



class StreamReader:
    def __init__(self, packet_marker = 4):
        self.idx = 0
        self.buffer = deque()
        self.packet_marker = packet_marker

    def read_char(self, c):
        # Not enough characters to sync
        if len(self.buffer) < self.packet_marker:
            self.buffer.append(c)
            self.idx += 1
            return 0

        result = 0

        # Hey, it's constant time ;D
        if len(set([i for i in self.buffer])) == self.packet_marker:
            result = self.idx

        self.buffer.popleft()
        self.buffer.append(c)
        self.idx += 1
        return result 


if __name__ == "__main__":
    input_file = Path("../input/input_6.txt")

    result_1 = 0
    result_2 = 0

    with open(input_file, 'r') as f:
        reader_1 = StreamReader(packet_marker = 4)
        reader_2 = StreamReader(packet_marker = 14)
        result_1 = 0
        result_2 = 0
        result_1_read = False
        result_2_read = False

        for idx, line in enumerate(f):
            for c in line:
                if not result_1:
                    result_1 = reader_1.read_char(c)
                    
                if not result_2:
                    result_2 = reader_2.read_char(c)

                if not result_1_read and result_1:
                    print(f"Result 1: {result_1}")
                    result_1_read = True

                if not result_2_read and result_2:
                    print(f"Result 2: {result_2}")
                    result_2_read = True
