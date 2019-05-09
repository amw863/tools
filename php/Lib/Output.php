<?php
/**
 * Copyright (c) 2019,2345
 * 摘    要:
 * 作    者: wangb
 * 修改日期: 2019/5/9
 */
namespace Lib;

class Output
{
    const JSON_SUCC  = 0;
    const JSON_FAIL = 1;

    /**
     * 功能: 输出json 对象
     * 日期:
     *
     * @param int $code 状态码: 0 = 成功, 1 = 失败
     * @param string $msg 描述
     * @param array $data 数据
     * @return null
     */
    public static function json($code, $msg = '', $data = array())
    {
        $data = [
            'code' => $code,
            'msg' => $msg,
            'data' => $data
        ];

        echo json_encode($data, JSON_UNESCAPED_UNICODE);
        die();
    }
}
