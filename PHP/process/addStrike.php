<?php
include_once '../../PHP/includes/dbh-inc.php';

$user = $_POST['user'];
$addStrikeSQL = "UPDATE user SET UserNumStrikes = UserNumStrikes + 1 WHERE UserName = '$user'";

$result = mysqli_query($conn, $addStrikeSQL);

header("Location: ../index.php?update=success");
?>