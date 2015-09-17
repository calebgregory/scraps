// game.moves() -> Array
// game.scoreFinistedGame -> number
// game.applyMove(move)

function bestMoveAndScore(game) {
  var bestMove;
  var bestScore;
  game.moves().forEach(function(move) {
    var score = scoreMove(game, move);
    if (score > bestScore) {
      bestScore = score;
      bestMove = move;
    }
  });
  return {move: bestMove, score: bestScore};
}

function scoreMove(game, move) {
  var after = game.applyMove(move);
  var replies = after.moves();
  if (replies.length === 0) {
    return after.scoreFinishedGame(); // game is over
  } else {
    return -bestMoveAndScore(after).score; // game continues
  }
}
