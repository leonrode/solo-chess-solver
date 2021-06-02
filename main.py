import chess
import utils
# create an empty board
board = chess.Board("8/8/8/8/8/8/8/8")

numberOfPieces = int(input("Enter number of pieces: "))

pieces = []
kingIsPresent = False
moves = []

# input pieces 
for _ in range(numberOfPieces):
  pieceStr, squareStr = input().split(" ")

  # assign the chess.SQUARE type
  square = chess.SQUARES[chess.parse_square(squareStr)]

  # create a piece with the piece type mapped from the letter (ex. B -> bishop, N -> knight)
  piece = chess.Piece(utils.pieceStringToPiece(pieceStr), chess.WHITE)

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
    return True


  # generate attacks from the current position and pieces
  generatedAttacks = utils.findAttacks(remainingPieces, board)
  
  for attack in generatedAttacks:
    # if the piece can actually move, then continue the attack
    if remainingPieces[remainingPieces.index(attack["piece"])]["moveCount"] < 2:
      
      # setting up for backtracking
      oldRemainingPieces = remainingPieces.copy()
      oldMoves = moves.copy()

      attackedPiece = attack["attackedPiece"]
    
      # removing the attacked piece because it is taken
      remainingPieces.remove(attackedPiece)
      # updating the internal board
      board.remove_piece_at(attack["piece"]["square"])

      # set the attacking piece to the square of the attacked piece (taking the piece)

      updatedPiece = attack["piece"].copy()
      fromSquare = updatedPiece["square"]

      updatedPiece["square"] = attack["attackedSquare"]
      # updating the internal board
      board.set_piece_at(attackedPiece["square"], attack["piece"]["piece"])

      # increase the move count of the attacking piece
      updatedPiece["moveCount"] += 1
      
      # the old piece index is the index of the attacking piece as it is guaranteed to be in the list
      oldPieceIndex = remainingPieces.index(attack["piece"])

      # placing the updated piece in position of the old piece
      remainingPieces[oldPieceIndex] = updatedPiece

      newMove = {
        "piece": attack["piece"],
        "from": fromSquare,
        "to": attack["attackedSquare"],
      }

      moves.append(newMove)

      solve(remainingPieces, moves)

      # in case of a failed subtree

      # revert back
      remainingPieces = oldRemainingPieces.copy()
      moves = oldMoves.copy()

      # reverting the internal board
      board.set_piece_at(attackedPiece["square"], attackedPiece["piece"])
      board.set_piece_at(attack["piece"]["square"], attack["piece"]["piece"])

solve(pieces, moves)
