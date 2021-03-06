var cells = document.getElementsByTagName('td')
var grid = []
var row = []

// create empty matrix
for(i = 0; i < 81; i++){
    if(i%9==0 && i!=0){
        grid.push(row)
        row = []
        row.push(cells[i])
    }
    else{
        row.push(cells[i])
    }
}
grid.push(row);

var medBoard = [
  [4, 0, 0, 0, 0, 8, 0, 0, 1],
  [8, 0, 3, 0, 0, 0, 9, 4, 0],
  [0, 6, 9, 4, 0, 1, 0, 8, 0],
  [0, 3, 0, 6, 5, 2, 0, 0, 8],
  [0, 0, 0, 0, 0, 0, 6, 0, 0],
  [5, 0, 0, 0, 0, 4, 1, 0, 0],
  [0, 0, 0, 1, 8, 0, 0, 5, 0],
  [6, 9, 0, 7, 0, 3, 8, 1, 0],
  [1, 7, 0, 5, 0, 0, 0, 0, 4],
];
//set initial board 
setPuzzle(medBoard);

//set inputs for all empty squares
for(i = 0; i < 9; i++){
    for(j = 0; j < 9; j++){
        if(grid[i][j].innerText == ""){
            var input = document.createElement("input");
            input.type = "text";
            input.name = `${i}${j}`;
            grid[i][j].appendChild(input); 
        }
        else{
            var input = document.createElement("input");
            input.type = "text";
            input.name = `${i}${j}`;
            input.hidden = true;
            input.value = parseInt(grid[i][j].innerText)
            grid[i][j].appendChild(input); 
        }
    }
}

//verify if user answers are correct
$("#form").submit(function (e) {
  e.preventDefault(); // avoid to execute the actual submit of the form.

  var form = $(this);
  var url = form.attr("action");

  $.ajax({
    type: "POST",
    url: url,
    data: form.serialize(), // serializes the form's elements.
    success: function (data) {
      alert(data); // show response from the php script.
    },
  });
});

//solve puzzle
$("#solve").click(function(e) {
  e.preventDefault();
  var board = gridToList(medBoard);

  $.ajax({
    type: "POST",
    url: '/solve',
    data: JSON.stringify(board),
    success: function (data) {
      arr = JSON.parse(data)
      setPuzzle(arr);
    },
  });
});

//reset board
$("#clear").click(function (e) {
  e.preventDefault();
  setPuzzle(medBoard);
});

//set board based on grid matrix
function setPuzzle(board){
    for (i = 0; i < 9; i++) {
      for (j = 0; j < 9; j++) {
        if (board[i][j] == 0){
            grid[i][j].innerText = '';
        } 
        else{
            grid[i][j].innerText = board[i][j];
        } 
      }
    }
}

//convert matrix to list for parsing on backend
function gridToList(board){
    newList = [];
    for(i=0; i<9; i++){
        for(j=0; j<9; j++){
            newList.push(board[i][j]);
        }
    }
    return newList;
}