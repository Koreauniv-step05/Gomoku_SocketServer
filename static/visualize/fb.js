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


var channel = new Channel("1");
var games = new Array();
var stonepoints = [];
var board=1;

function showBoard(board) {
    for(var i = 0; i < board.length; i++) {
        for(var z = 0; z < board[i].length; z++) {
            $('#visualize').append(' ' + board[i][z]);
            console.log(board[i][z]);
        }
        $('#visualize').append('<br>');
    }
    $('#visualize').append('<br>');$('#visualize').append('<br>');
}
ref.on("child_added", function(snapshot, prevChildKey) {
    if(prevChildKey != null) {
        var stonePointsRef = ref.child(prevChildKey).child("stonepoints");
        board = snapshot.val().board;
        // console.log("Board : " + board.toString());
        // console.log("prevChildKey : " + prevChildKey);

        showBoard(board);

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