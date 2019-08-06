<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
  font-family: arial;
  float: left;
  margin-right: 30px;
  margin-bottom: 100px;
}

.title {
  color: grey;
  font-size: 18px;
}

button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}

a {
  text-decoration: none;
  font-size: 22px;
  color: white;
}

button:hover, a:hover {
  opacity: 0.7;
}
</style>
</head>
<body>
<?php
function readCSV($csvFile){
    $file_handle = fopen($csvFile, 'r');
    while (!feof($file_handle) ) {
        $line_of_text[] = fgetcsv($file_handle, 1024);
        
    }
    
    for($i=1;$i<sizeof($line_of_text)-1;$i++){

            echo '<div class="card">';
      
              echo '<h1>'.$line_of_text[$i][1].'</h1>';
              echo '<p class="title">'.$line_of_text[$i][2].'<br>'.$line_of_text[$i][3].'</p>';
              echo '<p>Harvard University</p>';
              echo '<div style="margin: 24px 0;">';
              echo '</div>';
              echo '<p><button ><a href="'.$line_of_text[$i][0].'">Go To Course</a></button></p>';
            echo '</div>';
        
    }
    fclose($file_handle);
    
}
 
 
// Set path to CSV file
readCSV('specCourse.csv');
readCSV('openCourse1.csv');

?>
</body>
</html>
