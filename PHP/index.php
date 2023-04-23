<?php
    include_once 'includes/dbh-inc.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>HarmonyBot WebGUI</title>
    <link rel="stylesheet" href="includes/styles.css">
</head>

<body>
    <div class="main">
        <div class="sidebar">
            <a href="index.php">Home</a>
            <a href="user.php">User</a>
            <a href="role.php">Role</a>
            <a href="status.php">Status</a>
        </div>
        <div class="content">
            <h1>HarmonyBot WebGUI</h1>
            <h2>User Data Table</h2>
            <table>
                <tr>
                    <th>UserName</th>
                    <th>UserTag</th>
                    <th>Status</th>
                    <th>Role</th>
                    <th>Strikes</th>
                </tr>
                <?php
                    $sql = "SELECT * FROM user;";
                    $result = mysqli_query($conn, $sql);
                    $resultCheck = mysqli_num_rows($result);
                    if ($resultCheck > 0) {
                        while ($row = mysqli_fetch_assoc($result)) {
                            // get the Role Name from the Role ID
                            // insert into variable $name
                            $roleID = $row["UserRoleID"];
                            $roleSQL = "SELECT RoleName FROM role WHERE RoleID = $roleID;";
                            $roleResult = mysqli_query($conn, $roleSQL);
                            $roleName = mysqli_fetch_assoc($roleResult);
                            $rName = $roleName["RoleName"];
                            mysqli_free_result($roleResult);
                            // get the Status Name from the Status ID
                            // insert into variable $status
                            $statusID = $row["UserStatusID"];
                            $statusSQL = "SELECT StatusName FROM status WHERE StatusID = $statusID;";
                            $statusResult = mysqli_query($conn, $statusSQL);
                            $statusName = mysqli_fetch_assoc($statusResult);
                            $status = $statusName["StatusName"];
                            mysqli_free_result($statusResult);
                            // display the plus and minus buttons
                            $displayMinus = "<form action='removeStrikeProcess.php' method='post'>
                                                <button type='submit' class='symbols'>&minus;</button>
                                                <input type='hidden' name='user' value='" . $row["UserName"] . "'>
                                            </form>";
                            $displayPlus = "<form action='addStrikeProcess.php' method='post'>
                                                <button type='submit' class='symbols'>&plus;</button>
                                                <input type='hidden' name='user' value='" . $row["UserName"] . "'>
                                            </form>";
                            // display the user table
                            echo "<tr><td>" . $row["UserName"] . "</td><td>#" . $row["UserTag"] . "</td><td>" . $status . "</td><td>" . $rName . "</td><td>" . $row["UserNumStrikes"] . $displayMinus . $displayPlus;
                        }
                    }
                ?>
            </table>
        </div>
        <p></p>
        <div class="content">
            <form method="post" action="process.php">
                <label for="user">Select a User: </label>
                <select name="user" id="user">
                    <?php
                        $userName = mysqli_query($conn, "SELECT UserName FROM user;");
                        while ($users = mysqli_fetch_assoc($userName)):;
                    ?>
                        <option value="<?php echo $users["UserName"];
                        ?>">
                            <?php echo $users["UserName"];
                            ?>
                        </option>
                        <?php
                            endwhile;
                        ?>
                </select>
                <br>
                <label for="role">Select a Role: </label>
                <select name="role" id="role">
                    <?php
                        $roleChosen = array();
                        $roleName = mysqli_query($conn,"SELECT RoleName FROM role;");
                        while ($roles = mysqli_fetch_assoc($roleName)):;
                    ?>
                        <option value="<?php echo $roles["RoleName"];
                        ?>">
                            <?php echo $roles["RoleName"];

                            ?>
                        </option>
                    <?php
                        endwhile;
                    ?>
                </select>
                <br>
                <button type="submit">Submit</button>
            <br>
        </div>
    </div>
</body>
</html>