import chess
def pieceStringToPieceType(pieceString):
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
  if len(remainingPieces) == 1:
    if wasKingOnBoard and chess.KING not in [piece["piece"].piece_type for piece in remainingPieces]:
      return False
    else:
      return True
  return False


def findAttacks(remainingPieces, board):
  squares = [piece["square"] for piece in remainingPieces]

  attacks = []
  
  for piece in remainingPieces:
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
