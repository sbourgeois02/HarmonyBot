<?php
    include_once 'includes/dbh-inc.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Commands</title>
    <link rel="stylesheet" href="includes/styles.css">
</head>

<!-- This is the same navbar on all pages -->
<body>
    <div class="banner">
        <div class="title">
            <button onclick="window.open('https://github.com/sbourgeois02/HarmonyBot','_blank')">HarmonyBot WebGUI</button>
        </div>
        <div class="buttons">
            <button onclick="window.location.href='index.php'">Users</button>
            <button onclick="window.location.href='commands.php'">Commands</button>
            <button onclick="window.location.href='roles.php'">Roles</button>
            <button onclick="window.location.href='modwords.php'">Modwords</button>
        </div>
    </div>
    <div class="main">
        <div class="content">
            <h1>Commands Data Table</h1>
            <table>
                <tr>
                    <th>CommandID</th>
                    <th>CommandInput</th>
                    <th>CommandAction</th>
                    <th>CommandOutput</th>
                    <th>CommandMinRoleID</th>
                </tr>
                <?php
                    $sql = "SELECT * FROM commands;";
                    $result = mysqli_query($conn, $sql);
                    $resultCheck = mysqli_num_rows($result);
                    if ($resultCheck > 0) {
                        while ($row = mysqli_fetch_assoc($result)) {
                            // get the RoleName from role table to display instead of RoleID
                            $roleID = $row['CommandMinRoleID'];
                            $roleSQL = "SELECT RoleName FROM role WHERE RoleID = $roleID;";
                            $roleResult = mysqli_query($conn, $roleSQL);
                            $roleName = mysqli_fetch_assoc($roleResult);
                            $rName = $roleName['RoleName'];
                            mysqli_free_result($roleResult);
                            // display the data
                            echo "<tr><td>" . $row['CommandID'] . "</td><td>" . $row['CommandInput'] . "</td><td>" . $row['CommandAction'] . "</td><td>" . $row['CommandOutput'] . "</td><td>" . $rName . "</td></tr>";
                        }
                    }
                ?>
            </table>
        </div>
    </div>
</body>
</html>