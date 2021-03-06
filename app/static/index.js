var cells = document.getElementsByTagName('td')

var grid = []
var row = []

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

var verifyBtn = document.getElementById('verify')
var solveBtn = document.getElementById("solve");

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

$("#solve").click(function (e) {
  e.preventDefault(); // avoid to execute the actual submit of the form.

  var board = [
    0, 7, 0, 9, 0, 2, 3, 0, 8,
    0, 0, 0, 0, 6, 0, 0, 0, 0,
    0, 0, 0, 0, 5, 7, 1, 0, 6,
    0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 6, 8, 4, 0, 0, 0, 0, 2,
    0, 0, 0, 0, 0, 9, 0, 3, 0,
    1, 0, 0, 0, 7, 3, 2, 0, 0,
    0, 8, 0, 0, 0, 1, 0, 4, 0,
    0, 0, 0, 0, 0, 0, 0, 6, 0
  ];

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


function setPuzzle(board){
    for (i = 0; i < 9; i++) {
      for (j = 0; j < 9; j++) {
        grid[i][j].innerText = board[i][j]
        
      }
    }
}