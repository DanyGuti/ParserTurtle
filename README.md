# Parser turtle by Daniel Gutiérrez <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python logo" width="60" height="60" style="float:right; margin-right:3%;">
   
Parser of turtle python algorithm (descent recursive)

## About

ParserTurtle is a Python project that parses turtle graphics commands using a descent recursive algorithm. 

## Usage

To use ParserTurtle, simply run the `ParserTurtle.py` with strings in `testCases.txt` containing the commands I implemented:
1. `md` Move upwards, followed by a number in the range: `1-9`
2. `ma` Move downards, followed by a number in the range: `1-9`
3. `mr` Turn to the right
4. `ml` Turn to the left
5. `lr` To raise the OVNI and not write
6. `br` To lower the OVNI and write
7. `repetir number[command number]` To repeat certain commands
8. `cc` to change colors, followed by a color :
- ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `rojo`
- ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) `verde`
- ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) `azul`
- ![#FFA433](https://via.placeholder.com/15/FFA433/000000?text=+) `naranja`
- ![#860DE1](https://via.placeholder.com/15/860DE1/000000?text=+) `morado`
- ![#FFF200](https://via.placeholder.com/15/FFF200/000000?text=+) `amarillo`
- ![#95724D](https://via.placeholder.com/15/95724D/000000?text=+) `cafe`
- ![#10F7E9](https://via.placeholder.com/15/10F7E9/000000?text=+) `cyan`

9. `ct` to Center and Clear your window
10. `0` to close the window and finish
