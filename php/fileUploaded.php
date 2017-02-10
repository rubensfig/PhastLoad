<?php
  session_start();
  include_once 'header.php';
  include_once 'config/config.php';
  include_once 'db/function.php';

  $target_file = $_SESSION['name'];
  $ID = generateRandomID();
  try{
      addToDB($ID, $target_file);
  } catch (Exception $e){
  }
 ?>
<h1> <?= $ID ?></h1>
