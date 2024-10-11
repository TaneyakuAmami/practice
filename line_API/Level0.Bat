echo off
rem アクセストークン
SET ACCESS-TOEKEN=pZFxCyN4Z8Co5cQ6LtbWrTxWEqX+srz+tXycVVlsT3LmskFaOAQ9VYWmLacgHYYe9MBZ9F7ZjblJRawYTjhMCaBrANeSFXPAMfN82gxSMOClb/5LH1dCbMDsZz94XrVbA9JZpkkb2tnaGGMW53dPuQdB04t89/1O/w1cDnyilFU=

rem メッセージ（s-jis）
rem SET TEXT1-1=■■熱中症情報■■
rem SET TEXT1-2=【レベル０：試験
rem SET TEXT1-3=試験送信
rem TEXT1-4=各地点の熱中症情報

rem メッセージ（UTF8）
SET TEXT1-1=\u25A0\u25A0\u71B1\u4E2D\u75C7\u60C5\u5831\u25A0\u25A0\r\n
SET TEXT1-2=\u3010\u30EC\u30D9\u30EB\uFF10\uFF1A\u8A66\u9A13\r\n
SET TEXT1-3=\u8A66\u9A13\u9001\u4FE1\r\n
SET TEXT1-4=\u5404\u5730\u70B9\u306E\u71B1\u4E2D\u75C7\u60C5\u5831\r\n

rem SET TEXT2-1=http://dim2web09.wni.co.jp/kashiwacity/pinpoint/index.html
SET TEXT2-1=http://18.181.68.102

rem 送信データ
set POST_DATA={ ^
  \"messages\":[ ^
    { ^
      \"type\":\"text\", ^
      \"text\":\"%TEXT1-1%%TEXT1-2%%TEXT1-3%%TEXT1-4%%TEXT2-1%\" ^
    }^
  ] ^
}

rem 送信URL
set LINE_PUSH_URL=https://api.line.me/v2/bot/message/broadcast

rem 送信
echo on
curl ^
  "%LINE_PUSH_URL%" ^
-v -X POST ^
-H "Content-Type: application/json;charset=utf-8" ^
-H "Authorization: Bearer %ACCESS-TOEKEN%" ^
-d "%POST_DATA%"

exit
