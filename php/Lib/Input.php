<?php
/**
 * Copyright (c) 2019,2345
 * 摘    要:
 * 作    者: wangb
 * 修改日期: 2019/5/9
 */

namespace Lib;

class Input
{
    /**
     * 功能: 接收 POST 提交
     * 修改日期:2019/5/9 10:02
     *
     * @param string $param 入参
     * @param string $default 默认值
     * @return string
     */
    public static function post($param, $default = '')
    {
        return isset($_POST[$param]) ? trim($_POST[$param]) : '';
    }

    /**
     * 功能: 接收 GET 提交
     * 修改日期:2019/5/9 10:05
     *
     * @param string $param 入参
     * @param string $default 默认值
     * @return string
     */
    public static function get($param, $default = '')
    {
        return isset($_GET[$param]) ? trim($_GET[$param]) : '';
    }

    /**
     * 功能: 接收 REQUEST 提交
     * 修改日期: 2019/5/9 10:07
     *
     * @param string $param 入参
     * @param string $default 默认值
     * @return string
     */
    public static function request($param, $default = '')
    {
        return isset($_REQUEST[$param]) ? trim($_REQUEST[$param]) : '';
    }
}