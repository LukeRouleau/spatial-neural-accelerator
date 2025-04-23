# spatial-neural-accelerator
A mock spatial neural accelerator with a grid of RISC-V cores around GEMV machines. Designed to wrap my head around spatial architectures.

## Project Overview
This project aims to develop a mocked (Python-modeled) spatial neural accelerator based on a specialized hardware architecture with RISC-V cores and processing elements organized in a grid structure.

## Hardware Architecture
The accelerator architecture features:
- 728 memory banks, each with dual RISC-V processor cores
- 512 processing elements (PEs) per bank arranged in 8 rows of 64 PEs
- SIMD processing within rows, MIMD across banks
- Bespoke network-on-chip (NoC) for East/West and North/South communication
- I/O interfaces including LPDDR4x/5 and PCI-Express Gen5

## Plan of Action

### Phase 1: Core Components (Python)
1. Implement basic RISC-V core simulator based on George Hotz's [twitchcore](https://github.com/geohot/twitchcore) or Anton Lydike's [riscemu](https://github.com/antonlydike/riscemu)
   - Support for standard RISC-V instructions
   - Add custom instructions for at-memory architecture
2. Model Processing Element (PE)
   - Implement MAC logic with masking capabilities
   - Model SRAM arrays (64x80 = 640 bytes per PE)
   - Implement register structure (A-Register, C-Register, T-Register)
3. Develop row controller simulation
   - Command queue execution
   - SIMD operation across 64 PEs

### Phase 2: Network and Communication
1. Implement Rotator Cuff for intra-row communication
   - Nearest neighbor connectivity
   - Support rotation patterns
2. Model Network-on-Chip (NoC)
   - E/W and N/S communication channels
   - Socket-based communication system
   - Packet routing between non-aligned rows
3. Simulate PCM (PBus Communication Managers)
   - Interface with NoC
   - I/O ring connectivity

### Phase 3: Memory System
1. Model memory bank structure (328KB SRAM per bank)
2. Implement LPDDR interface simulation
3. Design scratchpad memory access

### Phase 4: Integration and Testing
1. Integrate all components into a cohesive system
2. Develop test suite for validating operation
3. Implement simple neural network operations
4. Benchmark performance and identify bottlenecks

### Phase 5: Optimization and Extensions
1. Optimize the Python implementation
2. Explore C++ implementation for performance
3. Consider Rust implementation for memory safety and concurrency
4. Compare performance across implementations

### Phase 6: Documentation and Visualization
1. Create detailed documentation of the architecture
2. Develop visualization tools for system operation
3. Generate performance analysis reports

## Extensions
- C++ implementation for improved performance
- Rust implementation for memory safety and concurrency
- Hardware description language (HDL) implementation for FPGA testing
- Integration with popular machine learning frameworks

## Recommended Prerequisites
### RISCV Comprehension
1. Ch. 1 of the [RISCV ISA](./docs/riscv/unpriv-isa-asciidoc.pdf)
2. George Hotz "Twitchcore" stream

### Principles of a Spatial Architecture
Read my blog post summarizing my intuition on the spatial architecture that we will be emulating here:
- [ ](https://lukerouleau.com/blog/)