<?php
include_once '../../PHP/includes/dbh-inc.php';

$input = $_POST['input'];
$script = $_POST['action'];

// check if role already exists
// if it does, redirect to roles.php?update=exists
// if it doesn't, add it to the database and redirect to roles.php?update=success
$sql = "SELECT * FROM commands;";
$result = mysqli_query($conn, $sql);
while ($row = mysqli_fetch_assoc($result)) {
    if ($row['CommandInput'] == $input) {
        header("Location: ../commands.php?update=exists");
        exit();
    }
}
$addCommandSQL = "INSERT INTO commands (CommandInput, CommandAction) VALUES ('$input', '$script');";
mysqli_query($conn, $addCommandSQL);
mysqli_free_result($result);

header("Location: ../commands.php?update=success");
?>