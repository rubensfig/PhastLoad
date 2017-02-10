<?php
  //session_start();
  error_reporting(error_reporting() & ~E_NOTICE);
  $username = "sibd1602";
  $password = "palavrapasse";
  $servername = "dbm.fe.up.pt";

  try {
    $conn = new PDO("pgsql:host=$servername;port=5432;dbname=sibd1602", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    //echo "Connection sucess";
  }
  catch(PDOException $e)
  {
      echo "Connection failed: " . $e->getMessage();
  }
  $conn->exec('SET search_path TO draggable');

  print_r(error_get_last());
?>
