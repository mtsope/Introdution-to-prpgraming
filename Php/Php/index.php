<?php
include("db_connect.php");

if($_SERVER['REQUEST_METHOD'] == 'POST')
{
    $runDate = $_POST['runDate'];
    $runDistance = $_POST['runDistance'];
    $runCommnet = $_POST['runComent'];

    $sql = "INSERT INTO runs values(NUll, '" . $runDate . "','" . $runDistance . "','" . $runCommnet. "');";
    echo $sql;

    if($conn->query($sql) ==  TRUE) {
        //echo "New record reated sucessfully";
    }
    else {
        echo "Error: " .$sql . "<br>" . $conn ->error;

    }
    header("Refresh:0");
}
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
        $out .= "<tr class='odd'><th>Date</th><th>Distance</th><th>Notes</th></tr>";
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
            $out .= $row['runDate']."</td><td>".$row['runDistance']."</td><td>".$row['runComent']."</td></tr>";
            $odd = !$odd;
        }
        $out .= "</table>";
        echo $out;

    ?>

    <h2> Add new Run </h2>
    <form method="post" action="index.php" >
        <label for="runDate"> Date </label>
        <input type="date" mame="runDate" id="runDate" /> <br>
        <label for="runDistance"> Distance </label>
        <input type="text" mame="runDistance" id="runDistance" /> <br>
        <label for="runComent"> Comment </label>
        <input type="text" mame="runComent" id="runComent" /> <br>
        <input type="Submit" value="Save"/>
    </form>
</body>
</html>
