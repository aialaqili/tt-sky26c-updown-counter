/*
* Copyright (c) 2026 Abdulla Alaqili
* SPDX-License-Identifier: Apache-2.0
*/

`default_nettype none

module tt_um_aialaqili_updown_counter (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire ena,
    input  wire clk,
    input  wire rst_n
);

    wire direction = ui_in[0];
    wire count_en = ui_in[1];
    reg [3:0] count;

    always @(posedge clk) begin
        if (!rst_n) begin
            count <= 4'd0;
        end else if (count_en) begin
            if (direction)
                count <= count + 4'd1;
            else
                count <= count - 4'd1;
        end
    end

    assign uo_out = {4'b0000, count};
    assign uio_out = 8'b0;
    assign uio_oe = 8'b0;

    wire _unused = &{ena, ui_in[7:2], uio_in, 1'b0};

endmodule
