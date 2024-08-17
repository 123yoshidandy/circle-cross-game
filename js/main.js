const HEIGHT = 10;
const WIDTH = 10;
const COUNT_MAX = 5;

let field = null;
let cells = null;
let mark = null;
let isEnd = null;

reset();

function reset() {
    document.getElementById("h1_title").textContent = "五目並べ";
    field = document.getElementById("table_field");
    cells = [];
    mark = "○";
    isEnd = false;

    for (let i = field.rows.length - 1; i >= 0; i--) {
        field.deleteRow(i);
    }

    for (let row = 0; row < HEIGHT; row++) {
        let tr = document.createElement("tr");
        for (let col = 0; col < WIDTH; col++) {
            let td = document.createElement("td");
            
            if(document.addEventListener){
                td.addEventListener("click" , onClick);
            }else if(document.attachEvent){
                td.attachEvent("onclick" , onClick);
            }

            tr.appendChild(td);
        }
        field.appendChild(tr);
    }

    let td_array = document.getElementsByTagName("td");
    let index = 0;
    for (let row = 0; row < HEIGHT; row++) {
        cells.push([]); // 配列のそれぞれの要素を配列にする（2次元配列にする）
        for (let col = 0; col < WIDTH; col++) {
            cells[row].push(td_array[index]);
            index++;
        }
    }
}

function onClick(event) {
    let x = event.target.cellIndex;
    let y = event.target.parentElement.rowIndex;

    if (isEnd || cells[y][x].textContent != "") {
        return;
    }

    cells[y][x].textContent = mark;

    let count = Math.max(
        1 + countStone(x, y, 1,  0) + countStone(x, y, -1,  0),
        1 + countStone(x, y, 0,  1) + countStone(x, y,  0, -1),
        1 + countStone(x, y, 1,  1) + countStone(x, y, -1, -1),
        1 + countStone(x, y, 1, -1) + countStone(x, y, -1,  1)
    );
    if (count >= COUNT_MAX) {
        isEnd = true;
        document.getElementById("h1_title").textContent = document.getElementById("h1_title").textContent + "：" + mark + "の勝ち";
    }

    if (mark == "○") {
        mark = "●";
    } else {
        mark = "○";
    }

}

function countStone(x, y, dx, dy) {
    x += dx;
    y += dy;
    if (0 <= x && x < WIDTH && 0 <= y && y < HEIGHT && cells[y][x].textContent == mark) {
        return 1 + countStone(x, y, dx, dy);
    } else {
        return 0;
    }
}
