<?php
include_once '../../PHP/includes/dbh-inc.php';

$modword = $_POST['modword'];

// check for empty fields
if (empty($modword)) {
    header("Location: ../modwords.php?update=empty");
    exit();
}

// check if the command already exists
$sql = "SELECT * FROM modwords;";
$result = mysqli_query($conn, $sql);
while ($row = mysqli_fetch_assoc($result)) {
    if ($row['BadWords'] == $modword) {
        header("Location: ../modwords.php?update=exists");
        exit();
    }
}
// add the command to the database
$addModwordSQL = "INSERT INTO modwords (BadWords) VALUES ('$modword');";
mysqli_query($conn, $addModwordSQL);
mysqli_free_result($result);

header("Location: ../modwords.php?update=success");
?>