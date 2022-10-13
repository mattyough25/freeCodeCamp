<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <form action="hello_world.php" method="post">
        <input type="text" name="student">
        <input type="submit">
    </form>
    <?php 
        $grades = array("Jim"=>"A+","Pam"=>"B-","Oscar"=>"C+");
        echo $grades[$_POST["student"]];
    ?>
</body>
</html>