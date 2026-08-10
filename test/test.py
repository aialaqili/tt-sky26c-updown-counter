# SPDX-FileCopyrightText: (c) 2026 Abdulla Alaqili
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 2)
    assert dut.uo_out.value == 0
    dut._log.info("Count up")
    dut.ui_in.value = 0b11
    await ClockCycles(dut.clk, 2)
    start = int(dut.uo_out.value)
    await ClockCycles(dut.clk, 1)
    assert int(dut.uo_out.value) == (start + 1) & 0xF
    await ClockCycles(dut.clk, 1)
    assert int(dut.uo_out.value) == (start + 2) & 0xF
    await ClockCycles(dut.clk, 1)
    assert int(dut.uo_out.value) == (start + 3) & 0xF
    dut._log.info("Hold")
    dut.ui_in.value = 0b01
    await ClockCycles(dut.clk, 2)
    held = int(dut.uo_out.value)
    await ClockCycles(dut.clk, 3)
    assert int(dut.uo_out.value) == held
    dut._log.info("Count down")
    dut.ui_in.value = 0b10
    await ClockCycles(dut.clk, 2)
    start2 = int(dut.uo_out.value)
    await ClockCycles(dut.clk, 1)
    assert int(dut.uo_out.value) == (start2 - 1) & 0xF
    await ClockCycles(dut.clk, 1)
    assert int(dut.uo_out.value) == (start2 - 2) & 0xF
    await ClockCycles(dut.clk, 1)
    assert int(dut.uo_out.value) == (start2 - 3) & 0xF
    dut._log.info("Reset again")
    dut.ui_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 2)
    assert dut.uo_out.value == 0
    dut._log.info("Test complete")
    
