<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>WorkBook</title>
</head>
<body>
   
    <?php 
      $isMale = true;
      $isTall = false;
      if ($isMale && $isTall){
        echo "You are a tall male";
      } elseif($isMale && !$isTall){
        echo "You are a short male";
      } elseif(!$isMale && $isTall){
        echo "You are not male but are tall";
      } else{
        echo "You are not male and not tall";
      }
    ?>
</body>
</html>