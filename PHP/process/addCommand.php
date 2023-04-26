<?php
include_once '../../PHP/includes/dbh-inc.php';

$input = $_POST['input'];
$script = $_POST['action'];

// check for empty fields
if (empty($input) || empty($script)) {
    header("Location: ../commands.php?update=empty");
    exit();
}

// check if the command already exists
$sql = "SELECT * FROM commands;";
$result = mysqli_query($conn, $sql);
while ($row = mysqli_fetch_assoc($result)) {
    if ($row['CommandInput'] == $input) {
        header("Location: ../commands.php?update=exists");
        exit();
    }
}
// add the command to the database
$addCommandSQL = "INSERT INTO commands (CommandInput, CommandAction) VALUES ('$input', '$script');";
mysqli_query($conn, $addCommandSQL);
mysqli_free_result($result);

header("Location: ../commands.php?update=success");
?>