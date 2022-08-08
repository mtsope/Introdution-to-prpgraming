<?php
include("db_connect.php");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    table, tr, th, td 
    {
        border: solid black 1px;
    }
    table
    {
        border-collapse: collapse;
    }
    .odd
    {
        background-color: #ccc;
    }
    .even
    {
        background-color: #eee;
    }

</style>
<body>
    <h1> Run History</h1>
    <?php
        $odd = false;
        $query = "Select * from runs";
        $result = $conn->query($query);
        $out = "<table>";
        $out = "<tr class='odd'><th>Date</th><th>Distance</th><th>Notes</th></tr>"
        while($row = $result->fetch_assoc())
        {
            if($odd) {
                $out .= "<tr class='odd'>";
            }
            else
            {
                $out .= "<tr class='even'>";
            }
            $out .= "<td>";
            $out .= $row['runDate']."</td><td>".$row['runDistance']."</td><td>".$row['runComment']."</td></tr>";
            $odd = !$odd;
        }
        $out .= "</table>";
        echo $out;
</body>
</html>
