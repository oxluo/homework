<?php
    $pdo = new PDO("mysql:host=localhost;dbname=ox","root","");
    $userName = $_POST['registerName'];
    $pwd = $_POST['registerPassword'];
    $cfmpwd = $_POST['confirmPassword'];
    $pdo = new PDO("mysql:host=localhost;dbname=ox", "root", "");
    $exist = strstr($userName, $pdo->query("SELECT username FROM users WHERE username='" . $userName . "'"));
    if($exist)
        echo "用户名已被注册";
    else if(strlen($pwd) < 6)
        echo "密码长度过短";
    else if(!strstr($pwd, $cfmpwd))
        echo "两次输入密码不一致";
    else{
        $md5Pwd = md5($pwd);
        $pdo->exec("INSERT INTO users (username,password) VALUES ('" . $userName . "','" . $md5Pwd . "')");
        echo "注册成功！<br />";
        echo "用户名：".$userName."<br />";
        echo "密码：".$pwd."<br />";
    }
?>