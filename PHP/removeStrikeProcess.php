<?php
include_once 'includes/dbh-inc.php';

$user = $_POST['user'];
$removeStrikeSQL = "UPDATE user SET UserNumStrikes = UserNumStrikes - 1 WHERE UserName = '$user'";

$result = mysqli_query($conn, $removeStrikeSQL);

header("Location: index.php?update=success");
?>