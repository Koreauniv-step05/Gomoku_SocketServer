/**
 * Created by jaeyoung on 2017. 5. 9..
 */


var config = {
    apiKey: "AIzaSyC0Ehm8LasZTsjCzWgcLRpNSee0G-46yCY",
    authDomain: "gomoku-8955a.firebaseapp.com",
    databaseURL: "https://gomoku-8955a.firebaseio.com",
    projectId: "gomoku-8955a",
    storageBucket: "gomoku-8955a.appspot.com",
    messagingSenderId: "857557511237"
};

firebase.initializeApp(config);

var db = firebase.database();
var ref = db.ref("gomoku");

class StonePoint {
    constructor(key,stonePoint,stoneType) {
        this.key = key;
        this.stonePoint = stonePoint;
        this.stoneType = stoneType;
    }
}
class Game {
    constructor(key,board) {
        this.key = key;
        this.board = board;
        this.stonepoints = new Array();
    }
}
class Channel {
  constructor(id) {
    this.id = id;
    this.games = new Array();
  }
}


// var channel = new Channel("1");
// var games = new Array();
// var stonepoints = [];
var boards=new Array();

// function showBoard(board) {
//     for(var i = 0; i < board.length; i++) {
//         for(var z = 0; z < board[i].length; z++) {
//             $('#visualize').append(' ' + board[i][z]);
//             console.log(board[i][z]);
//         }
//         $('#visualize').append('<br>');
//     }
//     $('#visualize').append('<br>');$('#visualize').append('<br>');
// }

function drawBoard(canvas, boardArr) {
    clearBoard(canvas);
        // console.log("drawBoard");
        for(var i=0, leni=boardArr.length; i<leni; i++) {
            for(var j=0, lenj=boardArr[i].length; j<lenj; j++) {
                var stoneType = boardArr[i][j];
                var circleFlag = false;
                if (stoneType > 2) {
                    console.log("stoneType "+stoneType);
                    circleFlag = true;
                    stoneType -= 2;
                }
                if(stoneType == 1) {
                    // console.log("Black");
                    stone = WGo.B;
                    drawStone(canvas, i,j, stone,circleFlag);
                } else if(stoneType == 2) {
                    stone = WGo.W;
                    drawStone(canvas, i, j, stone, circleFlag);
                }
            }
        }
}
function clearBoard(canvas) {
    // console.log("drawStone");
    canvas.removeAllObjects();
}

function removeStone(canvas,i,j) {
    canvas.removeObjectsAt(i,j);
}

function drawStone(canvas, x,y, stone,circleFlag) {
    console.log("drawStone "+circleFlag);
    if (circleFlag) {
        canvas.addObject({x: x, y: y, type: "CR"});
    }
    canvas.addObject({
        x: x,
        y: y,
        c: stone
    });
}

var numbering = {
    // draw on grid layer
    grid: {
        draw: function(args, board) {
            var x = board.getX(args.x);
            var y = board.getX(args.y);

            removeStone(board,args.x,args.y);
            console.log(args);
            this.fillStyle = "rgba(0.5,0.5,0.5,0.7)";
            this.textBaseline="middle";
            this.textAlign="center";
            // if(board.obj_arr[args.x][args.y][0].c == WGo.B) this.fillStyle = "white";
            //     else this.fillStyle = "black";
            this.font = board.stoneRadius+"px "+(board.font || "");
            this.fillText(String.fromCharCode(args.c.charCodeAt(0)), x, y);

            console.log("Style="+this.fillStyle+" x="+x+" y="+y);
        }
    }
};

ref.on("child_added", function(snapshot, prevChildKey) {
    if(prevChildKey != null) {
        var stonePointsRef = ref.child(prevChildKey).child("stonepoints");
        var board = snapshot.val().board;
        drawBoard(canvas, board);
        // console.log("Board : " + board.toString());
        // console.log("prevChildKey : " + prevChildKey);

        // showBoard(board);

        // console.log("stonePointsRef : " + stonePointsRef);
        stonePointsRef.on("child_added", function (snapshot, prevChildKey) {
            // var stonePoints = snapshot.val().stonePoint;
            // console.log("StonePoints : " + stonePoints.toString());
            // var stoneType = snapshot.val().stoneType;
            // console.log("stoneType : " + stoneType);
            // console.log("prevChildKey : " + prevChildKey);
        });
    }
});

ref.on("child_changed", function(snapshot) {
    var board = snapshot.val().board;
    drawBoard(canvas, board);
});

var canvas;
var canvas2;

function loadBoard() {
    canvas = new WGo.Board(document.getElementById("board"), {
        width: 600,
    section: {
        top: -0.5,
        left: -0.5,
        right: -0.5,
        bottom: -0.5
    }});

    // canvas2 = new WGo.Board(document.getElementById("board"), {
    //     width: 600,
    // section: {
    //     top: -0.5,
    //     left: -0.5,
    //     right: -0.5,
    //     bottom: -0.5
    // });



    // var coordinates = {
    //     // draw on grid layer
    //     grid: {
    //         draw: function(args, board) {
    //             var ch, t, xright, xleft, ytop, ybottom;
    //
    //             this.fillStyle = "rgba(0,0,0,0.7)";
    //             this.textBaseline="middle";
    //             this.textAlign="center";
    //             this.font = board.stoneRadius+"px "+(board.font || "");
    //
    //             xright = board.getX(-0.75);
    //             xleft = board.getX(board.size-0.25);
    //             ytop = board.getY(-0.75);
    //             ybottom = board.getY(board.size-0.25);
    //
    //             for(var i = 0; i < board.size; i++) {
    //                 ch = i+"A".charCodeAt(0);
    //                 if(ch >= "I".charCodeAt(0)) ch++;
    //
    //                 t = board.getY(i);
    //                 this.fillText(board.size-i, xright, t);
    //                 this.fillText(board.size-i, xleft, t);
    //
    //                 t = board.getX(i);
    //                 this.fillText(String.fromCharCode(ch), t, ytop);
    //                 this.fillText(String.fromCharCode(ch), t, ybottom);
    //             }
    //
    //             this.fillStyle = "black";
    //         }
    //     }
    // };
    // canvas.addCustomObject(coordinates);

    console.log("loadBoard");
}