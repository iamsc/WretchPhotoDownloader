# WretchPhotoDownloader

伴隨我們走過<del>年幼無知</del>的無名小站即將謝幕，9/2 起開放讓平凡大眾下載備份。然而，無名在資料備份並不那麼親民，例如相片影片等都只以網址呈現，因此就寫了個跨台平小 script 幫助大家下載。

P.S.

無名也有提供 Windows 的下載方式，請見 [http://www.wretch.cc/blog/WretchFAQ/13637278](http://www.wretch.cc/blog/WretchFAQ/13637278)

## 作業系統測試報告

## 可正常使用
* Mac
* Windows 7

## 無法使用
* Windows XP

## 操作說明

### Step 0
先至[無名小站](http://www.wretch.cc/)備份你的資料，發個呆後，就可以下載打包好的備份檔 (無名帳號-wretch.zip)。

### Step 1
解壓縮備份檔之後，裡面會有一個 `album` 的資料夾。

把我們這個 repository 的 `download.py` 檔案放到 `album` 資料夾中。

### Step 2
打開終端機(可以用鍵盤的 `Control+空白鍵` 搜尋 `終端機` 或 `terminal`)。

### Step 3
把終端機切換至你的 `album` 資料夾中。

    > cd /path/to/your/無名帳號-wretch/album/
    
### Step 4
執行 `download.py`

    > python download.py
    
### Step 5
大功告成！恭喜各位~
    
## 致青春

    All these trifling things.. collectively form that pleasing je ne sais quoi, that ensemble.
    
    所有這些小事...
    共同組成了令人愉悅、難以言喻的事物，
    成了一曲合奏。

    ~ Lord Chesterfield, 1748