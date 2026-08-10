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
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0
    dut._log.info("Count up")
    dut.ui_in.value = 0b11
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 1
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 2
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 3
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 4
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 5
    dut._log.info("Hold")
    dut.ui_in.value = 0b01
    await ClockCycles(dut.clk, 3)
    assert dut.uo_out.value == 5
    dut._log.info("Count down")
    dut.ui_in.value = 0b10
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 4
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 3
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 2
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 1
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0
    dut._log.info("Underflow wraps to 15")
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 15
    dut._log.info("Reset again")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0
