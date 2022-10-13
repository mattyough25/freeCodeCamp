<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mad Lib</title>
</head>
<body>

    <form action="mad_lib.php" method="get">
        Color: <input type="text" name="color"> <br>
        Plural Noun: <input type="text" name="pluralNoun"> <br>
        Celebrity: <input type="text" name="celebrity"> <br>
        <input type="submit">
    </form>
    <br><br>
    <?php
        $color = $_GET["color"];
        $pluralNoun = $_GET["pluralNoun"];
        $celebrity = $_GET["celebrity"];

        echo "Roses are $color <br>";
        echo "$pluralNoun are blue <br>";
        echo "I love $celebrity <br>";
    ?>
</body>
</html>