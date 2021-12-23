<?php
// sudo docker run -d -p 80:80 --name php -v /home/msr/estudo/docker/PHP/messages:/var/www/html/messages --rm php

// bind mount
// sudo docker run -d -p 80:80 --name php -v /home/msr/estudo/docker/PHP/:/var/www/html/ --rm php


$message = $_POST['message'];

$files = scandir('./messages');
$numFiles = count($files) - 2;

$fileName = 'msg-'.$numFiles;

$file = fopen('./messages/'.$fileName, 'x');

fwrite($file, $message);

header('Location: index.php');