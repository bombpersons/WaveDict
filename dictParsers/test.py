# -*- coding: utf-8 -*-
# This file parses the definitions at http://dic.yahoo.co.jp

from scrapemark import scrape

if __name__ == "__main__":
	html = """
		<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja"> 
<head> 
<meta http-equiv="content-type" content="text/html; charset=UTF-8"> 
<meta name="description" content="Yahoo!辞書 大辞泉 国語辞書 たん‐ご【単語】 文法上、意味・職能をもった最小の言語単位。例えば「鳥が鳴く」という文は、「鳥」「が」「鳴く」の三つの"> 
<meta name="keywords" content="Yahoo!辞書 大辞泉 国語辞書 たん‐ご【単語】"> 
<meta name="author" content="Yahoo! JAPAN"> 
<title>Yahoo!辞書 - たん‐ご【単語】</title> 
<meta http-equiv="content-type" content="text/html; charset=UTF-8"> 
<link rel="stylesheet" href="http://i.yimg.jp/images/search/css/dic/srp/061212/srp_combine.css" type="text/css" media="all"> 
<link rel="stylesheet" href="http://i.yimg.jp/images/search/css/dic/srp/061212/srp_print.css" type="text/css" media="print"> 
<link rel="stylesheet" href="http://i.yimg.jp/images/dic/css/yj_dic_090107.css" type="text/css"> 
<link rel="stylesheet" href="http://i.yimg.jp/images/dic/css/dic_070910.css" type="text/css"> 
<link rel="alternate" type="application/rss+xml" title="Yahoo!辞書 - 新語探検" href="http://dic.yahoo.co.jp/rss"> 
<link rel="search" type="application/opensearchdescription+xml" title="Yahoo!辞書" href="http://dic.yahoo.co.jp/dic-search-yahoo.xml"> 
</head> 
<body class="quirks"> 
 
<!--header--> 
<div id="ygunav"><span id="ygps">こんにちは、<strong>ゲスト</strong> さん [<a href="https://login.yahoo.co.jp/config/login?.direct=1&.lg=jp&.intl=jp&.src=dic&.done=http%3A%2F%2Fdic.yahoo.co.jp%2Fdsearch%3Fenc%3DUTF-8%26amp%3Bp%3D%25E5%258D%2598%25E8%25AA%259E%26amp%3Bstype%3D0%26amp%3Bdtype%3D0">ログイン</a>]</span> 
<a href="http://www.yahoo.co.jp/">Yahoo! JAPAN</a> - 
<a href="http://search.yahoo.co.jp">Yahoo!検索</a> - 
 
<a href="http://bb.yahoo.co.jp/">Yahoo! BB</a> - 
<a href="http://help.yahoo.co.jp/help/jp/dic/">ヘルプ</a> 
</div><!---/#ygunav --><!--/header--> 
 
<!--AD_EMGS --> 
<!-- SpaceID=2077683385 loc=EMG noad --> 
<!-- SpaceID=2077683385 loc=EMG2 noad-spid --> 
<!-- SpaceID=2077683385 loc=EMG3 noad-spid --> 
 
<!--/AD_EMGS --> 
 
<div id=ygma> 
<a href="http://dic.yahoo.co.jp/"><img src="http://i.yimg.jp/images/dic/diclogo_3.gif" alt="Yahoo!辞書" title="Yahoo!辞書" border="0"></a> 
 
<div id="yschqcon"> 
<div id="yschtg"> 
<a href="http://search.yahoo.co.jp/search?p=%E5%8D%98%E8%AA%9E&ei=UTF-8&fr=sfp" class="yschfirst">ウェブ</a><span class="yschsep"> | </span> 
<a href="http://search.yahoo.co.jp/search/dir?p=%E5%8D%98%E8%AA%9E&ei=UTF-8&fr=sfp">登録サイト</a><span class="yschsep"> | </span> 
<a href="http://image-search.yahoo.co.jp/search?p=%E5%8D%98%E8%AA%9E">画像</a><span class="yschsep"> | </span> 
<a href="http://music-search.yahoo.co.jp/search?p=%E5%8D%98%E8%AA%9E&fr=sfp">音楽</a><span class="yschsep"> | </span> 
<a href="http://video-search.yahoo.co.jp/search?p=%E5%8D%98%E8%AA%9E&fr=sfp">動画</a><span class="yschsep"> | </span> 
<a href="http://nsearch.yahoo.co.jp/bin/query?p=%C3%B1%B8%EC">ニュース</a><span class="yschsep"> | </span> 
<a href="http://blog-search.yahoo.co.jp/search?p=%C3%B1%B8%EC">ブログ</a><span class="yschsep"> | </span> 
<strong class="yschon">辞書</strong><span class="yschsep"> | </span> 
<a href="http://search.chiebukuro.yahoo.co.jp/search/search.php?p=%E5%8D%98%E8%AA%9E&ei=UTF-8">知恵袋</a><span class="yschsep"> | </span> 
<a href="http://search.map.yahoo.co.jp/search?ei=UTF-8&p=%E5%8D%98%E8%AA%9E">地図</a><span class="yschsep"> | </span> 
<a href="http://psearch.yahoo.co.jp/search?cop=mss&__yltc=s%3A%2Cd%3A14489115%2Csec%3Asrchtab%2Cslk%3Aproducts%2Ck%3A&ei=UTF-8&fr=sfp&p=%C3%B1%B8%EC">商品</a><span class="yschsep"> | </span></div><!---/yschtg --> 
 
<!--dic search--> 
<form action="http://dic.yahoo.co.jp/dsearch" method=get> 
<input type="hidden" name="enc" value="UTF-8"> 
<input id=yschsp name=p value="単語"> 
<select name="stype" class="pldwn"><option value="0" selected="selected">で始まる</option><option value="1">に一致する</option><option value="2">を含む</option><option value="3">で終わる</option><option value="4">を解説に含む</option></select>項目を<input type=submit value="検索" class="ygbt"> 
<div class="yschact"><label for="Ndtype0"><input name="dtype" id="Ndtype0" value="0" class="radiobtn" type="radio" checked="checked">国語</label>&nbsp;<label for="Ndtype5"><input name="dtype" id="Ndtype5" value="5" class="radiobtn" type="radio">類語</label>&nbsp;<label for="Ndtype1"><input name="dtype" id="Ndtype1" value="1" class="radiobtn" type="radio">英和</label>&nbsp;<label for="Ndtype3"><input name="dtype" id="Ndtype3" value="3" class="radiobtn" type="radio">和英</label>&nbsp;<label for="Ndtype2"><input name="dtype" id="Ndtype2" value="2" class="radiobtn" type="radio">すべての辞書</label>&nbsp;</div><!---/yschact --> 
</form><!--/dic search--> 
 
</div><!---/#yschqcon --> 
</div><!---/#ygma --> 
 
<!--dic news--> 
<div id=yschtools> 
<table border="0" cellpadding="0" cellspacing="0" width="100%"> 
<tbody><tr> 
 
<td><img src="http://i.yimg.jp/images/clear.gif" width="1" height="20"></td> 
</tr></tbody></table> 
</div> 
<!--/dic news--> 
<div id=yschinfo><h1>辞書検索結果</h1> 
<p><strong>単語</strong>で辞書検索した結果　<strong>1〜1</strong>件目 / <strong>1</strong>件  （<a href="http://help.yahoo.co.jp/help/jp/dic/dic-06.html">検索結果の見方</a>）</p> 
</div> 
 
 
<div id="contents"> 
 
<!--AD_CT --> 
<table width="100%" border="0" cellpadding="2" cellspacing="10"> 
<tr><td bgcolor="#bbbbbb"> 
<table width="100%" border="0" cellpadding="5" cellspacing="0"> 
<tr><td align="center" bgcolor="#ffffff">[PR] <a href="http://ard.yahoo.co.jp/SIG=1540f1et3/M=300434257.301196119.302703199.300710096/D=jp_dic/S=2077683385:CT/Y=jp/EXP=1255815049/L=EcqcLnJvS9imoUphStobXmnbUivpAUraG2kAACwa/B=auP9BHJvSHo-/J=1255807849034962/A=301067185/SIG=12267l36l/R=0/*http://realestate.feature.yahoo.co.jp/daikibo0910/index.html">ピンとくる！　魅力たっぷりの住まいを直感で探してみよう</a><script language=javascript> 
if(window.yzq_d==null)window.yzq_d=new Object();
window.yzq_d['auP9BHJvSHo-']='&U=13i1s2ah2%2fN%3dauP9BHJvSHo-%2fC%3d300434257.301196119.302703199.300710096%2fD%3dCT%2fB%3d301067185';
</script><noscript><div style="position:absolute;"><img width=1 height=1 alt="" src="http://b5.yahoo.co.jp/b?P=EcqcLnJvS9imoUphStobXmnbUivpAUraG2kAACwa&T=13t1efhlq%2fX%3d1255807849%2fE%3d2077683385%2fR%3djp_dic%2fK%3d5%2fV%3d2.1%2fW%3dH%2fY%3djp%2fF%3d57908223%2fQ%3d-1%2fS%3d1%2fJ%3d524A6F72&U=13i1s2ah2%2fN%3dauP9BHJvSHo-%2fC%3d300434257.301196119.302703199.300710096%2fD%3dCT%2fB%3d301067185"></div></noscript></td></tr></table> 
</td></tr></table> 
<!--/AD_CT --> 
 
<!--メイン --> 
<!--タブ --> 
<div id="nav-pri"> 
<ul> 
<li class="on"><strong><a id="tab_0" href="http://rd.yahoo.co.jp/dic/tab/jj/?http://dic.yahoo.co.jp/dsearch?p=%E5%8D%98%E8%AA%9E&enc=UTF-8&stype=0&dtype=0"><em>国語辞書</em></a></strong></li> 
<li><a id="tab_1" href="http://rd.yahoo.co.jp/dic/tab/jt/?http://dic.yahoo.co.jp/dsearch?p=%E5%8D%98%E8%AA%9E&enc=UTF-8&stype=0&dtype=5"><em>類語辞書</em></a></li> 
<li><a id="tab_2" href="http://rd.yahoo.co.jp/dic/tab/ej/?http://dic.yahoo.co.jp/dsearch?p=%E5%8D%98%E8%AA%9E&enc=UTF-8&stype=0&dtype=1"><em>英和辞書</em></a></li> 
<li><a id="tab_3" href="http://rd.yahoo.co.jp/dic/tab/je/?http://dic.yahoo.co.jp/dsearch?p=%E5%8D%98%E8%AA%9E&enc=UTF-8&stype=0&dtype=3"><em>和英辞書</em></a></li> 
<li><a id="tab_4" href="http://rd.yahoo.co.jp/dic/tab/al/?http://dic.yahoo.co.jp/dsearch?p=%E5%8D%98%E8%AA%9E&enc=UTF-8&stype=0&dtype=2"><em>すべての辞書</em></a></li> 
</ul> 
</div> 
 
<table class="tabtable" bgcolor="#d6b58f" border="0" cellpadding="0" cellspacing="5" width="100%"> 
<tbody><tr> 
<td> 
<font color="#333333"><small><img src="http://i.yimg.jp/images/dic/img/dic_koku_01.gif" alt="国語辞典" align="absbottom" height="16" hspace="2" width="16">辞書切り替え：
<b>大辞泉</b>&nbsp;|&nbsp;
<a href="http://rd.yahoo.co.jp/dic/tab/0ss/?http://dic.yahoo.co.jp/dsearch?p=%E5%8D%98%E8%AA%9E&enc=UTF-8&stype=0&dtype=0&dname=0ss">大辞林</a></small></font></td> 
<td></td> 
</tr></tbody> 
</table><!--/タブ --> 
 
<img src="http://i.yimg.jp/images/clear.gif" width=1 height=15> 
 
<div align="center"> 
 
<!--メインテーブル --> 
<table width="98%"  border="0" cellspacing="0" cellpadding="0"> 
<tr> 
<!--メインカラム --> 
<td valign="top"> 
<!--詳細 Title--> 
<table width="100%"  border="0" cellspacing="5" cellpadding="0"> 
<tr> 
<td><b>たん‐ご【単語】</b></td> 
</tr> 
 
<tr><td align=right><small><a href="http://dic.yahoo.co.jp/dsearch?enc=UTF-8&p=%E3%81%9F%E3%82%93%E3%81%94&dtype=0&stype=1&dname=0ss">「<b>たんご</b>」を大辞林でも検索する</a></small></td></tr> 
 
</table> 
<!--/詳細 Title--> 
 
<table width="100%"  border="0" cellspacing="0" cellpadding="0"> 
<tr> 
<td bgcolor="#EAE4BF"><img src="http://i.yimg.jp/images/clear.gif" width=10 height=1></td> 
</tr> 
</table> 
<img src="http://i.yimg.jp/images/clear.gif" width=1 height=5><br> 
<!--詳細--> 
<table border=0 cellspacing=10 cellpadding=0 width=100%> 
<tr> 
<!-- <td class=s130> --> 
<td> 
文法上、意味・職能をもった最小の言語単位。例えば「鳥が鳴く」という文は、「鳥」「が」「鳴く」の三つの単語からなる。日本語では自立語・付属語に大別される。<br> 
</td> 
</tr> 
</table> 
<!--/詳細--> 
 
<br> 
 
<!--ヘルプ--> 
<table border="0" cellpadding="0" cellspacing="5" width="100%"> 
<tbody><tr> 
<td><small>[ 大辞泉　提供：<a href="http://www.japanknowledge.com/" target="_new_window">JapanKnowledge</a> ] </small> </td> 
<td align="right"><small><a href="http://dic.yahoo.co.jp/guide/jj/">凡例</a> </small><a href="http://dic.yahoo.co.jp/guide/jj/"><img src="http://i.yimg.jp/images/dic/img_button.gif" alt="凡例" align="absbottom" border="0"></a></td> 
</tr> 
</tbody></table> 
<!--/ヘルプ--> 
 
<table border="0" cellpadding="0" cellspacing="0" width="100%"> 
<tbody><tr> 
<td bgcolor="#eae4bf"><img src="http://i.yimg.jp/images/clear.gif" height="1" width="10"></td> 
</tr> 
</tbody></table> 
 
<!--リンク--> 
<table border="0" cellpadding="0" cellspacing="5" width="100%"> 
<tbody><tr> 
<td width="1%"><a href="http://www.japanknowledge.com/"><img src="http://i.yimg.jp/images/dic/banner_01.gif" alt="JapanKnowledge" border="0" height="40" width="170"></a></td> 
</tr> 
</tbody></table> 
<!--/リンク--> 
<script type="text/javascript" language="javascript"> 
yjaxc_ad_ds = 'tmpl_dic_ams_002_utf8'; yjaxc_ad_id = 'ydictionary';
</script> 
<script type="text/javascript" language="javascript"
src="http://yjaxc.yahoo.co.jp/js/yjaxc.js"> 
</script> 
 
</td> 
<!--メインカラム --> 
 
<td><img src="http://i.yimg.jp/images/clear.gif" width=10 height=1></td> 
 
<!--右カラム --> 
<td width="180" align="right" valign="top"> 
 
<!--検索結果--> 
<table width=100% border=0 cellpadding=1 cellspacing=0 bgcolor="#EAE4BF"> 
<tr> 
<td> 
<!--件数--> 
<table cellpadding=0 cellspacing=5 border=0 width=100%> 
<tr> 
<td align="center"><small><font color=#333333>&nbsp;<b>1〜1</b>件目 / <b>1</b>件</font></small></td> 
</tr> 
</table> 
<!--/件数--> 
<!--結果--> 
<table width=100% border=0 cellpadding=0 cellspacing=0 bgcolor="#FFFFFF"> 
<tr> 
<td align="center" valign="top"> 
<img src="http://i.yimg.jp/images/clear.gif" height=5 width=1 border=0><br> 
<!--結果内容--> 
<table cellspacing=0 cellpadding=2 border=0 width=95%> 
<tr bgcolor="#FAF2D6" class=s130><td width=1% valign="top"><small>1</small></td><td width=99% valign="top"><small><b>たん‐ご【単語】</b></small></td></tr> 
</table> 
<!--/結果内容--> 
<!--ページ送りナビ--> 
<table width="100%"  border="0" cellspacing="0" cellpadding="0"> 
<tr> 
<td align="center"> 
 
</td> 
</tr> 
</table> 
<!--/ページ送りナビ--> 
<img src="http://i.yimg.jp/images/clear.gif" width=1 height=5><br> 
</td> 
</tr> 
</table> 
<!--/結果--> 
</td> 
</tr> 
</table> 
<!--/検索結果--> 
<img src="http://i.yimg.jp/images/clear.gif" height=10 width=1 border=0><br> 
<!--AD_MSQ --> 
 
<!--/AD_MSQ --> 
<img src="http://i.yimg.jp/images/clear.gif" height=10 width=1 border=0><br> 
 
<!--QR --> 
<table class="qrmid" border="0" cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td class="qrimg"> 
<a href="http://dic.yahoo.co.jp/promo/"><img src="http://i.yimg.jp/images/dic/img/qrcode_detail_s.gif" alt="モバイル版Yahoo!辞書にアクセス！" border="0" height="74" width="74"></a> 
</td> 
</tr><tr><td class="mobtext"> 
モバイル版Yahoo!辞書にアクセス！</td> 
</tr> 
<tr> 
<td class="moblink"> 
<a href="http://dic.yahoo.co.jp/promo/">説明を見る</a><br> 
<img src="http://i.yimg.jp/images/mobile/common/phonemail.gif" alt="URL送信" border="0" height="19" width="30"><a href="http://mtf.yahoo.co.jp/mailto?prop=mobile&locale=jp&url=http%3A%2F%2Fmobile.yahoo.co.jp%2Fbin%2Frd%3Fq%3D1161&title=Yahoo%21%A5%E2%A5%D0%A5%A4%A5%EB+-+Yahoo%21%BC%AD%BD%F1&h1=http%3A%2F%2Fdic.yahoo.co.jp%2F&h5=0">URLをケータイに送信</a> 
<br> 
（Yahoo! JAPAN IDでのログインが必要です）
</td> 
</tr></tbody></table> 
<!--/QR --> 
 
<!--翻訳--> 
<table width=100% border=0 cellpadding=1 cellspacing=0 bgcolor="#EAE4BF"> 
<tr> 
<td> 
<table width=100% cellpadding=2 cellspacing=0 border=0> 
<tr bgcolor=#ffffff> 
<td width=20% align=center><a href="http://rd.yahoo.co.jp/dic/right_promo/honyaku/?http://honyaku.yahoo.co.jp/"><img src="http://i.yimg.jp/images/sicons/trans28.gif" width="28" height="28" border=0 alt="Yahoo!翻訳"></a> 
</td> 
<td width=80%> 
<small><a href="http://rd.yahoo.co.jp/dic/right_promo/honyaku/?http://honyaku.yahoo.co.jp/">文章やウェブページをYahoo!翻訳</a></small> 
</td> 
</tr> 
</table> 
</td> 
</tr> 
</table> 
<!--/翻訳--> 
<img src="http://i.yimg.jp/images/clear.gif" height=10 width=1 border=0><br> 
<!--ツールバー--> 
<table width=100% border=0 cellpadding=1 cellspacing=0 bgcolor="#EAE4BF"> 
<tr> 
<td> 
<table width=100% cellpadding=2 cellspacing=0 border=0> 
<tr bgcolor=#ffffff> 
<td width=20% align=center><a href="http://rd.yahoo.co.jp/dic/right_promo/toolbar/?http://toolbar.yahoo.co.jp/"><img src="http://i.yimg.jp/images/sicons/y.gif" alt="Yahoo!ツールバー" width="28" height="28" border=0></a> </td> 
<td width=80%> <small><a href="http://rd.yahoo.co.jp/dic/right_promo/toolbar/?http://toolbar.yahoo.co.jp/">Yahoo!ツールバーでいつでも辞書検索</a></small> </td> 
</tr> 
</table></td> 
</tr> 
</table> 
<!--/ツールバー--> 
<!--banner--> 
<a href="/promo/accelerator/"><img src="http://i.yimg.jp/images/dic/promo_01/accelerator_090629/banner_180.gif" alt="文字をなぞって直接検索! Yahoo!辞書アクセラレータ for Internet Explorer 8" width="180" height="60" vspace="10" border="0"></a> 
<!--/banner--> 
</td> 
<!--/右カラム --> 
 
</tr> 
</table> 
<!--/メインテーブル --> 
 
</div> 
 
<img src="http://i.yimg.jp/images/clear.gif" width=1 height=15> 
 
<!--タブ --> 
<div id="nav-pri"> 
<ul> 
<li class="on"><strong><a id="tab_0" href="http://rd.yahoo.co.jp/dic/tab/jj/?http://dic.yahoo.co.jp/dsearch?p=%E5%8D%98%E8%AA%9E&enc=UTF-8&stype=0&dtype=0"><em>国語辞書</em></a></strong></li> 
<li><a id="tab_1" href="http://rd.yahoo.co.jp/dic/tab/jt/?http://dic.yahoo.co.jp/dsearch?p=%E5%8D%98%E8%AA%9E&enc=UTF-8&stype=0&dtype=5"><em>類語辞書</em></a></li> 
<li><a id="tab_2" href="http://rd.yahoo.co.jp/dic/tab/ej/?http://dic.yahoo.co.jp/dsearch?p=%E5%8D%98%E8%AA%9E&enc=UTF-8&stype=0&dtype=1"><em>英和辞書</em></a></li> 
<li><a id="tab_3" href="http://rd.yahoo.co.jp/dic/tab/je/?http://dic.yahoo.co.jp/dsearch?p=%E5%8D%98%E8%AA%9E&enc=UTF-8&stype=0&dtype=3"><em>和英辞書</em></a></li> 
<li><a id="tab_4" href="http://rd.yahoo.co.jp/dic/tab/al/?http://dic.yahoo.co.jp/dsearch?p=%E5%8D%98%E8%AA%9E&enc=UTF-8&stype=0&dtype=2"><em>すべての辞書</em></a></li> 
</ul> 
</div> 
 
<table class="tabtable" bgcolor="#d6b58f" border="0" cellpadding="0" cellspacing="5" width="100%"> 
<tbody><tr> 
<td> 
<font color="#333333"><small><img src="http://i.yimg.jp/images/dic/img/dic_koku_01.gif" alt="国語辞典" align="absbottom" height="16" hspace="2" width="16">辞書切り替え：
<b>大辞泉</b>&nbsp;|&nbsp;
<a href="http://rd.yahoo.co.jp/dic/tab/0ss/?http://dic.yahoo.co.jp/dsearch?p=%E5%8D%98%E8%AA%9E&enc=UTF-8&stype=0&dtype=0&dname=0ss">大辞林</a></small></font></td> 
<td></td> 
</tr></tbody> 
</table><!--/タブ --> 
<!--/メイン --> 
</div> 
 
 
<!---/#contents --> 
 
<div id="yschssbxl"> 
<div id="yschssbx"> 
<div id="yschstg"> 
<a href="http://search.yahoo.co.jp/search?p=%E5%8D%98%E8%AA%9E&ei=UTF-8&fr=sfp" class="yschfirst">ウェブ</a><span class="yschsep"> | </span> 
<a href="http://search.yahoo.co.jp/search/dir?p=%E5%8D%98%E8%AA%9E&ei=UTF-8&fr=sfp">登録サイト</a><span class="yschsep"> | </span> 
<a href="http://image-search.yahoo.co.jp/search?p=%E5%8D%98%E8%AA%9E">画像</a><span class="yschsep"> | </span> 
<a href="http://music-search.yahoo.co.jp/search?p=%E5%8D%98%E8%AA%9E&fr=sfp">音楽</a><span class="yschsep"> | </span> 
<a href="http://video-search.yahoo.co.jp/search?p=%E5%8D%98%E8%AA%9E&fr=sfp">動画</a><span class="yschsep"> | </span> 
<a href="http://nsearch.yahoo.co.jp/bin/query?p=%C3%B1%B8%EC">ニュース</a><span class="yschsep"> | </span> 
<a href="http://blog-search.yahoo.co.jp/search?p=%C3%B1%B8%EC">ブログ</a><span class="yschsep"> | </span> 
<strong class="yschon">辞書</strong><span class="yschsep"> | </span> 
<a href="http://search.chiebukuro.yahoo.co.jp/search/search.php?p=%E5%8D%98%E8%AA%9E&ei=UTF-8">知恵袋</a><span class="yschsep"> | </span> 
<a href="http://search.map.yahoo.co.jp/search?ei=UTF-8&p=%E5%8D%98%E8%AA%9E">地図</a><span class="yschsep"> | </span> 
<a href="http://psearch.yahoo.co.jp/search?cop=mss&__yltc=s%3A%2Cd%3A14489115%2Csec%3Asrchtab%2Cslk%3Aproducts%2Ck%3A&ei=UTF-8&fr=sfp&p=%C3%B1%B8%EC">商品</a><span class="yschsep"> | </span></div><!---/yschstg --> 
 
<!--dic search--> 
<form action="http://dic.yahoo.co.jp/dsearch" method=get> 
<input type="hidden" name="enc" value="UTF-8"> 
<input id=yschsp name=p value="単語"> 
<select name="stype" class="pldwn"><option value="0" selected="selected">で始まる</option><option value="1">に一致する</option><option value="2">を含む</option><option value="3">で終わる</option><option value="4">を解説に含む</option></select>項目を<input type=submit value="検索" class="ygbt"> 
<div class="yschact"><label for="Sdtype0"><input name="dtype" id="Sdtype0" value="0" class="radiobtn" type="radio" checked="checked">国語</label>&nbsp;<label for="Sdtype5"><input name="dtype" id="Sdtype5" value="5" class="radiobtn" type="radio">類語</label>&nbsp;<label for="Sdtype1"><input name="dtype" id="Sdtype1" value="1" class="radiobtn" type="radio">英和</label>&nbsp;<label for="Sdtype3"><input name="dtype" id="Sdtype3" value="3" class="radiobtn" type="radio">和英</label>&nbsp;<label for="Sdtype2"><input name="dtype" id="Sdtype2" value="2" class="radiobtn" type="radio">すべての辞書</label>&nbsp;</div><!---/yschact --> 
</form><!--/dic search--> 
 
</div><!---/#yschssbx --> 
</div><!---/#yschssbxl --> 
 
<div id="yschft"> 
<hr> 
<p> 
<a href="http://privacy.yahoo.co.jp/privacy/jp/">プライバシーの考え方</a> - <a href="http://docs.yahoo.co.jp/docs/info/terms/">利用規約</a> - <a href="http://help.yahoo.co.jp/help/jp/dic/">ヘルプ・お問い合わせ</a><br> 
 
Copyright (C) Shogakukan All Rights Reserved.<br>Copyright (C) 2009 Yahoo Japan Corporation. All Rights Reserved.
</p> 
</div><!---/#yschft --> 
 
</body> 
</html><script language=javascript> 
if(window.yzq_p==null)document.write("<scr"+"ipt language=javascript src=http://ai.yimg.jp/bdv/yahoo/javascript/csc/20060824/lib2obf_b5.js></scr"+"ipt>");
</script><script language=javascript> 
if(window.yzq_p)yzq_p('P=EcqcLnJvS9imoUphStobXmnbUivpAUraG2kAACwa&T=13pqq90i1%2fX%3d1255807849%2fE%3d2077683385%2fR%3djp_dic%2fK%3d5%2fV%3d1.1%2fW%3dJ%2fY%3djp%2fF%3d139133272%2fS%3d1%2fJ%3d524A6F72');
if(window.yzq_s)yzq_s();
</script><noscript><div style="position:absolute;"><img width=1 height=1 alt="" src="http://b5.yahoo.co.jp/b?P=EcqcLnJvS9imoUphStobXmnbUivpAUraG2kAACwa&T=13vc5biu3%2fX%3d1255807849%2fE%3d2077683385%2fR%3djp_dic%2fK%3d5%2fV%3d3.1%2fW%3dJ%2fY%3djp%2fF%3d1038199582%2fQ%3d-1%2fS%3d1%2fJ%3d524A6F72"></div></noscript> 
<!-- fe04.dic.kks.yahoo.co.jp compressed/chunked Sun Oct 18 04:30:49 JST 2009 --> 
"""
	
	definition  = scrape(""" 
	<table border=0 cellspacing=10 cellpadding=0 width=100%> 
		<tr> 
			<td> 			
				{{ }}
			</td> 
		</tr> 
	</table> 
	""", html)
	
	print definition
