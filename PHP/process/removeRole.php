<?php
include_once '../../PHP/includes/dbh-inc.php';

$roleString = $_POST['roleName'];

// delete the role from the database
$sql = "DELETE FROM role WHERE RoleName = '$roleString';";
$roleIDSQL = "SELECT RoleID FROM role WHERE RoleName = '$roleString';";
$roleID = mysqli_query($conn, $roleIDSQL);
$id = mysqli_fetch_assoc($roleID);
$id = $id['RoleID'];
$result = mysqli_query($conn, "SELECT RoleID FROM role;");
mysqli_query($conn, $sql);

// update the RoleID of all roles with a RoleID greater than the deleted role
while ($row = mysqli_fetch_assoc($result)) {
    $currentID = $row['RoleID'];
    if ($currentID > $id) {
        $updateRoleIDSQL = "UPDATE role SET RoleID = $currentID - 1 WHERE RoleID = $currentID;";
        mysqli_query($conn, $updateRoleIDSQL);
    }
}

header("Location: ../roles.php?update=success");
?>