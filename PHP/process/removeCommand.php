<?php
include_once '../../PHP/includes/dbh-inc.php';

$input = $_POST['remove'];

// delete the command from the database
$sql = "DELETE FROM commands WHERE CommandInput = '$input';";
mysqli_query($conn, $sql);

header("Location: ../commands.php?update=success");
?>