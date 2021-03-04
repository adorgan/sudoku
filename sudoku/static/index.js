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


console.log(grid)