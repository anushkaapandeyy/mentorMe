//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");

const homeStartingContent = "welcome to a mentor website";
const app = express();
//set the view engine to ejs
app.set('view engine', 'ejs');


app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

//global array to store objects
var posts = [];

//sending home.ejs file to webpage as well as paragraph to home.ejs
app.get("/",function(req,res){
  res.render("home", {startingcontent: homeStartingContent,
//rendering key as postTitle
});

  //res.redirect brought it to here
  //console.log(posts);
});

app.get("/signup",function(req,res){
  res.render("signup");
});









app.listen(3000, function(){
  console.log("Server started on port 3000");
});
