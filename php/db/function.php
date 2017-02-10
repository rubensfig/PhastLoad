<?php
  function downloadFile($path){
    $mime_type = '';
    $name = explode('/', $path)[2];
    #if(!is_readable($path)) die('File not found or inaccessible!');

    $known_mime_types=array(
       "htm" => "text/html",
       "exe" => "application/octet-stream",
       "zip" => "application/zip",
       "doc" => "application/msword",
       "jpg" => "image/jpg",
       "php" => "text/plain",
       "xls" => "application/vnd.ms-excel",
       "ppt" => "application/vnd.ms-powerpoint",
       "gif" => "image/gif",
       "pdf" => "application/pdf",
       "txt" => "text/plain",
       "html"=> "text/html",
       "png" => "image/png",
       "jpeg"=> "image/jpg"
    );

    if($mime_type==''){
      $file_extension = strtolower(substr(strrchr($name,"."),1));
      if(array_key_exists($file_extension, $known_mime_types)){
          $mime_type=$known_mime_types[$file_extension];
      } else {
          $mime_type="application/force-download";
      }
    }
    header('Content-Disposition: attachment; filename="'.$name.'"');
    header("Content-Length: " . filesize($path));
    header('Content-Type: ' . $mime_type);

    readfile($path);
  }

  function findinDB($id){
    global $conn;

    $query = "SELECT paths FROM files WHERE sessionid = ?";
    $stmt  = $conn->prepare($query);
    $stmt->execute(array($id));

    $result = $stmt->fetch();
    return  $result['paths'];
  }

  function addToDB($id, $path){
    global $conn;

    $query = "INSERT INTO files VALUES (?,?)";
    $stmt = $conn->prepare($query);
    $stmt->execute(array($id, $path));
  }

  function generateRandomID(){
    $id = rand(1000,9999);
    return $id;
  }
 ?>
