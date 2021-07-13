var field = document.getElementById("field_table");
var cells = [];

const HEIGHT = 10;
const WIDTH = 10;
const COUNT_MAX = 5;

var mark = "○";
var isEnd = false;

init();

function init() {
    for (var row = 0; row < HEIGHT; row++) {
        var tr = document.createElement("tr");
        for (var col = 0; col < WIDTH; col++) {
            var td = document.createElement("td");
            
            if(document.addEventListener){
                td.addEventListener("click" , onClick);
            }else if(document.attachEvent){
                td.attachEvent("onclick" , onClick);
            }

            tr.appendChild(td);
        }
        field.appendChild(tr);
    }

    var td_array = document.getElementsByTagName("td");
    var index = 0;
    for (var row = 0; row < HEIGHT; row++) {
        cells.push([]); // 配列のそれぞれの要素を配列にする（2次元配列にする）
        for (var col = 0; col < WIDTH; col++) {
            cells[row].push(td_array[index]);
            index++;
        }
    }
}

function onClick(event) {
    var x = event.target.cellIndex;
    var y = event.target.parentElement.rowIndex;

    if (isEnd || cells[y][x].textContent != "") {
        return;
    }

    cells[y][x].textContent = mark;

    var count = Math.max(
        1 + countStone(x, y, 1,  0) + countStone(x, y, -1,  0),
        1 + countStone(x, y, 0,  1) + countStone(x, y,  0, -1),
        1 + countStone(x, y, 1,  1) + countStone(x, y, -1, -1),
        1 + countStone(x, y, 1, -1) + countStone(x, y, -1,  1)
    );
    if (count >= COUNT_MAX) {
        isEnd = true;
        document.getElementById("title_text").textContent = document.getElementById("title_text").textContent + "：" + mark + "の勝ち";
    }

    if (mark == "○") {
        mark = "×";
    } else {
        mark = "○";
    }

}

function countStone(x, y, dx, dy) {
    x += dx;
    y += dy;
    if (0 <= x < WIDTH && 0 < y <= HEIGHT && cells[y][x].textContent == mark) {
        return 1 + countStone(x, y, dx, dy);
    } else {
        return 0;
    }
}
