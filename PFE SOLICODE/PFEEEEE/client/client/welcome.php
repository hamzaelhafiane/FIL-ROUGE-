<?php
// Initialize the session
session_start();
// Check if the user is logged in, if not then redirect him to login page
if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
    header("location: login.php");
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body{ font: 14px sans-serif; text-align: center; }
    </style>
</head>
<body>
    <h1 class="my-5">Bonjour, <b><?php echo htmlspecialchars($_SESSION["username"]); ?></h1>
    
    <p>
    
        <a href="index.php" class="btn btn-primary">Mon solde</a>
        <a href="payer.php" class="btn btn-success">Payer Ma Commande</a>
        <a href="reset-password.php" class="btn btn-warning">Reset Your Password</a>
        <a href="logout.php" class="btn btn-danger ml-3">Sign Out of Your Account</a>
        <a href="blq.php" class="btn btn-danger ml-3">Bloquer ma carte</a>
        <a href="dmd.php" class="btn btn-danger ml-3">Demander ma carte</a>
        <a href="ac.php" class="btn btn-danger ml-3">Activé ma carte</a>
        <a href="hs.php" id ="pos" class="btn btn-danger ml-3">Historique</a>
    </p>
   
</body>
</html>