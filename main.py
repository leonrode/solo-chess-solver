import chess
import utils
# create an empty board
board = chess.Board(None)

numberOfPieces = int(input("Enter number of pieces: "))

pieces = []
kingIsPresent = False
moves = []

print(f"Input the {numberOfPieces} pieces on the following lines using this format: [Piece Letter] [Square]")
print("Example: K g2")

# input pieces
for _ in range(numberOfPieces):
  pieceStr, squareStr = input().split(" ")

  # assign the chess.SQUARE type
  square = chess.parse_square(squareStr)

  # create a piece with the piece type mapped from the letter (ex. B -> bishop, N -> knight)
  piece = chess.Piece(utils.pieceStringToPieceType(pieceStr), chess.WHITE)

  # acknowledging that a king is on the board
  if piece.piece_type == chess.KING: kingIsPresent = True

  # pieces are objects with moves and squares
  pieces.append({"piece": piece, "moveCount": 0, "square": square})

  # setting the internal board's square to the piece
  board.set_piece_at(square, piece)



def solve(remainingPieces, moves):


  # goal case, print the moves they have
  if utils.isFinished(remainingPieces, kingIsPresent):
    print("--")
    for move in moves:

      print(move["piece"]["piece"].symbol(), chess.square_name(move["from"]), chess.square_name(move["to"]))
    print("--")
    # stop finding other solutions and exit
    quit()


  # generate attacks from the current position and pieces
  #generatedAttacks = utils.findAttacks(remainingPieces, board)
  board.turn = False
  generatedAttacks = utils.findAttacks(remainingPieces, board)

  for attack in generatedAttacks:
    # we never will want to attack a king
    if attack["attackedPiece"]["piece"].piece_type != chess.KING:

      # if the piece can actually move, then continue the attack
      if attack["piece"]["moveCount"] < 2:

        # setting up for backtracking
        oldRemainingPieces = remainingPieces.copy()
        oldMoves = moves.copy()

        attackingPiece = attack["piece"]
        attackedPiece = attack["attackedPiece"]

        # removing the attacked piece because it is taken
        remainingPieces.remove(attackedPiece)

        # updating the internal board
        board.remove_piece_at(attackingPiece["square"])

        # set the attacking piece to the square of the attacked piece (taking the piece)
        updatedPiece = attackingPiece.copy()
        fromSquare = updatedPiece["square"]

        # update the position of the piece
        updatedPiece["square"] = attack["attackedSquare"]
        toSquare = updatedPiece["square"]

        # updating the internal board
        board.set_piece_at(attackedPiece["square"], attackingPiece["piece"])

        # increase the move count of the attacking piece
        updatedPiece["moveCount"] += 1

        # the old piece index is the index of the attacking piece as it is guaranteed to be in the list
        oldPieceIndex = remainingPieces.index(attackingPiece)

        # placing the updated piece in position of the old piece
        remainingPieces[oldPieceIndex] = updatedPiece

        newMove = {
          "piece": attackingPiece,
          "from": fromSquare,
          "to": toSquare,
        }

        moves.append(newMove)

        solve(remainingPieces, moves)


        # revert back
        remainingPieces = oldRemainingPieces.copy()
        moves = oldMoves.copy()

        # reverting the internal board
        board.set_piece_at(attackedPiece["square"], attackedPiece["piece"])
        board.set_piece_at(attackingPiece["square"], attackingPiece["piece"])

print("All pieces inputted. Solving...")
solve(pieces, moves)
