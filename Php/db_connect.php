<?php
$servername = "localhost";
$db_name = "runner_log";

$conn = new mysqli($servername, $db_name);

if($conn -> connect_error)
{
    die("Conncetion failed: ", $conn -> connect_error);
}
else
{
    echo "Conneted Successfuly"
}

mysqli_select_db($conn,$db_name);

?>