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
  color: black;
}

button:hover, a:hover {
  opacity: 0.7;
}
</style>
</head>
<body>
<?php
function show_file($name){

  $row = 1;
  if (($handle = fopen($name, "r")) !== FALSE) {
      while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        $num = count($data);

          for ($c=0; $c < $num; $c++) {
            //echo $data[$c] . "<br />\n";
            if(empty($data[$c])) {
               $value = "&nbsp;";
            }else{
               $value = $data[$c];
            }
  }
    echo '<div class="card">';
      
      echo '<h1>John Doe</h1>';
      echo '<p class="title">CEO & Founder, Example</p>';
      echo '<p>Harvard University</p>';
      echo '<div style="margin: 24px 0;">';
        echo '<a href="#"><i class="fa fa-dribbble"></i></a>'; 
        echo '<a href="#"><i class="fa fa-twitter"></i></a>';  
        echo '<a href="#"><i class="fa fa-linkedin"></i></a>';  
        echo '<a href="#"><i class="fa fa-facebook"></i></a>'; 
      echo '</div>';
      echo '<p><button>Go To Course</button></p>';
    echo '</div>';
}
?>
</body>
</html>
