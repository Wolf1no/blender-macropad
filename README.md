<img width="1197" height="643" alt="Screenshot 2026-10-12 at 1 20 19 AM" src="https://github.com/user-attachments/assets/6361f233-d3f8-461d-9d3a-ae043af83765" />

# Blender Macropad

Custom 12 key macropad with rotary encoder and OLED display, designed for better Blender workflow. Made for Half Life PCB project.

## What is this

I am learning Blender and I have a TKL keyboard (no numpad), so viewport navigation is painful. This macropad gives me numpad keys (0-9, dot, enter) for viewport shortcuts, a rotary encoder for zooming/volume control and an OLED display for showing playing audio/telemetry

## Hardware

- 12x Cherry MX compatible switches in 4x3 grid
- EC11 rotary encoder with push button
- 2.08" SSD1322 OLED display (SPI)
- Pro Micro RP2040 microcontroller
- 3D printed case (designed separately)

## How it works

Keys are wired in a 4x3 matrix with 1N4148 diodes which prevents ghosting (details in JOURNAL.md). The Pro Micro scans rows and columns to detect which key is pressed. Encoder uses two signal lines with 10k pullup resistors. OLED connects over SPI (5 pins).

Firmware runs KMK (keyboard focused layer). Bindings are fully customizable in code.py.

## Pin mapping

- Rows: GP6 GP7, GP8
- Columns: GP2, GP3, GP4, GP5
- Encoder: GP10 (A), GP11 (B), GP12(click)
- OLED: GP15 (RST), GP16 (DC), GP17 (CS), GP18 (CLK), GP19 (MOSI)

## Build

1. Order PCB from JLCPCB using gerber files in /gerbers
2. Solder diodes, resistors, MX switches, encoder, pin headers
3. Flash CircuitPython on Pro Micro RP2040
4. Copy code.py and KMK library to the board
5. Print case (STL in /case when available)
