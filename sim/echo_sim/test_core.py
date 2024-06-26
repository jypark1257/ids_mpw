# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

# test_my_design.py (simple)

import os
import random
from pathlib import Path
import cocotb
from cocotb.clock import Clock
from cocotb.runner import get_runner
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge
from cocotb.triggers import Timer
from cocotb.types import LogicArray
@cocotb.test()
async def core_bench(dut):

    dut.i_rst_n.value = 0
    # memory initialization

    imem_path = "../../software/echo_bios/echo_bios.hex"

    # Create a 10ns period clock on port clk
    clock = Clock(dut.i_clk, 10, units="ns")  
    # Start the clock. Start it low to avoid issues on the first RisingEdge
    cocotb.start_soon(clock.start(start_high=False))

    await RisingEdge(dut.i_clk)
    await Timer(1, units="ns")
    for idx in range (0, 256):
        dut.top.imem_0.imem_sram.mem[idx].value = 0
        dut.top.dmem_0.dmem_sram.mem[idx].value = 0
    await RisingEdge(dut.i_clk)
    await Timer(1, units="ns")

    # dmem_path = "/home/pjy-wsl/rv32i/dmem.mem"
    with open(imem_path, "r") as mem:
        first_line = mem.readline()
        idx  = 0
        for line in mem:
            inst = line.strip()  # Remove leading/trailing whitespaces and newline characters
            inst_decimal = int(inst, 16)
            mux_addr = idx & 0x00000003     # 2-bit
            row_addr = (idx & 0x000003fc) >> 2     # 8-bit
            if idx < 1024:
                data =  dut.top.imem_0.imem_sram.mem[row_addr].value
                data = data | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                data = data | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                data = data | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                data = data | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                data = data | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                data = data | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                data = data | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                data = data | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                data = data | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                data = data | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                data = data | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                data = data | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                data = data | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                data = data | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                data = data | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                data = data | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                data = data | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                data = data | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                data = data | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                data = data | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                data = data | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                data = data | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.top.imem_0.imem_sram.mem[row_addr].value = data
            else:
                ddata =  dut.top.dmem_0.dmem_sram.mem[row_addr].value
                ddata = ddata | (((inst_decimal & 0x00000001) >> 0)  << ( 0*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000002) >> 1)  << ( 1*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000004) >> 2)  << ( 2*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000008) >> 3)  << ( 3*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000010) >> 4)  << ( 4*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000020) >> 5)  << ( 5*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000040) >> 6)  << ( 6*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000080) >> 7)  << ( 7*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000100) >> 8)  << ( 8*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000200) >> 9)  << ( 9*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000400) >> 10) << (10*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00000800) >> 11) << (11*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00001000) >> 12) << (12*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00002000) >> 13) << (13*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00004000) >> 14) << (14*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00008000) >> 15) << (15*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00010000) >> 16) << (16*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00020000) >> 17) << (17*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00040000) >> 18) << (18*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00080000) >> 19) << (19*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00100000) >> 20) << (20*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00200000) >> 21) << (21*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00400000) >> 22) << (22*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x00800000) >> 23) << (23*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x01000000) >> 24) << (24*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x02000000) >> 25) << (25*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x04000000) >> 26) << (26*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x08000000) >> 27) << (27*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x10000000) >> 28) << (28*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x20000000) >> 29) << (29*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x40000000) >> 30) << (30*4  + mux_addr))
                ddata = ddata | (((inst_decimal & 0x80000000) >> 31) << (31*4  + mux_addr))
                dut.top.dmem_0.dmem_sram.mem[row_addr].value = ddata
            await RisingEdge(dut.i_clk)
            idx = idx + 1

    await Timer(1, units="ns")
    dut.i_rst_n.value = 1
    dut.data_out_ready.value = 0

    for _ in range(5):
        await RisingEdge(dut.i_clk)
        await Timer(1, units="ns")

    done = 0

    #while True:
    #    if dut.data_in_ready.value == 1:
    #        print("SEND: ", end="")
    #        data = input()
    #        dut.data_in.value = ord(data)
    #        dut.data_in_valid.value = 1
    #        await RisingEdge(dut.i_clk)
    #        await Timer(1, units="ns")
    #        dut.data_in.value = 0
    #        dut.data_in_valid.value = 0
    #        break
    #        
    #    else:
    #        await RisingEdge(dut.i_clk)
    #        await Timer(1, units="ns")

    for _ in range(10):
        while True:
            if dut.data_out_valid.value == 1:
                print(chr(int(dut.data_out.value.binstr,2)), end="")
                dut.data_out_ready.value = 1
                await RisingEdge(dut.i_clk)
                await Timer(1, units="ns")
                dut.data_out_ready.value = 0
                break
            else:
                await RisingEdge(dut.i_clk)
                await Timer(1, units="ns")
    print("")
    for _ in range(10):
        while True:
            if dut.data_out_valid.value == 1:
                print(chr(int(dut.data_out.value.binstr,2)), end="")
                dut.data_out_ready.value = 1
                await RisingEdge(dut.i_clk)
                await Timer(1, units="ns")
                dut.data_out_ready.value = 0
                break
            else:
                await RisingEdge(dut.i_clk)
                await Timer(1, units="ns")
    print("")
    for _ in range (5):
        await RisingEdge(dut.i_clk)
        await Timer(1, units="ns")
