<head>
	<title>Cloud Computing & Big Data</title>
	<link rel="stylesheet" type="text/css" href="main.css"
</head>
<body>

<?php
$size = 5

if(isset($_POST['info']))
{
$size = $_POST['info']
}
?>

<form method="POST">
      Enter Information:<input type="string" name="info">
      <input type="submit">
</form>

 <?php

        $size = 5

        echo '<table border = "1">'\n'
        for($y = 0; $y < $size; $y++){
        echo "<tr>"\n;
        for($x = 0; $x < $size; $x++){
          echo " <td>"
          echo $x * $y
          echo "</td>"\n
          }
          echo "</tr>"\n
          }

          echo "<table>"\n

?>
</body>
</html>