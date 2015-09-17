var readline = require('readline');

function createCLI (opt) {

  var rl = readline.createInterface({
    input    : opt.input,
    output   : opt.output,
    terminal : opt.terminal || true,
    completer: opt.completer ||
      function asyncCompleter(linePartial, callback) {
        var completion = linePartial.split(/[ ]+/);
        callback(null, [completion, linePartial]);
      }
  });

  rl.on('line', function(line) {
    if ( !line.trim() ) {
      this.prompt();
    } else {
      this.write(line);
      this.prompt();
    }
  }).on('close', function() {
    this.output.write('\n Have a great day!\n');
    process.exit(0);
  }).setPrompt(' > ');

  rl.output.write(' CLI initialized\n');
  return rl;
}

var cli = createCLI({
  input : process.stdin,
  output: process.stdout
});

cli.prompt();
