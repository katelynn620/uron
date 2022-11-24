# Merchant Story

---

## 專案簡介
本專案原始碼為商人物語原始發佈網站：[商人物語*あきんどものがたり](http://www.geocities.co.jp/Playtown-Bingo/8587/)下載所得，使用的版本為`商人物語システム 05-03-30 ＋ うどん＆そばアイテムセット`，即烏龍麵&蕎麥麵的版本，預計進行的修正如下：

* 將檔案編碼從 Shift-JIS 改為 UTF8
* 將檔案換行從 CRLF 改為 LF
* 少許BUG修正(例如舊版Perl語法)

原始發佈檔案所包含之音樂以及圖片為禁止重新發佈，故本專案只包含程式碼部份，如需要音樂以及圖片請自行取得。

## 部署

本程式在Linux環境上進行開發與測試，相容於其他Unix-like系統，理論上也可於Windows上進行部署，但暫時不提供此部分的技術支持。需於可支援CGI執行的網頁伺服器部署，例如：Apache、Nginx，或者其他相容伺服器。

開發與測試環境如下：
* Debian 11.4 / Ubuntu 20.04
* Nginx 1.22
* Perl 5.30

亦可直接使用事先製作好的容器鏡像進行部署，請參考下方[部署鏡像repo](#佈署容器鏡像)。若需額外安裝cpan套件時，請自行修改`Dockerfile`，加入遊戲原始碼，並重新建立容器鏡像。若使用Kubernetes進行部署，請掛載Persistent Volume於`common`以及`uron/data`資料夾。

相依套件如下所列，請使用cpan或cpanm進行安裝。
* Locale::Maketext::Lexicon

## 中文化修改

### 主界面
由於希望儘量保留原味，故使用gettext的方式加入多國語言支援，以保留原本的日文詞條。在想修改中文化內容或者新增其他語言支援的情況，可直接修改`locale`下面的*.po檔案，目前中文化支援是使用`tw.po`，若想新增其他語言，可使用樣板`uron.pot`，修改成自己的語言製作成.po檔案，或者可使用poedit之類的編輯器進行編輯，翻譯完成後，再將語言名稱於`_config.cgi`進行設定內即可。如有異動程式碼內gettext格式的情況下，則需要使用xgettext.pl將檔案進行更新，可使用指令進行更新，修改過的區塊便會更新於新的gettext檔案內。

### 道具資料
至於道具相關資料並非使用gettext方式，因本身設計做成可以自行修改的特殊格式，故直接修改`custom/inc-item-data.cgi`，再產生商品資料就會是修改後的版本了。

### 其他中文化
部分像是貨幣、盜賊名稱由於是設定類型，請直接修改`_config.cgi`即可。

## 佈署容器鏡像
請參考以下專案
https://github.com/katelynn620/nginx-perl

## 版權聲明
本專案著作權為原始發佈者「由來 @ 商人物語」所有，程式碼以GPLv2授權進行發佈，故要進行發佈時需以相同模式授權，並保留原始作者名稱。