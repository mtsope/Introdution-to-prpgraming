<?php
$servername = "localhost";
$username = "root";
$password = "";
$db_name = "ruuner_log";

$conn = new mysqli($servername, $username, $password, $db_name);
//$conn = new mysqli($servername);

if($conn -> connect_error)
{
    die("Conncetion failed: " . $conn -> connect_error);
}
else
{
   // echo "Conneted Successfuly";
}

mysqli_select_db($conn, $db_name);