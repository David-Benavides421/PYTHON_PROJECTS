<?php
$servername ='localhost';
$username ='root';
$password ="";
$dbname = "biblioteca_db";

$conn = new mysqli($servername, $username,$password,$dbname);

//check connection
if( $conn ->connect_error) {
    die("connection failed: " . $conn->connect_error);
}
?>