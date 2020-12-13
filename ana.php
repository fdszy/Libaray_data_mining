<?php

header ( "Content-type:text/html;charset=utf-8" );

$name = $_POST['school'];



echo "<script language='javascript' type='text/javascript'>window.location.href='./$name.html'</script>";

?>