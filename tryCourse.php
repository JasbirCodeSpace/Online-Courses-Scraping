<?php
function show_file($name){
$row = 1;
if (($handle = fopen($name, "r")) !== FALSE) {
    
    echo '<table border="1">';
    
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        $num = count($data);
        if ($row == 1) {
            echo "<thead><tr>";
        }else{
            echo "<tr>";
        }
        
        for ($c=0; $c < $num; $c++) {
            //echo $data[$c] . "<br />\n";
            if(empty($data[$c])) {
               $value = "&nbsp;";
            }else{
               $value = $data[$c];
            }

            if ($row == 1) {
                echo "<th>".$value."</th>";
            }else{
               $reg_exUrl = "/(http|https|ftp|ftps)\:\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(\/\S*)?/";
                $text = $value;
                if(preg_match($reg_exUrl, $text, $url)){
                       echo preg_replace($reg_exUrl, '<td><a href="'.$url[0].'" rel="nofollow">'.$url[0].'</td></a>', $text);
                }
                else
                echo "<td>".$value."</td>";
            }
        }
        
        if ($row == 1) {
            echo "</tr></thead><tbody>";
        }else{
            echo "</tr>";
        }
        $row++;
    }
    
    echo "</tbody></table>";
    fclose($handle);
}
}

show_file("openCourse1.csv");

echo "<br><br>";

show_file("specCourse.csv");
?>