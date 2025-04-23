import struct

# A 32-entry register file. 
# A register file is a list of 32 integers, each representing a register.
# The first entry, regfile[0], is hardwired to 0.
regfile = [0] * 32

# A 32-entry instruction memory.
# An instruction memory is a list of 32 integers, each representing an instruction.
# The first entry, imem[0], is hardwired to 0.
imem = [0] * 32