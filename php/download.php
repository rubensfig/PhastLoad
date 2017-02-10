<?php
  session_start();
  include_once 'db/function.php';

  $ex = downloadFile($_POST['path']);
  header('Location: findFile.php');
 ?>
