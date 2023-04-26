<?php
    include_once 'includes/dbh-inc.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Modwords</title>
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
            <h1>Modwords Data Table</h1>
            <?php
                include('process/displayModwordsTable.php');
            ?>
            <p></p>
        </div>
        <div class="content">
            <h1>Add Bad Word</h1>
            <form action="process/addModword.php" method="POST">
                <input type="text" name="modword" placeholder="Modword">
                <button type="submit" name="submit">Add Modword</button>
            </form>
        </div>
        <div class="content">
            <h1>Remove Bad Word</h1>
            <form action="process/removeModword.php" method="POST">
                <input type="text" name="modword" placeholder="Modword">
                <button type="submit" name="submit">Remove Modword</button>
            </form>
        </div>
    </div>
</body>