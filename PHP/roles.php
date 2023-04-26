<?php
    include_once 'includes/dbh-inc.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Roles</title>
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
            <h1>Role Data Table</h1>
            <table>
                <tr>
                    <th>RoleID</th>
                    <th>Role Name</th>
                </tr>
                <?php
                    $sql = "SELECT * FROM role;";
                    $result = mysqli_query($conn, $sql);
                    $resultCheck = mysqli_num_rows($result);
                    if ($resultCheck > 0) {
                        while ($row = mysqli_fetch_assoc($result)) {
                            // display the data
                            echo "<tr><td>" . $row['RoleID'] . "</td><td>" . $row['RoleName'] . "</td></tr>";
                        }
                    }
                ?>
            </table>
        </div>
        <div class="content">
            <h2>Add Role</h2>
            <form action="../PHP/process/addRole.php" method="POST">
                <input type="text" name="roleName" placeholder="Role Name">
                <button type="submit" name="submit">Add Role</button>
                </form>
            <h2>Remove Role</h2>
            <form action="../PHP/process/removeRole.php" method="POST">
                <select name="roleName">
                        <?php
                            $roleName = mysqli_query($conn, "SELECT RoleName FROM role;");
                            while ($roles = mysqli_fetch_assoc($roleName)):;
                        ?>
                        <option value="<?php echo $roles["RoleName"];?>">
                            <?php 
                                echo $roles["RoleName"];
                            ?>
                        </option>
                        <?php
                            endwhile;
                        ?>
                </select>
            <button onclick="return confirm('Are you sure you want to remove this role permanently?');" type="submit" name="submit">Remove Role</button>
        </div>
</body>