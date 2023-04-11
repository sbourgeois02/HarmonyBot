<?php
include_once 'includes/dbh-inc.php';
$user = $_POST['user'];
$roleString = $_POST['role'];

// get the Role ID
$roleSQL = "SELECT RoleID FROM role WHERE RoleName = '$roleString';";
$roleResult = mysqli_query($conn, $roleSQL);
$roleID = mysqli_fetch_assoc($roleResult);
$id = $roleID["RoleID"];
mysqli_free_result($roleResult);

$updateUserSQL = "UPDATE user SET UserRoleID = $id WHERE UserName = '$user'";
$result = mysqli_query($conn, $updateUserSQL);
if ($result) {
    echo $user . "'s role updated to: " . $roleString;
} else {
    echo "Error: " . $insertUser . "<br>" . mysqli_error($conn);
}

mysqli_close($conn);

?>