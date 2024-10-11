echo off
rem アクセストークン
SET ACCESS-TOEKEN=pZFxCyN4Z8Co5cQ6LtbWrTxWEqX+srz+tXycVVlsT3LmskFaOAQ9VYWmLacgHYYe9MBZ9F7ZjblJRawYTjhMCaBrANeSFXPAMfN82gxSMOClb/5LH1dCbMDsZz94XrVbA9JZpkkb2tnaGGMW53dPuQdB04t89/1O/w1cDnyilFU=

rem メッセージ（s-jis）
rem SET TEXT1-1=■■熱中症情報■■
rem SET TEXT1-2=【レベル５：運動中止】
rem SET TEXT1-3=運動は控えて、涼しい場所で休むようにしましょう。
rem TEXT1-4=各地点の熱中症情報

rem メッセージ（UTF8）
SET TEXT1-1=\u25A0\u25A0\u71B1\u4E2D\u75C7\u60C5\u5831\u25A0\u25A0\r\n
SET TEXT1-2=\u3010\u30EC\u30D9\u30EB\uFF15\uFF1A\u904B\u52D5\u4E2D\u6B62\u3011\r\n
SET TEXT1-3=\u904B\u52D5\u306F\u63A7\u3048\u3066\u3001\u6DBC\u3057\u3044\u5834\u6240\u3067\u4F11\u3080\u3088\u3046\u306B\u3057\u307E\u3057\u3087\u3046\u3002\r\n
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
