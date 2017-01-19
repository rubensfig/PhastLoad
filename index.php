<?php
  include_once './config/config.php';
  include_once './header.php';
 ?>
 <img id="logo" src="./img/phastload_logo.png"> </img>

 <form action = "findFile.php" method = "post" onsubmit="return Validate();">
   <div id="inputField">

    <input id="input" name = "fileId" type ="text"/ placeholder = "File ID" required>

    <input id="button" name="submit" type ="submit"/>
  </div>
 </form>
  <form action="upload.php" class="dropzone" id="my-awesome-dropzone">
     <div class="fallback">
       <input name="file" type="file" multiple />
     </div>
  </form>

  <script src="js/main.js"></script>
</body>
