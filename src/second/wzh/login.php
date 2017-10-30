<?php
    session_start();
    function set_token() {
        $_SESSION['token'] = md5(microtime(true));
    }

    function valid_token() {
        $return = $_REQUEST['token'] === $_SESSION['token'] ? true : false;
        set_token();
        return $return;
    }

    if(!isset($_SESSION['token']) || $_SESSION['token']=='') {
        set_token();
    }

    if(!valid_token())
        echo "token error";
    else if(!isset($_COOKIE['userName']) || $_COOKIE['userName'] == null){
        $pdo = new PDO("mysql:host=localhost;dbname=ox", "root", "");
        $userName = $_POST['loginName'];
        $pwd = $_POST['loginPassword'];
        if(!$_POST['encoded'])
            $md5Pwd = $pwd;
        else
            $md5Pwd = md5($pwd);
    }
    else{
        $userName = $_COOKIE['userName'];
        $md5Pwd = $_COOKIE['password'];
    }

    if (strlen($pwd) < 6) echo "密码长度过短";
    else {
        $r = $pdo->query("SELECT * FROM users WHERE username='" . $userName . "'");
        if ($r == null)
            echo "不存在此账号";
        else if (!strstr($r['password'], $md5Pwd))
            echo "密码和账号不符";
    }
    echo "登陆成功";
    setcookie("userName", $userName, time()+3600);
    setcookie("password", $md5Pwd, time()+3600);

?>