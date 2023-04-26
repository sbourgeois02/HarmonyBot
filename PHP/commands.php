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
                    <th>Command Input</th>
                    <th>Command Script</th>
                </tr>
                <?php
                    $sql = "SELECT * FROM commands;";
                    $result = mysqli_query($conn, $sql);
                    $resultCheck = mysqli_num_rows($result);
                    if ($resultCheck > 0) {
                        while ($row = mysqli_fetch_assoc($result)) {
                            // display the data
                            echo "<tr><td>" . $row['CommandInput'] . "</td><td>" . $row['CommandAction'] . "</td></tr>";
                        }
                    }
                ?>
            </table>
        </div>
        <div class="content">
            <h1>Add Command</h1>
            <form action="../PHP/process/addCommand.php" method="post">
                <input type="text" name="input" placeholder="User Input">
                <p></p>
                <div class="script">
                    <input type="text" size="50" height="100px" name="action" placeholder="Command Script">
                </div>
                <p></p>
                <button type="submit" name="submit">Add Command</button>
                <p></p>
            </form>
        </div>
        <div class="content">
            <h1>Remove Command</h1>
            <form action="../PHP/process/removeCommand.php" method="post">
                <select name="remove">
                        <?php
                            $input = mysqli_query($conn, "SELECT CommandInput FROM commands;");
                            while ($inputs = mysqli_fetch_assoc($input)):;
                        ?>
                        <option value="<?php echo $inputs["CommandInput"];?>">
                            <?php echo $inputs["CommandInput"];?>
                        </option>
                        <?php endwhile;?>
                </select>
                <p></p>
                <button onclick="return confirm('Are you sure you want to remove this command permanently?');" type="submit" name="submit">Remove Command</button>
                <p></p>
            </form>
        </div>
    </div>
</body>
</html>