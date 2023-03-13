<?php
    include_once 'includes/dbh-inc.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>HarmonyBot WebGUI</title>
</head>
<body>

    <form method="POST">
        <label>Select a Role: </label>
        <select name="Role">
            <?php
                $roleName = mysqli_query($conn,"SELECT RoleName FROM role;");
                while ($category = mysqli_fetch_assoc($roleName)):;
            ?>
                <option value="<?php echo $category["RoleName"];
                ?>">
                    <?php echo $category["RoleName"];

                    ?>
                </option>
            <?php
                endwhile;
            ?>
        </select>
        <br>
        <input type="submit" value="Submit" name="submit">
    </form>
    <br>
</body>
</html>