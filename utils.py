import chess
def pieceStringToPiece(pieceString):
  pieces = {
    "N": chess.KNIGHT,
    "Q": chess.QUEEN,
    "R": chess.ROOK,
    "P": chess.PAWN,
    "B": chess.BISHOP,
    "K": chess.KING
  }

  return pieces[pieceString]


def kingPresent(board):
  boardSquares = board.king(chess.WHITE)
  if boardSquares:
    return True
  return False

def isFinished(remainingPieces, wasKingOnBoard):
  """
  Capture a piece with every move until just one remains
  If 
  there is a King on the board, it must be the final piece
  """
  if len(remainingPieces) == 1:
    
    if wasKingOnBoard and chess.KING not in [piece["piece"].piece_type for piece in remainingPieces]:
      return False
    else:
      return True


  return False


def printMoves(moves):
  for move in moves:
    move["piece"]["square"] = chess.square_name(move["piece"]["square"])
    move["to"] = chess.square_name(move["to"])
    move["from"] = chess.square_name(move["from"])
    print(move)
def findAttacks(remainingPieces, board):
  squares = [piece["square"] for piece in remainingPieces]
  """
  remainingPieces:
  {
    "piece": *chess.PIECE*,
    "moveCount": int,
    "square": int (0-63)
  }
  """


  attacks = []

  """
  for each piece of remainingPieces
  : find the squares that the piece attacks
   : for each square in the squares
    : if square not in squares
     : remove square from the piece's attacking squares
   : add object to the attacks
    {
      "piece": {
        "piece": *chess.PIECE*,
        "moveCount": int
      },
      "attackingSquare": *chess.SQUARE*
    }
  """
  
  for piece in remainingPieces:
    """
      piece = {
      "piece": *chess.PIECE*,
      "moveCount": int
    }
    """

    pieceAttacks = board.attacks(piece["square"])

    for attack in pieceAttacks:
      if attack not in [piece["square"] for piece in remainingPieces]:
        pieceAttacks.remove(attack)
      else:
        attackedPiece = list(filter(lambda piece: piece["square"] == attack, remainingPieces))[0]
        
        attacks.append({
        "piece": piece,
        "attackedSquare": attack,
        "attackedPiece": attackedPiece
      })
    

      
  


  return attacks

def pieceCanMove(piece):
  return (piece["moveCount"] < 2)