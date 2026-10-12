<img width="1563" height="1026" alt="Screenshot 2026-10-12 at 4 51 22 AM" src="https://github.com/user-attachments/assets/53cdb34c-b60b-4788-89b2-5796013c21a6" />

# Blender Macropad

Custom 12 key macropad with rotary encoder and OLED display, designed for better Blender workflow. Made for Half Life PCB project.

## What is this

I am learning Blender and I have a TKL keyboard (no numpad), so viewport navigation is painful. This macropad gives me numpad keys (0-9, dot, enter) for viewport shortcuts, a rotary encoder for zooming/volume control and an OLED display for showing playing audio/telemetry

## Hardware

- 12x Cherry MX compatible switches in 4x3 grid
- EC11 rotary encoder with push button
- 2.08" SH1122 OLED display (SPI)
- Pro Micro RP2040 (TENSTAR clone, mounted on back side, parts facing out)
- 3D printed case (designed separately)

## How it works

Keys are wired in a 4x3 matrix with 1N4148 diodes which prevents ghosting (details in JOURNAL.md). The Pro Micro scans rows and columns to detect which key is pressed. Encoder uses two signal lines with 10k pullup resistors. OLED connects over SPI (5 pins).

Firmware runs KMK (keyboard focused layer). Bindings are fully customizable in code.py. OLED driver for SH1122 is not yet available in KMK, commented out in code for now.

## Board

- Size: 98 x 99.2mm (2 layer, under JLCPCB 100x100 cheap limit)
- 4x M3 mounting holes
- Pro Micro USB-C aligns with top edge
- Diode direction: ROW2COL

## Pin mapping

- Rows: GP2, GP3, GP4
- Columns: GP5, GP6, GP7, GP8
- Encoder: GP27 (A), GP28 (B), GP29 (click)
- OLED: GP22 (CLK), GP23 (MOSI), GP21 (CS), GP20 (DC), GP26 (RST)
- Power: 3V3 to VCC, all GND to GND

## Build

1. Order PCB from JLCPCB using gerber files in /gerbers
2. Solder diodes, resistors, MX switches, encoder, pin headers
3. Mount Pro Micro on back side (parts facing out, check TX0/RAW marking on silkscreen)
4. Flash CircuitPython on Pro Micro RP2040
5. Copy code.py and KMK library to the board
6. Print case (STL in /case when available)
