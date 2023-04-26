<?php
$db = new PDO('mysql:host=localhost;dbname=harmonybot', 'root', '');
// Connect to the database.

// Get the total number of rows in the table.
$sql = 'SELECT COUNT(*) FROM modwords';
$stmt = $db->prepare($sql);
$stmt->execute();
$total_rows = $stmt->fetchColumn();

// Set the number of rows per page.
$rows_per_page = 20;

// Get the current page number.
$page_number = isset($_GET['page_number']) ? $_GET['page_number'] : 1;

// Calculate the offset.
$offset = ($page_number - 1) * $rows_per_page;

// Get the rows for the current page.
$sql = 'SELECT * FROM modwords LIMIT ' . $offset . ',' . $rows_per_page;
$stmt = $db->prepare($sql);
$stmt->execute();
$rows = $stmt->fetchAll();

// Create the table header.
echo '<table>';
echo '<thead>';
echo '<tr>';
echo '<th>ID</th>';
echo '<th>Bad Word</th>';
echo '</tr>';
echo '</thead>';

// Create the table body.
foreach ($rows as $row) {
  echo '<tr>';
  echo '<td>' . $row['ModWordsID'] . '</td>';
  echo '<td>' . $row['BadWords'] . '</td>';
  echo '</tr>';
}

// Create the table footer.
echo '</table>';

// Create the pagination links.
$pages = ceil($total_rows / $rows_per_page);
for ($i = 1; $i <= $pages; $i++) {
  echo '<a href="?page_number=' . $i . '">' . $i . '</a> ';
}

?>