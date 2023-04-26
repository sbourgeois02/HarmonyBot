<?php
include_once '../../PHP/includes/dbh-inc.php';

$roleString = strtoupper($_POST['roleName']);
if ($roleString == " " || $roleString == NULL || $roleString == "") {
    header("Location: ../roles.php?update=exists");
    exit();
}

// check if role already exists
// if it does, redirect to roles.php?update=exists
// if it doesn't, add it to the database and redirect to roles.php?update=success
$sql = "SELECT * FROM role;";
$result = mysqli_query($conn, $sql);
while ($row = mysqli_fetch_assoc($result)) {
    $roleID = $row['RoleID'];
    if ($row['RoleName'] == $roleString) {
        header("Location: ../roles.php?update=exists");
        exit();
    }
}
$addRoleSQL = "INSERT INTO role (RoleID, RoleName) VALUES ($roleID + 1, '$roleString');";
mysqli_query($conn, $addRoleSQL);
mysqli_free_result($result);

header("Location: ../roles.php?update=success");
?>