<?php
  include_once 'header.php';
  include_once 'config/config.php';
  include_once 'db/function.php';

  $id = $_POST['fileId'];
  $path = findinDB($id);
 ?>
 <h1> <?= $path;?></h1>
 <form method = "post" action = "download.php">
   <input type = "hidden" name="path" value="<?=$path;?>" />
   <input type = "submit" value= "Download"/>
</form>
