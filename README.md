# solo-chess-solver

Solve chess.com's [Solo-Chess puzzles](https://www.chess.com/solo-chess) using a new recursive-backtracking algorithm.

## Introduction

This script uses basic backtracking to test combinations of moves that reach a specific goal.

### Solo-Chess

Solo-Chess is a type of chess puzzle with simple rules. The end goal is a position with only one piece left, achieved through these rules.

- Each move made must be a capture
- No piece can capture more than two pieces
- If there is a king on the board, it must be the final piece

The puzzles can become extremely complex extremely quickly, hence the inspiration of the program.

### Basic Example

<img src="https://i.imgur.com/6Ap1u9k.png" width=500></src>

Here, the solution is

- Kxf2
- Kxe2

### Complex Example

<img src="https://imgur.com/w7c7h1S.png" width=500></src>

The solution isn't as easy this time.

## Usage

`main.py` contains the algorithm. Just fire it up with `utils.py` in the same directory and you'll have to input the number of pieces (`n`) on the board.

Then, for the next `n` lines, you will have to input the pieces in this format.

`[Piece] [Square]`

where piece is the symbol for the piece:

```
K => king
Q => queen
R => rook
B => bishop
N => knight
P => pawn
```

Example:

```
Enter number of pieces: 3
Input the 3 pieces on the following lines using this format: [Piece] [Square]
Example: K g2
K g1
R f2
B e2
```

Hit `Enter` after the last piece and wait for the sequence of moves to be outputted.

The output is in the format

```
[Piece] [FromSquare] [ToSquare]
```

For example, a King move from g3 to g4 would be indicated by `K g3 g4`

Longer example:

```
---
R b8 b3
R b3 a3
R a7 a3
R a3 d3
Q a1 g1
Q g1 d4
Q h7 d3
Q d3 d4
Q d7 d4
Q d4 f4
---
```

## Contact

For questions or suggestions, contact me [here](mailto:leon.rode13@gmail.com) or on Discord at <strong>lionrocker#3960</strong>.

## License

This program is released under the GNU GPL v3 License. More information can be found in the LICENSE file.
