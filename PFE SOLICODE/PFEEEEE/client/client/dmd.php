<?php
// Initialize the session
session_start();
// Check if the user is logged in, if not then redirect him to login page
if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
    header("location: login.php");
    exit;
}

?>
<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "demo";
$qq=$_SESSION["username"];
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "UPDATE users SET carte =' 5A BF 38 3B' WHERE username ='$qq'";

if ($conn->query($sql) === TRUE) {
  echo "votre carte est disponible";
} else {
  echo "Error updating record: " . $conn->error;
}

$conn->close();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<a href="welcome.php" class="btn btn-primary">Acceuil</a>
</body>
</html>