<?php
include_once '../../PHP/includes/dbh-inc.php';

$modword = $_POST['modword'];

// delete the modword from the database
$sql = "DELETE FROM modwords WHERE BadWords = '$modword';";
mysqli_query($conn, $sql);

header("Location: ../modwords.php?update=success");
?>