<?php
  session_start();
  $target_dir = "../uploads/";
  $target_file = $target_dir . basename($_FILES["file"]["name"]);
  $uploadOk = 1;


  if ($uploadOk == 0) {
      echo "Sorry, your file was not uploaded.";
  } else {
      if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
          echo "The file ". basename( $_FILES["file"]["name"]). " has been uploaded.";
      } else {
          echo "Sorry, there was an error uploading your file.";
      }
  }

  $_SESSION['name'] = $target_file;
  $_SESSION['id'] = generateRandomID();
  header('Location: fileUploaded.php');
?>
