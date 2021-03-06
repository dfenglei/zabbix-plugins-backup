



<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" >
 
 <meta name="ROBOTS" content="NOARCHIVE">
 
 <link rel="icon" type="image/vnd.microsoft.icon" href="https://ssl.gstatic.com/codesite/ph/images/phosting.ico">
 
 
 <script type="text/javascript">
 
 
 
 
 var codesite_token = null;
 
 
 var CS_env = {"assetVersionPath": "https://ssl.gstatic.com/codesite/ph/10671232128890609530", "projectName": "argparse", "projectHomeUrl": "/p/argparse", "relativeBaseUrl": "", "loggedInUserEmail": null, "profileUrl": null, "token": null, "domainName": null, "assetHostPath": "https://ssl.gstatic.com/codesite/ph"};
 var _gaq = _gaq || [];
 _gaq.push(
 ['siteTracker._setAccount', 'UA-18071-1'],
 ['siteTracker._trackPageview']);
 
 _gaq.push(
 ['projectTracker._setAccount', 'UA-8140347-1'],
 ['projectTracker._trackPageview']);
 
 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
 })();
 
 </script>
 
 
 <title>argparse.py - 
 argparse -
 
 
 Python command line parsing - Google Project Hosting
 </title>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/10671232128890609530/css/core.css">
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/10671232128890609530/css/ph_detail.css" >
 
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/10671232128890609530/css/d_sb.css" >
 
 
 
<!--[if IE]>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/10671232128890609530/css/d_ie.css" >
<![endif]-->
 <style type="text/css">
 .menuIcon.off { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -42px }
 .menuIcon.on { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -28px }
 .menuIcon.down { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 0; }
 
 
 
  tr.inline_comment {
 background: #fff;
 vertical-align: top;
 }
 div.draft, div.published {
 padding: .3em;
 border: 1px solid #999; 
 margin-bottom: .1em;
 font-family: arial, sans-serif;
 max-width: 60em;
 }
 div.draft {
 background: #ffa;
 } 
 div.published {
 background: #e5ecf9;
 }
 div.published .body, div.draft .body {
 padding: .5em .1em .1em .1em;
 max-width: 60em;
 white-space: pre-wrap;
 white-space: -moz-pre-wrap;
 white-space: -pre-wrap;
 white-space: -o-pre-wrap;
 word-wrap: break-word;
 font-size: 1em;
 }
 div.draft .actions {
 margin-left: 1em;
 font-size: 90%;
 }
 div.draft form {
 padding: .5em .5em .5em 0;
 }
 div.draft textarea, div.published textarea {
 width: 95%;
 height: 10em;
 font-family: arial, sans-serif;
 margin-bottom: .5em;
 }

 
 .nocursor, .nocursor td, .cursor_hidden, .cursor_hidden td {
 background-color: white;
 height: 2px;
 }
 .cursor, .cursor td {
 background-color: darkblue;
 height: 2px;
 display: '';
 }
 
 
.list {
 border: 1px solid white;
 border-bottom: 0;
}

 
 </style>
</head>
<body class="t4">
<script type="text/javascript">
 window.___gcfg = {lang: 'en'};
 (function() 
 {var po = document.createElement("script");
 po.type = "text/javascript"; po.async = true;po.src = "https://apis.google.com/js/plusone.js";
 var s = document.getElementsByTagName("script")[0];
 s.parentNode.insertBefore(po, s);
 })();
</script>
<div class="headbg">

 <div id="gaia">
 

 <span>
 
 
 <a href="#" id="projects-dropdown" onclick="return false;"><u>My favorites</u> <small>&#9660;</small></a>
 | <a href="https://www.google.com/accounts/ServiceLogin?service=code&amp;ltmpl=phosting&amp;continue=https%3A%2F%2Fcode.google.com%2Fp%2Fargparse%2Fsource%2Fbrowse%2Fargparse.py&amp;followup=https%3A%2F%2Fcode.google.com%2Fp%2Fargparse%2Fsource%2Fbrowse%2Fargparse.py" onclick="_CS_click('/gb/ph/signin');"><u>Sign in</u></a>
 
 </span>

 </div>

 <div class="gbh" style="left: 0pt;"></div>
 <div class="gbh" style="right: 0pt;"></div>
 
 
 <div style="height: 1px"></div>
<!--[if lte IE 7]>
<div style="text-align:center;">
Your version of Internet Explorer is not supported. Try a browser that
contributes to open source, such as <a href="http://www.firefox.com">Firefox</a>,
<a href="http://www.google.com/chrome">Google Chrome</a>, or
<a href="http://code.google.com/chrome/chromeframe/">Google Chrome Frame</a>.
</div>
<![endif]-->



 <table style="padding:0px; margin: 0px 0px 10px 0px; width:100%" cellpadding="0" cellspacing="0"
 itemscope itemtype="http://schema.org/CreativeWork">
 <tr style="height: 58px;">
 
 
 
 <td id="plogo">
 <link itemprop="url" href="/p/argparse">
 <a href="/p/argparse/">
 
 <img src="https://ssl.gstatic.com/codesite/ph/images/defaultlogo.png" alt="Logo" itemprop="image">
 
 </a>
 </td>
 
 <td style="padding-left: 0.5em">
 
 <div id="pname">
 <a href="/p/argparse/"><span itemprop="name">argparse</span></a>
 </div>
 
 <div id="psum">
 <a id="project_summary_link"
 href="/p/argparse/"><span itemprop="description">Python command line parsing</span></a>
 
 </div>
 
 
 </td>
 <td style="white-space:nowrap;text-align:right; vertical-align:bottom;">
 
 <form action="/hosting/search">
 <input size="30" name="q" value="" type="text">
 
 <input type="submit" name="projectsearch" value="Search projects" >
 </form>
 
 </tr>
 </table>

</div>

 
<div id="mt" class="gtb"> 
 <a href="/p/argparse/" class="tab ">Project&nbsp;Home</a>
 
 
 
 
 <a href="/p/argparse/downloads/list" class="tab ">Downloads</a>
 
 
 
 
 
 
 
 
 
 <a href="/p/argparse/source/checkout"
 class="tab active">Source</a>
 
 
 
 
 
 
 
 
 <a href="https://code.google.com/export-to-github/export?project=argparse">
 <button>Export to GitHub</button>
 
 </a>
 
 
 <div class=gtbc></div>
</div>

 
 <div style="font-weight: bold; color: #c00; margin-top: 5px; margin-left: 13px;">
 READ-ONLY: This project has been <a href='https://code.google.com/archive/p/argparse'>archived</a>. For more information see <a href='https://code.google.com/p/support/wiki/ReadOnlyTransition'>this post</a>.
 </div>
 

<table cellspacing="0" cellpadding="0" width="100%" align="center" border="0" class="st">
 <tr>
 
 
 
 
 
 
 <td class="subt">
 <div class="st2">
 <div class="isf">
 
 <form action="/p/argparse/source/browse" style="display: inline">
 
 Repository:
 <select name="repo" id="repo" style="font-size: 92%" onchange="submit()">
 <option value="default">default</option><option value="wiki">wiki</option>
 </select>
 </form>
 
 


 <span class="inst1"><a href="/p/argparse/source/checkout">Checkout</a></span> &nbsp;
 <span class="inst2"><a href="/p/argparse/source/browse/">Browse</a></span> &nbsp;
 <span class="inst3"><a href="/p/argparse/source/list">Changes</a></span> &nbsp;
 
 
 
 </form>
 <script type="text/javascript">
 
 function codesearchQuery(form) {
 var query = document.getElementById('q').value;
 if (query) { form.action += '%20' + query; }
 }
 </script>
 </div>
</div>

 </td>
 
 
 
 <td align="right" valign="top" class="bevel-right"></td>
 </tr>
</table>


<script type="text/javascript">
 var cancelBubble = false;
 function _go(url) { document.location = url; }
</script>
<div id="maincol"
 
>

 




<div class="expand">
<div id="colcontrol">
<style type="text/css">
 #file_flipper { white-space: nowrap; padding-right: 2em; }
 #file_flipper.hidden { display: none; }
 #file_flipper .pagelink { color: #0000CC; text-decoration: underline; }
 #file_flipper #visiblefiles { padding-left: 0.5em; padding-right: 0.5em; }
</style>
<table id="nav_and_rev" class="list"
 cellpadding="0" cellspacing="0" width="100%">
 <tr>
 
 <td nowrap="nowrap" class="src_crumbs src_nav" width="33%">
 <strong class="src_nav">Source path:&nbsp;</strong>
 <span id="crumb_root">
 
 <a href="/p/argparse/source/browse/">hg</a>/&nbsp;</span>
 <span id="crumb_links" class="ifClosed">argparse.py</span>
 
 
 
 
 
 <form class="src_nav">
 
 <span class="sourcelabel"><strong>Branch:</strong>
 <select id="branch_select" name="name" onchange="submit()">
 
 <option value="default"
 selected>
 default
 </option>
 
 <option value="function-arguments"
 >
 function-arguments
 </option>
 
 <option value="r101-bsd"
 >
 r101-bsd
 </option>
 
 
 </select>
 </span>
 </form>
 
 
 
 
 <form class="src_nav">
 
 <span class="sourcelabel">
 <strong>Tag:</strong>
 <select id="tag_select" name="name" onchange="submit()">
 <option value="">&lt;none&gt;</option>
 
 <option value="r10" >r10</option>
 
 <option value="r101" >r101</option>
 
 <option value="r11" >r11</option>
 
 <option value="r12" >r12</option>
 
 <option value="r121" >r121</option>
 
 <option value="r122" >r122</option>
 
 <option value="r130" >r130</option>
 
 </select>
 </span>
 </form>
 
 


 <span class="sourcelabel">Download
 <a href="//argparse.googlecode.com/archive/e26233c6cc8f631e27c9ed7fb2bd47b58746c895.zip" rel="nofollow">zip</a> | <a href="//argparse.googlecode.com/archive/e26233c6cc8f631e27c9ed7fb2bd47b58746c895.tar.gz" rel="nofollow">tar.gz</a>
 </span>


 </td>
 
 
 <td nowrap="nowrap" width="33%" align="right">
 <table cellpadding="0" cellspacing="0" style="font-size: 100%"><tr>
 
 
 <td class="flipper">
 <ul class="leftside">
 
 <li><a href="/p/argparse/source/browse/argparse.py?r=8bcccc85a584f5c3790c6cb8f80c7cadc7864049" title="Previous">&lsaquo;8bcccc85a584</a></li>
 
 </ul>
 </td>
 
 <td class="flipper"><b>e26233c6cc8f</b></td>
 
 </tr></table>
 </td> 
 </tr>
</table>

<div class="fc">
 
 
 
<style type="text/css">
.undermouse span {
 background-image: url(https://ssl.gstatic.com/codesite/ph/images/comments.gif); }
</style>
<table class="opened" id="review_comment_area"
><tr>
<td id="nums">
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
<pre><table width="100%" id="nums_table_0"><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1"

><td id="1"><a href="#1">1</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2"

><td id="2"><a href="#2">2</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_3"

><td id="3"><a href="#3">3</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_4"

><td id="4"><a href="#4">4</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_5"

><td id="5"><a href="#5">5</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_6"

><td id="6"><a href="#6">6</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_7"

><td id="7"><a href="#7">7</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_8"

><td id="8"><a href="#8">8</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_9"

><td id="9"><a href="#9">9</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_10"

><td id="10"><a href="#10">10</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_11"

><td id="11"><a href="#11">11</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_12"

><td id="12"><a href="#12">12</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_13"

><td id="13"><a href="#13">13</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_14"

><td id="14"><a href="#14">14</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_15"

><td id="15"><a href="#15">15</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_16"

><td id="16"><a href="#16">16</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_17"

><td id="17"><a href="#17">17</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_18"

><td id="18"><a href="#18">18</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_19"

><td id="19"><a href="#19">19</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_20"

><td id="20"><a href="#20">20</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_21"

><td id="21"><a href="#21">21</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_22"

><td id="22"><a href="#22">22</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_23"

><td id="23"><a href="#23">23</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_24"

><td id="24"><a href="#24">24</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_25"

><td id="25"><a href="#25">25</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_26"

><td id="26"><a href="#26">26</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_27"

><td id="27"><a href="#27">27</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_28"

><td id="28"><a href="#28">28</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_29"

><td id="29"><a href="#29">29</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_30"

><td id="30"><a href="#30">30</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_31"

><td id="31"><a href="#31">31</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_32"

><td id="32"><a href="#32">32</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_33"

><td id="33"><a href="#33">33</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_34"

><td id="34"><a href="#34">34</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_35"

><td id="35"><a href="#35">35</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_36"

><td id="36"><a href="#36">36</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_37"

><td id="37"><a href="#37">37</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_38"

><td id="38"><a href="#38">38</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_39"

><td id="39"><a href="#39">39</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_40"

><td id="40"><a href="#40">40</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_41"

><td id="41"><a href="#41">41</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_42"

><td id="42"><a href="#42">42</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_43"

><td id="43"><a href="#43">43</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_44"

><td id="44"><a href="#44">44</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_45"

><td id="45"><a href="#45">45</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_46"

><td id="46"><a href="#46">46</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_47"

><td id="47"><a href="#47">47</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_48"

><td id="48"><a href="#48">48</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_49"

><td id="49"><a href="#49">49</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_50"

><td id="50"><a href="#50">50</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_51"

><td id="51"><a href="#51">51</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_52"

><td id="52"><a href="#52">52</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_53"

><td id="53"><a href="#53">53</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_54"

><td id="54"><a href="#54">54</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_55"

><td id="55"><a href="#55">55</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_56"

><td id="56"><a href="#56">56</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_57"

><td id="57"><a href="#57">57</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_58"

><td id="58"><a href="#58">58</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_59"

><td id="59"><a href="#59">59</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_60"

><td id="60"><a href="#60">60</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_61"

><td id="61"><a href="#61">61</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_62"

><td id="62"><a href="#62">62</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_63"

><td id="63"><a href="#63">63</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_64"

><td id="64"><a href="#64">64</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_65"

><td id="65"><a href="#65">65</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_66"

><td id="66"><a href="#66">66</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_67"

><td id="67"><a href="#67">67</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_68"

><td id="68"><a href="#68">68</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_69"

><td id="69"><a href="#69">69</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_70"

><td id="70"><a href="#70">70</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_71"

><td id="71"><a href="#71">71</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_72"

><td id="72"><a href="#72">72</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_73"

><td id="73"><a href="#73">73</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_74"

><td id="74"><a href="#74">74</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_75"

><td id="75"><a href="#75">75</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_76"

><td id="76"><a href="#76">76</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_77"

><td id="77"><a href="#77">77</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_78"

><td id="78"><a href="#78">78</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_79"

><td id="79"><a href="#79">79</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_80"

><td id="80"><a href="#80">80</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_81"

><td id="81"><a href="#81">81</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_82"

><td id="82"><a href="#82">82</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_83"

><td id="83"><a href="#83">83</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_84"

><td id="84"><a href="#84">84</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_85"

><td id="85"><a href="#85">85</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_86"

><td id="86"><a href="#86">86</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_87"

><td id="87"><a href="#87">87</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_88"

><td id="88"><a href="#88">88</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_89"

><td id="89"><a href="#89">89</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_90"

><td id="90"><a href="#90">90</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_91"

><td id="91"><a href="#91">91</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_92"

><td id="92"><a href="#92">92</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_93"

><td id="93"><a href="#93">93</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_94"

><td id="94"><a href="#94">94</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_95"

><td id="95"><a href="#95">95</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_96"

><td id="96"><a href="#96">96</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_97"

><td id="97"><a href="#97">97</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_98"

><td id="98"><a href="#98">98</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_99"

><td id="99"><a href="#99">99</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_100"

><td id="100"><a href="#100">100</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_101"

><td id="101"><a href="#101">101</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_102"

><td id="102"><a href="#102">102</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_103"

><td id="103"><a href="#103">103</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_104"

><td id="104"><a href="#104">104</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_105"

><td id="105"><a href="#105">105</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_106"

><td id="106"><a href="#106">106</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_107"

><td id="107"><a href="#107">107</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_108"

><td id="108"><a href="#108">108</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_109"

><td id="109"><a href="#109">109</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_110"

><td id="110"><a href="#110">110</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_111"

><td id="111"><a href="#111">111</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_112"

><td id="112"><a href="#112">112</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_113"

><td id="113"><a href="#113">113</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_114"

><td id="114"><a href="#114">114</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_115"

><td id="115"><a href="#115">115</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_116"

><td id="116"><a href="#116">116</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_117"

><td id="117"><a href="#117">117</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_118"

><td id="118"><a href="#118">118</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_119"

><td id="119"><a href="#119">119</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_120"

><td id="120"><a href="#120">120</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_121"

><td id="121"><a href="#121">121</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_122"

><td id="122"><a href="#122">122</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_123"

><td id="123"><a href="#123">123</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_124"

><td id="124"><a href="#124">124</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_125"

><td id="125"><a href="#125">125</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_126"

><td id="126"><a href="#126">126</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_127"

><td id="127"><a href="#127">127</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_128"

><td id="128"><a href="#128">128</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_129"

><td id="129"><a href="#129">129</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_130"

><td id="130"><a href="#130">130</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_131"

><td id="131"><a href="#131">131</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_132"

><td id="132"><a href="#132">132</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_133"

><td id="133"><a href="#133">133</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_134"

><td id="134"><a href="#134">134</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_135"

><td id="135"><a href="#135">135</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_136"

><td id="136"><a href="#136">136</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_137"

><td id="137"><a href="#137">137</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_138"

><td id="138"><a href="#138">138</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_139"

><td id="139"><a href="#139">139</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_140"

><td id="140"><a href="#140">140</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_141"

><td id="141"><a href="#141">141</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_142"

><td id="142"><a href="#142">142</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_143"

><td id="143"><a href="#143">143</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_144"

><td id="144"><a href="#144">144</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_145"

><td id="145"><a href="#145">145</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_146"

><td id="146"><a href="#146">146</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_147"

><td id="147"><a href="#147">147</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_148"

><td id="148"><a href="#148">148</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_149"

><td id="149"><a href="#149">149</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_150"

><td id="150"><a href="#150">150</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_151"

><td id="151"><a href="#151">151</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_152"

><td id="152"><a href="#152">152</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_153"

><td id="153"><a href="#153">153</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_154"

><td id="154"><a href="#154">154</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_155"

><td id="155"><a href="#155">155</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_156"

><td id="156"><a href="#156">156</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_157"

><td id="157"><a href="#157">157</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_158"

><td id="158"><a href="#158">158</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_159"

><td id="159"><a href="#159">159</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_160"

><td id="160"><a href="#160">160</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_161"

><td id="161"><a href="#161">161</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_162"

><td id="162"><a href="#162">162</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_163"

><td id="163"><a href="#163">163</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_164"

><td id="164"><a href="#164">164</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_165"

><td id="165"><a href="#165">165</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_166"

><td id="166"><a href="#166">166</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_167"

><td id="167"><a href="#167">167</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_168"

><td id="168"><a href="#168">168</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_169"

><td id="169"><a href="#169">169</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_170"

><td id="170"><a href="#170">170</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_171"

><td id="171"><a href="#171">171</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_172"

><td id="172"><a href="#172">172</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_173"

><td id="173"><a href="#173">173</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_174"

><td id="174"><a href="#174">174</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_175"

><td id="175"><a href="#175">175</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_176"

><td id="176"><a href="#176">176</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_177"

><td id="177"><a href="#177">177</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_178"

><td id="178"><a href="#178">178</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_179"

><td id="179"><a href="#179">179</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_180"

><td id="180"><a href="#180">180</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_181"

><td id="181"><a href="#181">181</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_182"

><td id="182"><a href="#182">182</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_183"

><td id="183"><a href="#183">183</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_184"

><td id="184"><a href="#184">184</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_185"

><td id="185"><a href="#185">185</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_186"

><td id="186"><a href="#186">186</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_187"

><td id="187"><a href="#187">187</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_188"

><td id="188"><a href="#188">188</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_189"

><td id="189"><a href="#189">189</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_190"

><td id="190"><a href="#190">190</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_191"

><td id="191"><a href="#191">191</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_192"

><td id="192"><a href="#192">192</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_193"

><td id="193"><a href="#193">193</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_194"

><td id="194"><a href="#194">194</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_195"

><td id="195"><a href="#195">195</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_196"

><td id="196"><a href="#196">196</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_197"

><td id="197"><a href="#197">197</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_198"

><td id="198"><a href="#198">198</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_199"

><td id="199"><a href="#199">199</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_200"

><td id="200"><a href="#200">200</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_201"

><td id="201"><a href="#201">201</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_202"

><td id="202"><a href="#202">202</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_203"

><td id="203"><a href="#203">203</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_204"

><td id="204"><a href="#204">204</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_205"

><td id="205"><a href="#205">205</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_206"

><td id="206"><a href="#206">206</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_207"

><td id="207"><a href="#207">207</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_208"

><td id="208"><a href="#208">208</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_209"

><td id="209"><a href="#209">209</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_210"

><td id="210"><a href="#210">210</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_211"

><td id="211"><a href="#211">211</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_212"

><td id="212"><a href="#212">212</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_213"

><td id="213"><a href="#213">213</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_214"

><td id="214"><a href="#214">214</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_215"

><td id="215"><a href="#215">215</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_216"

><td id="216"><a href="#216">216</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_217"

><td id="217"><a href="#217">217</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_218"

><td id="218"><a href="#218">218</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_219"

><td id="219"><a href="#219">219</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_220"

><td id="220"><a href="#220">220</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_221"

><td id="221"><a href="#221">221</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_222"

><td id="222"><a href="#222">222</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_223"

><td id="223"><a href="#223">223</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_224"

><td id="224"><a href="#224">224</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_225"

><td id="225"><a href="#225">225</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_226"

><td id="226"><a href="#226">226</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_227"

><td id="227"><a href="#227">227</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_228"

><td id="228"><a href="#228">228</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_229"

><td id="229"><a href="#229">229</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_230"

><td id="230"><a href="#230">230</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_231"

><td id="231"><a href="#231">231</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_232"

><td id="232"><a href="#232">232</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_233"

><td id="233"><a href="#233">233</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_234"

><td id="234"><a href="#234">234</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_235"

><td id="235"><a href="#235">235</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_236"

><td id="236"><a href="#236">236</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_237"

><td id="237"><a href="#237">237</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_238"

><td id="238"><a href="#238">238</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_239"

><td id="239"><a href="#239">239</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_240"

><td id="240"><a href="#240">240</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_241"

><td id="241"><a href="#241">241</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_242"

><td id="242"><a href="#242">242</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_243"

><td id="243"><a href="#243">243</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_244"

><td id="244"><a href="#244">244</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_245"

><td id="245"><a href="#245">245</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_246"

><td id="246"><a href="#246">246</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_247"

><td id="247"><a href="#247">247</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_248"

><td id="248"><a href="#248">248</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_249"

><td id="249"><a href="#249">249</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_250"

><td id="250"><a href="#250">250</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_251"

><td id="251"><a href="#251">251</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_252"

><td id="252"><a href="#252">252</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_253"

><td id="253"><a href="#253">253</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_254"

><td id="254"><a href="#254">254</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_255"

><td id="255"><a href="#255">255</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_256"

><td id="256"><a href="#256">256</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_257"

><td id="257"><a href="#257">257</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_258"

><td id="258"><a href="#258">258</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_259"

><td id="259"><a href="#259">259</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_260"

><td id="260"><a href="#260">260</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_261"

><td id="261"><a href="#261">261</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_262"

><td id="262"><a href="#262">262</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_263"

><td id="263"><a href="#263">263</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_264"

><td id="264"><a href="#264">264</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_265"

><td id="265"><a href="#265">265</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_266"

><td id="266"><a href="#266">266</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_267"

><td id="267"><a href="#267">267</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_268"

><td id="268"><a href="#268">268</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_269"

><td id="269"><a href="#269">269</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_270"

><td id="270"><a href="#270">270</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_271"

><td id="271"><a href="#271">271</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_272"

><td id="272"><a href="#272">272</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_273"

><td id="273"><a href="#273">273</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_274"

><td id="274"><a href="#274">274</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_275"

><td id="275"><a href="#275">275</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_276"

><td id="276"><a href="#276">276</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_277"

><td id="277"><a href="#277">277</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_278"

><td id="278"><a href="#278">278</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_279"

><td id="279"><a href="#279">279</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_280"

><td id="280"><a href="#280">280</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_281"

><td id="281"><a href="#281">281</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_282"

><td id="282"><a href="#282">282</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_283"

><td id="283"><a href="#283">283</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_284"

><td id="284"><a href="#284">284</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_285"

><td id="285"><a href="#285">285</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_286"

><td id="286"><a href="#286">286</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_287"

><td id="287"><a href="#287">287</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_288"

><td id="288"><a href="#288">288</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_289"

><td id="289"><a href="#289">289</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_290"

><td id="290"><a href="#290">290</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_291"

><td id="291"><a href="#291">291</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_292"

><td id="292"><a href="#292">292</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_293"

><td id="293"><a href="#293">293</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_294"

><td id="294"><a href="#294">294</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_295"

><td id="295"><a href="#295">295</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_296"

><td id="296"><a href="#296">296</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_297"

><td id="297"><a href="#297">297</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_298"

><td id="298"><a href="#298">298</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_299"

><td id="299"><a href="#299">299</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_300"

><td id="300"><a href="#300">300</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_301"

><td id="301"><a href="#301">301</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_302"

><td id="302"><a href="#302">302</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_303"

><td id="303"><a href="#303">303</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_304"

><td id="304"><a href="#304">304</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_305"

><td id="305"><a href="#305">305</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_306"

><td id="306"><a href="#306">306</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_307"

><td id="307"><a href="#307">307</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_308"

><td id="308"><a href="#308">308</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_309"

><td id="309"><a href="#309">309</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_310"

><td id="310"><a href="#310">310</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_311"

><td id="311"><a href="#311">311</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_312"

><td id="312"><a href="#312">312</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_313"

><td id="313"><a href="#313">313</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_314"

><td id="314"><a href="#314">314</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_315"

><td id="315"><a href="#315">315</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_316"

><td id="316"><a href="#316">316</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_317"

><td id="317"><a href="#317">317</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_318"

><td id="318"><a href="#318">318</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_319"

><td id="319"><a href="#319">319</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_320"

><td id="320"><a href="#320">320</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_321"

><td id="321"><a href="#321">321</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_322"

><td id="322"><a href="#322">322</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_323"

><td id="323"><a href="#323">323</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_324"

><td id="324"><a href="#324">324</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_325"

><td id="325"><a href="#325">325</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_326"

><td id="326"><a href="#326">326</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_327"

><td id="327"><a href="#327">327</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_328"

><td id="328"><a href="#328">328</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_329"

><td id="329"><a href="#329">329</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_330"

><td id="330"><a href="#330">330</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_331"

><td id="331"><a href="#331">331</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_332"

><td id="332"><a href="#332">332</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_333"

><td id="333"><a href="#333">333</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_334"

><td id="334"><a href="#334">334</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_335"

><td id="335"><a href="#335">335</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_336"

><td id="336"><a href="#336">336</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_337"

><td id="337"><a href="#337">337</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_338"

><td id="338"><a href="#338">338</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_339"

><td id="339"><a href="#339">339</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_340"

><td id="340"><a href="#340">340</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_341"

><td id="341"><a href="#341">341</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_342"

><td id="342"><a href="#342">342</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_343"

><td id="343"><a href="#343">343</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_344"

><td id="344"><a href="#344">344</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_345"

><td id="345"><a href="#345">345</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_346"

><td id="346"><a href="#346">346</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_347"

><td id="347"><a href="#347">347</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_348"

><td id="348"><a href="#348">348</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_349"

><td id="349"><a href="#349">349</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_350"

><td id="350"><a href="#350">350</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_351"

><td id="351"><a href="#351">351</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_352"

><td id="352"><a href="#352">352</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_353"

><td id="353"><a href="#353">353</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_354"

><td id="354"><a href="#354">354</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_355"

><td id="355"><a href="#355">355</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_356"

><td id="356"><a href="#356">356</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_357"

><td id="357"><a href="#357">357</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_358"

><td id="358"><a href="#358">358</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_359"

><td id="359"><a href="#359">359</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_360"

><td id="360"><a href="#360">360</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_361"

><td id="361"><a href="#361">361</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_362"

><td id="362"><a href="#362">362</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_363"

><td id="363"><a href="#363">363</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_364"

><td id="364"><a href="#364">364</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_365"

><td id="365"><a href="#365">365</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_366"

><td id="366"><a href="#366">366</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_367"

><td id="367"><a href="#367">367</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_368"

><td id="368"><a href="#368">368</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_369"

><td id="369"><a href="#369">369</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_370"

><td id="370"><a href="#370">370</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_371"

><td id="371"><a href="#371">371</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_372"

><td id="372"><a href="#372">372</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_373"

><td id="373"><a href="#373">373</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_374"

><td id="374"><a href="#374">374</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_375"

><td id="375"><a href="#375">375</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_376"

><td id="376"><a href="#376">376</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_377"

><td id="377"><a href="#377">377</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_378"

><td id="378"><a href="#378">378</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_379"

><td id="379"><a href="#379">379</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_380"

><td id="380"><a href="#380">380</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_381"

><td id="381"><a href="#381">381</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_382"

><td id="382"><a href="#382">382</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_383"

><td id="383"><a href="#383">383</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_384"

><td id="384"><a href="#384">384</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_385"

><td id="385"><a href="#385">385</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_386"

><td id="386"><a href="#386">386</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_387"

><td id="387"><a href="#387">387</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_388"

><td id="388"><a href="#388">388</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_389"

><td id="389"><a href="#389">389</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_390"

><td id="390"><a href="#390">390</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_391"

><td id="391"><a href="#391">391</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_392"

><td id="392"><a href="#392">392</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_393"

><td id="393"><a href="#393">393</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_394"

><td id="394"><a href="#394">394</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_395"

><td id="395"><a href="#395">395</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_396"

><td id="396"><a href="#396">396</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_397"

><td id="397"><a href="#397">397</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_398"

><td id="398"><a href="#398">398</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_399"

><td id="399"><a href="#399">399</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_400"

><td id="400"><a href="#400">400</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_401"

><td id="401"><a href="#401">401</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_402"

><td id="402"><a href="#402">402</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_403"

><td id="403"><a href="#403">403</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_404"

><td id="404"><a href="#404">404</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_405"

><td id="405"><a href="#405">405</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_406"

><td id="406"><a href="#406">406</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_407"

><td id="407"><a href="#407">407</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_408"

><td id="408"><a href="#408">408</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_409"

><td id="409"><a href="#409">409</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_410"

><td id="410"><a href="#410">410</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_411"

><td id="411"><a href="#411">411</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_412"

><td id="412"><a href="#412">412</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_413"

><td id="413"><a href="#413">413</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_414"

><td id="414"><a href="#414">414</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_415"

><td id="415"><a href="#415">415</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_416"

><td id="416"><a href="#416">416</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_417"

><td id="417"><a href="#417">417</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_418"

><td id="418"><a href="#418">418</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_419"

><td id="419"><a href="#419">419</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_420"

><td id="420"><a href="#420">420</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_421"

><td id="421"><a href="#421">421</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_422"

><td id="422"><a href="#422">422</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_423"

><td id="423"><a href="#423">423</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_424"

><td id="424"><a href="#424">424</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_425"

><td id="425"><a href="#425">425</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_426"

><td id="426"><a href="#426">426</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_427"

><td id="427"><a href="#427">427</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_428"

><td id="428"><a href="#428">428</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_429"

><td id="429"><a href="#429">429</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_430"

><td id="430"><a href="#430">430</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_431"

><td id="431"><a href="#431">431</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_432"

><td id="432"><a href="#432">432</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_433"

><td id="433"><a href="#433">433</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_434"

><td id="434"><a href="#434">434</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_435"

><td id="435"><a href="#435">435</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_436"

><td id="436"><a href="#436">436</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_437"

><td id="437"><a href="#437">437</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_438"

><td id="438"><a href="#438">438</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_439"

><td id="439"><a href="#439">439</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_440"

><td id="440"><a href="#440">440</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_441"

><td id="441"><a href="#441">441</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_442"

><td id="442"><a href="#442">442</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_443"

><td id="443"><a href="#443">443</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_444"

><td id="444"><a href="#444">444</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_445"

><td id="445"><a href="#445">445</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_446"

><td id="446"><a href="#446">446</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_447"

><td id="447"><a href="#447">447</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_448"

><td id="448"><a href="#448">448</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_449"

><td id="449"><a href="#449">449</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_450"

><td id="450"><a href="#450">450</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_451"

><td id="451"><a href="#451">451</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_452"

><td id="452"><a href="#452">452</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_453"

><td id="453"><a href="#453">453</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_454"

><td id="454"><a href="#454">454</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_455"

><td id="455"><a href="#455">455</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_456"

><td id="456"><a href="#456">456</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_457"

><td id="457"><a href="#457">457</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_458"

><td id="458"><a href="#458">458</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_459"

><td id="459"><a href="#459">459</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_460"

><td id="460"><a href="#460">460</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_461"

><td id="461"><a href="#461">461</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_462"

><td id="462"><a href="#462">462</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_463"

><td id="463"><a href="#463">463</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_464"

><td id="464"><a href="#464">464</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_465"

><td id="465"><a href="#465">465</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_466"

><td id="466"><a href="#466">466</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_467"

><td id="467"><a href="#467">467</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_468"

><td id="468"><a href="#468">468</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_469"

><td id="469"><a href="#469">469</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_470"

><td id="470"><a href="#470">470</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_471"

><td id="471"><a href="#471">471</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_472"

><td id="472"><a href="#472">472</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_473"

><td id="473"><a href="#473">473</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_474"

><td id="474"><a href="#474">474</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_475"

><td id="475"><a href="#475">475</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_476"

><td id="476"><a href="#476">476</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_477"

><td id="477"><a href="#477">477</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_478"

><td id="478"><a href="#478">478</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_479"

><td id="479"><a href="#479">479</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_480"

><td id="480"><a href="#480">480</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_481"

><td id="481"><a href="#481">481</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_482"

><td id="482"><a href="#482">482</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_483"

><td id="483"><a href="#483">483</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_484"

><td id="484"><a href="#484">484</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_485"

><td id="485"><a href="#485">485</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_486"

><td id="486"><a href="#486">486</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_487"

><td id="487"><a href="#487">487</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_488"

><td id="488"><a href="#488">488</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_489"

><td id="489"><a href="#489">489</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_490"

><td id="490"><a href="#490">490</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_491"

><td id="491"><a href="#491">491</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_492"

><td id="492"><a href="#492">492</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_493"

><td id="493"><a href="#493">493</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_494"

><td id="494"><a href="#494">494</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_495"

><td id="495"><a href="#495">495</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_496"

><td id="496"><a href="#496">496</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_497"

><td id="497"><a href="#497">497</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_498"

><td id="498"><a href="#498">498</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_499"

><td id="499"><a href="#499">499</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_500"

><td id="500"><a href="#500">500</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_501"

><td id="501"><a href="#501">501</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_502"

><td id="502"><a href="#502">502</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_503"

><td id="503"><a href="#503">503</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_504"

><td id="504"><a href="#504">504</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_505"

><td id="505"><a href="#505">505</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_506"

><td id="506"><a href="#506">506</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_507"

><td id="507"><a href="#507">507</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_508"

><td id="508"><a href="#508">508</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_509"

><td id="509"><a href="#509">509</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_510"

><td id="510"><a href="#510">510</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_511"

><td id="511"><a href="#511">511</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_512"

><td id="512"><a href="#512">512</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_513"

><td id="513"><a href="#513">513</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_514"

><td id="514"><a href="#514">514</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_515"

><td id="515"><a href="#515">515</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_516"

><td id="516"><a href="#516">516</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_517"

><td id="517"><a href="#517">517</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_518"

><td id="518"><a href="#518">518</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_519"

><td id="519"><a href="#519">519</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_520"

><td id="520"><a href="#520">520</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_521"

><td id="521"><a href="#521">521</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_522"

><td id="522"><a href="#522">522</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_523"

><td id="523"><a href="#523">523</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_524"

><td id="524"><a href="#524">524</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_525"

><td id="525"><a href="#525">525</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_526"

><td id="526"><a href="#526">526</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_527"

><td id="527"><a href="#527">527</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_528"

><td id="528"><a href="#528">528</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_529"

><td id="529"><a href="#529">529</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_530"

><td id="530"><a href="#530">530</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_531"

><td id="531"><a href="#531">531</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_532"

><td id="532"><a href="#532">532</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_533"

><td id="533"><a href="#533">533</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_534"

><td id="534"><a href="#534">534</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_535"

><td id="535"><a href="#535">535</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_536"

><td id="536"><a href="#536">536</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_537"

><td id="537"><a href="#537">537</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_538"

><td id="538"><a href="#538">538</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_539"

><td id="539"><a href="#539">539</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_540"

><td id="540"><a href="#540">540</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_541"

><td id="541"><a href="#541">541</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_542"

><td id="542"><a href="#542">542</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_543"

><td id="543"><a href="#543">543</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_544"

><td id="544"><a href="#544">544</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_545"

><td id="545"><a href="#545">545</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_546"

><td id="546"><a href="#546">546</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_547"

><td id="547"><a href="#547">547</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_548"

><td id="548"><a href="#548">548</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_549"

><td id="549"><a href="#549">549</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_550"

><td id="550"><a href="#550">550</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_551"

><td id="551"><a href="#551">551</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_552"

><td id="552"><a href="#552">552</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_553"

><td id="553"><a href="#553">553</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_554"

><td id="554"><a href="#554">554</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_555"

><td id="555"><a href="#555">555</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_556"

><td id="556"><a href="#556">556</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_557"

><td id="557"><a href="#557">557</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_558"

><td id="558"><a href="#558">558</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_559"

><td id="559"><a href="#559">559</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_560"

><td id="560"><a href="#560">560</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_561"

><td id="561"><a href="#561">561</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_562"

><td id="562"><a href="#562">562</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_563"

><td id="563"><a href="#563">563</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_564"

><td id="564"><a href="#564">564</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_565"

><td id="565"><a href="#565">565</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_566"

><td id="566"><a href="#566">566</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_567"

><td id="567"><a href="#567">567</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_568"

><td id="568"><a href="#568">568</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_569"

><td id="569"><a href="#569">569</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_570"

><td id="570"><a href="#570">570</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_571"

><td id="571"><a href="#571">571</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_572"

><td id="572"><a href="#572">572</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_573"

><td id="573"><a href="#573">573</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_574"

><td id="574"><a href="#574">574</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_575"

><td id="575"><a href="#575">575</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_576"

><td id="576"><a href="#576">576</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_577"

><td id="577"><a href="#577">577</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_578"

><td id="578"><a href="#578">578</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_579"

><td id="579"><a href="#579">579</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_580"

><td id="580"><a href="#580">580</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_581"

><td id="581"><a href="#581">581</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_582"

><td id="582"><a href="#582">582</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_583"

><td id="583"><a href="#583">583</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_584"

><td id="584"><a href="#584">584</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_585"

><td id="585"><a href="#585">585</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_586"

><td id="586"><a href="#586">586</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_587"

><td id="587"><a href="#587">587</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_588"

><td id="588"><a href="#588">588</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_589"

><td id="589"><a href="#589">589</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_590"

><td id="590"><a href="#590">590</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_591"

><td id="591"><a href="#591">591</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_592"

><td id="592"><a href="#592">592</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_593"

><td id="593"><a href="#593">593</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_594"

><td id="594"><a href="#594">594</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_595"

><td id="595"><a href="#595">595</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_596"

><td id="596"><a href="#596">596</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_597"

><td id="597"><a href="#597">597</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_598"

><td id="598"><a href="#598">598</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_599"

><td id="599"><a href="#599">599</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_600"

><td id="600"><a href="#600">600</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_601"

><td id="601"><a href="#601">601</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_602"

><td id="602"><a href="#602">602</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_603"

><td id="603"><a href="#603">603</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_604"

><td id="604"><a href="#604">604</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_605"

><td id="605"><a href="#605">605</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_606"

><td id="606"><a href="#606">606</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_607"

><td id="607"><a href="#607">607</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_608"

><td id="608"><a href="#608">608</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_609"

><td id="609"><a href="#609">609</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_610"

><td id="610"><a href="#610">610</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_611"

><td id="611"><a href="#611">611</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_612"

><td id="612"><a href="#612">612</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_613"

><td id="613"><a href="#613">613</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_614"

><td id="614"><a href="#614">614</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_615"

><td id="615"><a href="#615">615</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_616"

><td id="616"><a href="#616">616</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_617"

><td id="617"><a href="#617">617</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_618"

><td id="618"><a href="#618">618</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_619"

><td id="619"><a href="#619">619</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_620"

><td id="620"><a href="#620">620</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_621"

><td id="621"><a href="#621">621</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_622"

><td id="622"><a href="#622">622</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_623"

><td id="623"><a href="#623">623</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_624"

><td id="624"><a href="#624">624</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_625"

><td id="625"><a href="#625">625</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_626"

><td id="626"><a href="#626">626</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_627"

><td id="627"><a href="#627">627</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_628"

><td id="628"><a href="#628">628</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_629"

><td id="629"><a href="#629">629</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_630"

><td id="630"><a href="#630">630</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_631"

><td id="631"><a href="#631">631</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_632"

><td id="632"><a href="#632">632</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_633"

><td id="633"><a href="#633">633</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_634"

><td id="634"><a href="#634">634</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_635"

><td id="635"><a href="#635">635</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_636"

><td id="636"><a href="#636">636</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_637"

><td id="637"><a href="#637">637</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_638"

><td id="638"><a href="#638">638</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_639"

><td id="639"><a href="#639">639</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_640"

><td id="640"><a href="#640">640</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_641"

><td id="641"><a href="#641">641</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_642"

><td id="642"><a href="#642">642</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_643"

><td id="643"><a href="#643">643</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_644"

><td id="644"><a href="#644">644</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_645"

><td id="645"><a href="#645">645</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_646"

><td id="646"><a href="#646">646</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_647"

><td id="647"><a href="#647">647</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_648"

><td id="648"><a href="#648">648</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_649"

><td id="649"><a href="#649">649</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_650"

><td id="650"><a href="#650">650</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_651"

><td id="651"><a href="#651">651</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_652"

><td id="652"><a href="#652">652</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_653"

><td id="653"><a href="#653">653</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_654"

><td id="654"><a href="#654">654</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_655"

><td id="655"><a href="#655">655</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_656"

><td id="656"><a href="#656">656</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_657"

><td id="657"><a href="#657">657</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_658"

><td id="658"><a href="#658">658</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_659"

><td id="659"><a href="#659">659</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_660"

><td id="660"><a href="#660">660</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_661"

><td id="661"><a href="#661">661</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_662"

><td id="662"><a href="#662">662</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_663"

><td id="663"><a href="#663">663</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_664"

><td id="664"><a href="#664">664</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_665"

><td id="665"><a href="#665">665</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_666"

><td id="666"><a href="#666">666</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_667"

><td id="667"><a href="#667">667</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_668"

><td id="668"><a href="#668">668</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_669"

><td id="669"><a href="#669">669</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_670"

><td id="670"><a href="#670">670</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_671"

><td id="671"><a href="#671">671</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_672"

><td id="672"><a href="#672">672</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_673"

><td id="673"><a href="#673">673</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_674"

><td id="674"><a href="#674">674</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_675"

><td id="675"><a href="#675">675</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_676"

><td id="676"><a href="#676">676</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_677"

><td id="677"><a href="#677">677</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_678"

><td id="678"><a href="#678">678</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_679"

><td id="679"><a href="#679">679</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_680"

><td id="680"><a href="#680">680</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_681"

><td id="681"><a href="#681">681</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_682"

><td id="682"><a href="#682">682</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_683"

><td id="683"><a href="#683">683</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_684"

><td id="684"><a href="#684">684</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_685"

><td id="685"><a href="#685">685</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_686"

><td id="686"><a href="#686">686</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_687"

><td id="687"><a href="#687">687</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_688"

><td id="688"><a href="#688">688</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_689"

><td id="689"><a href="#689">689</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_690"

><td id="690"><a href="#690">690</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_691"

><td id="691"><a href="#691">691</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_692"

><td id="692"><a href="#692">692</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_693"

><td id="693"><a href="#693">693</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_694"

><td id="694"><a href="#694">694</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_695"

><td id="695"><a href="#695">695</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_696"

><td id="696"><a href="#696">696</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_697"

><td id="697"><a href="#697">697</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_698"

><td id="698"><a href="#698">698</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_699"

><td id="699"><a href="#699">699</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_700"

><td id="700"><a href="#700">700</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_701"

><td id="701"><a href="#701">701</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_702"

><td id="702"><a href="#702">702</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_703"

><td id="703"><a href="#703">703</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_704"

><td id="704"><a href="#704">704</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_705"

><td id="705"><a href="#705">705</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_706"

><td id="706"><a href="#706">706</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_707"

><td id="707"><a href="#707">707</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_708"

><td id="708"><a href="#708">708</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_709"

><td id="709"><a href="#709">709</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_710"

><td id="710"><a href="#710">710</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_711"

><td id="711"><a href="#711">711</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_712"

><td id="712"><a href="#712">712</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_713"

><td id="713"><a href="#713">713</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_714"

><td id="714"><a href="#714">714</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_715"

><td id="715"><a href="#715">715</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_716"

><td id="716"><a href="#716">716</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_717"

><td id="717"><a href="#717">717</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_718"

><td id="718"><a href="#718">718</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_719"

><td id="719"><a href="#719">719</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_720"

><td id="720"><a href="#720">720</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_721"

><td id="721"><a href="#721">721</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_722"

><td id="722"><a href="#722">722</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_723"

><td id="723"><a href="#723">723</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_724"

><td id="724"><a href="#724">724</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_725"

><td id="725"><a href="#725">725</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_726"

><td id="726"><a href="#726">726</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_727"

><td id="727"><a href="#727">727</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_728"

><td id="728"><a href="#728">728</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_729"

><td id="729"><a href="#729">729</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_730"

><td id="730"><a href="#730">730</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_731"

><td id="731"><a href="#731">731</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_732"

><td id="732"><a href="#732">732</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_733"

><td id="733"><a href="#733">733</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_734"

><td id="734"><a href="#734">734</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_735"

><td id="735"><a href="#735">735</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_736"

><td id="736"><a href="#736">736</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_737"

><td id="737"><a href="#737">737</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_738"

><td id="738"><a href="#738">738</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_739"

><td id="739"><a href="#739">739</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_740"

><td id="740"><a href="#740">740</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_741"

><td id="741"><a href="#741">741</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_742"

><td id="742"><a href="#742">742</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_743"

><td id="743"><a href="#743">743</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_744"

><td id="744"><a href="#744">744</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_745"

><td id="745"><a href="#745">745</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_746"

><td id="746"><a href="#746">746</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_747"

><td id="747"><a href="#747">747</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_748"

><td id="748"><a href="#748">748</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_749"

><td id="749"><a href="#749">749</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_750"

><td id="750"><a href="#750">750</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_751"

><td id="751"><a href="#751">751</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_752"

><td id="752"><a href="#752">752</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_753"

><td id="753"><a href="#753">753</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_754"

><td id="754"><a href="#754">754</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_755"

><td id="755"><a href="#755">755</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_756"

><td id="756"><a href="#756">756</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_757"

><td id="757"><a href="#757">757</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_758"

><td id="758"><a href="#758">758</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_759"

><td id="759"><a href="#759">759</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_760"

><td id="760"><a href="#760">760</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_761"

><td id="761"><a href="#761">761</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_762"

><td id="762"><a href="#762">762</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_763"

><td id="763"><a href="#763">763</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_764"

><td id="764"><a href="#764">764</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_765"

><td id="765"><a href="#765">765</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_766"

><td id="766"><a href="#766">766</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_767"

><td id="767"><a href="#767">767</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_768"

><td id="768"><a href="#768">768</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_769"

><td id="769"><a href="#769">769</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_770"

><td id="770"><a href="#770">770</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_771"

><td id="771"><a href="#771">771</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_772"

><td id="772"><a href="#772">772</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_773"

><td id="773"><a href="#773">773</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_774"

><td id="774"><a href="#774">774</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_775"

><td id="775"><a href="#775">775</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_776"

><td id="776"><a href="#776">776</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_777"

><td id="777"><a href="#777">777</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_778"

><td id="778"><a href="#778">778</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_779"

><td id="779"><a href="#779">779</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_780"

><td id="780"><a href="#780">780</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_781"

><td id="781"><a href="#781">781</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_782"

><td id="782"><a href="#782">782</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_783"

><td id="783"><a href="#783">783</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_784"

><td id="784"><a href="#784">784</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_785"

><td id="785"><a href="#785">785</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_786"

><td id="786"><a href="#786">786</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_787"

><td id="787"><a href="#787">787</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_788"

><td id="788"><a href="#788">788</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_789"

><td id="789"><a href="#789">789</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_790"

><td id="790"><a href="#790">790</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_791"

><td id="791"><a href="#791">791</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_792"

><td id="792"><a href="#792">792</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_793"

><td id="793"><a href="#793">793</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_794"

><td id="794"><a href="#794">794</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_795"

><td id="795"><a href="#795">795</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_796"

><td id="796"><a href="#796">796</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_797"

><td id="797"><a href="#797">797</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_798"

><td id="798"><a href="#798">798</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_799"

><td id="799"><a href="#799">799</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_800"

><td id="800"><a href="#800">800</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_801"

><td id="801"><a href="#801">801</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_802"

><td id="802"><a href="#802">802</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_803"

><td id="803"><a href="#803">803</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_804"

><td id="804"><a href="#804">804</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_805"

><td id="805"><a href="#805">805</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_806"

><td id="806"><a href="#806">806</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_807"

><td id="807"><a href="#807">807</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_808"

><td id="808"><a href="#808">808</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_809"

><td id="809"><a href="#809">809</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_810"

><td id="810"><a href="#810">810</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_811"

><td id="811"><a href="#811">811</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_812"

><td id="812"><a href="#812">812</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_813"

><td id="813"><a href="#813">813</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_814"

><td id="814"><a href="#814">814</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_815"

><td id="815"><a href="#815">815</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_816"

><td id="816"><a href="#816">816</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_817"

><td id="817"><a href="#817">817</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_818"

><td id="818"><a href="#818">818</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_819"

><td id="819"><a href="#819">819</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_820"

><td id="820"><a href="#820">820</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_821"

><td id="821"><a href="#821">821</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_822"

><td id="822"><a href="#822">822</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_823"

><td id="823"><a href="#823">823</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_824"

><td id="824"><a href="#824">824</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_825"

><td id="825"><a href="#825">825</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_826"

><td id="826"><a href="#826">826</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_827"

><td id="827"><a href="#827">827</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_828"

><td id="828"><a href="#828">828</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_829"

><td id="829"><a href="#829">829</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_830"

><td id="830"><a href="#830">830</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_831"

><td id="831"><a href="#831">831</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_832"

><td id="832"><a href="#832">832</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_833"

><td id="833"><a href="#833">833</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_834"

><td id="834"><a href="#834">834</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_835"

><td id="835"><a href="#835">835</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_836"

><td id="836"><a href="#836">836</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_837"

><td id="837"><a href="#837">837</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_838"

><td id="838"><a href="#838">838</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_839"

><td id="839"><a href="#839">839</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_840"

><td id="840"><a href="#840">840</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_841"

><td id="841"><a href="#841">841</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_842"

><td id="842"><a href="#842">842</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_843"

><td id="843"><a href="#843">843</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_844"

><td id="844"><a href="#844">844</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_845"

><td id="845"><a href="#845">845</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_846"

><td id="846"><a href="#846">846</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_847"

><td id="847"><a href="#847">847</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_848"

><td id="848"><a href="#848">848</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_849"

><td id="849"><a href="#849">849</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_850"

><td id="850"><a href="#850">850</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_851"

><td id="851"><a href="#851">851</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_852"

><td id="852"><a href="#852">852</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_853"

><td id="853"><a href="#853">853</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_854"

><td id="854"><a href="#854">854</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_855"

><td id="855"><a href="#855">855</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_856"

><td id="856"><a href="#856">856</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_857"

><td id="857"><a href="#857">857</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_858"

><td id="858"><a href="#858">858</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_859"

><td id="859"><a href="#859">859</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_860"

><td id="860"><a href="#860">860</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_861"

><td id="861"><a href="#861">861</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_862"

><td id="862"><a href="#862">862</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_863"

><td id="863"><a href="#863">863</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_864"

><td id="864"><a href="#864">864</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_865"

><td id="865"><a href="#865">865</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_866"

><td id="866"><a href="#866">866</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_867"

><td id="867"><a href="#867">867</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_868"

><td id="868"><a href="#868">868</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_869"

><td id="869"><a href="#869">869</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_870"

><td id="870"><a href="#870">870</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_871"

><td id="871"><a href="#871">871</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_872"

><td id="872"><a href="#872">872</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_873"

><td id="873"><a href="#873">873</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_874"

><td id="874"><a href="#874">874</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_875"

><td id="875"><a href="#875">875</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_876"

><td id="876"><a href="#876">876</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_877"

><td id="877"><a href="#877">877</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_878"

><td id="878"><a href="#878">878</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_879"

><td id="879"><a href="#879">879</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_880"

><td id="880"><a href="#880">880</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_881"

><td id="881"><a href="#881">881</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_882"

><td id="882"><a href="#882">882</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_883"

><td id="883"><a href="#883">883</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_884"

><td id="884"><a href="#884">884</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_885"

><td id="885"><a href="#885">885</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_886"

><td id="886"><a href="#886">886</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_887"

><td id="887"><a href="#887">887</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_888"

><td id="888"><a href="#888">888</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_889"

><td id="889"><a href="#889">889</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_890"

><td id="890"><a href="#890">890</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_891"

><td id="891"><a href="#891">891</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_892"

><td id="892"><a href="#892">892</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_893"

><td id="893"><a href="#893">893</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_894"

><td id="894"><a href="#894">894</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_895"

><td id="895"><a href="#895">895</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_896"

><td id="896"><a href="#896">896</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_897"

><td id="897"><a href="#897">897</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_898"

><td id="898"><a href="#898">898</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_899"

><td id="899"><a href="#899">899</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_900"

><td id="900"><a href="#900">900</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_901"

><td id="901"><a href="#901">901</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_902"

><td id="902"><a href="#902">902</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_903"

><td id="903"><a href="#903">903</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_904"

><td id="904"><a href="#904">904</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_905"

><td id="905"><a href="#905">905</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_906"

><td id="906"><a href="#906">906</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_907"

><td id="907"><a href="#907">907</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_908"

><td id="908"><a href="#908">908</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_909"

><td id="909"><a href="#909">909</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_910"

><td id="910"><a href="#910">910</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_911"

><td id="911"><a href="#911">911</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_912"

><td id="912"><a href="#912">912</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_913"

><td id="913"><a href="#913">913</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_914"

><td id="914"><a href="#914">914</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_915"

><td id="915"><a href="#915">915</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_916"

><td id="916"><a href="#916">916</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_917"

><td id="917"><a href="#917">917</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_918"

><td id="918"><a href="#918">918</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_919"

><td id="919"><a href="#919">919</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_920"

><td id="920"><a href="#920">920</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_921"

><td id="921"><a href="#921">921</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_922"

><td id="922"><a href="#922">922</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_923"

><td id="923"><a href="#923">923</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_924"

><td id="924"><a href="#924">924</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_925"

><td id="925"><a href="#925">925</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_926"

><td id="926"><a href="#926">926</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_927"

><td id="927"><a href="#927">927</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_928"

><td id="928"><a href="#928">928</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_929"

><td id="929"><a href="#929">929</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_930"

><td id="930"><a href="#930">930</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_931"

><td id="931"><a href="#931">931</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_932"

><td id="932"><a href="#932">932</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_933"

><td id="933"><a href="#933">933</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_934"

><td id="934"><a href="#934">934</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_935"

><td id="935"><a href="#935">935</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_936"

><td id="936"><a href="#936">936</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_937"

><td id="937"><a href="#937">937</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_938"

><td id="938"><a href="#938">938</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_939"

><td id="939"><a href="#939">939</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_940"

><td id="940"><a href="#940">940</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_941"

><td id="941"><a href="#941">941</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_942"

><td id="942"><a href="#942">942</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_943"

><td id="943"><a href="#943">943</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_944"

><td id="944"><a href="#944">944</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_945"

><td id="945"><a href="#945">945</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_946"

><td id="946"><a href="#946">946</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_947"

><td id="947"><a href="#947">947</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_948"

><td id="948"><a href="#948">948</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_949"

><td id="949"><a href="#949">949</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_950"

><td id="950"><a href="#950">950</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_951"

><td id="951"><a href="#951">951</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_952"

><td id="952"><a href="#952">952</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_953"

><td id="953"><a href="#953">953</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_954"

><td id="954"><a href="#954">954</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_955"

><td id="955"><a href="#955">955</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_956"

><td id="956"><a href="#956">956</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_957"

><td id="957"><a href="#957">957</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_958"

><td id="958"><a href="#958">958</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_959"

><td id="959"><a href="#959">959</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_960"

><td id="960"><a href="#960">960</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_961"

><td id="961"><a href="#961">961</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_962"

><td id="962"><a href="#962">962</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_963"

><td id="963"><a href="#963">963</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_964"

><td id="964"><a href="#964">964</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_965"

><td id="965"><a href="#965">965</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_966"

><td id="966"><a href="#966">966</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_967"

><td id="967"><a href="#967">967</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_968"

><td id="968"><a href="#968">968</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_969"

><td id="969"><a href="#969">969</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_970"

><td id="970"><a href="#970">970</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_971"

><td id="971"><a href="#971">971</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_972"

><td id="972"><a href="#972">972</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_973"

><td id="973"><a href="#973">973</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_974"

><td id="974"><a href="#974">974</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_975"

><td id="975"><a href="#975">975</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_976"

><td id="976"><a href="#976">976</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_977"

><td id="977"><a href="#977">977</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_978"

><td id="978"><a href="#978">978</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_979"

><td id="979"><a href="#979">979</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_980"

><td id="980"><a href="#980">980</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_981"

><td id="981"><a href="#981">981</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_982"

><td id="982"><a href="#982">982</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_983"

><td id="983"><a href="#983">983</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_984"

><td id="984"><a href="#984">984</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_985"

><td id="985"><a href="#985">985</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_986"

><td id="986"><a href="#986">986</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_987"

><td id="987"><a href="#987">987</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_988"

><td id="988"><a href="#988">988</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_989"

><td id="989"><a href="#989">989</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_990"

><td id="990"><a href="#990">990</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_991"

><td id="991"><a href="#991">991</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_992"

><td id="992"><a href="#992">992</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_993"

><td id="993"><a href="#993">993</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_994"

><td id="994"><a href="#994">994</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_995"

><td id="995"><a href="#995">995</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_996"

><td id="996"><a href="#996">996</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_997"

><td id="997"><a href="#997">997</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_998"

><td id="998"><a href="#998">998</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_999"

><td id="999"><a href="#999">999</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1000"

><td id="1000"><a href="#1000">1000</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1001"

><td id="1001"><a href="#1001">1001</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1002"

><td id="1002"><a href="#1002">1002</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1003"

><td id="1003"><a href="#1003">1003</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1004"

><td id="1004"><a href="#1004">1004</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1005"

><td id="1005"><a href="#1005">1005</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1006"

><td id="1006"><a href="#1006">1006</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1007"

><td id="1007"><a href="#1007">1007</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1008"

><td id="1008"><a href="#1008">1008</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1009"

><td id="1009"><a href="#1009">1009</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1010"

><td id="1010"><a href="#1010">1010</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1011"

><td id="1011"><a href="#1011">1011</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1012"

><td id="1012"><a href="#1012">1012</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1013"

><td id="1013"><a href="#1013">1013</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1014"

><td id="1014"><a href="#1014">1014</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1015"

><td id="1015"><a href="#1015">1015</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1016"

><td id="1016"><a href="#1016">1016</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1017"

><td id="1017"><a href="#1017">1017</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1018"

><td id="1018"><a href="#1018">1018</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1019"

><td id="1019"><a href="#1019">1019</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1020"

><td id="1020"><a href="#1020">1020</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1021"

><td id="1021"><a href="#1021">1021</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1022"

><td id="1022"><a href="#1022">1022</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1023"

><td id="1023"><a href="#1023">1023</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1024"

><td id="1024"><a href="#1024">1024</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1025"

><td id="1025"><a href="#1025">1025</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1026"

><td id="1026"><a href="#1026">1026</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1027"

><td id="1027"><a href="#1027">1027</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1028"

><td id="1028"><a href="#1028">1028</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1029"

><td id="1029"><a href="#1029">1029</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1030"

><td id="1030"><a href="#1030">1030</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1031"

><td id="1031"><a href="#1031">1031</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1032"

><td id="1032"><a href="#1032">1032</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1033"

><td id="1033"><a href="#1033">1033</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1034"

><td id="1034"><a href="#1034">1034</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1035"

><td id="1035"><a href="#1035">1035</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1036"

><td id="1036"><a href="#1036">1036</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1037"

><td id="1037"><a href="#1037">1037</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1038"

><td id="1038"><a href="#1038">1038</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1039"

><td id="1039"><a href="#1039">1039</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1040"

><td id="1040"><a href="#1040">1040</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1041"

><td id="1041"><a href="#1041">1041</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1042"

><td id="1042"><a href="#1042">1042</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1043"

><td id="1043"><a href="#1043">1043</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1044"

><td id="1044"><a href="#1044">1044</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1045"

><td id="1045"><a href="#1045">1045</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1046"

><td id="1046"><a href="#1046">1046</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1047"

><td id="1047"><a href="#1047">1047</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1048"

><td id="1048"><a href="#1048">1048</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1049"

><td id="1049"><a href="#1049">1049</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1050"

><td id="1050"><a href="#1050">1050</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1051"

><td id="1051"><a href="#1051">1051</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1052"

><td id="1052"><a href="#1052">1052</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1053"

><td id="1053"><a href="#1053">1053</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1054"

><td id="1054"><a href="#1054">1054</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1055"

><td id="1055"><a href="#1055">1055</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1056"

><td id="1056"><a href="#1056">1056</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1057"

><td id="1057"><a href="#1057">1057</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1058"

><td id="1058"><a href="#1058">1058</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1059"

><td id="1059"><a href="#1059">1059</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1060"

><td id="1060"><a href="#1060">1060</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1061"

><td id="1061"><a href="#1061">1061</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1062"

><td id="1062"><a href="#1062">1062</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1063"

><td id="1063"><a href="#1063">1063</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1064"

><td id="1064"><a href="#1064">1064</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1065"

><td id="1065"><a href="#1065">1065</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1066"

><td id="1066"><a href="#1066">1066</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1067"

><td id="1067"><a href="#1067">1067</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1068"

><td id="1068"><a href="#1068">1068</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1069"

><td id="1069"><a href="#1069">1069</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1070"

><td id="1070"><a href="#1070">1070</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1071"

><td id="1071"><a href="#1071">1071</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1072"

><td id="1072"><a href="#1072">1072</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1073"

><td id="1073"><a href="#1073">1073</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1074"

><td id="1074"><a href="#1074">1074</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1075"

><td id="1075"><a href="#1075">1075</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1076"

><td id="1076"><a href="#1076">1076</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1077"

><td id="1077"><a href="#1077">1077</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1078"

><td id="1078"><a href="#1078">1078</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1079"

><td id="1079"><a href="#1079">1079</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1080"

><td id="1080"><a href="#1080">1080</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1081"

><td id="1081"><a href="#1081">1081</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1082"

><td id="1082"><a href="#1082">1082</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1083"

><td id="1083"><a href="#1083">1083</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1084"

><td id="1084"><a href="#1084">1084</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1085"

><td id="1085"><a href="#1085">1085</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1086"

><td id="1086"><a href="#1086">1086</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1087"

><td id="1087"><a href="#1087">1087</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1088"

><td id="1088"><a href="#1088">1088</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1089"

><td id="1089"><a href="#1089">1089</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1090"

><td id="1090"><a href="#1090">1090</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1091"

><td id="1091"><a href="#1091">1091</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1092"

><td id="1092"><a href="#1092">1092</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1093"

><td id="1093"><a href="#1093">1093</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1094"

><td id="1094"><a href="#1094">1094</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1095"

><td id="1095"><a href="#1095">1095</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1096"

><td id="1096"><a href="#1096">1096</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1097"

><td id="1097"><a href="#1097">1097</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1098"

><td id="1098"><a href="#1098">1098</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1099"

><td id="1099"><a href="#1099">1099</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1100"

><td id="1100"><a href="#1100">1100</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1101"

><td id="1101"><a href="#1101">1101</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1102"

><td id="1102"><a href="#1102">1102</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1103"

><td id="1103"><a href="#1103">1103</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1104"

><td id="1104"><a href="#1104">1104</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1105"

><td id="1105"><a href="#1105">1105</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1106"

><td id="1106"><a href="#1106">1106</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1107"

><td id="1107"><a href="#1107">1107</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1108"

><td id="1108"><a href="#1108">1108</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1109"

><td id="1109"><a href="#1109">1109</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1110"

><td id="1110"><a href="#1110">1110</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1111"

><td id="1111"><a href="#1111">1111</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1112"

><td id="1112"><a href="#1112">1112</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1113"

><td id="1113"><a href="#1113">1113</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1114"

><td id="1114"><a href="#1114">1114</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1115"

><td id="1115"><a href="#1115">1115</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1116"

><td id="1116"><a href="#1116">1116</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1117"

><td id="1117"><a href="#1117">1117</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1118"

><td id="1118"><a href="#1118">1118</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1119"

><td id="1119"><a href="#1119">1119</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1120"

><td id="1120"><a href="#1120">1120</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1121"

><td id="1121"><a href="#1121">1121</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1122"

><td id="1122"><a href="#1122">1122</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1123"

><td id="1123"><a href="#1123">1123</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1124"

><td id="1124"><a href="#1124">1124</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1125"

><td id="1125"><a href="#1125">1125</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1126"

><td id="1126"><a href="#1126">1126</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1127"

><td id="1127"><a href="#1127">1127</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1128"

><td id="1128"><a href="#1128">1128</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1129"

><td id="1129"><a href="#1129">1129</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1130"

><td id="1130"><a href="#1130">1130</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1131"

><td id="1131"><a href="#1131">1131</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1132"

><td id="1132"><a href="#1132">1132</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1133"

><td id="1133"><a href="#1133">1133</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1134"

><td id="1134"><a href="#1134">1134</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1135"

><td id="1135"><a href="#1135">1135</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1136"

><td id="1136"><a href="#1136">1136</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1137"

><td id="1137"><a href="#1137">1137</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1138"

><td id="1138"><a href="#1138">1138</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1139"

><td id="1139"><a href="#1139">1139</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1140"

><td id="1140"><a href="#1140">1140</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1141"

><td id="1141"><a href="#1141">1141</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1142"

><td id="1142"><a href="#1142">1142</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1143"

><td id="1143"><a href="#1143">1143</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1144"

><td id="1144"><a href="#1144">1144</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1145"

><td id="1145"><a href="#1145">1145</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1146"

><td id="1146"><a href="#1146">1146</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1147"

><td id="1147"><a href="#1147">1147</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1148"

><td id="1148"><a href="#1148">1148</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1149"

><td id="1149"><a href="#1149">1149</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1150"

><td id="1150"><a href="#1150">1150</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1151"

><td id="1151"><a href="#1151">1151</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1152"

><td id="1152"><a href="#1152">1152</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1153"

><td id="1153"><a href="#1153">1153</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1154"

><td id="1154"><a href="#1154">1154</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1155"

><td id="1155"><a href="#1155">1155</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1156"

><td id="1156"><a href="#1156">1156</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1157"

><td id="1157"><a href="#1157">1157</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1158"

><td id="1158"><a href="#1158">1158</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1159"

><td id="1159"><a href="#1159">1159</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1160"

><td id="1160"><a href="#1160">1160</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1161"

><td id="1161"><a href="#1161">1161</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1162"

><td id="1162"><a href="#1162">1162</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1163"

><td id="1163"><a href="#1163">1163</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1164"

><td id="1164"><a href="#1164">1164</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1165"

><td id="1165"><a href="#1165">1165</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1166"

><td id="1166"><a href="#1166">1166</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1167"

><td id="1167"><a href="#1167">1167</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1168"

><td id="1168"><a href="#1168">1168</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1169"

><td id="1169"><a href="#1169">1169</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1170"

><td id="1170"><a href="#1170">1170</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1171"

><td id="1171"><a href="#1171">1171</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1172"

><td id="1172"><a href="#1172">1172</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1173"

><td id="1173"><a href="#1173">1173</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1174"

><td id="1174"><a href="#1174">1174</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1175"

><td id="1175"><a href="#1175">1175</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1176"

><td id="1176"><a href="#1176">1176</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1177"

><td id="1177"><a href="#1177">1177</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1178"

><td id="1178"><a href="#1178">1178</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1179"

><td id="1179"><a href="#1179">1179</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1180"

><td id="1180"><a href="#1180">1180</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1181"

><td id="1181"><a href="#1181">1181</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1182"

><td id="1182"><a href="#1182">1182</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1183"

><td id="1183"><a href="#1183">1183</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1184"

><td id="1184"><a href="#1184">1184</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1185"

><td id="1185"><a href="#1185">1185</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1186"

><td id="1186"><a href="#1186">1186</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1187"

><td id="1187"><a href="#1187">1187</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1188"

><td id="1188"><a href="#1188">1188</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1189"

><td id="1189"><a href="#1189">1189</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1190"

><td id="1190"><a href="#1190">1190</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1191"

><td id="1191"><a href="#1191">1191</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1192"

><td id="1192"><a href="#1192">1192</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1193"

><td id="1193"><a href="#1193">1193</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1194"

><td id="1194"><a href="#1194">1194</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1195"

><td id="1195"><a href="#1195">1195</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1196"

><td id="1196"><a href="#1196">1196</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1197"

><td id="1197"><a href="#1197">1197</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1198"

><td id="1198"><a href="#1198">1198</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1199"

><td id="1199"><a href="#1199">1199</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1200"

><td id="1200"><a href="#1200">1200</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1201"

><td id="1201"><a href="#1201">1201</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1202"

><td id="1202"><a href="#1202">1202</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1203"

><td id="1203"><a href="#1203">1203</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1204"

><td id="1204"><a href="#1204">1204</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1205"

><td id="1205"><a href="#1205">1205</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1206"

><td id="1206"><a href="#1206">1206</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1207"

><td id="1207"><a href="#1207">1207</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1208"

><td id="1208"><a href="#1208">1208</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1209"

><td id="1209"><a href="#1209">1209</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1210"

><td id="1210"><a href="#1210">1210</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1211"

><td id="1211"><a href="#1211">1211</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1212"

><td id="1212"><a href="#1212">1212</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1213"

><td id="1213"><a href="#1213">1213</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1214"

><td id="1214"><a href="#1214">1214</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1215"

><td id="1215"><a href="#1215">1215</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1216"

><td id="1216"><a href="#1216">1216</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1217"

><td id="1217"><a href="#1217">1217</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1218"

><td id="1218"><a href="#1218">1218</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1219"

><td id="1219"><a href="#1219">1219</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1220"

><td id="1220"><a href="#1220">1220</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1221"

><td id="1221"><a href="#1221">1221</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1222"

><td id="1222"><a href="#1222">1222</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1223"

><td id="1223"><a href="#1223">1223</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1224"

><td id="1224"><a href="#1224">1224</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1225"

><td id="1225"><a href="#1225">1225</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1226"

><td id="1226"><a href="#1226">1226</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1227"

><td id="1227"><a href="#1227">1227</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1228"

><td id="1228"><a href="#1228">1228</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1229"

><td id="1229"><a href="#1229">1229</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1230"

><td id="1230"><a href="#1230">1230</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1231"

><td id="1231"><a href="#1231">1231</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1232"

><td id="1232"><a href="#1232">1232</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1233"

><td id="1233"><a href="#1233">1233</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1234"

><td id="1234"><a href="#1234">1234</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1235"

><td id="1235"><a href="#1235">1235</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1236"

><td id="1236"><a href="#1236">1236</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1237"

><td id="1237"><a href="#1237">1237</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1238"

><td id="1238"><a href="#1238">1238</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1239"

><td id="1239"><a href="#1239">1239</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1240"

><td id="1240"><a href="#1240">1240</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1241"

><td id="1241"><a href="#1241">1241</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1242"

><td id="1242"><a href="#1242">1242</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1243"

><td id="1243"><a href="#1243">1243</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1244"

><td id="1244"><a href="#1244">1244</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1245"

><td id="1245"><a href="#1245">1245</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1246"

><td id="1246"><a href="#1246">1246</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1247"

><td id="1247"><a href="#1247">1247</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1248"

><td id="1248"><a href="#1248">1248</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1249"

><td id="1249"><a href="#1249">1249</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1250"

><td id="1250"><a href="#1250">1250</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1251"

><td id="1251"><a href="#1251">1251</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1252"

><td id="1252"><a href="#1252">1252</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1253"

><td id="1253"><a href="#1253">1253</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1254"

><td id="1254"><a href="#1254">1254</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1255"

><td id="1255"><a href="#1255">1255</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1256"

><td id="1256"><a href="#1256">1256</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1257"

><td id="1257"><a href="#1257">1257</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1258"

><td id="1258"><a href="#1258">1258</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1259"

><td id="1259"><a href="#1259">1259</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1260"

><td id="1260"><a href="#1260">1260</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1261"

><td id="1261"><a href="#1261">1261</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1262"

><td id="1262"><a href="#1262">1262</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1263"

><td id="1263"><a href="#1263">1263</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1264"

><td id="1264"><a href="#1264">1264</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1265"

><td id="1265"><a href="#1265">1265</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1266"

><td id="1266"><a href="#1266">1266</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1267"

><td id="1267"><a href="#1267">1267</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1268"

><td id="1268"><a href="#1268">1268</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1269"

><td id="1269"><a href="#1269">1269</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1270"

><td id="1270"><a href="#1270">1270</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1271"

><td id="1271"><a href="#1271">1271</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1272"

><td id="1272"><a href="#1272">1272</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1273"

><td id="1273"><a href="#1273">1273</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1274"

><td id="1274"><a href="#1274">1274</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1275"

><td id="1275"><a href="#1275">1275</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1276"

><td id="1276"><a href="#1276">1276</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1277"

><td id="1277"><a href="#1277">1277</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1278"

><td id="1278"><a href="#1278">1278</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1279"

><td id="1279"><a href="#1279">1279</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1280"

><td id="1280"><a href="#1280">1280</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1281"

><td id="1281"><a href="#1281">1281</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1282"

><td id="1282"><a href="#1282">1282</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1283"

><td id="1283"><a href="#1283">1283</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1284"

><td id="1284"><a href="#1284">1284</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1285"

><td id="1285"><a href="#1285">1285</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1286"

><td id="1286"><a href="#1286">1286</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1287"

><td id="1287"><a href="#1287">1287</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1288"

><td id="1288"><a href="#1288">1288</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1289"

><td id="1289"><a href="#1289">1289</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1290"

><td id="1290"><a href="#1290">1290</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1291"

><td id="1291"><a href="#1291">1291</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1292"

><td id="1292"><a href="#1292">1292</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1293"

><td id="1293"><a href="#1293">1293</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1294"

><td id="1294"><a href="#1294">1294</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1295"

><td id="1295"><a href="#1295">1295</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1296"

><td id="1296"><a href="#1296">1296</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1297"

><td id="1297"><a href="#1297">1297</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1298"

><td id="1298"><a href="#1298">1298</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1299"

><td id="1299"><a href="#1299">1299</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1300"

><td id="1300"><a href="#1300">1300</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1301"

><td id="1301"><a href="#1301">1301</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1302"

><td id="1302"><a href="#1302">1302</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1303"

><td id="1303"><a href="#1303">1303</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1304"

><td id="1304"><a href="#1304">1304</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1305"

><td id="1305"><a href="#1305">1305</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1306"

><td id="1306"><a href="#1306">1306</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1307"

><td id="1307"><a href="#1307">1307</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1308"

><td id="1308"><a href="#1308">1308</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1309"

><td id="1309"><a href="#1309">1309</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1310"

><td id="1310"><a href="#1310">1310</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1311"

><td id="1311"><a href="#1311">1311</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1312"

><td id="1312"><a href="#1312">1312</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1313"

><td id="1313"><a href="#1313">1313</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1314"

><td id="1314"><a href="#1314">1314</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1315"

><td id="1315"><a href="#1315">1315</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1316"

><td id="1316"><a href="#1316">1316</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1317"

><td id="1317"><a href="#1317">1317</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1318"

><td id="1318"><a href="#1318">1318</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1319"

><td id="1319"><a href="#1319">1319</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1320"

><td id="1320"><a href="#1320">1320</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1321"

><td id="1321"><a href="#1321">1321</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1322"

><td id="1322"><a href="#1322">1322</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1323"

><td id="1323"><a href="#1323">1323</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1324"

><td id="1324"><a href="#1324">1324</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1325"

><td id="1325"><a href="#1325">1325</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1326"

><td id="1326"><a href="#1326">1326</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1327"

><td id="1327"><a href="#1327">1327</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1328"

><td id="1328"><a href="#1328">1328</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1329"

><td id="1329"><a href="#1329">1329</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1330"

><td id="1330"><a href="#1330">1330</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1331"

><td id="1331"><a href="#1331">1331</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1332"

><td id="1332"><a href="#1332">1332</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1333"

><td id="1333"><a href="#1333">1333</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1334"

><td id="1334"><a href="#1334">1334</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1335"

><td id="1335"><a href="#1335">1335</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1336"

><td id="1336"><a href="#1336">1336</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1337"

><td id="1337"><a href="#1337">1337</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1338"

><td id="1338"><a href="#1338">1338</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1339"

><td id="1339"><a href="#1339">1339</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1340"

><td id="1340"><a href="#1340">1340</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1341"

><td id="1341"><a href="#1341">1341</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1342"

><td id="1342"><a href="#1342">1342</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1343"

><td id="1343"><a href="#1343">1343</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1344"

><td id="1344"><a href="#1344">1344</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1345"

><td id="1345"><a href="#1345">1345</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1346"

><td id="1346"><a href="#1346">1346</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1347"

><td id="1347"><a href="#1347">1347</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1348"

><td id="1348"><a href="#1348">1348</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1349"

><td id="1349"><a href="#1349">1349</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1350"

><td id="1350"><a href="#1350">1350</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1351"

><td id="1351"><a href="#1351">1351</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1352"

><td id="1352"><a href="#1352">1352</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1353"

><td id="1353"><a href="#1353">1353</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1354"

><td id="1354"><a href="#1354">1354</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1355"

><td id="1355"><a href="#1355">1355</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1356"

><td id="1356"><a href="#1356">1356</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1357"

><td id="1357"><a href="#1357">1357</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1358"

><td id="1358"><a href="#1358">1358</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1359"

><td id="1359"><a href="#1359">1359</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1360"

><td id="1360"><a href="#1360">1360</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1361"

><td id="1361"><a href="#1361">1361</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1362"

><td id="1362"><a href="#1362">1362</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1363"

><td id="1363"><a href="#1363">1363</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1364"

><td id="1364"><a href="#1364">1364</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1365"

><td id="1365"><a href="#1365">1365</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1366"

><td id="1366"><a href="#1366">1366</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1367"

><td id="1367"><a href="#1367">1367</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1368"

><td id="1368"><a href="#1368">1368</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1369"

><td id="1369"><a href="#1369">1369</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1370"

><td id="1370"><a href="#1370">1370</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1371"

><td id="1371"><a href="#1371">1371</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1372"

><td id="1372"><a href="#1372">1372</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1373"

><td id="1373"><a href="#1373">1373</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1374"

><td id="1374"><a href="#1374">1374</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1375"

><td id="1375"><a href="#1375">1375</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1376"

><td id="1376"><a href="#1376">1376</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1377"

><td id="1377"><a href="#1377">1377</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1378"

><td id="1378"><a href="#1378">1378</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1379"

><td id="1379"><a href="#1379">1379</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1380"

><td id="1380"><a href="#1380">1380</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1381"

><td id="1381"><a href="#1381">1381</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1382"

><td id="1382"><a href="#1382">1382</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1383"

><td id="1383"><a href="#1383">1383</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1384"

><td id="1384"><a href="#1384">1384</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1385"

><td id="1385"><a href="#1385">1385</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1386"

><td id="1386"><a href="#1386">1386</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1387"

><td id="1387"><a href="#1387">1387</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1388"

><td id="1388"><a href="#1388">1388</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1389"

><td id="1389"><a href="#1389">1389</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1390"

><td id="1390"><a href="#1390">1390</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1391"

><td id="1391"><a href="#1391">1391</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1392"

><td id="1392"><a href="#1392">1392</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1393"

><td id="1393"><a href="#1393">1393</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1394"

><td id="1394"><a href="#1394">1394</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1395"

><td id="1395"><a href="#1395">1395</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1396"

><td id="1396"><a href="#1396">1396</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1397"

><td id="1397"><a href="#1397">1397</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1398"

><td id="1398"><a href="#1398">1398</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1399"

><td id="1399"><a href="#1399">1399</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1400"

><td id="1400"><a href="#1400">1400</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1401"

><td id="1401"><a href="#1401">1401</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1402"

><td id="1402"><a href="#1402">1402</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1403"

><td id="1403"><a href="#1403">1403</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1404"

><td id="1404"><a href="#1404">1404</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1405"

><td id="1405"><a href="#1405">1405</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1406"

><td id="1406"><a href="#1406">1406</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1407"

><td id="1407"><a href="#1407">1407</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1408"

><td id="1408"><a href="#1408">1408</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1409"

><td id="1409"><a href="#1409">1409</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1410"

><td id="1410"><a href="#1410">1410</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1411"

><td id="1411"><a href="#1411">1411</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1412"

><td id="1412"><a href="#1412">1412</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1413"

><td id="1413"><a href="#1413">1413</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1414"

><td id="1414"><a href="#1414">1414</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1415"

><td id="1415"><a href="#1415">1415</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1416"

><td id="1416"><a href="#1416">1416</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1417"

><td id="1417"><a href="#1417">1417</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1418"

><td id="1418"><a href="#1418">1418</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1419"

><td id="1419"><a href="#1419">1419</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1420"

><td id="1420"><a href="#1420">1420</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1421"

><td id="1421"><a href="#1421">1421</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1422"

><td id="1422"><a href="#1422">1422</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1423"

><td id="1423"><a href="#1423">1423</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1424"

><td id="1424"><a href="#1424">1424</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1425"

><td id="1425"><a href="#1425">1425</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1426"

><td id="1426"><a href="#1426">1426</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1427"

><td id="1427"><a href="#1427">1427</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1428"

><td id="1428"><a href="#1428">1428</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1429"

><td id="1429"><a href="#1429">1429</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1430"

><td id="1430"><a href="#1430">1430</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1431"

><td id="1431"><a href="#1431">1431</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1432"

><td id="1432"><a href="#1432">1432</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1433"

><td id="1433"><a href="#1433">1433</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1434"

><td id="1434"><a href="#1434">1434</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1435"

><td id="1435"><a href="#1435">1435</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1436"

><td id="1436"><a href="#1436">1436</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1437"

><td id="1437"><a href="#1437">1437</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1438"

><td id="1438"><a href="#1438">1438</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1439"

><td id="1439"><a href="#1439">1439</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1440"

><td id="1440"><a href="#1440">1440</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1441"

><td id="1441"><a href="#1441">1441</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1442"

><td id="1442"><a href="#1442">1442</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1443"

><td id="1443"><a href="#1443">1443</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1444"

><td id="1444"><a href="#1444">1444</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1445"

><td id="1445"><a href="#1445">1445</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1446"

><td id="1446"><a href="#1446">1446</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1447"

><td id="1447"><a href="#1447">1447</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1448"

><td id="1448"><a href="#1448">1448</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1449"

><td id="1449"><a href="#1449">1449</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1450"

><td id="1450"><a href="#1450">1450</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1451"

><td id="1451"><a href="#1451">1451</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1452"

><td id="1452"><a href="#1452">1452</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1453"

><td id="1453"><a href="#1453">1453</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1454"

><td id="1454"><a href="#1454">1454</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1455"

><td id="1455"><a href="#1455">1455</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1456"

><td id="1456"><a href="#1456">1456</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1457"

><td id="1457"><a href="#1457">1457</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1458"

><td id="1458"><a href="#1458">1458</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1459"

><td id="1459"><a href="#1459">1459</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1460"

><td id="1460"><a href="#1460">1460</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1461"

><td id="1461"><a href="#1461">1461</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1462"

><td id="1462"><a href="#1462">1462</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1463"

><td id="1463"><a href="#1463">1463</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1464"

><td id="1464"><a href="#1464">1464</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1465"

><td id="1465"><a href="#1465">1465</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1466"

><td id="1466"><a href="#1466">1466</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1467"

><td id="1467"><a href="#1467">1467</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1468"

><td id="1468"><a href="#1468">1468</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1469"

><td id="1469"><a href="#1469">1469</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1470"

><td id="1470"><a href="#1470">1470</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1471"

><td id="1471"><a href="#1471">1471</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1472"

><td id="1472"><a href="#1472">1472</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1473"

><td id="1473"><a href="#1473">1473</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1474"

><td id="1474"><a href="#1474">1474</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1475"

><td id="1475"><a href="#1475">1475</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1476"

><td id="1476"><a href="#1476">1476</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1477"

><td id="1477"><a href="#1477">1477</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1478"

><td id="1478"><a href="#1478">1478</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1479"

><td id="1479"><a href="#1479">1479</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1480"

><td id="1480"><a href="#1480">1480</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1481"

><td id="1481"><a href="#1481">1481</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1482"

><td id="1482"><a href="#1482">1482</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1483"

><td id="1483"><a href="#1483">1483</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1484"

><td id="1484"><a href="#1484">1484</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1485"

><td id="1485"><a href="#1485">1485</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1486"

><td id="1486"><a href="#1486">1486</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1487"

><td id="1487"><a href="#1487">1487</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1488"

><td id="1488"><a href="#1488">1488</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1489"

><td id="1489"><a href="#1489">1489</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1490"

><td id="1490"><a href="#1490">1490</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1491"

><td id="1491"><a href="#1491">1491</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1492"

><td id="1492"><a href="#1492">1492</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1493"

><td id="1493"><a href="#1493">1493</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1494"

><td id="1494"><a href="#1494">1494</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1495"

><td id="1495"><a href="#1495">1495</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1496"

><td id="1496"><a href="#1496">1496</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1497"

><td id="1497"><a href="#1497">1497</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1498"

><td id="1498"><a href="#1498">1498</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1499"

><td id="1499"><a href="#1499">1499</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1500"

><td id="1500"><a href="#1500">1500</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1501"

><td id="1501"><a href="#1501">1501</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1502"

><td id="1502"><a href="#1502">1502</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1503"

><td id="1503"><a href="#1503">1503</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1504"

><td id="1504"><a href="#1504">1504</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1505"

><td id="1505"><a href="#1505">1505</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1506"

><td id="1506"><a href="#1506">1506</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1507"

><td id="1507"><a href="#1507">1507</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1508"

><td id="1508"><a href="#1508">1508</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1509"

><td id="1509"><a href="#1509">1509</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1510"

><td id="1510"><a href="#1510">1510</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1511"

><td id="1511"><a href="#1511">1511</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1512"

><td id="1512"><a href="#1512">1512</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1513"

><td id="1513"><a href="#1513">1513</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1514"

><td id="1514"><a href="#1514">1514</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1515"

><td id="1515"><a href="#1515">1515</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1516"

><td id="1516"><a href="#1516">1516</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1517"

><td id="1517"><a href="#1517">1517</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1518"

><td id="1518"><a href="#1518">1518</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1519"

><td id="1519"><a href="#1519">1519</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1520"

><td id="1520"><a href="#1520">1520</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1521"

><td id="1521"><a href="#1521">1521</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1522"

><td id="1522"><a href="#1522">1522</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1523"

><td id="1523"><a href="#1523">1523</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1524"

><td id="1524"><a href="#1524">1524</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1525"

><td id="1525"><a href="#1525">1525</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1526"

><td id="1526"><a href="#1526">1526</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1527"

><td id="1527"><a href="#1527">1527</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1528"

><td id="1528"><a href="#1528">1528</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1529"

><td id="1529"><a href="#1529">1529</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1530"

><td id="1530"><a href="#1530">1530</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1531"

><td id="1531"><a href="#1531">1531</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1532"

><td id="1532"><a href="#1532">1532</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1533"

><td id="1533"><a href="#1533">1533</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1534"

><td id="1534"><a href="#1534">1534</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1535"

><td id="1535"><a href="#1535">1535</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1536"

><td id="1536"><a href="#1536">1536</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1537"

><td id="1537"><a href="#1537">1537</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1538"

><td id="1538"><a href="#1538">1538</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1539"

><td id="1539"><a href="#1539">1539</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1540"

><td id="1540"><a href="#1540">1540</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1541"

><td id="1541"><a href="#1541">1541</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1542"

><td id="1542"><a href="#1542">1542</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1543"

><td id="1543"><a href="#1543">1543</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1544"

><td id="1544"><a href="#1544">1544</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1545"

><td id="1545"><a href="#1545">1545</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1546"

><td id="1546"><a href="#1546">1546</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1547"

><td id="1547"><a href="#1547">1547</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1548"

><td id="1548"><a href="#1548">1548</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1549"

><td id="1549"><a href="#1549">1549</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1550"

><td id="1550"><a href="#1550">1550</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1551"

><td id="1551"><a href="#1551">1551</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1552"

><td id="1552"><a href="#1552">1552</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1553"

><td id="1553"><a href="#1553">1553</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1554"

><td id="1554"><a href="#1554">1554</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1555"

><td id="1555"><a href="#1555">1555</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1556"

><td id="1556"><a href="#1556">1556</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1557"

><td id="1557"><a href="#1557">1557</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1558"

><td id="1558"><a href="#1558">1558</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1559"

><td id="1559"><a href="#1559">1559</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1560"

><td id="1560"><a href="#1560">1560</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1561"

><td id="1561"><a href="#1561">1561</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1562"

><td id="1562"><a href="#1562">1562</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1563"

><td id="1563"><a href="#1563">1563</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1564"

><td id="1564"><a href="#1564">1564</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1565"

><td id="1565"><a href="#1565">1565</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1566"

><td id="1566"><a href="#1566">1566</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1567"

><td id="1567"><a href="#1567">1567</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1568"

><td id="1568"><a href="#1568">1568</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1569"

><td id="1569"><a href="#1569">1569</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1570"

><td id="1570"><a href="#1570">1570</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1571"

><td id="1571"><a href="#1571">1571</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1572"

><td id="1572"><a href="#1572">1572</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1573"

><td id="1573"><a href="#1573">1573</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1574"

><td id="1574"><a href="#1574">1574</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1575"

><td id="1575"><a href="#1575">1575</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1576"

><td id="1576"><a href="#1576">1576</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1577"

><td id="1577"><a href="#1577">1577</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1578"

><td id="1578"><a href="#1578">1578</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1579"

><td id="1579"><a href="#1579">1579</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1580"

><td id="1580"><a href="#1580">1580</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1581"

><td id="1581"><a href="#1581">1581</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1582"

><td id="1582"><a href="#1582">1582</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1583"

><td id="1583"><a href="#1583">1583</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1584"

><td id="1584"><a href="#1584">1584</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1585"

><td id="1585"><a href="#1585">1585</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1586"

><td id="1586"><a href="#1586">1586</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1587"

><td id="1587"><a href="#1587">1587</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1588"

><td id="1588"><a href="#1588">1588</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1589"

><td id="1589"><a href="#1589">1589</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1590"

><td id="1590"><a href="#1590">1590</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1591"

><td id="1591"><a href="#1591">1591</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1592"

><td id="1592"><a href="#1592">1592</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1593"

><td id="1593"><a href="#1593">1593</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1594"

><td id="1594"><a href="#1594">1594</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1595"

><td id="1595"><a href="#1595">1595</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1596"

><td id="1596"><a href="#1596">1596</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1597"

><td id="1597"><a href="#1597">1597</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1598"

><td id="1598"><a href="#1598">1598</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1599"

><td id="1599"><a href="#1599">1599</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1600"

><td id="1600"><a href="#1600">1600</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1601"

><td id="1601"><a href="#1601">1601</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1602"

><td id="1602"><a href="#1602">1602</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1603"

><td id="1603"><a href="#1603">1603</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1604"

><td id="1604"><a href="#1604">1604</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1605"

><td id="1605"><a href="#1605">1605</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1606"

><td id="1606"><a href="#1606">1606</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1607"

><td id="1607"><a href="#1607">1607</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1608"

><td id="1608"><a href="#1608">1608</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1609"

><td id="1609"><a href="#1609">1609</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1610"

><td id="1610"><a href="#1610">1610</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1611"

><td id="1611"><a href="#1611">1611</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1612"

><td id="1612"><a href="#1612">1612</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1613"

><td id="1613"><a href="#1613">1613</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1614"

><td id="1614"><a href="#1614">1614</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1615"

><td id="1615"><a href="#1615">1615</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1616"

><td id="1616"><a href="#1616">1616</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1617"

><td id="1617"><a href="#1617">1617</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1618"

><td id="1618"><a href="#1618">1618</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1619"

><td id="1619"><a href="#1619">1619</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1620"

><td id="1620"><a href="#1620">1620</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1621"

><td id="1621"><a href="#1621">1621</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1622"

><td id="1622"><a href="#1622">1622</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1623"

><td id="1623"><a href="#1623">1623</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1624"

><td id="1624"><a href="#1624">1624</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1625"

><td id="1625"><a href="#1625">1625</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1626"

><td id="1626"><a href="#1626">1626</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1627"

><td id="1627"><a href="#1627">1627</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1628"

><td id="1628"><a href="#1628">1628</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1629"

><td id="1629"><a href="#1629">1629</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1630"

><td id="1630"><a href="#1630">1630</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1631"

><td id="1631"><a href="#1631">1631</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1632"

><td id="1632"><a href="#1632">1632</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1633"

><td id="1633"><a href="#1633">1633</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1634"

><td id="1634"><a href="#1634">1634</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1635"

><td id="1635"><a href="#1635">1635</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1636"

><td id="1636"><a href="#1636">1636</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1637"

><td id="1637"><a href="#1637">1637</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1638"

><td id="1638"><a href="#1638">1638</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1639"

><td id="1639"><a href="#1639">1639</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1640"

><td id="1640"><a href="#1640">1640</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1641"

><td id="1641"><a href="#1641">1641</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1642"

><td id="1642"><a href="#1642">1642</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1643"

><td id="1643"><a href="#1643">1643</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1644"

><td id="1644"><a href="#1644">1644</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1645"

><td id="1645"><a href="#1645">1645</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1646"

><td id="1646"><a href="#1646">1646</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1647"

><td id="1647"><a href="#1647">1647</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1648"

><td id="1648"><a href="#1648">1648</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1649"

><td id="1649"><a href="#1649">1649</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1650"

><td id="1650"><a href="#1650">1650</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1651"

><td id="1651"><a href="#1651">1651</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1652"

><td id="1652"><a href="#1652">1652</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1653"

><td id="1653"><a href="#1653">1653</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1654"

><td id="1654"><a href="#1654">1654</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1655"

><td id="1655"><a href="#1655">1655</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1656"

><td id="1656"><a href="#1656">1656</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1657"

><td id="1657"><a href="#1657">1657</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1658"

><td id="1658"><a href="#1658">1658</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1659"

><td id="1659"><a href="#1659">1659</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1660"

><td id="1660"><a href="#1660">1660</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1661"

><td id="1661"><a href="#1661">1661</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1662"

><td id="1662"><a href="#1662">1662</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1663"

><td id="1663"><a href="#1663">1663</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1664"

><td id="1664"><a href="#1664">1664</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1665"

><td id="1665"><a href="#1665">1665</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1666"

><td id="1666"><a href="#1666">1666</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1667"

><td id="1667"><a href="#1667">1667</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1668"

><td id="1668"><a href="#1668">1668</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1669"

><td id="1669"><a href="#1669">1669</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1670"

><td id="1670"><a href="#1670">1670</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1671"

><td id="1671"><a href="#1671">1671</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1672"

><td id="1672"><a href="#1672">1672</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1673"

><td id="1673"><a href="#1673">1673</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1674"

><td id="1674"><a href="#1674">1674</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1675"

><td id="1675"><a href="#1675">1675</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1676"

><td id="1676"><a href="#1676">1676</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1677"

><td id="1677"><a href="#1677">1677</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1678"

><td id="1678"><a href="#1678">1678</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1679"

><td id="1679"><a href="#1679">1679</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1680"

><td id="1680"><a href="#1680">1680</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1681"

><td id="1681"><a href="#1681">1681</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1682"

><td id="1682"><a href="#1682">1682</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1683"

><td id="1683"><a href="#1683">1683</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1684"

><td id="1684"><a href="#1684">1684</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1685"

><td id="1685"><a href="#1685">1685</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1686"

><td id="1686"><a href="#1686">1686</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1687"

><td id="1687"><a href="#1687">1687</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1688"

><td id="1688"><a href="#1688">1688</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1689"

><td id="1689"><a href="#1689">1689</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1690"

><td id="1690"><a href="#1690">1690</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1691"

><td id="1691"><a href="#1691">1691</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1692"

><td id="1692"><a href="#1692">1692</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1693"

><td id="1693"><a href="#1693">1693</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1694"

><td id="1694"><a href="#1694">1694</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1695"

><td id="1695"><a href="#1695">1695</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1696"

><td id="1696"><a href="#1696">1696</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1697"

><td id="1697"><a href="#1697">1697</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1698"

><td id="1698"><a href="#1698">1698</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1699"

><td id="1699"><a href="#1699">1699</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1700"

><td id="1700"><a href="#1700">1700</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1701"

><td id="1701"><a href="#1701">1701</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1702"

><td id="1702"><a href="#1702">1702</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1703"

><td id="1703"><a href="#1703">1703</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1704"

><td id="1704"><a href="#1704">1704</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1705"

><td id="1705"><a href="#1705">1705</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1706"

><td id="1706"><a href="#1706">1706</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1707"

><td id="1707"><a href="#1707">1707</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1708"

><td id="1708"><a href="#1708">1708</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1709"

><td id="1709"><a href="#1709">1709</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1710"

><td id="1710"><a href="#1710">1710</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1711"

><td id="1711"><a href="#1711">1711</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1712"

><td id="1712"><a href="#1712">1712</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1713"

><td id="1713"><a href="#1713">1713</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1714"

><td id="1714"><a href="#1714">1714</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1715"

><td id="1715"><a href="#1715">1715</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1716"

><td id="1716"><a href="#1716">1716</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1717"

><td id="1717"><a href="#1717">1717</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1718"

><td id="1718"><a href="#1718">1718</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1719"

><td id="1719"><a href="#1719">1719</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1720"

><td id="1720"><a href="#1720">1720</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1721"

><td id="1721"><a href="#1721">1721</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1722"

><td id="1722"><a href="#1722">1722</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1723"

><td id="1723"><a href="#1723">1723</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1724"

><td id="1724"><a href="#1724">1724</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1725"

><td id="1725"><a href="#1725">1725</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1726"

><td id="1726"><a href="#1726">1726</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1727"

><td id="1727"><a href="#1727">1727</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1728"

><td id="1728"><a href="#1728">1728</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1729"

><td id="1729"><a href="#1729">1729</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1730"

><td id="1730"><a href="#1730">1730</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1731"

><td id="1731"><a href="#1731">1731</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1732"

><td id="1732"><a href="#1732">1732</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1733"

><td id="1733"><a href="#1733">1733</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1734"

><td id="1734"><a href="#1734">1734</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1735"

><td id="1735"><a href="#1735">1735</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1736"

><td id="1736"><a href="#1736">1736</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1737"

><td id="1737"><a href="#1737">1737</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1738"

><td id="1738"><a href="#1738">1738</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1739"

><td id="1739"><a href="#1739">1739</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1740"

><td id="1740"><a href="#1740">1740</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1741"

><td id="1741"><a href="#1741">1741</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1742"

><td id="1742"><a href="#1742">1742</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1743"

><td id="1743"><a href="#1743">1743</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1744"

><td id="1744"><a href="#1744">1744</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1745"

><td id="1745"><a href="#1745">1745</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1746"

><td id="1746"><a href="#1746">1746</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1747"

><td id="1747"><a href="#1747">1747</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1748"

><td id="1748"><a href="#1748">1748</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1749"

><td id="1749"><a href="#1749">1749</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1750"

><td id="1750"><a href="#1750">1750</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1751"

><td id="1751"><a href="#1751">1751</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1752"

><td id="1752"><a href="#1752">1752</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1753"

><td id="1753"><a href="#1753">1753</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1754"

><td id="1754"><a href="#1754">1754</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1755"

><td id="1755"><a href="#1755">1755</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1756"

><td id="1756"><a href="#1756">1756</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1757"

><td id="1757"><a href="#1757">1757</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1758"

><td id="1758"><a href="#1758">1758</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1759"

><td id="1759"><a href="#1759">1759</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1760"

><td id="1760"><a href="#1760">1760</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1761"

><td id="1761"><a href="#1761">1761</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1762"

><td id="1762"><a href="#1762">1762</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1763"

><td id="1763"><a href="#1763">1763</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1764"

><td id="1764"><a href="#1764">1764</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1765"

><td id="1765"><a href="#1765">1765</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1766"

><td id="1766"><a href="#1766">1766</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1767"

><td id="1767"><a href="#1767">1767</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1768"

><td id="1768"><a href="#1768">1768</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1769"

><td id="1769"><a href="#1769">1769</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1770"

><td id="1770"><a href="#1770">1770</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1771"

><td id="1771"><a href="#1771">1771</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1772"

><td id="1772"><a href="#1772">1772</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1773"

><td id="1773"><a href="#1773">1773</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1774"

><td id="1774"><a href="#1774">1774</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1775"

><td id="1775"><a href="#1775">1775</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1776"

><td id="1776"><a href="#1776">1776</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1777"

><td id="1777"><a href="#1777">1777</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1778"

><td id="1778"><a href="#1778">1778</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1779"

><td id="1779"><a href="#1779">1779</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1780"

><td id="1780"><a href="#1780">1780</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1781"

><td id="1781"><a href="#1781">1781</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1782"

><td id="1782"><a href="#1782">1782</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1783"

><td id="1783"><a href="#1783">1783</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1784"

><td id="1784"><a href="#1784">1784</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1785"

><td id="1785"><a href="#1785">1785</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1786"

><td id="1786"><a href="#1786">1786</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1787"

><td id="1787"><a href="#1787">1787</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1788"

><td id="1788"><a href="#1788">1788</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1789"

><td id="1789"><a href="#1789">1789</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1790"

><td id="1790"><a href="#1790">1790</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1791"

><td id="1791"><a href="#1791">1791</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1792"

><td id="1792"><a href="#1792">1792</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1793"

><td id="1793"><a href="#1793">1793</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1794"

><td id="1794"><a href="#1794">1794</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1795"

><td id="1795"><a href="#1795">1795</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1796"

><td id="1796"><a href="#1796">1796</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1797"

><td id="1797"><a href="#1797">1797</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1798"

><td id="1798"><a href="#1798">1798</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1799"

><td id="1799"><a href="#1799">1799</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1800"

><td id="1800"><a href="#1800">1800</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1801"

><td id="1801"><a href="#1801">1801</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1802"

><td id="1802"><a href="#1802">1802</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1803"

><td id="1803"><a href="#1803">1803</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1804"

><td id="1804"><a href="#1804">1804</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1805"

><td id="1805"><a href="#1805">1805</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1806"

><td id="1806"><a href="#1806">1806</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1807"

><td id="1807"><a href="#1807">1807</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1808"

><td id="1808"><a href="#1808">1808</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1809"

><td id="1809"><a href="#1809">1809</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1810"

><td id="1810"><a href="#1810">1810</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1811"

><td id="1811"><a href="#1811">1811</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1812"

><td id="1812"><a href="#1812">1812</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1813"

><td id="1813"><a href="#1813">1813</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1814"

><td id="1814"><a href="#1814">1814</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1815"

><td id="1815"><a href="#1815">1815</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1816"

><td id="1816"><a href="#1816">1816</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1817"

><td id="1817"><a href="#1817">1817</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1818"

><td id="1818"><a href="#1818">1818</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1819"

><td id="1819"><a href="#1819">1819</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1820"

><td id="1820"><a href="#1820">1820</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1821"

><td id="1821"><a href="#1821">1821</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1822"

><td id="1822"><a href="#1822">1822</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1823"

><td id="1823"><a href="#1823">1823</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1824"

><td id="1824"><a href="#1824">1824</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1825"

><td id="1825"><a href="#1825">1825</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1826"

><td id="1826"><a href="#1826">1826</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1827"

><td id="1827"><a href="#1827">1827</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1828"

><td id="1828"><a href="#1828">1828</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1829"

><td id="1829"><a href="#1829">1829</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1830"

><td id="1830"><a href="#1830">1830</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1831"

><td id="1831"><a href="#1831">1831</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1832"

><td id="1832"><a href="#1832">1832</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1833"

><td id="1833"><a href="#1833">1833</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1834"

><td id="1834"><a href="#1834">1834</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1835"

><td id="1835"><a href="#1835">1835</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1836"

><td id="1836"><a href="#1836">1836</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1837"

><td id="1837"><a href="#1837">1837</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1838"

><td id="1838"><a href="#1838">1838</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1839"

><td id="1839"><a href="#1839">1839</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1840"

><td id="1840"><a href="#1840">1840</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1841"

><td id="1841"><a href="#1841">1841</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1842"

><td id="1842"><a href="#1842">1842</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1843"

><td id="1843"><a href="#1843">1843</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1844"

><td id="1844"><a href="#1844">1844</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1845"

><td id="1845"><a href="#1845">1845</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1846"

><td id="1846"><a href="#1846">1846</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1847"

><td id="1847"><a href="#1847">1847</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1848"

><td id="1848"><a href="#1848">1848</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1849"

><td id="1849"><a href="#1849">1849</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1850"

><td id="1850"><a href="#1850">1850</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1851"

><td id="1851"><a href="#1851">1851</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1852"

><td id="1852"><a href="#1852">1852</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1853"

><td id="1853"><a href="#1853">1853</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1854"

><td id="1854"><a href="#1854">1854</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1855"

><td id="1855"><a href="#1855">1855</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1856"

><td id="1856"><a href="#1856">1856</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1857"

><td id="1857"><a href="#1857">1857</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1858"

><td id="1858"><a href="#1858">1858</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1859"

><td id="1859"><a href="#1859">1859</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1860"

><td id="1860"><a href="#1860">1860</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1861"

><td id="1861"><a href="#1861">1861</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1862"

><td id="1862"><a href="#1862">1862</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1863"

><td id="1863"><a href="#1863">1863</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1864"

><td id="1864"><a href="#1864">1864</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1865"

><td id="1865"><a href="#1865">1865</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1866"

><td id="1866"><a href="#1866">1866</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1867"

><td id="1867"><a href="#1867">1867</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1868"

><td id="1868"><a href="#1868">1868</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1869"

><td id="1869"><a href="#1869">1869</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1870"

><td id="1870"><a href="#1870">1870</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1871"

><td id="1871"><a href="#1871">1871</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1872"

><td id="1872"><a href="#1872">1872</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1873"

><td id="1873"><a href="#1873">1873</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1874"

><td id="1874"><a href="#1874">1874</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1875"

><td id="1875"><a href="#1875">1875</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1876"

><td id="1876"><a href="#1876">1876</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1877"

><td id="1877"><a href="#1877">1877</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1878"

><td id="1878"><a href="#1878">1878</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1879"

><td id="1879"><a href="#1879">1879</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1880"

><td id="1880"><a href="#1880">1880</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1881"

><td id="1881"><a href="#1881">1881</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1882"

><td id="1882"><a href="#1882">1882</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1883"

><td id="1883"><a href="#1883">1883</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1884"

><td id="1884"><a href="#1884">1884</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1885"

><td id="1885"><a href="#1885">1885</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1886"

><td id="1886"><a href="#1886">1886</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1887"

><td id="1887"><a href="#1887">1887</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1888"

><td id="1888"><a href="#1888">1888</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1889"

><td id="1889"><a href="#1889">1889</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1890"

><td id="1890"><a href="#1890">1890</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1891"

><td id="1891"><a href="#1891">1891</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1892"

><td id="1892"><a href="#1892">1892</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1893"

><td id="1893"><a href="#1893">1893</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1894"

><td id="1894"><a href="#1894">1894</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1895"

><td id="1895"><a href="#1895">1895</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1896"

><td id="1896"><a href="#1896">1896</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1897"

><td id="1897"><a href="#1897">1897</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1898"

><td id="1898"><a href="#1898">1898</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1899"

><td id="1899"><a href="#1899">1899</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1900"

><td id="1900"><a href="#1900">1900</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1901"

><td id="1901"><a href="#1901">1901</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1902"

><td id="1902"><a href="#1902">1902</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1903"

><td id="1903"><a href="#1903">1903</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1904"

><td id="1904"><a href="#1904">1904</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1905"

><td id="1905"><a href="#1905">1905</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1906"

><td id="1906"><a href="#1906">1906</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1907"

><td id="1907"><a href="#1907">1907</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1908"

><td id="1908"><a href="#1908">1908</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1909"

><td id="1909"><a href="#1909">1909</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1910"

><td id="1910"><a href="#1910">1910</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1911"

><td id="1911"><a href="#1911">1911</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1912"

><td id="1912"><a href="#1912">1912</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1913"

><td id="1913"><a href="#1913">1913</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1914"

><td id="1914"><a href="#1914">1914</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1915"

><td id="1915"><a href="#1915">1915</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1916"

><td id="1916"><a href="#1916">1916</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1917"

><td id="1917"><a href="#1917">1917</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1918"

><td id="1918"><a href="#1918">1918</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1919"

><td id="1919"><a href="#1919">1919</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1920"

><td id="1920"><a href="#1920">1920</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1921"

><td id="1921"><a href="#1921">1921</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1922"

><td id="1922"><a href="#1922">1922</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1923"

><td id="1923"><a href="#1923">1923</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1924"

><td id="1924"><a href="#1924">1924</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1925"

><td id="1925"><a href="#1925">1925</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1926"

><td id="1926"><a href="#1926">1926</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1927"

><td id="1927"><a href="#1927">1927</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1928"

><td id="1928"><a href="#1928">1928</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1929"

><td id="1929"><a href="#1929">1929</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1930"

><td id="1930"><a href="#1930">1930</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1931"

><td id="1931"><a href="#1931">1931</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1932"

><td id="1932"><a href="#1932">1932</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1933"

><td id="1933"><a href="#1933">1933</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1934"

><td id="1934"><a href="#1934">1934</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1935"

><td id="1935"><a href="#1935">1935</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1936"

><td id="1936"><a href="#1936">1936</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1937"

><td id="1937"><a href="#1937">1937</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1938"

><td id="1938"><a href="#1938">1938</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1939"

><td id="1939"><a href="#1939">1939</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1940"

><td id="1940"><a href="#1940">1940</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1941"

><td id="1941"><a href="#1941">1941</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1942"

><td id="1942"><a href="#1942">1942</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1943"

><td id="1943"><a href="#1943">1943</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1944"

><td id="1944"><a href="#1944">1944</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1945"

><td id="1945"><a href="#1945">1945</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1946"

><td id="1946"><a href="#1946">1946</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1947"

><td id="1947"><a href="#1947">1947</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1948"

><td id="1948"><a href="#1948">1948</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1949"

><td id="1949"><a href="#1949">1949</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1950"

><td id="1950"><a href="#1950">1950</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1951"

><td id="1951"><a href="#1951">1951</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1952"

><td id="1952"><a href="#1952">1952</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1953"

><td id="1953"><a href="#1953">1953</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1954"

><td id="1954"><a href="#1954">1954</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1955"

><td id="1955"><a href="#1955">1955</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1956"

><td id="1956"><a href="#1956">1956</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1957"

><td id="1957"><a href="#1957">1957</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1958"

><td id="1958"><a href="#1958">1958</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1959"

><td id="1959"><a href="#1959">1959</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1960"

><td id="1960"><a href="#1960">1960</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1961"

><td id="1961"><a href="#1961">1961</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1962"

><td id="1962"><a href="#1962">1962</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1963"

><td id="1963"><a href="#1963">1963</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1964"

><td id="1964"><a href="#1964">1964</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1965"

><td id="1965"><a href="#1965">1965</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1966"

><td id="1966"><a href="#1966">1966</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1967"

><td id="1967"><a href="#1967">1967</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1968"

><td id="1968"><a href="#1968">1968</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1969"

><td id="1969"><a href="#1969">1969</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1970"

><td id="1970"><a href="#1970">1970</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1971"

><td id="1971"><a href="#1971">1971</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1972"

><td id="1972"><a href="#1972">1972</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1973"

><td id="1973"><a href="#1973">1973</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1974"

><td id="1974"><a href="#1974">1974</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1975"

><td id="1975"><a href="#1975">1975</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1976"

><td id="1976"><a href="#1976">1976</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1977"

><td id="1977"><a href="#1977">1977</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1978"

><td id="1978"><a href="#1978">1978</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1979"

><td id="1979"><a href="#1979">1979</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1980"

><td id="1980"><a href="#1980">1980</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1981"

><td id="1981"><a href="#1981">1981</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1982"

><td id="1982"><a href="#1982">1982</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1983"

><td id="1983"><a href="#1983">1983</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1984"

><td id="1984"><a href="#1984">1984</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1985"

><td id="1985"><a href="#1985">1985</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1986"

><td id="1986"><a href="#1986">1986</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1987"

><td id="1987"><a href="#1987">1987</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1988"

><td id="1988"><a href="#1988">1988</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1989"

><td id="1989"><a href="#1989">1989</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1990"

><td id="1990"><a href="#1990">1990</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1991"

><td id="1991"><a href="#1991">1991</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1992"

><td id="1992"><a href="#1992">1992</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1993"

><td id="1993"><a href="#1993">1993</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1994"

><td id="1994"><a href="#1994">1994</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1995"

><td id="1995"><a href="#1995">1995</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1996"

><td id="1996"><a href="#1996">1996</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1997"

><td id="1997"><a href="#1997">1997</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1998"

><td id="1998"><a href="#1998">1998</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1999"

><td id="1999"><a href="#1999">1999</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2000"

><td id="2000"><a href="#2000">2000</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2001"

><td id="2001"><a href="#2001">2001</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2002"

><td id="2002"><a href="#2002">2002</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2003"

><td id="2003"><a href="#2003">2003</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2004"

><td id="2004"><a href="#2004">2004</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2005"

><td id="2005"><a href="#2005">2005</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2006"

><td id="2006"><a href="#2006">2006</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2007"

><td id="2007"><a href="#2007">2007</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2008"

><td id="2008"><a href="#2008">2008</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2009"

><td id="2009"><a href="#2009">2009</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2010"

><td id="2010"><a href="#2010">2010</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2011"

><td id="2011"><a href="#2011">2011</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2012"

><td id="2012"><a href="#2012">2012</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2013"

><td id="2013"><a href="#2013">2013</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2014"

><td id="2014"><a href="#2014">2014</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2015"

><td id="2015"><a href="#2015">2015</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2016"

><td id="2016"><a href="#2016">2016</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2017"

><td id="2017"><a href="#2017">2017</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2018"

><td id="2018"><a href="#2018">2018</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2019"

><td id="2019"><a href="#2019">2019</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2020"

><td id="2020"><a href="#2020">2020</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2021"

><td id="2021"><a href="#2021">2021</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2022"

><td id="2022"><a href="#2022">2022</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2023"

><td id="2023"><a href="#2023">2023</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2024"

><td id="2024"><a href="#2024">2024</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2025"

><td id="2025"><a href="#2025">2025</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2026"

><td id="2026"><a href="#2026">2026</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2027"

><td id="2027"><a href="#2027">2027</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2028"

><td id="2028"><a href="#2028">2028</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2029"

><td id="2029"><a href="#2029">2029</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2030"

><td id="2030"><a href="#2030">2030</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2031"

><td id="2031"><a href="#2031">2031</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2032"

><td id="2032"><a href="#2032">2032</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2033"

><td id="2033"><a href="#2033">2033</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2034"

><td id="2034"><a href="#2034">2034</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2035"

><td id="2035"><a href="#2035">2035</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2036"

><td id="2036"><a href="#2036">2036</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2037"

><td id="2037"><a href="#2037">2037</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2038"

><td id="2038"><a href="#2038">2038</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2039"

><td id="2039"><a href="#2039">2039</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2040"

><td id="2040"><a href="#2040">2040</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2041"

><td id="2041"><a href="#2041">2041</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2042"

><td id="2042"><a href="#2042">2042</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2043"

><td id="2043"><a href="#2043">2043</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2044"

><td id="2044"><a href="#2044">2044</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2045"

><td id="2045"><a href="#2045">2045</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2046"

><td id="2046"><a href="#2046">2046</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2047"

><td id="2047"><a href="#2047">2047</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2048"

><td id="2048"><a href="#2048">2048</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2049"

><td id="2049"><a href="#2049">2049</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2050"

><td id="2050"><a href="#2050">2050</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2051"

><td id="2051"><a href="#2051">2051</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2052"

><td id="2052"><a href="#2052">2052</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2053"

><td id="2053"><a href="#2053">2053</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2054"

><td id="2054"><a href="#2054">2054</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2055"

><td id="2055"><a href="#2055">2055</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2056"

><td id="2056"><a href="#2056">2056</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2057"

><td id="2057"><a href="#2057">2057</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2058"

><td id="2058"><a href="#2058">2058</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2059"

><td id="2059"><a href="#2059">2059</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2060"

><td id="2060"><a href="#2060">2060</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2061"

><td id="2061"><a href="#2061">2061</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2062"

><td id="2062"><a href="#2062">2062</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2063"

><td id="2063"><a href="#2063">2063</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2064"

><td id="2064"><a href="#2064">2064</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2065"

><td id="2065"><a href="#2065">2065</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2066"

><td id="2066"><a href="#2066">2066</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2067"

><td id="2067"><a href="#2067">2067</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2068"

><td id="2068"><a href="#2068">2068</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2069"

><td id="2069"><a href="#2069">2069</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2070"

><td id="2070"><a href="#2070">2070</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2071"

><td id="2071"><a href="#2071">2071</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2072"

><td id="2072"><a href="#2072">2072</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2073"

><td id="2073"><a href="#2073">2073</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2074"

><td id="2074"><a href="#2074">2074</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2075"

><td id="2075"><a href="#2075">2075</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2076"

><td id="2076"><a href="#2076">2076</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2077"

><td id="2077"><a href="#2077">2077</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2078"

><td id="2078"><a href="#2078">2078</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2079"

><td id="2079"><a href="#2079">2079</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2080"

><td id="2080"><a href="#2080">2080</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2081"

><td id="2081"><a href="#2081">2081</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2082"

><td id="2082"><a href="#2082">2082</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2083"

><td id="2083"><a href="#2083">2083</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2084"

><td id="2084"><a href="#2084">2084</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2085"

><td id="2085"><a href="#2085">2085</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2086"

><td id="2086"><a href="#2086">2086</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2087"

><td id="2087"><a href="#2087">2087</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2088"

><td id="2088"><a href="#2088">2088</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2089"

><td id="2089"><a href="#2089">2089</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2090"

><td id="2090"><a href="#2090">2090</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2091"

><td id="2091"><a href="#2091">2091</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2092"

><td id="2092"><a href="#2092">2092</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2093"

><td id="2093"><a href="#2093">2093</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2094"

><td id="2094"><a href="#2094">2094</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2095"

><td id="2095"><a href="#2095">2095</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2096"

><td id="2096"><a href="#2096">2096</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2097"

><td id="2097"><a href="#2097">2097</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2098"

><td id="2098"><a href="#2098">2098</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2099"

><td id="2099"><a href="#2099">2099</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2100"

><td id="2100"><a href="#2100">2100</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2101"

><td id="2101"><a href="#2101">2101</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2102"

><td id="2102"><a href="#2102">2102</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2103"

><td id="2103"><a href="#2103">2103</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2104"

><td id="2104"><a href="#2104">2104</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2105"

><td id="2105"><a href="#2105">2105</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2106"

><td id="2106"><a href="#2106">2106</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2107"

><td id="2107"><a href="#2107">2107</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2108"

><td id="2108"><a href="#2108">2108</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2109"

><td id="2109"><a href="#2109">2109</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2110"

><td id="2110"><a href="#2110">2110</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2111"

><td id="2111"><a href="#2111">2111</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2112"

><td id="2112"><a href="#2112">2112</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2113"

><td id="2113"><a href="#2113">2113</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2114"

><td id="2114"><a href="#2114">2114</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2115"

><td id="2115"><a href="#2115">2115</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2116"

><td id="2116"><a href="#2116">2116</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2117"

><td id="2117"><a href="#2117">2117</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2118"

><td id="2118"><a href="#2118">2118</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2119"

><td id="2119"><a href="#2119">2119</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2120"

><td id="2120"><a href="#2120">2120</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2121"

><td id="2121"><a href="#2121">2121</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2122"

><td id="2122"><a href="#2122">2122</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2123"

><td id="2123"><a href="#2123">2123</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2124"

><td id="2124"><a href="#2124">2124</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2125"

><td id="2125"><a href="#2125">2125</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2126"

><td id="2126"><a href="#2126">2126</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2127"

><td id="2127"><a href="#2127">2127</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2128"

><td id="2128"><a href="#2128">2128</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2129"

><td id="2129"><a href="#2129">2129</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2130"

><td id="2130"><a href="#2130">2130</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2131"

><td id="2131"><a href="#2131">2131</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2132"

><td id="2132"><a href="#2132">2132</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2133"

><td id="2133"><a href="#2133">2133</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2134"

><td id="2134"><a href="#2134">2134</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2135"

><td id="2135"><a href="#2135">2135</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2136"

><td id="2136"><a href="#2136">2136</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2137"

><td id="2137"><a href="#2137">2137</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2138"

><td id="2138"><a href="#2138">2138</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2139"

><td id="2139"><a href="#2139">2139</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2140"

><td id="2140"><a href="#2140">2140</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2141"

><td id="2141"><a href="#2141">2141</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2142"

><td id="2142"><a href="#2142">2142</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2143"

><td id="2143"><a href="#2143">2143</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2144"

><td id="2144"><a href="#2144">2144</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2145"

><td id="2145"><a href="#2145">2145</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2146"

><td id="2146"><a href="#2146">2146</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2147"

><td id="2147"><a href="#2147">2147</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2148"

><td id="2148"><a href="#2148">2148</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2149"

><td id="2149"><a href="#2149">2149</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2150"

><td id="2150"><a href="#2150">2150</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2151"

><td id="2151"><a href="#2151">2151</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2152"

><td id="2152"><a href="#2152">2152</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2153"

><td id="2153"><a href="#2153">2153</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2154"

><td id="2154"><a href="#2154">2154</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2155"

><td id="2155"><a href="#2155">2155</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2156"

><td id="2156"><a href="#2156">2156</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2157"

><td id="2157"><a href="#2157">2157</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2158"

><td id="2158"><a href="#2158">2158</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2159"

><td id="2159"><a href="#2159">2159</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2160"

><td id="2160"><a href="#2160">2160</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2161"

><td id="2161"><a href="#2161">2161</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2162"

><td id="2162"><a href="#2162">2162</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2163"

><td id="2163"><a href="#2163">2163</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2164"

><td id="2164"><a href="#2164">2164</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2165"

><td id="2165"><a href="#2165">2165</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2166"

><td id="2166"><a href="#2166">2166</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2167"

><td id="2167"><a href="#2167">2167</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2168"

><td id="2168"><a href="#2168">2168</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2169"

><td id="2169"><a href="#2169">2169</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2170"

><td id="2170"><a href="#2170">2170</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2171"

><td id="2171"><a href="#2171">2171</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2172"

><td id="2172"><a href="#2172">2172</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2173"

><td id="2173"><a href="#2173">2173</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2174"

><td id="2174"><a href="#2174">2174</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2175"

><td id="2175"><a href="#2175">2175</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2176"

><td id="2176"><a href="#2176">2176</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2177"

><td id="2177"><a href="#2177">2177</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2178"

><td id="2178"><a href="#2178">2178</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2179"

><td id="2179"><a href="#2179">2179</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2180"

><td id="2180"><a href="#2180">2180</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2181"

><td id="2181"><a href="#2181">2181</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2182"

><td id="2182"><a href="#2182">2182</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2183"

><td id="2183"><a href="#2183">2183</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2184"

><td id="2184"><a href="#2184">2184</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2185"

><td id="2185"><a href="#2185">2185</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2186"

><td id="2186"><a href="#2186">2186</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2187"

><td id="2187"><a href="#2187">2187</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2188"

><td id="2188"><a href="#2188">2188</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2189"

><td id="2189"><a href="#2189">2189</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2190"

><td id="2190"><a href="#2190">2190</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2191"

><td id="2191"><a href="#2191">2191</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2192"

><td id="2192"><a href="#2192">2192</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2193"

><td id="2193"><a href="#2193">2193</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2194"

><td id="2194"><a href="#2194">2194</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2195"

><td id="2195"><a href="#2195">2195</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2196"

><td id="2196"><a href="#2196">2196</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2197"

><td id="2197"><a href="#2197">2197</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2198"

><td id="2198"><a href="#2198">2198</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2199"

><td id="2199"><a href="#2199">2199</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2200"

><td id="2200"><a href="#2200">2200</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2201"

><td id="2201"><a href="#2201">2201</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2202"

><td id="2202"><a href="#2202">2202</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2203"

><td id="2203"><a href="#2203">2203</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2204"

><td id="2204"><a href="#2204">2204</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2205"

><td id="2205"><a href="#2205">2205</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2206"

><td id="2206"><a href="#2206">2206</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2207"

><td id="2207"><a href="#2207">2207</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2208"

><td id="2208"><a href="#2208">2208</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2209"

><td id="2209"><a href="#2209">2209</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2210"

><td id="2210"><a href="#2210">2210</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2211"

><td id="2211"><a href="#2211">2211</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2212"

><td id="2212"><a href="#2212">2212</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2213"

><td id="2213"><a href="#2213">2213</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2214"

><td id="2214"><a href="#2214">2214</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2215"

><td id="2215"><a href="#2215">2215</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2216"

><td id="2216"><a href="#2216">2216</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2217"

><td id="2217"><a href="#2217">2217</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2218"

><td id="2218"><a href="#2218">2218</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2219"

><td id="2219"><a href="#2219">2219</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2220"

><td id="2220"><a href="#2220">2220</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2221"

><td id="2221"><a href="#2221">2221</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2222"

><td id="2222"><a href="#2222">2222</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2223"

><td id="2223"><a href="#2223">2223</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2224"

><td id="2224"><a href="#2224">2224</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2225"

><td id="2225"><a href="#2225">2225</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2226"

><td id="2226"><a href="#2226">2226</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2227"

><td id="2227"><a href="#2227">2227</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2228"

><td id="2228"><a href="#2228">2228</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2229"

><td id="2229"><a href="#2229">2229</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2230"

><td id="2230"><a href="#2230">2230</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2231"

><td id="2231"><a href="#2231">2231</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2232"

><td id="2232"><a href="#2232">2232</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2233"

><td id="2233"><a href="#2233">2233</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2234"

><td id="2234"><a href="#2234">2234</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2235"

><td id="2235"><a href="#2235">2235</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2236"

><td id="2236"><a href="#2236">2236</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2237"

><td id="2237"><a href="#2237">2237</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2238"

><td id="2238"><a href="#2238">2238</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2239"

><td id="2239"><a href="#2239">2239</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2240"

><td id="2240"><a href="#2240">2240</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2241"

><td id="2241"><a href="#2241">2241</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2242"

><td id="2242"><a href="#2242">2242</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2243"

><td id="2243"><a href="#2243">2243</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2244"

><td id="2244"><a href="#2244">2244</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2245"

><td id="2245"><a href="#2245">2245</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2246"

><td id="2246"><a href="#2246">2246</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2247"

><td id="2247"><a href="#2247">2247</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2248"

><td id="2248"><a href="#2248">2248</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2249"

><td id="2249"><a href="#2249">2249</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2250"

><td id="2250"><a href="#2250">2250</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2251"

><td id="2251"><a href="#2251">2251</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2252"

><td id="2252"><a href="#2252">2252</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2253"

><td id="2253"><a href="#2253">2253</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2254"

><td id="2254"><a href="#2254">2254</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2255"

><td id="2255"><a href="#2255">2255</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2256"

><td id="2256"><a href="#2256">2256</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2257"

><td id="2257"><a href="#2257">2257</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2258"

><td id="2258"><a href="#2258">2258</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2259"

><td id="2259"><a href="#2259">2259</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2260"

><td id="2260"><a href="#2260">2260</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2261"

><td id="2261"><a href="#2261">2261</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2262"

><td id="2262"><a href="#2262">2262</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2263"

><td id="2263"><a href="#2263">2263</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2264"

><td id="2264"><a href="#2264">2264</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2265"

><td id="2265"><a href="#2265">2265</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2266"

><td id="2266"><a href="#2266">2266</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2267"

><td id="2267"><a href="#2267">2267</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2268"

><td id="2268"><a href="#2268">2268</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2269"

><td id="2269"><a href="#2269">2269</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2270"

><td id="2270"><a href="#2270">2270</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2271"

><td id="2271"><a href="#2271">2271</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2272"

><td id="2272"><a href="#2272">2272</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2273"

><td id="2273"><a href="#2273">2273</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2274"

><td id="2274"><a href="#2274">2274</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2275"

><td id="2275"><a href="#2275">2275</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2276"

><td id="2276"><a href="#2276">2276</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2277"

><td id="2277"><a href="#2277">2277</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2278"

><td id="2278"><a href="#2278">2278</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2279"

><td id="2279"><a href="#2279">2279</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2280"

><td id="2280"><a href="#2280">2280</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2281"

><td id="2281"><a href="#2281">2281</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2282"

><td id="2282"><a href="#2282">2282</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2283"

><td id="2283"><a href="#2283">2283</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2284"

><td id="2284"><a href="#2284">2284</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2285"

><td id="2285"><a href="#2285">2285</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2286"

><td id="2286"><a href="#2286">2286</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2287"

><td id="2287"><a href="#2287">2287</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2288"

><td id="2288"><a href="#2288">2288</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2289"

><td id="2289"><a href="#2289">2289</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2290"

><td id="2290"><a href="#2290">2290</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2291"

><td id="2291"><a href="#2291">2291</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2292"

><td id="2292"><a href="#2292">2292</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2293"

><td id="2293"><a href="#2293">2293</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2294"

><td id="2294"><a href="#2294">2294</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2295"

><td id="2295"><a href="#2295">2295</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2296"

><td id="2296"><a href="#2296">2296</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2297"

><td id="2297"><a href="#2297">2297</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2298"

><td id="2298"><a href="#2298">2298</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2299"

><td id="2299"><a href="#2299">2299</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2300"

><td id="2300"><a href="#2300">2300</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2301"

><td id="2301"><a href="#2301">2301</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2302"

><td id="2302"><a href="#2302">2302</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2303"

><td id="2303"><a href="#2303">2303</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2304"

><td id="2304"><a href="#2304">2304</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2305"

><td id="2305"><a href="#2305">2305</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2306"

><td id="2306"><a href="#2306">2306</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2307"

><td id="2307"><a href="#2307">2307</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2308"

><td id="2308"><a href="#2308">2308</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2309"

><td id="2309"><a href="#2309">2309</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2310"

><td id="2310"><a href="#2310">2310</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2311"

><td id="2311"><a href="#2311">2311</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2312"

><td id="2312"><a href="#2312">2312</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2313"

><td id="2313"><a href="#2313">2313</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2314"

><td id="2314"><a href="#2314">2314</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2315"

><td id="2315"><a href="#2315">2315</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2316"

><td id="2316"><a href="#2316">2316</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2317"

><td id="2317"><a href="#2317">2317</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2318"

><td id="2318"><a href="#2318">2318</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2319"

><td id="2319"><a href="#2319">2319</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2320"

><td id="2320"><a href="#2320">2320</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2321"

><td id="2321"><a href="#2321">2321</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2322"

><td id="2322"><a href="#2322">2322</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2323"

><td id="2323"><a href="#2323">2323</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2324"

><td id="2324"><a href="#2324">2324</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2325"

><td id="2325"><a href="#2325">2325</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2326"

><td id="2326"><a href="#2326">2326</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2327"

><td id="2327"><a href="#2327">2327</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2328"

><td id="2328"><a href="#2328">2328</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2329"

><td id="2329"><a href="#2329">2329</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2330"

><td id="2330"><a href="#2330">2330</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2331"

><td id="2331"><a href="#2331">2331</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2332"

><td id="2332"><a href="#2332">2332</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2333"

><td id="2333"><a href="#2333">2333</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2334"

><td id="2334"><a href="#2334">2334</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2335"

><td id="2335"><a href="#2335">2335</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2336"

><td id="2336"><a href="#2336">2336</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2337"

><td id="2337"><a href="#2337">2337</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2338"

><td id="2338"><a href="#2338">2338</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2339"

><td id="2339"><a href="#2339">2339</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2340"

><td id="2340"><a href="#2340">2340</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2341"

><td id="2341"><a href="#2341">2341</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2342"

><td id="2342"><a href="#2342">2342</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2343"

><td id="2343"><a href="#2343">2343</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2344"

><td id="2344"><a href="#2344">2344</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2345"

><td id="2345"><a href="#2345">2345</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2346"

><td id="2346"><a href="#2346">2346</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2347"

><td id="2347"><a href="#2347">2347</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2348"

><td id="2348"><a href="#2348">2348</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2349"

><td id="2349"><a href="#2349">2349</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2350"

><td id="2350"><a href="#2350">2350</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2351"

><td id="2351"><a href="#2351">2351</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2352"

><td id="2352"><a href="#2352">2352</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2353"

><td id="2353"><a href="#2353">2353</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2354"

><td id="2354"><a href="#2354">2354</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2355"

><td id="2355"><a href="#2355">2355</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2356"

><td id="2356"><a href="#2356">2356</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2357"

><td id="2357"><a href="#2357">2357</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2358"

><td id="2358"><a href="#2358">2358</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2359"

><td id="2359"><a href="#2359">2359</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2360"

><td id="2360"><a href="#2360">2360</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2361"

><td id="2361"><a href="#2361">2361</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2362"

><td id="2362"><a href="#2362">2362</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2363"

><td id="2363"><a href="#2363">2363</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2364"

><td id="2364"><a href="#2364">2364</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2365"

><td id="2365"><a href="#2365">2365</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2366"

><td id="2366"><a href="#2366">2366</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2367"

><td id="2367"><a href="#2367">2367</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2368"

><td id="2368"><a href="#2368">2368</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2369"

><td id="2369"><a href="#2369">2369</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2370"

><td id="2370"><a href="#2370">2370</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2371"

><td id="2371"><a href="#2371">2371</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2372"

><td id="2372"><a href="#2372">2372</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2373"

><td id="2373"><a href="#2373">2373</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2374"

><td id="2374"><a href="#2374">2374</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2375"

><td id="2375"><a href="#2375">2375</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2376"

><td id="2376"><a href="#2376">2376</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2377"

><td id="2377"><a href="#2377">2377</a></td></tr
><tr id="gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2378"

><td id="2378"><a href="#2378">2378</a></td></tr
></table></pre>
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
</td>
<td id="lines">
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
<pre class="prettyprint lang-py"><table id="src_table_0"><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1

><td class="source"># Author: Steven J. Bethard &lt;steven.bethard@gmail.com&gt;.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_3

><td class="source">&quot;&quot;&quot;Command-line parsing library<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_4

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_5

><td class="source">This module is an optparse-inspired command-line parsing library that:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_6

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_7

><td class="source">    - handles both optional and positional arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_8

><td class="source">    - produces highly informative usage messages<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_9

><td class="source">    - supports parsers that dispatch to sub-parsers<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_10

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_11

><td class="source">The following is a simple usage example that sums integers from the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_12

><td class="source">command-line and writes the result to a file::<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_13

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_14

><td class="source">    parser = argparse.ArgumentParser(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_15

><td class="source">        description=&#39;sum the integers at the command line&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_16

><td class="source">    parser.add_argument(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_17

><td class="source">        &#39;integers&#39;, metavar=&#39;int&#39;, nargs=&#39;+&#39;, type=int,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_18

><td class="source">        help=&#39;an integer to be summed&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_19

><td class="source">    parser.add_argument(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_20

><td class="source">        &#39;--log&#39;, default=sys.stdout, type=argparse.FileType(&#39;w&#39;),<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_21

><td class="source">        help=&#39;the file where the sum should be written&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_22

><td class="source">    args = parser.parse_args()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_23

><td class="source">    args.log.write(&#39;%s&#39; % sum(args.integers))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_24

><td class="source">    args.log.close()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_25

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_26

><td class="source">The module contains the following public classes:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_27

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_28

><td class="source">    - ArgumentParser -- The main entry point for command-line parsing. As the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_29

><td class="source">        example above shows, the add_argument() method is used to populate<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_30

><td class="source">        the parser with actions for optional and positional arguments. Then<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_31

><td class="source">        the parse_args() method is invoked to convert the args at the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_32

><td class="source">        command-line into an object with attributes.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_33

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_34

><td class="source">    - ArgumentError -- The exception raised by ArgumentParser objects when<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_35

><td class="source">        there are errors with the parser&#39;s actions. Errors raised while<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_36

><td class="source">        parsing the command-line are caught by ArgumentParser and emitted<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_37

><td class="source">        as command-line messages.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_38

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_39

><td class="source">    - FileType -- A factory for defining types of files to be created. As the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_40

><td class="source">        example above shows, instances of FileType are typically passed as<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_41

><td class="source">        the type= argument of add_argument() calls.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_42

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_43

><td class="source">    - Action -- The base class for parser actions. Typically actions are<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_44

><td class="source">        selected by passing strings like &#39;store_true&#39; or &#39;append_const&#39; to<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_45

><td class="source">        the action= argument of add_argument(). However, for greater<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_46

><td class="source">        customization of ArgumentParser actions, subclasses of Action may<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_47

><td class="source">        be defined and passed as the action= argument.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_48

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_49

><td class="source">    - HelpFormatter, RawDescriptionHelpFormatter, RawTextHelpFormatter,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_50

><td class="source">        ArgumentDefaultsHelpFormatter -- Formatter classes which<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_51

><td class="source">        may be passed as the formatter_class= argument to the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_52

><td class="source">        ArgumentParser constructor. HelpFormatter is the default,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_53

><td class="source">        RawDescriptionHelpFormatter and RawTextHelpFormatter tell the parser<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_54

><td class="source">        not to change the formatting for help text, and<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_55

><td class="source">        ArgumentDefaultsHelpFormatter adds information about argument defaults<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_56

><td class="source">        to the help.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_57

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_58

><td class="source">All other classes in this module are considered implementation details.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_59

><td class="source">(Also note that HelpFormatter and RawDescriptionHelpFormatter are only<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_60

><td class="source">considered public as object names -- the API of the formatter objects is<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_61

><td class="source">still considered an implementation detail.)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_62

><td class="source">&quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_63

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_64

><td class="source">__version__ = &#39;1.3.0&#39;  # we use our own version number independant of the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_65

><td class="source">                       # one in stdlib and we release this on pypi.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_66

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_67

><td class="source">__external_lib__ = True  # to make sure the tests really test THIS lib,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_68

><td class="source">                         # not the builtin one in Python stdlib<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_69

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_70

><td class="source">__all__ = [<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_71

><td class="source">    &#39;ArgumentParser&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_72

><td class="source">    &#39;ArgumentError&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_73

><td class="source">    &#39;ArgumentTypeError&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_74

><td class="source">    &#39;FileType&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_75

><td class="source">    &#39;HelpFormatter&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_76

><td class="source">    &#39;ArgumentDefaultsHelpFormatter&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_77

><td class="source">    &#39;RawDescriptionHelpFormatter&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_78

><td class="source">    &#39;RawTextHelpFormatter&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_79

><td class="source">    &#39;Namespace&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_80

><td class="source">    &#39;Action&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_81

><td class="source">    &#39;ONE_OR_MORE&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_82

><td class="source">    &#39;OPTIONAL&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_83

><td class="source">    &#39;PARSER&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_84

><td class="source">    &#39;REMAINDER&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_85

><td class="source">    &#39;SUPPRESS&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_86

><td class="source">    &#39;ZERO_OR_MORE&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_87

><td class="source">]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_88

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_89

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_90

><td class="source">import copy as _copy<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_91

><td class="source">import os as _os<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_92

><td class="source">import re as _re<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_93

><td class="source">import sys as _sys<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_94

><td class="source">import textwrap as _textwrap<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_95

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_96

><td class="source">from gettext import gettext as _<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_97

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_98

><td class="source">try:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_99

><td class="source">    set<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_100

><td class="source">except NameError:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_101

><td class="source">    # for python &lt; 2.4 compatibility (sets module is there since 2.3):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_102

><td class="source">    from sets import Set as set<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_103

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_104

><td class="source">try:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_105

><td class="source">    basestring<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_106

><td class="source">except NameError:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_107

><td class="source">    basestring = str<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_108

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_109

><td class="source">try:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_110

><td class="source">    sorted<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_111

><td class="source">except NameError:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_112

><td class="source">    # for python &lt; 2.4 compatibility:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_113

><td class="source">    def sorted(iterable, reverse=False):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_114

><td class="source">        result = list(iterable)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_115

><td class="source">        result.sort()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_116

><td class="source">        if reverse:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_117

><td class="source">            result.reverse()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_118

><td class="source">        return result<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_119

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_120

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_121

><td class="source">def _callable(obj):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_122

><td class="source">    return hasattr(obj, &#39;__call__&#39;) or hasattr(obj, &#39;__bases__&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_123

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_124

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_125

><td class="source">SUPPRESS = &#39;==SUPPRESS==&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_126

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_127

><td class="source">OPTIONAL = &#39;?&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_128

><td class="source">ZERO_OR_MORE = &#39;*&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_129

><td class="source">ONE_OR_MORE = &#39;+&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_130

><td class="source">PARSER = &#39;A...&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_131

><td class="source">REMAINDER = &#39;...&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_132

><td class="source">_UNRECOGNIZED_ARGS_ATTR = &#39;_unrecognized_args&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_133

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_134

><td class="source"># =============================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_135

><td class="source"># Utility functions and classes<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_136

><td class="source"># =============================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_137

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_138

><td class="source">class _AttributeHolder(object):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_139

><td class="source">    &quot;&quot;&quot;Abstract base class that provides __repr__.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_140

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_141

><td class="source">    The __repr__ method returns a string in the format::<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_142

><td class="source">        ClassName(attr=name, attr=name, ...)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_143

><td class="source">    The attributes are determined either by a class-level attribute,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_144

><td class="source">    &#39;_kwarg_names&#39;, or by inspecting the instance __dict__.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_145

><td class="source">    &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_146

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_147

><td class="source">    def __repr__(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_148

><td class="source">        type_name = type(self).__name__<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_149

><td class="source">        arg_strings = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_150

><td class="source">        for arg in self._get_args():<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_151

><td class="source">            arg_strings.append(repr(arg))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_152

><td class="source">        for name, value in self._get_kwargs():<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_153

><td class="source">            arg_strings.append(&#39;%s=%r&#39; % (name, value))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_154

><td class="source">        return &#39;%s(%s)&#39; % (type_name, &#39;, &#39;.join(arg_strings))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_155

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_156

><td class="source">    def _get_kwargs(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_157

><td class="source">        return sorted(self.__dict__.items())<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_158

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_159

><td class="source">    def _get_args(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_160

><td class="source">        return []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_161

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_162

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_163

><td class="source">def _ensure_value(namespace, name, value):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_164

><td class="source">    if getattr(namespace, name, None) is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_165

><td class="source">        setattr(namespace, name, value)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_166

><td class="source">    return getattr(namespace, name)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_167

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_168

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_169

><td class="source"># ===============<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_170

><td class="source"># Formatting Help<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_171

><td class="source"># ===============<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_172

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_173

><td class="source">class HelpFormatter(object):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_174

><td class="source">    &quot;&quot;&quot;Formatter for generating usage messages and argument help strings.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_175

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_176

><td class="source">    Only the name of this class is considered a public API. All the methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_177

><td class="source">    provided by the class are considered an implementation detail.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_178

><td class="source">    &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_179

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_180

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_181

><td class="source">                 prog,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_182

><td class="source">                 indent_increment=2,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_183

><td class="source">                 max_help_position=24,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_184

><td class="source">                 width=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_185

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_186

><td class="source">        # default setting for width<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_187

><td class="source">        if width is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_188

><td class="source">            try:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_189

><td class="source">                width = int(_os.environ[&#39;COLUMNS&#39;])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_190

><td class="source">            except (KeyError, ValueError):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_191

><td class="source">                width = 80<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_192

><td class="source">            width -= 2<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_193

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_194

><td class="source">        self._prog = prog<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_195

><td class="source">        self._indent_increment = indent_increment<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_196

><td class="source">        self._max_help_position = max_help_position<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_197

><td class="source">        self._width = width<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_198

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_199

><td class="source">        self._current_indent = 0<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_200

><td class="source">        self._level = 0<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_201

><td class="source">        self._action_max_length = 0<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_202

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_203

><td class="source">        self._root_section = self._Section(self, None)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_204

><td class="source">        self._current_section = self._root_section<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_205

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_206

><td class="source">        self._whitespace_matcher = _re.compile(r&#39;\s+&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_207

><td class="source">        self._long_break_matcher = _re.compile(r&#39;\n\n\n+&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_208

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_209

><td class="source">    # ===============================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_210

><td class="source">    # Section and indentation methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_211

><td class="source">    # ===============================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_212

><td class="source">    def _indent(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_213

><td class="source">        self._current_indent += self._indent_increment<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_214

><td class="source">        self._level += 1<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_215

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_216

><td class="source">    def _dedent(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_217

><td class="source">        self._current_indent -= self._indent_increment<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_218

><td class="source">        assert self._current_indent &gt;= 0, &#39;Indent decreased below 0.&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_219

><td class="source">        self._level -= 1<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_220

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_221

><td class="source">    class _Section(object):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_222

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_223

><td class="source">        def __init__(self, formatter, parent, heading=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_224

><td class="source">            self.formatter = formatter<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_225

><td class="source">            self.parent = parent<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_226

><td class="source">            self.heading = heading<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_227

><td class="source">            self.items = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_228

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_229

><td class="source">        def format_help(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_230

><td class="source">            # format the indented section<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_231

><td class="source">            if self.parent is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_232

><td class="source">                self.formatter._indent()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_233

><td class="source">            join = self.formatter._join_parts<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_234

><td class="source">            for func, args in self.items:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_235

><td class="source">                func(*args)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_236

><td class="source">            item_help = join([func(*args) for func, args in self.items])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_237

><td class="source">            if self.parent is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_238

><td class="source">                self.formatter._dedent()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_239

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_240

><td class="source">            # return nothing if the section was empty<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_241

><td class="source">            if not item_help:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_242

><td class="source">                return &#39;&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_243

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_244

><td class="source">            # add the heading if the section was non-empty<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_245

><td class="source">            if self.heading is not SUPPRESS and self.heading is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_246

><td class="source">                current_indent = self.formatter._current_indent<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_247

><td class="source">                heading = &#39;%*s%s:\n&#39; % (current_indent, &#39;&#39;, self.heading)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_248

><td class="source">            else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_249

><td class="source">                heading = &#39;&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_250

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_251

><td class="source">            # join the section-initial newline, the heading and the help<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_252

><td class="source">            return join([&#39;\n&#39;, heading, item_help, &#39;\n&#39;])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_253

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_254

><td class="source">    def _add_item(self, func, args):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_255

><td class="source">        self._current_section.items.append((func, args))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_256

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_257

><td class="source">    # ========================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_258

><td class="source">    # Message building methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_259

><td class="source">    # ========================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_260

><td class="source">    def start_section(self, heading):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_261

><td class="source">        self._indent()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_262

><td class="source">        section = self._Section(self, self._current_section, heading)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_263

><td class="source">        self._add_item(section.format_help, [])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_264

><td class="source">        self._current_section = section<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_265

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_266

><td class="source">    def end_section(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_267

><td class="source">        self._current_section = self._current_section.parent<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_268

><td class="source">        self._dedent()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_269

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_270

><td class="source">    def add_text(self, text):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_271

><td class="source">        if text is not SUPPRESS and text is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_272

><td class="source">            self._add_item(self._format_text, [text])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_273

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_274

><td class="source">    def add_usage(self, usage, actions, groups, prefix=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_275

><td class="source">        if usage is not SUPPRESS:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_276

><td class="source">            args = usage, actions, groups, prefix<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_277

><td class="source">            self._add_item(self._format_usage, args)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_278

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_279

><td class="source">    def add_argument(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_280

><td class="source">        if action.help is not SUPPRESS:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_281

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_282

><td class="source">            # find all invocations<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_283

><td class="source">            get_invocation = self._format_action_invocation<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_284

><td class="source">            invocations = [get_invocation(action)]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_285

><td class="source">            for subaction in self._iter_indented_subactions(action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_286

><td class="source">                invocations.append(get_invocation(subaction))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_287

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_288

><td class="source">            # update the maximum item length<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_289

><td class="source">            invocation_length = max([len(s) for s in invocations])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_290

><td class="source">            action_length = invocation_length + self._current_indent<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_291

><td class="source">            self._action_max_length = max(self._action_max_length,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_292

><td class="source">                                          action_length)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_293

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_294

><td class="source">            # add the item to the list<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_295

><td class="source">            self._add_item(self._format_action, [action])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_296

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_297

><td class="source">    def add_arguments(self, actions):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_298

><td class="source">        for action in actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_299

><td class="source">            self.add_argument(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_300

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_301

><td class="source">    # =======================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_302

><td class="source">    # Help-formatting methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_303

><td class="source">    # =======================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_304

><td class="source">    def format_help(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_305

><td class="source">        help = self._root_section.format_help()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_306

><td class="source">        if help:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_307

><td class="source">            help = self._long_break_matcher.sub(&#39;\n\n&#39;, help)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_308

><td class="source">            help = help.strip(&#39;\n&#39;) + &#39;\n&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_309

><td class="source">        return help<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_310

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_311

><td class="source">    def _join_parts(self, part_strings):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_312

><td class="source">        return &#39;&#39;.join([part<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_313

><td class="source">                        for part in part_strings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_314

><td class="source">                        if part and part is not SUPPRESS])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_315

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_316

><td class="source">    def _format_usage(self, usage, actions, groups, prefix):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_317

><td class="source">        if prefix is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_318

><td class="source">            prefix = _(&#39;usage: &#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_319

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_320

><td class="source">        # if usage is specified, use that<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_321

><td class="source">        if usage is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_322

><td class="source">            usage = usage % dict(prog=self._prog)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_323

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_324

><td class="source">        # if no optionals or positionals are available, usage is just prog<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_325

><td class="source">        elif usage is None and not actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_326

><td class="source">            usage = &#39;%(prog)s&#39; % dict(prog=self._prog)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_327

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_328

><td class="source">        # if optionals and positionals are available, calculate usage<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_329

><td class="source">        elif usage is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_330

><td class="source">            prog = &#39;%(prog)s&#39; % dict(prog=self._prog)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_331

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_332

><td class="source">            # split optionals from positionals<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_333

><td class="source">            optionals = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_334

><td class="source">            positionals = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_335

><td class="source">            for action in actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_336

><td class="source">                if action.option_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_337

><td class="source">                    optionals.append(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_338

><td class="source">                else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_339

><td class="source">                    positionals.append(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_340

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_341

><td class="source">            # build full usage string<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_342

><td class="source">            format = self._format_actions_usage<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_343

><td class="source">            action_usage = format(optionals + positionals, groups)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_344

><td class="source">            usage = &#39; &#39;.join([s for s in [prog, action_usage] if s])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_345

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_346

><td class="source">            # wrap the usage parts if it&#39;s too long<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_347

><td class="source">            text_width = self._width - self._current_indent<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_348

><td class="source">            if len(prefix) + len(usage) &gt; text_width:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_349

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_350

><td class="source">                # break usage into wrappable parts<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_351

><td class="source">                part_regexp = r&#39;\(.*?\)+|\[.*?\]+|\S+&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_352

><td class="source">                opt_usage = format(optionals, groups)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_353

><td class="source">                pos_usage = format(positionals, groups)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_354

><td class="source">                opt_parts = _re.findall(part_regexp, opt_usage)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_355

><td class="source">                pos_parts = _re.findall(part_regexp, pos_usage)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_356

><td class="source">                assert &#39; &#39;.join(opt_parts) == opt_usage<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_357

><td class="source">                assert &#39; &#39;.join(pos_parts) == pos_usage<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_358

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_359

><td class="source">                # helper for wrapping lines<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_360

><td class="source">                def get_lines(parts, indent, prefix=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_361

><td class="source">                    lines = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_362

><td class="source">                    line = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_363

><td class="source">                    if prefix is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_364

><td class="source">                        line_len = len(prefix) - 1<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_365

><td class="source">                    else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_366

><td class="source">                        line_len = len(indent) - 1<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_367

><td class="source">                    for part in parts:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_368

><td class="source">                        if line_len + 1 + len(part) &gt; text_width:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_369

><td class="source">                            lines.append(indent + &#39; &#39;.join(line))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_370

><td class="source">                            line = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_371

><td class="source">                            line_len = len(indent) - 1<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_372

><td class="source">                        line.append(part)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_373

><td class="source">                        line_len += len(part) + 1<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_374

><td class="source">                    if line:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_375

><td class="source">                        lines.append(indent + &#39; &#39;.join(line))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_376

><td class="source">                    if prefix is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_377

><td class="source">                        lines[0] = lines[0][len(indent):]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_378

><td class="source">                    return lines<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_379

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_380

><td class="source">                # if prog is short, follow it with optionals or positionals<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_381

><td class="source">                if len(prefix) + len(prog) &lt;= 0.75 * text_width:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_382

><td class="source">                    indent = &#39; &#39; * (len(prefix) + len(prog) + 1)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_383

><td class="source">                    if opt_parts:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_384

><td class="source">                        lines = get_lines([prog] + opt_parts, indent, prefix)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_385

><td class="source">                        lines.extend(get_lines(pos_parts, indent))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_386

><td class="source">                    elif pos_parts:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_387

><td class="source">                        lines = get_lines([prog] + pos_parts, indent, prefix)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_388

><td class="source">                    else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_389

><td class="source">                        lines = [prog]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_390

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_391

><td class="source">                # if prog is long, put it on its own line<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_392

><td class="source">                else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_393

><td class="source">                    indent = &#39; &#39; * len(prefix)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_394

><td class="source">                    parts = opt_parts + pos_parts<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_395

><td class="source">                    lines = get_lines(parts, indent)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_396

><td class="source">                    if len(lines) &gt; 1:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_397

><td class="source">                        lines = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_398

><td class="source">                        lines.extend(get_lines(opt_parts, indent))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_399

><td class="source">                        lines.extend(get_lines(pos_parts, indent))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_400

><td class="source">                    lines = [prog] + lines<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_401

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_402

><td class="source">                # join lines into usage<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_403

><td class="source">                usage = &#39;\n&#39;.join(lines)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_404

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_405

><td class="source">        # prefix with &#39;usage:&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_406

><td class="source">        return &#39;%s%s\n\n&#39; % (prefix, usage)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_407

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_408

><td class="source">    def _format_actions_usage(self, actions, groups):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_409

><td class="source">        # find group indices and identify actions in groups<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_410

><td class="source">        group_actions = set()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_411

><td class="source">        inserts = {}<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_412

><td class="source">        for group in groups:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_413

><td class="source">            try:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_414

><td class="source">                start = actions.index(group._group_actions[0])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_415

><td class="source">            except ValueError:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_416

><td class="source">                continue<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_417

><td class="source">            else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_418

><td class="source">                end = start + len(group._group_actions)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_419

><td class="source">                if actions[start:end] == group._group_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_420

><td class="source">                    for action in group._group_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_421

><td class="source">                        group_actions.add(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_422

><td class="source">                    if not group.required:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_423

><td class="source">                        if start in inserts:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_424

><td class="source">                            inserts[start] += &#39; [&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_425

><td class="source">                        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_426

><td class="source">                            inserts[start] = &#39;[&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_427

><td class="source">                        inserts[end] = &#39;]&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_428

><td class="source">                    else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_429

><td class="source">                        if start in inserts:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_430

><td class="source">                            inserts[start] += &#39; (&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_431

><td class="source">                        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_432

><td class="source">                            inserts[start] = &#39;(&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_433

><td class="source">                        inserts[end] = &#39;)&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_434

><td class="source">                    for i in range(start + 1, end):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_435

><td class="source">                        inserts[i] = &#39;|&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_436

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_437

><td class="source">        # collect all actions format strings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_438

><td class="source">        parts = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_439

><td class="source">        for i, action in enumerate(actions):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_440

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_441

><td class="source">            # suppressed arguments are marked with None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_442

><td class="source">            # remove | separators for suppressed arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_443

><td class="source">            if action.help is SUPPRESS:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_444

><td class="source">                parts.append(None)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_445

><td class="source">                if inserts.get(i) == &#39;|&#39;:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_446

><td class="source">                    inserts.pop(i)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_447

><td class="source">                elif inserts.get(i + 1) == &#39;|&#39;:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_448

><td class="source">                    inserts.pop(i + 1)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_449

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_450

><td class="source">            # produce all arg strings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_451

><td class="source">            elif not action.option_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_452

><td class="source">                part = self._format_args(action, action.dest)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_453

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_454

><td class="source">                # if it&#39;s in a group, strip the outer []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_455

><td class="source">                if action in group_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_456

><td class="source">                    if part[0] == &#39;[&#39; and part[-1] == &#39;]&#39;:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_457

><td class="source">                        part = part[1:-1]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_458

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_459

><td class="source">                # add the action string to the list<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_460

><td class="source">                parts.append(part)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_461

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_462

><td class="source">            # produce the first way to invoke the option in brackets<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_463

><td class="source">            else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_464

><td class="source">                option_string = action.option_strings[0]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_465

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_466

><td class="source">                # if the Optional doesn&#39;t take a value, format is:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_467

><td class="source">                #    -s or --long<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_468

><td class="source">                if action.nargs == 0:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_469

><td class="source">                    part = &#39;%s&#39; % option_string<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_470

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_471

><td class="source">                # if the Optional takes a value, format is:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_472

><td class="source">                #    -s ARGS or --long ARGS<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_473

><td class="source">                else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_474

><td class="source">                    default = action.dest.upper()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_475

><td class="source">                    args_string = self._format_args(action, default)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_476

><td class="source">                    part = &#39;%s %s&#39; % (option_string, args_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_477

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_478

><td class="source">                # make it look optional if it&#39;s not required or in a group<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_479

><td class="source">                if not action.required and action not in group_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_480

><td class="source">                    part = &#39;[%s]&#39; % part<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_481

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_482

><td class="source">                # add the action string to the list<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_483

><td class="source">                parts.append(part)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_484

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_485

><td class="source">        # insert things at the necessary indices<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_486

><td class="source">        for i in sorted(inserts, reverse=True):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_487

><td class="source">            parts[i:i] = [inserts[i]]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_488

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_489

><td class="source">        # join all the action items with spaces<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_490

><td class="source">        text = &#39; &#39;.join([item for item in parts if item is not None])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_491

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_492

><td class="source">        # clean up separators for mutually exclusive groups<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_493

><td class="source">        open = r&#39;[\[(]&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_494

><td class="source">        close = r&#39;[\])]&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_495

><td class="source">        text = _re.sub(r&#39;(%s) &#39; % open, r&#39;\1&#39;, text)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_496

><td class="source">        text = _re.sub(r&#39; (%s)&#39; % close, r&#39;\1&#39;, text)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_497

><td class="source">        text = _re.sub(r&#39;%s *%s&#39; % (open, close), r&#39;&#39;, text)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_498

><td class="source">        text = _re.sub(r&#39;\(([^|]*)\)&#39;, r&#39;\1&#39;, text)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_499

><td class="source">        text = text.strip()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_500

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_501

><td class="source">        # return the text<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_502

><td class="source">        return text<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_503

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_504

><td class="source">    def _format_text(self, text):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_505

><td class="source">        if &#39;%(prog)&#39; in text:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_506

><td class="source">            text = text % dict(prog=self._prog)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_507

><td class="source">        text_width = self._width - self._current_indent<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_508

><td class="source">        indent = &#39; &#39; * self._current_indent<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_509

><td class="source">        return self._fill_text(text, text_width, indent) + &#39;\n\n&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_510

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_511

><td class="source">    def _format_action(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_512

><td class="source">        # determine the required width and the entry label<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_513

><td class="source">        help_position = min(self._action_max_length + 2,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_514

><td class="source">                            self._max_help_position)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_515

><td class="source">        help_width = self._width - help_position<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_516

><td class="source">        action_width = help_position - self._current_indent - 2<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_517

><td class="source">        action_header = self._format_action_invocation(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_518

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_519

><td class="source">        # ho nelp; start on same line and add a final newline<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_520

><td class="source">        if not action.help:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_521

><td class="source">            tup = self._current_indent, &#39;&#39;, action_header<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_522

><td class="source">            action_header = &#39;%*s%s\n&#39; % tup<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_523

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_524

><td class="source">        # short action name; start on the same line and pad two spaces<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_525

><td class="source">        elif len(action_header) &lt;= action_width:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_526

><td class="source">            tup = self._current_indent, &#39;&#39;, action_width, action_header<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_527

><td class="source">            action_header = &#39;%*s%-*s  &#39; % tup<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_528

><td class="source">            indent_first = 0<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_529

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_530

><td class="source">        # long action name; start on the next line<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_531

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_532

><td class="source">            tup = self._current_indent, &#39;&#39;, action_header<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_533

><td class="source">            action_header = &#39;%*s%s\n&#39; % tup<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_534

><td class="source">            indent_first = help_position<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_535

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_536

><td class="source">        # collect the pieces of the action help<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_537

><td class="source">        parts = [action_header]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_538

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_539

><td class="source">        # if there was help for the action, add lines of help text<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_540

><td class="source">        if action.help:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_541

><td class="source">            help_text = self._expand_help(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_542

><td class="source">            help_lines = self._split_lines(help_text, help_width)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_543

><td class="source">            parts.append(&#39;%*s%s\n&#39; % (indent_first, &#39;&#39;, help_lines[0]))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_544

><td class="source">            for line in help_lines[1:]:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_545

><td class="source">                parts.append(&#39;%*s%s\n&#39; % (help_position, &#39;&#39;, line))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_546

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_547

><td class="source">        # or add a newline if the description doesn&#39;t end with one<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_548

><td class="source">        elif not action_header.endswith(&#39;\n&#39;):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_549

><td class="source">            parts.append(&#39;\n&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_550

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_551

><td class="source">        # if there are any sub-actions, add their help as well<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_552

><td class="source">        for subaction in self._iter_indented_subactions(action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_553

><td class="source">            parts.append(self._format_action(subaction))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_554

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_555

><td class="source">        # return a single string<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_556

><td class="source">        return self._join_parts(parts)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_557

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_558

><td class="source">    def _format_action_invocation(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_559

><td class="source">        if not action.option_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_560

><td class="source">            metavar, = self._metavar_formatter(action, action.dest)(1)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_561

><td class="source">            return metavar<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_562

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_563

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_564

><td class="source">            parts = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_565

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_566

><td class="source">            # if the Optional doesn&#39;t take a value, format is:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_567

><td class="source">            #    -s, --long<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_568

><td class="source">            if action.nargs == 0:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_569

><td class="source">                parts.extend(action.option_strings)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_570

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_571

><td class="source">            # if the Optional takes a value, format is:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_572

><td class="source">            #    -s ARGS, --long ARGS<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_573

><td class="source">            else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_574

><td class="source">                default = action.dest.upper()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_575

><td class="source">                args_string = self._format_args(action, default)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_576

><td class="source">                for option_string in action.option_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_577

><td class="source">                    parts.append(&#39;%s %s&#39; % (option_string, args_string))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_578

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_579

><td class="source">            return &#39;, &#39;.join(parts)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_580

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_581

><td class="source">    def _metavar_formatter(self, action, default_metavar):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_582

><td class="source">        if action.metavar is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_583

><td class="source">            result = action.metavar<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_584

><td class="source">        elif action.choices is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_585

><td class="source">            choice_strs = [str(choice) for choice in action.choices]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_586

><td class="source">            result = &#39;{%s}&#39; % &#39;,&#39;.join(choice_strs)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_587

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_588

><td class="source">            result = default_metavar<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_589

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_590

><td class="source">        def format(tuple_size):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_591

><td class="source">            if isinstance(result, tuple):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_592

><td class="source">                return result<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_593

><td class="source">            else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_594

><td class="source">                return (result, ) * tuple_size<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_595

><td class="source">        return format<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_596

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_597

><td class="source">    def _format_args(self, action, default_metavar):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_598

><td class="source">        get_metavar = self._metavar_formatter(action, default_metavar)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_599

><td class="source">        if action.nargs is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_600

><td class="source">            result = &#39;%s&#39; % get_metavar(1)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_601

><td class="source">        elif action.nargs == OPTIONAL:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_602

><td class="source">            result = &#39;[%s]&#39; % get_metavar(1)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_603

><td class="source">        elif action.nargs == ZERO_OR_MORE:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_604

><td class="source">            result = &#39;[%s [%s ...]]&#39; % get_metavar(2)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_605

><td class="source">        elif action.nargs == ONE_OR_MORE:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_606

><td class="source">            result = &#39;%s [%s ...]&#39; % get_metavar(2)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_607

><td class="source">        elif action.nargs == REMAINDER:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_608

><td class="source">            result = &#39;...&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_609

><td class="source">        elif action.nargs == PARSER:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_610

><td class="source">            result = &#39;%s ...&#39; % get_metavar(1)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_611

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_612

><td class="source">            formats = [&#39;%s&#39; for _ in range(action.nargs)]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_613

><td class="source">            result = &#39; &#39;.join(formats) % get_metavar(action.nargs)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_614

><td class="source">        return result<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_615

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_616

><td class="source">    def _expand_help(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_617

><td class="source">        params = dict(vars(action), prog=self._prog)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_618

><td class="source">        for name in list(params):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_619

><td class="source">            if params[name] is SUPPRESS:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_620

><td class="source">                del params[name]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_621

><td class="source">        for name in list(params):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_622

><td class="source">            if hasattr(params[name], &#39;__name__&#39;):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_623

><td class="source">                params[name] = params[name].__name__<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_624

><td class="source">        if params.get(&#39;choices&#39;) is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_625

><td class="source">            choices_str = &#39;, &#39;.join([str(c) for c in params[&#39;choices&#39;]])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_626

><td class="source">            params[&#39;choices&#39;] = choices_str<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_627

><td class="source">        return self._get_help_string(action) % params<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_628

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_629

><td class="source">    def _iter_indented_subactions(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_630

><td class="source">        try:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_631

><td class="source">            get_subactions = action._get_subactions<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_632

><td class="source">        except AttributeError:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_633

><td class="source">            pass<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_634

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_635

><td class="source">            self._indent()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_636

><td class="source">            for subaction in get_subactions():<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_637

><td class="source">                yield subaction<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_638

><td class="source">            self._dedent()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_639

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_640

><td class="source">    def _split_lines(self, text, width):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_641

><td class="source">        text = self._whitespace_matcher.sub(&#39; &#39;, text).strip()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_642

><td class="source">        return _textwrap.wrap(text, width)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_643

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_644

><td class="source">    def _fill_text(self, text, width, indent):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_645

><td class="source">        text = self._whitespace_matcher.sub(&#39; &#39;, text).strip()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_646

><td class="source">        return _textwrap.fill(text, width, initial_indent=indent,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_647

><td class="source">                                           subsequent_indent=indent)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_648

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_649

><td class="source">    def _get_help_string(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_650

><td class="source">        return action.help<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_651

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_652

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_653

><td class="source">class RawDescriptionHelpFormatter(HelpFormatter):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_654

><td class="source">    &quot;&quot;&quot;Help message formatter which retains any formatting in descriptions.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_655

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_656

><td class="source">    Only the name of this class is considered a public API. All the methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_657

><td class="source">    provided by the class are considered an implementation detail.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_658

><td class="source">    &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_659

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_660

><td class="source">    def _fill_text(self, text, width, indent):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_661

><td class="source">        return &#39;&#39;.join([indent + line for line in text.splitlines(True)])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_662

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_663

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_664

><td class="source">class RawTextHelpFormatter(RawDescriptionHelpFormatter):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_665

><td class="source">    &quot;&quot;&quot;Help message formatter which retains formatting of all help text.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_666

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_667

><td class="source">    Only the name of this class is considered a public API. All the methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_668

><td class="source">    provided by the class are considered an implementation detail.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_669

><td class="source">    &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_670

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_671

><td class="source">    def _split_lines(self, text, width):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_672

><td class="source">        return text.splitlines()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_673

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_674

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_675

><td class="source">class ArgumentDefaultsHelpFormatter(HelpFormatter):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_676

><td class="source">    &quot;&quot;&quot;Help message formatter which adds default values to argument help.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_677

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_678

><td class="source">    Only the name of this class is considered a public API. All the methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_679

><td class="source">    provided by the class are considered an implementation detail.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_680

><td class="source">    &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_681

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_682

><td class="source">    def _get_help_string(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_683

><td class="source">        help = action.help<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_684

><td class="source">        if &#39;%(default)&#39; not in action.help:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_685

><td class="source">            if action.default is not SUPPRESS:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_686

><td class="source">                defaulting_nargs = [OPTIONAL, ZERO_OR_MORE]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_687

><td class="source">                if action.option_strings or action.nargs in defaulting_nargs:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_688

><td class="source">                    help += &#39; (default: %(default)s)&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_689

><td class="source">        return help<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_690

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_691

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_692

><td class="source"># =====================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_693

><td class="source"># Options and Arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_694

><td class="source"># =====================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_695

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_696

><td class="source">def _get_action_name(argument):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_697

><td class="source">    if argument is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_698

><td class="source">        return None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_699

><td class="source">    elif argument.option_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_700

><td class="source">        return  &#39;/&#39;.join(argument.option_strings)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_701

><td class="source">    elif argument.metavar not in (None, SUPPRESS):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_702

><td class="source">        return argument.metavar<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_703

><td class="source">    elif argument.dest not in (None, SUPPRESS):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_704

><td class="source">        return argument.dest<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_705

><td class="source">    else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_706

><td class="source">        return None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_707

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_708

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_709

><td class="source">class ArgumentError(Exception):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_710

><td class="source">    &quot;&quot;&quot;An error from creating or using an argument (optional or positional).<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_711

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_712

><td class="source">    The string value of this exception is the message, augmented with<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_713

><td class="source">    information about the argument that caused it.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_714

><td class="source">    &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_715

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_716

><td class="source">    def __init__(self, argument, message):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_717

><td class="source">        self.argument_name = _get_action_name(argument)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_718

><td class="source">        self.message = message<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_719

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_720

><td class="source">    def __str__(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_721

><td class="source">        if self.argument_name is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_722

><td class="source">            format = &#39;%(message)s&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_723

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_724

><td class="source">            format = &#39;argument %(argument_name)s: %(message)s&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_725

><td class="source">        return format % dict(message=self.message,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_726

><td class="source">                             argument_name=self.argument_name)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_727

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_728

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_729

><td class="source">class ArgumentTypeError(Exception):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_730

><td class="source">    &quot;&quot;&quot;An error from trying to convert a command line string to a type.&quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_731

><td class="source">    pass<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_732

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_733

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_734

><td class="source"># ==============<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_735

><td class="source"># Action classes<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_736

><td class="source"># ==============<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_737

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_738

><td class="source">class Action(_AttributeHolder):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_739

><td class="source">    &quot;&quot;&quot;Information about how to convert command line strings to Python objects.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_740

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_741

><td class="source">    Action objects are used by an ArgumentParser to represent the information<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_742

><td class="source">    needed to parse a single argument from one or more strings from the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_743

><td class="source">    command line. The keyword arguments to the Action constructor are also<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_744

><td class="source">    all attributes of Action instances.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_745

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_746

><td class="source">    Keyword Arguments:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_747

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_748

><td class="source">        - option_strings -- A list of command-line option strings which<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_749

><td class="source">            should be associated with this action.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_750

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_751

><td class="source">        - dest -- The name of the attribute to hold the created object(s)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_752

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_753

><td class="source">        - nargs -- The number of command-line arguments that should be<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_754

><td class="source">            consumed. By default, one argument will be consumed and a single<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_755

><td class="source">            value will be produced.  Other values include:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_756

><td class="source">                - N (an integer) consumes N arguments (and produces a list)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_757

><td class="source">                - &#39;?&#39; consumes zero or one arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_758

><td class="source">                - &#39;*&#39; consumes zero or more arguments (and produces a list)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_759

><td class="source">                - &#39;+&#39; consumes one or more arguments (and produces a list)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_760

><td class="source">            Note that the difference between the default and nargs=1 is that<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_761

><td class="source">            with the default, a single value will be produced, while with<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_762

><td class="source">            nargs=1, a list containing a single value will be produced.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_763

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_764

><td class="source">        - const -- The value to be produced if the option is specified and the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_765

><td class="source">            option uses an action that takes no values.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_766

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_767

><td class="source">        - default -- The value to be produced if the option is not specified.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_768

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_769

><td class="source">        - type -- The type which the command-line arguments should be converted<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_770

><td class="source">            to, should be one of &#39;string&#39;, &#39;int&#39;, &#39;float&#39;, &#39;complex&#39; or a<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_771

><td class="source">            callable object that accepts a single string argument. If None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_772

><td class="source">            &#39;string&#39; is assumed.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_773

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_774

><td class="source">        - choices -- A container of values that should be allowed. If not None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_775

><td class="source">            after a command-line argument has been converted to the appropriate<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_776

><td class="source">            type, an exception will be raised if it is not a member of this<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_777

><td class="source">            collection.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_778

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_779

><td class="source">        - required -- True if the action must always be specified at the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_780

><td class="source">            command line. This is only meaningful for optional command-line<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_781

><td class="source">            arguments.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_782

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_783

><td class="source">        - help -- The help string describing the argument.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_784

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_785

><td class="source">        - metavar -- The name to be used for the option&#39;s argument with the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_786

><td class="source">            help string. If None, the &#39;dest&#39; value will be used as the name.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_787

><td class="source">    &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_788

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_789

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_790

><td class="source">                 option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_791

><td class="source">                 dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_792

><td class="source">                 nargs=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_793

><td class="source">                 const=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_794

><td class="source">                 default=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_795

><td class="source">                 type=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_796

><td class="source">                 choices=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_797

><td class="source">                 required=False,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_798

><td class="source">                 help=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_799

><td class="source">                 metavar=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_800

><td class="source">        self.option_strings = option_strings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_801

><td class="source">        self.dest = dest<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_802

><td class="source">        self.nargs = nargs<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_803

><td class="source">        self.const = const<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_804

><td class="source">        self.default = default<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_805

><td class="source">        self.type = type<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_806

><td class="source">        self.choices = choices<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_807

><td class="source">        self.required = required<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_808

><td class="source">        self.help = help<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_809

><td class="source">        self.metavar = metavar<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_810

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_811

><td class="source">    def _get_kwargs(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_812

><td class="source">        names = [<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_813

><td class="source">            &#39;option_strings&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_814

><td class="source">            &#39;dest&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_815

><td class="source">            &#39;nargs&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_816

><td class="source">            &#39;const&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_817

><td class="source">            &#39;default&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_818

><td class="source">            &#39;type&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_819

><td class="source">            &#39;choices&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_820

><td class="source">            &#39;help&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_821

><td class="source">            &#39;metavar&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_822

><td class="source">        ]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_823

><td class="source">        return [(name, getattr(self, name)) for name in names]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_824

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_825

><td class="source">    def __call__(self, parser, namespace, values, option_string=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_826

><td class="source">        raise NotImplementedError(_(&#39;.__call__() not defined&#39;))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_827

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_828

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_829

><td class="source">class _StoreAction(Action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_830

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_831

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_832

><td class="source">                 option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_833

><td class="source">                 dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_834

><td class="source">                 nargs=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_835

><td class="source">                 const=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_836

><td class="source">                 default=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_837

><td class="source">                 type=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_838

><td class="source">                 choices=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_839

><td class="source">                 required=False,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_840

><td class="source">                 help=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_841

><td class="source">                 metavar=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_842

><td class="source">        if nargs == 0:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_843

><td class="source">            raise ValueError(&#39;nargs for store actions must be &gt; 0; if you &#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_844

><td class="source">                             &#39;have nothing to store, actions such as store &#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_845

><td class="source">                             &#39;true or store const may be more appropriate&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_846

><td class="source">        if const is not None and nargs != OPTIONAL:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_847

><td class="source">            raise ValueError(&#39;nargs must be %r to supply const&#39; % OPTIONAL)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_848

><td class="source">        super(_StoreAction, self).__init__(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_849

><td class="source">            option_strings=option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_850

><td class="source">            dest=dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_851

><td class="source">            nargs=nargs,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_852

><td class="source">            const=const,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_853

><td class="source">            default=default,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_854

><td class="source">            type=type,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_855

><td class="source">            choices=choices,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_856

><td class="source">            required=required,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_857

><td class="source">            help=help,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_858

><td class="source">            metavar=metavar)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_859

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_860

><td class="source">    def __call__(self, parser, namespace, values, option_string=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_861

><td class="source">        setattr(namespace, self.dest, values)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_862

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_863

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_864

><td class="source">class _StoreConstAction(Action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_865

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_866

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_867

><td class="source">                 option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_868

><td class="source">                 dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_869

><td class="source">                 const,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_870

><td class="source">                 default=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_871

><td class="source">                 required=False,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_872

><td class="source">                 help=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_873

><td class="source">                 metavar=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_874

><td class="source">        super(_StoreConstAction, self).__init__(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_875

><td class="source">            option_strings=option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_876

><td class="source">            dest=dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_877

><td class="source">            nargs=0,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_878

><td class="source">            const=const,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_879

><td class="source">            default=default,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_880

><td class="source">            required=required,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_881

><td class="source">            help=help)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_882

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_883

><td class="source">    def __call__(self, parser, namespace, values, option_string=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_884

><td class="source">        setattr(namespace, self.dest, self.const)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_885

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_886

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_887

><td class="source">class _StoreTrueAction(_StoreConstAction):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_888

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_889

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_890

><td class="source">                 option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_891

><td class="source">                 dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_892

><td class="source">                 default=False,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_893

><td class="source">                 required=False,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_894

><td class="source">                 help=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_895

><td class="source">        super(_StoreTrueAction, self).__init__(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_896

><td class="source">            option_strings=option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_897

><td class="source">            dest=dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_898

><td class="source">            const=True,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_899

><td class="source">            default=default,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_900

><td class="source">            required=required,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_901

><td class="source">            help=help)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_902

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_903

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_904

><td class="source">class _StoreFalseAction(_StoreConstAction):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_905

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_906

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_907

><td class="source">                 option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_908

><td class="source">                 dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_909

><td class="source">                 default=True,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_910

><td class="source">                 required=False,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_911

><td class="source">                 help=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_912

><td class="source">        super(_StoreFalseAction, self).__init__(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_913

><td class="source">            option_strings=option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_914

><td class="source">            dest=dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_915

><td class="source">            const=False,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_916

><td class="source">            default=default,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_917

><td class="source">            required=required,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_918

><td class="source">            help=help)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_919

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_920

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_921

><td class="source">class _AppendAction(Action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_922

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_923

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_924

><td class="source">                 option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_925

><td class="source">                 dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_926

><td class="source">                 nargs=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_927

><td class="source">                 const=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_928

><td class="source">                 default=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_929

><td class="source">                 type=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_930

><td class="source">                 choices=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_931

><td class="source">                 required=False,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_932

><td class="source">                 help=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_933

><td class="source">                 metavar=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_934

><td class="source">        if nargs == 0:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_935

><td class="source">            raise ValueError(&#39;nargs for append actions must be &gt; 0; if arg &#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_936

><td class="source">                             &#39;strings are not supplying the value to append, &#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_937

><td class="source">                             &#39;the append const action may be more appropriate&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_938

><td class="source">        if const is not None and nargs != OPTIONAL:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_939

><td class="source">            raise ValueError(&#39;nargs must be %r to supply const&#39; % OPTIONAL)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_940

><td class="source">        super(_AppendAction, self).__init__(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_941

><td class="source">            option_strings=option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_942

><td class="source">            dest=dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_943

><td class="source">            nargs=nargs,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_944

><td class="source">            const=const,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_945

><td class="source">            default=default,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_946

><td class="source">            type=type,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_947

><td class="source">            choices=choices,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_948

><td class="source">            required=required,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_949

><td class="source">            help=help,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_950

><td class="source">            metavar=metavar)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_951

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_952

><td class="source">    def __call__(self, parser, namespace, values, option_string=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_953

><td class="source">        items = _copy.copy(_ensure_value(namespace, self.dest, []))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_954

><td class="source">        items.append(values)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_955

><td class="source">        setattr(namespace, self.dest, items)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_956

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_957

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_958

><td class="source">class _AppendConstAction(Action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_959

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_960

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_961

><td class="source">                 option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_962

><td class="source">                 dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_963

><td class="source">                 const,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_964

><td class="source">                 default=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_965

><td class="source">                 required=False,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_966

><td class="source">                 help=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_967

><td class="source">                 metavar=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_968

><td class="source">        super(_AppendConstAction, self).__init__(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_969

><td class="source">            option_strings=option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_970

><td class="source">            dest=dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_971

><td class="source">            nargs=0,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_972

><td class="source">            const=const,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_973

><td class="source">            default=default,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_974

><td class="source">            required=required,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_975

><td class="source">            help=help,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_976

><td class="source">            metavar=metavar)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_977

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_978

><td class="source">    def __call__(self, parser, namespace, values, option_string=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_979

><td class="source">        items = _copy.copy(_ensure_value(namespace, self.dest, []))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_980

><td class="source">        items.append(self.const)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_981

><td class="source">        setattr(namespace, self.dest, items)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_982

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_983

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_984

><td class="source">class _CountAction(Action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_985

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_986

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_987

><td class="source">                 option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_988

><td class="source">                 dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_989

><td class="source">                 default=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_990

><td class="source">                 required=False,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_991

><td class="source">                 help=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_992

><td class="source">        super(_CountAction, self).__init__(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_993

><td class="source">            option_strings=option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_994

><td class="source">            dest=dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_995

><td class="source">            nargs=0,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_996

><td class="source">            default=default,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_997

><td class="source">            required=required,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_998

><td class="source">            help=help)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_999

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1000

><td class="source">    def __call__(self, parser, namespace, values, option_string=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1001

><td class="source">        new_count = _ensure_value(namespace, self.dest, 0) + 1<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1002

><td class="source">        setattr(namespace, self.dest, new_count)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1003

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1004

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1005

><td class="source">class _HelpAction(Action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1006

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1007

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1008

><td class="source">                 option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1009

><td class="source">                 dest=SUPPRESS,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1010

><td class="source">                 default=SUPPRESS,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1011

><td class="source">                 help=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1012

><td class="source">        super(_HelpAction, self).__init__(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1013

><td class="source">            option_strings=option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1014

><td class="source">            dest=dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1015

><td class="source">            default=default,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1016

><td class="source">            nargs=0,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1017

><td class="source">            help=help)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1018

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1019

><td class="source">    def __call__(self, parser, namespace, values, option_string=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1020

><td class="source">        parser.print_help()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1021

><td class="source">        parser.exit()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1022

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1023

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1024

><td class="source">class _VersionAction(Action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1025

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1026

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1027

><td class="source">                 option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1028

><td class="source">                 version=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1029

><td class="source">                 dest=SUPPRESS,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1030

><td class="source">                 default=SUPPRESS,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1031

><td class="source">                 help=&quot;show program&#39;s version number and exit&quot;):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1032

><td class="source">        super(_VersionAction, self).__init__(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1033

><td class="source">            option_strings=option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1034

><td class="source">            dest=dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1035

><td class="source">            default=default,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1036

><td class="source">            nargs=0,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1037

><td class="source">            help=help)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1038

><td class="source">        self.version = version<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1039

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1040

><td class="source">    def __call__(self, parser, namespace, values, option_string=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1041

><td class="source">        version = self.version<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1042

><td class="source">        if version is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1043

><td class="source">            version = parser.version<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1044

><td class="source">        formatter = parser._get_formatter()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1045

><td class="source">        formatter.add_text(version)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1046

><td class="source">        parser.exit(message=formatter.format_help())<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1047

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1048

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1049

><td class="source">class _SubParsersAction(Action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1050

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1051

><td class="source">    class _ChoicesPseudoAction(Action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1052

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1053

><td class="source">        def __init__(self, name, aliases, help):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1054

><td class="source">            metavar = dest = name<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1055

><td class="source">            if aliases:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1056

><td class="source">                metavar += &#39; (%s)&#39; % &#39;, &#39;.join(aliases)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1057

><td class="source">            sup = super(_SubParsersAction._ChoicesPseudoAction, self)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1058

><td class="source">            sup.__init__(option_strings=[], dest=dest, help=help,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1059

><td class="source">                        metavar=metavar)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1060

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1061

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1062

><td class="source">                 option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1063

><td class="source">                 prog,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1064

><td class="source">                 parser_class,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1065

><td class="source">                 dest=SUPPRESS,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1066

><td class="source">                 help=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1067

><td class="source">                 metavar=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1068

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1069

><td class="source">        self._prog_prefix = prog<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1070

><td class="source">        self._parser_class = parser_class<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1071

><td class="source">        self._name_parser_map = {}<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1072

><td class="source">        self._choices_actions = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1073

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1074

><td class="source">        super(_SubParsersAction, self).__init__(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1075

><td class="source">            option_strings=option_strings,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1076

><td class="source">            dest=dest,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1077

><td class="source">            nargs=PARSER,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1078

><td class="source">            choices=self._name_parser_map,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1079

><td class="source">            help=help,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1080

><td class="source">            metavar=metavar)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1081

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1082

><td class="source">    def add_parser(self, name, **kwargs):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1083

><td class="source">        # set prog from the existing prefix<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1084

><td class="source">        if kwargs.get(&#39;prog&#39;) is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1085

><td class="source">            kwargs[&#39;prog&#39;] = &#39;%s %s&#39; % (self._prog_prefix, name)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1086

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1087

><td class="source">        aliases = kwargs.pop(&#39;aliases&#39;, ())<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1088

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1089

><td class="source">        # create a pseudo-action to hold the choice help<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1090

><td class="source">        if &#39;help&#39; in kwargs:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1091

><td class="source">            help = kwargs.pop(&#39;help&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1092

><td class="source">            choice_action = self._ChoicesPseudoAction(name, aliases, help)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1093

><td class="source">            self._choices_actions.append(choice_action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1094

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1095

><td class="source">        # create the parser and add it to the map<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1096

><td class="source">        parser = self._parser_class(**kwargs)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1097

><td class="source">        self._name_parser_map[name] = parser<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1098

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1099

><td class="source">        # make parser available under aliases also<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1100

><td class="source">        for alias in aliases:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1101

><td class="source">            self._name_parser_map[alias] = parser<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1102

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1103

><td class="source">        return parser<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1104

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1105

><td class="source">    def _get_subactions(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1106

><td class="source">        return self._choices_actions<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1107

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1108

><td class="source">    def __call__(self, parser, namespace, values, option_string=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1109

><td class="source">        parser_name = values[0]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1110

><td class="source">        arg_strings = values[1:]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1111

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1112

><td class="source">        # set the parser name if requested<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1113

><td class="source">        if self.dest is not SUPPRESS:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1114

><td class="source">            setattr(namespace, self.dest, parser_name)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1115

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1116

><td class="source">        # select the parser<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1117

><td class="source">        try:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1118

><td class="source">            parser = self._name_parser_map[parser_name]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1119

><td class="source">        except KeyError:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1120

><td class="source">            tup = parser_name, &#39;, &#39;.join(self._name_parser_map)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1121

><td class="source">            msg = _(&#39;unknown parser %r (choices: %s)&#39; % tup)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1122

><td class="source">            raise ArgumentError(self, msg)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1123

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1124

><td class="source">        # parse all the remaining options into the namespace<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1125

><td class="source">        # store any unrecognized options on the object, so that the top<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1126

><td class="source">        # level parser can decide what to do with them<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1127

><td class="source">        namespace, arg_strings = parser.parse_known_args(arg_strings, namespace)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1128

><td class="source">        if arg_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1129

><td class="source">            vars(namespace).setdefault(_UNRECOGNIZED_ARGS_ATTR, [])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1130

><td class="source">            getattr(namespace, _UNRECOGNIZED_ARGS_ATTR).extend(arg_strings)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1131

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1132

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1133

><td class="source"># ==============<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1134

><td class="source"># Type classes<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1135

><td class="source"># ==============<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1136

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1137

><td class="source">class FileType(object):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1138

><td class="source">    &quot;&quot;&quot;Factory for creating file object types<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1139

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1140

><td class="source">    Instances of FileType are typically passed as type= arguments to the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1141

><td class="source">    ArgumentParser add_argument() method.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1142

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1143

><td class="source">    Keyword Arguments:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1144

><td class="source">        - mode -- A string indicating how the file is to be opened. Accepts the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1145

><td class="source">            same values as the builtin open() function.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1146

><td class="source">        - bufsize -- The file&#39;s desired buffer size. Accepts the same values as<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1147

><td class="source">            the builtin open() function.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1148

><td class="source">    &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1149

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1150

><td class="source">    def __init__(self, mode=&#39;r&#39;, bufsize=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1151

><td class="source">        self._mode = mode<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1152

><td class="source">        self._bufsize = bufsize<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1153

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1154

><td class="source">    def __call__(self, string):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1155

><td class="source">        # the special argument &quot;-&quot; means sys.std{in,out}<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1156

><td class="source">        if string == &#39;-&#39;:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1157

><td class="source">            if &#39;r&#39; in self._mode:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1158

><td class="source">                return _sys.stdin<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1159

><td class="source">            elif &#39;w&#39; in self._mode:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1160

><td class="source">                return _sys.stdout<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1161

><td class="source">            else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1162

><td class="source">                msg = _(&#39;argument &quot;-&quot; with mode %r&#39; % self._mode)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1163

><td class="source">                raise ValueError(msg)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1164

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1165

><td class="source">        # all other arguments are used as file names<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1166

><td class="source">        if self._bufsize:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1167

><td class="source">            return open(string, self._mode, self._bufsize)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1168

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1169

><td class="source">            return open(string, self._mode)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1170

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1171

><td class="source">    def __repr__(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1172

><td class="source">        args = [self._mode, self._bufsize]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1173

><td class="source">        args_str = &#39;, &#39;.join([repr(arg) for arg in args if arg is not None])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1174

><td class="source">        return &#39;%s(%s)&#39; % (type(self).__name__, args_str)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1175

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1176

><td class="source"># ===========================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1177

><td class="source"># Optional and Positional Parsing<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1178

><td class="source"># ===========================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1179

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1180

><td class="source">class Namespace(_AttributeHolder):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1181

><td class="source">    &quot;&quot;&quot;Simple object for storing attributes.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1182

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1183

><td class="source">    Implements equality by attribute names and values, and provides a simple<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1184

><td class="source">    string representation.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1185

><td class="source">    &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1186

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1187

><td class="source">    def __init__(self, **kwargs):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1188

><td class="source">        for name in kwargs:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1189

><td class="source">            setattr(self, name, kwargs[name])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1190

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1191

><td class="source">    __hash__ = None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1192

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1193

><td class="source">    def __eq__(self, other):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1194

><td class="source">        return vars(self) == vars(other)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1195

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1196

><td class="source">    def __ne__(self, other):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1197

><td class="source">        return not (self == other)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1198

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1199

><td class="source">    def __contains__(self, key):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1200

><td class="source">        return key in self.__dict__<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1201

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1202

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1203

><td class="source">class _ActionsContainer(object):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1204

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1205

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1206

><td class="source">                 description,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1207

><td class="source">                 prefix_chars,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1208

><td class="source">                 argument_default,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1209

><td class="source">                 conflict_handler):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1210

><td class="source">        super(_ActionsContainer, self).__init__()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1211

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1212

><td class="source">        self.description = description<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1213

><td class="source">        self.argument_default = argument_default<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1214

><td class="source">        self.prefix_chars = prefix_chars<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1215

><td class="source">        self.conflict_handler = conflict_handler<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1216

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1217

><td class="source">        # set up registries<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1218

><td class="source">        self._registries = {}<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1219

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1220

><td class="source">        # register actions<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1221

><td class="source">        self.register(&#39;action&#39;, None, _StoreAction)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1222

><td class="source">        self.register(&#39;action&#39;, &#39;store&#39;, _StoreAction)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1223

><td class="source">        self.register(&#39;action&#39;, &#39;store_const&#39;, _StoreConstAction)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1224

><td class="source">        self.register(&#39;action&#39;, &#39;store_true&#39;, _StoreTrueAction)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1225

><td class="source">        self.register(&#39;action&#39;, &#39;store_false&#39;, _StoreFalseAction)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1226

><td class="source">        self.register(&#39;action&#39;, &#39;append&#39;, _AppendAction)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1227

><td class="source">        self.register(&#39;action&#39;, &#39;append_const&#39;, _AppendConstAction)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1228

><td class="source">        self.register(&#39;action&#39;, &#39;count&#39;, _CountAction)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1229

><td class="source">        self.register(&#39;action&#39;, &#39;help&#39;, _HelpAction)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1230

><td class="source">        self.register(&#39;action&#39;, &#39;version&#39;, _VersionAction)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1231

><td class="source">        self.register(&#39;action&#39;, &#39;parsers&#39;, _SubParsersAction)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1232

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1233

><td class="source">        # raise an exception if the conflict handler is invalid<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1234

><td class="source">        self._get_handler()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1235

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1236

><td class="source">        # action storage<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1237

><td class="source">        self._actions = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1238

><td class="source">        self._option_string_actions = {}<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1239

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1240

><td class="source">        # groups<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1241

><td class="source">        self._action_groups = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1242

><td class="source">        self._mutually_exclusive_groups = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1243

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1244

><td class="source">        # defaults storage<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1245

><td class="source">        self._defaults = {}<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1246

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1247

><td class="source">        # determines whether an &quot;option&quot; looks like a negative number<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1248

><td class="source">        self._negative_number_matcher = _re.compile(r&#39;^-\d+$|^-\d*\.\d+$&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1249

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1250

><td class="source">        # whether or not there are any optionals that look like negative<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1251

><td class="source">        # numbers -- uses a list so it can be shared and edited<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1252

><td class="source">        self._has_negative_number_optionals = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1253

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1254

><td class="source">    # ====================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1255

><td class="source">    # Registration methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1256

><td class="source">    # ====================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1257

><td class="source">    def register(self, registry_name, value, object):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1258

><td class="source">        registry = self._registries.setdefault(registry_name, {})<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1259

><td class="source">        registry[value] = object<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1260

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1261

><td class="source">    def _registry_get(self, registry_name, value, default=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1262

><td class="source">        return self._registries[registry_name].get(value, default)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1263

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1264

><td class="source">    # ==================================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1265

><td class="source">    # Namespace default accessor methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1266

><td class="source">    # ==================================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1267

><td class="source">    def set_defaults(self, **kwargs):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1268

><td class="source">        self._defaults.update(kwargs)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1269

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1270

><td class="source">        # if these defaults match any existing arguments, replace<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1271

><td class="source">        # the previous default on the object with the new one<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1272

><td class="source">        for action in self._actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1273

><td class="source">            if action.dest in kwargs:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1274

><td class="source">                action.default = kwargs[action.dest]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1275

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1276

><td class="source">    def get_default(self, dest):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1277

><td class="source">        for action in self._actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1278

><td class="source">            if action.dest == dest and action.default is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1279

><td class="source">                return action.default<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1280

><td class="source">        return self._defaults.get(dest, None)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1281

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1282

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1283

><td class="source">    # =======================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1284

><td class="source">    # Adding argument actions<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1285

><td class="source">    # =======================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1286

><td class="source">    def add_argument(self, *args, **kwargs):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1287

><td class="source">        &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1288

><td class="source">        add_argument(dest, ..., name=value, ...)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1289

><td class="source">        add_argument(option_string, option_string, ..., name=value, ...)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1290

><td class="source">        &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1291

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1292

><td class="source">        # if no positional args are supplied or only one is supplied and<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1293

><td class="source">        # it doesn&#39;t look like an option string, parse a positional<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1294

><td class="source">        # argument<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1295

><td class="source">        chars = self.prefix_chars<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1296

><td class="source">        if not args or len(args) == 1 and args[0][0] not in chars:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1297

><td class="source">            if args and &#39;dest&#39; in kwargs:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1298

><td class="source">                raise ValueError(&#39;dest supplied twice for positional argument&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1299

><td class="source">            kwargs = self._get_positional_kwargs(*args, **kwargs)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1300

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1301

><td class="source">        # otherwise, we&#39;re adding an optional argument<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1302

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1303

><td class="source">            kwargs = self._get_optional_kwargs(*args, **kwargs)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1304

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1305

><td class="source">        # if no default was supplied, use the parser-level default<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1306

><td class="source">        if &#39;default&#39; not in kwargs:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1307

><td class="source">            dest = kwargs[&#39;dest&#39;]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1308

><td class="source">            if dest in self._defaults:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1309

><td class="source">                kwargs[&#39;default&#39;] = self._defaults[dest]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1310

><td class="source">            elif self.argument_default is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1311

><td class="source">                kwargs[&#39;default&#39;] = self.argument_default<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1312

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1313

><td class="source">        # create the action object, and add it to the parser<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1314

><td class="source">        action_class = self._pop_action_class(kwargs)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1315

><td class="source">        if not _callable(action_class):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1316

><td class="source">            raise ValueError(&#39;unknown action &quot;%s&quot;&#39; % action_class)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1317

><td class="source">        action = action_class(**kwargs)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1318

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1319

><td class="source">        # raise an error if the action type is not callable<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1320

><td class="source">        type_func = self._registry_get(&#39;type&#39;, action.type, action.type)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1321

><td class="source">        if not _callable(type_func):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1322

><td class="source">            raise ValueError(&#39;%r is not callable&#39; % type_func)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1323

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1324

><td class="source">        return self._add_action(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1325

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1326

><td class="source">    def add_argument_group(self, *args, **kwargs):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1327

><td class="source">        group = _ArgumentGroup(self, *args, **kwargs)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1328

><td class="source">        self._action_groups.append(group)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1329

><td class="source">        return group<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1330

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1331

><td class="source">    def add_mutually_exclusive_group(self, **kwargs):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1332

><td class="source">        group = _MutuallyExclusiveGroup(self, **kwargs)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1333

><td class="source">        self._mutually_exclusive_groups.append(group)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1334

><td class="source">        return group<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1335

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1336

><td class="source">    def _add_action(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1337

><td class="source">        # resolve any conflicts<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1338

><td class="source">        self._check_conflict(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1339

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1340

><td class="source">        # add to actions list<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1341

><td class="source">        self._actions.append(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1342

><td class="source">        action.container = self<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1343

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1344

><td class="source">        # index the action by any option strings it has<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1345

><td class="source">        for option_string in action.option_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1346

><td class="source">            self._option_string_actions[option_string] = action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1347

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1348

><td class="source">        # set the flag if any option strings look like negative numbers<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1349

><td class="source">        for option_string in action.option_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1350

><td class="source">            if self._negative_number_matcher.match(option_string):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1351

><td class="source">                if not self._has_negative_number_optionals:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1352

><td class="source">                    self._has_negative_number_optionals.append(True)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1353

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1354

><td class="source">        # return the created action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1355

><td class="source">        return action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1356

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1357

><td class="source">    def _remove_action(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1358

><td class="source">        self._actions.remove(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1359

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1360

><td class="source">    def _add_container_actions(self, container):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1361

><td class="source">        # collect groups by titles<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1362

><td class="source">        title_group_map = {}<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1363

><td class="source">        for group in self._action_groups:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1364

><td class="source">            if group.title in title_group_map:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1365

><td class="source">                msg = _(&#39;cannot merge actions - two groups are named %r&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1366

><td class="source">                raise ValueError(msg % (group.title))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1367

><td class="source">            title_group_map[group.title] = group<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1368

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1369

><td class="source">        # map each action to its group<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1370

><td class="source">        group_map = {}<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1371

><td class="source">        for group in container._action_groups:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1372

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1373

><td class="source">            # if a group with the title exists, use that, otherwise<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1374

><td class="source">            # create a new group matching the container&#39;s group<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1375

><td class="source">            if group.title not in title_group_map:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1376

><td class="source">                title_group_map[group.title] = self.add_argument_group(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1377

><td class="source">                    title=group.title,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1378

><td class="source">                    description=group.description,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1379

><td class="source">                    conflict_handler=group.conflict_handler)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1380

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1381

><td class="source">            # map the actions to their new group<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1382

><td class="source">            for action in group._group_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1383

><td class="source">                group_map[action] = title_group_map[group.title]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1384

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1385

><td class="source">        # add container&#39;s mutually exclusive groups<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1386

><td class="source">        # NOTE: if add_mutually_exclusive_group ever gains title= and<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1387

><td class="source">        # description= then this code will need to be expanded as above<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1388

><td class="source">        for group in container._mutually_exclusive_groups:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1389

><td class="source">            mutex_group = self.add_mutually_exclusive_group(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1390

><td class="source">                required=group.required)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1391

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1392

><td class="source">            # map the actions to their new mutex group<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1393

><td class="source">            for action in group._group_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1394

><td class="source">                group_map[action] = mutex_group<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1395

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1396

><td class="source">        # add all actions to this container or their group<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1397

><td class="source">        for action in container._actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1398

><td class="source">            group_map.get(action, self)._add_action(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1399

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1400

><td class="source">    def _get_positional_kwargs(self, dest, **kwargs):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1401

><td class="source">        # make sure required is not specified<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1402

><td class="source">        if &#39;required&#39; in kwargs:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1403

><td class="source">            msg = _(&quot;&#39;required&#39; is an invalid argument for positionals&quot;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1404

><td class="source">            raise TypeError(msg)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1405

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1406

><td class="source">        # mark positional arguments as required if at least one is<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1407

><td class="source">        # always required<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1408

><td class="source">        if kwargs.get(&#39;nargs&#39;) not in [OPTIONAL, ZERO_OR_MORE]:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1409

><td class="source">            kwargs[&#39;required&#39;] = True<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1410

><td class="source">        if kwargs.get(&#39;nargs&#39;) == ZERO_OR_MORE and &#39;default&#39; not in kwargs:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1411

><td class="source">            kwargs[&#39;required&#39;] = True<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1412

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1413

><td class="source">        # return the keyword arguments with no option strings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1414

><td class="source">        return dict(kwargs, dest=dest, option_strings=[])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1415

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1416

><td class="source">    def _get_optional_kwargs(self, *args, **kwargs):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1417

><td class="source">        # determine short and long option strings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1418

><td class="source">        option_strings = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1419

><td class="source">        long_option_strings = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1420

><td class="source">        for option_string in args:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1421

><td class="source">            # error on strings that don&#39;t start with an appropriate prefix<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1422

><td class="source">            if not option_string[0] in self.prefix_chars:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1423

><td class="source">                msg = _(&#39;invalid option string %r: &#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1424

><td class="source">                        &#39;must start with a character %r&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1425

><td class="source">                tup = option_string, self.prefix_chars<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1426

><td class="source">                raise ValueError(msg % tup)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1427

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1428

><td class="source">            # strings starting with two prefix characters are long options<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1429

><td class="source">            option_strings.append(option_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1430

><td class="source">            if option_string[0] in self.prefix_chars:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1431

><td class="source">                if len(option_string) &gt; 1:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1432

><td class="source">                    if option_string[1] in self.prefix_chars:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1433

><td class="source">                        long_option_strings.append(option_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1434

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1435

><td class="source">        # infer destination, &#39;--foo-bar&#39; -&gt; &#39;foo_bar&#39; and &#39;-x&#39; -&gt; &#39;x&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1436

><td class="source">        dest = kwargs.pop(&#39;dest&#39;, None)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1437

><td class="source">        if dest is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1438

><td class="source">            if long_option_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1439

><td class="source">                dest_option_string = long_option_strings[0]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1440

><td class="source">            else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1441

><td class="source">                dest_option_string = option_strings[0]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1442

><td class="source">            dest = dest_option_string.lstrip(self.prefix_chars)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1443

><td class="source">            if not dest:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1444

><td class="source">                msg = _(&#39;dest= is required for options like %r&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1445

><td class="source">                raise ValueError(msg % option_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1446

><td class="source">            dest = dest.replace(&#39;-&#39;, &#39;_&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1447

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1448

><td class="source">        # return the updated keyword arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1449

><td class="source">        return dict(kwargs, dest=dest, option_strings=option_strings)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1450

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1451

><td class="source">    def _pop_action_class(self, kwargs, default=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1452

><td class="source">        action = kwargs.pop(&#39;action&#39;, default)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1453

><td class="source">        return self._registry_get(&#39;action&#39;, action, action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1454

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1455

><td class="source">    def _get_handler(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1456

><td class="source">        # determine function from conflict handler string<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1457

><td class="source">        handler_func_name = &#39;_handle_conflict_%s&#39; % self.conflict_handler<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1458

><td class="source">        try:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1459

><td class="source">            return getattr(self, handler_func_name)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1460

><td class="source">        except AttributeError:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1461

><td class="source">            msg = _(&#39;invalid conflict_resolution value: %r&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1462

><td class="source">            raise ValueError(msg % self.conflict_handler)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1463

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1464

><td class="source">    def _check_conflict(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1465

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1466

><td class="source">        # find all options that conflict with this option<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1467

><td class="source">        confl_optionals = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1468

><td class="source">        for option_string in action.option_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1469

><td class="source">            if option_string in self._option_string_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1470

><td class="source">                confl_optional = self._option_string_actions[option_string]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1471

><td class="source">                confl_optionals.append((option_string, confl_optional))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1472

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1473

><td class="source">        # resolve any conflicts<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1474

><td class="source">        if confl_optionals:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1475

><td class="source">            conflict_handler = self._get_handler()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1476

><td class="source">            conflict_handler(action, confl_optionals)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1477

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1478

><td class="source">    def _handle_conflict_error(self, action, conflicting_actions):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1479

><td class="source">        message = _(&#39;conflicting option string(s): %s&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1480

><td class="source">        conflict_string = &#39;, &#39;.join([option_string<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1481

><td class="source">                                     for option_string, action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1482

><td class="source">                                     in conflicting_actions])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1483

><td class="source">        raise ArgumentError(action, message % conflict_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1484

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1485

><td class="source">    def _handle_conflict_resolve(self, action, conflicting_actions):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1486

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1487

><td class="source">        # remove all conflicting options<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1488

><td class="source">        for option_string, action in conflicting_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1489

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1490

><td class="source">            # remove the conflicting option<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1491

><td class="source">            action.option_strings.remove(option_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1492

><td class="source">            self._option_string_actions.pop(option_string, None)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1493

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1494

><td class="source">            # if the option now has no option string, remove it from the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1495

><td class="source">            # container holding it<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1496

><td class="source">            if not action.option_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1497

><td class="source">                action.container._remove_action(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1498

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1499

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1500

><td class="source">class _ArgumentGroup(_ActionsContainer):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1501

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1502

><td class="source">    def __init__(self, container, title=None, description=None, **kwargs):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1503

><td class="source">        # add any missing keyword arguments by checking the container<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1504

><td class="source">        update = kwargs.setdefault<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1505

><td class="source">        update(&#39;conflict_handler&#39;, container.conflict_handler)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1506

><td class="source">        update(&#39;prefix_chars&#39;, container.prefix_chars)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1507

><td class="source">        update(&#39;argument_default&#39;, container.argument_default)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1508

><td class="source">        super_init = super(_ArgumentGroup, self).__init__<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1509

><td class="source">        super_init(description=description, **kwargs)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1510

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1511

><td class="source">        # group attributes<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1512

><td class="source">        self.title = title<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1513

><td class="source">        self._group_actions = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1514

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1515

><td class="source">        # share most attributes with the container<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1516

><td class="source">        self._registries = container._registries<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1517

><td class="source">        self._actions = container._actions<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1518

><td class="source">        self._option_string_actions = container._option_string_actions<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1519

><td class="source">        self._defaults = container._defaults<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1520

><td class="source">        self._has_negative_number_optionals = \<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1521

><td class="source">            container._has_negative_number_optionals<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1522

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1523

><td class="source">    def _add_action(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1524

><td class="source">        action = super(_ArgumentGroup, self)._add_action(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1525

><td class="source">        self._group_actions.append(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1526

><td class="source">        return action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1527

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1528

><td class="source">    def _remove_action(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1529

><td class="source">        super(_ArgumentGroup, self)._remove_action(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1530

><td class="source">        self._group_actions.remove(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1531

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1532

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1533

><td class="source">class _MutuallyExclusiveGroup(_ArgumentGroup):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1534

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1535

><td class="source">    def __init__(self, container, required=False):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1536

><td class="source">        super(_MutuallyExclusiveGroup, self).__init__(container)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1537

><td class="source">        self.required = required<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1538

><td class="source">        self._container = container<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1539

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1540

><td class="source">    def _add_action(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1541

><td class="source">        if action.required:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1542

><td class="source">            msg = _(&#39;mutually exclusive arguments must be optional&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1543

><td class="source">            raise ValueError(msg)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1544

><td class="source">        action = self._container._add_action(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1545

><td class="source">        self._group_actions.append(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1546

><td class="source">        return action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1547

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1548

><td class="source">    def _remove_action(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1549

><td class="source">        self._container._remove_action(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1550

><td class="source">        self._group_actions.remove(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1551

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1552

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1553

><td class="source">class ArgumentParser(_AttributeHolder, _ActionsContainer):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1554

><td class="source">    &quot;&quot;&quot;Object for parsing command line strings into Python objects.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1555

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1556

><td class="source">    Keyword Arguments:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1557

><td class="source">        - prog -- The name of the program (default: sys.argv[0])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1558

><td class="source">        - usage -- A usage message (default: auto-generated from arguments)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1559

><td class="source">        - description -- A description of what the program does<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1560

><td class="source">        - epilog -- Text following the argument descriptions<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1561

><td class="source">        - parents -- Parsers whose arguments should be copied into this one<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1562

><td class="source">        - formatter_class -- HelpFormatter class for printing help messages<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1563

><td class="source">        - prefix_chars -- Characters that prefix optional arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1564

><td class="source">        - fromfile_prefix_chars -- Characters that prefix files containing<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1565

><td class="source">            additional arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1566

><td class="source">        - argument_default -- The default value for all arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1567

><td class="source">        - conflict_handler -- String indicating how to handle conflicts<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1568

><td class="source">        - add_help -- Add a -h/-help option<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1569

><td class="source">    &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1570

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1571

><td class="source">    def __init__(self,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1572

><td class="source">                 prog=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1573

><td class="source">                 usage=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1574

><td class="source">                 description=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1575

><td class="source">                 epilog=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1576

><td class="source">                 version=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1577

><td class="source">                 parents=[],<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1578

><td class="source">                 formatter_class=HelpFormatter,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1579

><td class="source">                 prefix_chars=&#39;-&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1580

><td class="source">                 fromfile_prefix_chars=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1581

><td class="source">                 argument_default=None,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1582

><td class="source">                 conflict_handler=&#39;error&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1583

><td class="source">                 add_help=True):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1584

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1585

><td class="source">        if version is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1586

><td class="source">            import warnings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1587

><td class="source">            warnings.warn(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1588

><td class="source">                &quot;&quot;&quot;The &quot;version&quot; argument to ArgumentParser is deprecated. &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1589

><td class="source">                &quot;&quot;&quot;Please use &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1590

><td class="source">                &quot;&quot;&quot;&quot;add_argument(..., action=&#39;version&#39;, version=&quot;N&quot;, ...)&quot; &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1591

><td class="source">                &quot;&quot;&quot;instead&quot;&quot;&quot;, DeprecationWarning)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1592

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1593

><td class="source">        superinit = super(ArgumentParser, self).__init__<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1594

><td class="source">        superinit(description=description,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1595

><td class="source">                  prefix_chars=prefix_chars,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1596

><td class="source">                  argument_default=argument_default,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1597

><td class="source">                  conflict_handler=conflict_handler)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1598

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1599

><td class="source">        # default setting for prog<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1600

><td class="source">        if prog is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1601

><td class="source">            prog = _os.path.basename(_sys.argv[0])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1602

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1603

><td class="source">        self.prog = prog<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1604

><td class="source">        self.usage = usage<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1605

><td class="source">        self.epilog = epilog<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1606

><td class="source">        self.version = version<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1607

><td class="source">        self.formatter_class = formatter_class<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1608

><td class="source">        self.fromfile_prefix_chars = fromfile_prefix_chars<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1609

><td class="source">        self.add_help = add_help<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1610

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1611

><td class="source">        add_group = self.add_argument_group<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1612

><td class="source">        self._positionals = add_group(_(&#39;positional arguments&#39;))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1613

><td class="source">        self._optionals = add_group(_(&#39;optional arguments&#39;))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1614

><td class="source">        self._subparsers = None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1615

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1616

><td class="source">        # register types<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1617

><td class="source">        def identity(string):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1618

><td class="source">            return string<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1619

><td class="source">        self.register(&#39;type&#39;, None, identity)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1620

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1621

><td class="source">        # add help and version arguments if necessary<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1622

><td class="source">        # (using explicit default to override global argument_default)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1623

><td class="source">        if &#39;-&#39; in prefix_chars:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1624

><td class="source">            default_prefix = &#39;-&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1625

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1626

><td class="source">            default_prefix = prefix_chars[0]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1627

><td class="source">        if self.add_help:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1628

><td class="source">            self.add_argument(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1629

><td class="source">                default_prefix+&#39;h&#39;, default_prefix*2+&#39;help&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1630

><td class="source">                action=&#39;help&#39;, default=SUPPRESS,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1631

><td class="source">                help=_(&#39;show this help message and exit&#39;))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1632

><td class="source">        if self.version:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1633

><td class="source">            self.add_argument(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1634

><td class="source">                default_prefix+&#39;v&#39;, default_prefix*2+&#39;version&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1635

><td class="source">                action=&#39;version&#39;, default=SUPPRESS,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1636

><td class="source">                version=self.version,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1637

><td class="source">                help=_(&quot;show program&#39;s version number and exit&quot;))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1638

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1639

><td class="source">        # add parent arguments and defaults<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1640

><td class="source">        for parent in parents:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1641

><td class="source">            self._add_container_actions(parent)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1642

><td class="source">            try:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1643

><td class="source">                defaults = parent._defaults<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1644

><td class="source">            except AttributeError:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1645

><td class="source">                pass<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1646

><td class="source">            else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1647

><td class="source">                self._defaults.update(defaults)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1648

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1649

><td class="source">    # =======================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1650

><td class="source">    # Pretty __repr__ methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1651

><td class="source">    # =======================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1652

><td class="source">    def _get_kwargs(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1653

><td class="source">        names = [<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1654

><td class="source">            &#39;prog&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1655

><td class="source">            &#39;usage&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1656

><td class="source">            &#39;description&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1657

><td class="source">            &#39;version&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1658

><td class="source">            &#39;formatter_class&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1659

><td class="source">            &#39;conflict_handler&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1660

><td class="source">            &#39;add_help&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1661

><td class="source">        ]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1662

><td class="source">        return [(name, getattr(self, name)) for name in names]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1663

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1664

><td class="source">    # ==================================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1665

><td class="source">    # Optional/Positional adding methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1666

><td class="source">    # ==================================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1667

><td class="source">    def add_subparsers(self, **kwargs):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1668

><td class="source">        if self._subparsers is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1669

><td class="source">            self.error(_(&#39;cannot have multiple subparser arguments&#39;))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1670

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1671

><td class="source">        # add the parser class to the arguments if it&#39;s not present<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1672

><td class="source">        kwargs.setdefault(&#39;parser_class&#39;, type(self))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1673

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1674

><td class="source">        if &#39;title&#39; in kwargs or &#39;description&#39; in kwargs:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1675

><td class="source">            title = _(kwargs.pop(&#39;title&#39;, &#39;subcommands&#39;))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1676

><td class="source">            description = _(kwargs.pop(&#39;description&#39;, None))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1677

><td class="source">            self._subparsers = self.add_argument_group(title, description)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1678

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1679

><td class="source">            self._subparsers = self._positionals<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1680

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1681

><td class="source">        # prog defaults to the usage message of this parser, skipping<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1682

><td class="source">        # optional arguments and with no &quot;usage:&quot; prefix<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1683

><td class="source">        if kwargs.get(&#39;prog&#39;) is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1684

><td class="source">            formatter = self._get_formatter()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1685

><td class="source">            positionals = self._get_positional_actions()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1686

><td class="source">            groups = self._mutually_exclusive_groups<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1687

><td class="source">            formatter.add_usage(self.usage, positionals, groups, &#39;&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1688

><td class="source">            kwargs[&#39;prog&#39;] = formatter.format_help().strip()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1689

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1690

><td class="source">        # create the parsers action and add it to the positionals list<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1691

><td class="source">        parsers_class = self._pop_action_class(kwargs, &#39;parsers&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1692

><td class="source">        action = parsers_class(option_strings=[], **kwargs)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1693

><td class="source">        self._subparsers._add_action(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1694

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1695

><td class="source">        # return the created parsers action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1696

><td class="source">        return action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1697

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1698

><td class="source">    def _add_action(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1699

><td class="source">        if action.option_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1700

><td class="source">            self._optionals._add_action(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1701

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1702

><td class="source">            self._positionals._add_action(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1703

><td class="source">        return action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1704

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1705

><td class="source">    def _get_optional_actions(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1706

><td class="source">        return [action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1707

><td class="source">                for action in self._actions<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1708

><td class="source">                if action.option_strings]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1709

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1710

><td class="source">    def _get_positional_actions(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1711

><td class="source">        return [action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1712

><td class="source">                for action in self._actions<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1713

><td class="source">                if not action.option_strings]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1714

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1715

><td class="source">    # =====================================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1716

><td class="source">    # Command line argument parsing methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1717

><td class="source">    # =====================================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1718

><td class="source">    def parse_args(self, args=None, namespace=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1719

><td class="source">        args, argv = self.parse_known_args(args, namespace)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1720

><td class="source">        if argv:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1721

><td class="source">            msg = _(&#39;unrecognized arguments: %s&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1722

><td class="source">            self.error(msg % &#39; &#39;.join(argv))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1723

><td class="source">        return args<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1724

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1725

><td class="source">    def parse_known_args(self, args=None, namespace=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1726

><td class="source">        # args default to the system args<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1727

><td class="source">        if args is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1728

><td class="source">            args = _sys.argv[1:]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1729

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1730

><td class="source">        # default Namespace built from parser defaults<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1731

><td class="source">        if namespace is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1732

><td class="source">            namespace = Namespace()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1733

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1734

><td class="source">        # add any action defaults that aren&#39;t present<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1735

><td class="source">        for action in self._actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1736

><td class="source">            if action.dest is not SUPPRESS:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1737

><td class="source">                if not hasattr(namespace, action.dest):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1738

><td class="source">                    if action.default is not SUPPRESS:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1739

><td class="source">                        default = action.default<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1740

><td class="source">                        if isinstance(action.default, basestring):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1741

><td class="source">                            default = self._get_value(action, default)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1742

><td class="source">                        setattr(namespace, action.dest, default)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1743

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1744

><td class="source">        # add any parser defaults that aren&#39;t present<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1745

><td class="source">        for dest in self._defaults:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1746

><td class="source">            if not hasattr(namespace, dest):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1747

><td class="source">                setattr(namespace, dest, self._defaults[dest])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1748

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1749

><td class="source">        # parse the arguments and exit if there are any errors<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1750

><td class="source">        try:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1751

><td class="source">            namespace, args = self._parse_known_args(args, namespace)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1752

><td class="source">            if hasattr(namespace, _UNRECOGNIZED_ARGS_ATTR):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1753

><td class="source">                args.extend(getattr(namespace, _UNRECOGNIZED_ARGS_ATTR))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1754

><td class="source">                delattr(namespace, _UNRECOGNIZED_ARGS_ATTR)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1755

><td class="source">            return namespace, args<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1756

><td class="source">        except ArgumentError:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1757

><td class="source">            err = _sys.exc_info()[1]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1758

><td class="source">            self.error(str(err))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1759

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1760

><td class="source">    def _parse_known_args(self, arg_strings, namespace):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1761

><td class="source">        # replace arg strings that are file references<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1762

><td class="source">        if self.fromfile_prefix_chars is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1763

><td class="source">            arg_strings = self._read_args_from_files(arg_strings)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1764

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1765

><td class="source">        # map all mutually exclusive arguments to the other arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1766

><td class="source">        # they can&#39;t occur with<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1767

><td class="source">        action_conflicts = {}<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1768

><td class="source">        for mutex_group in self._mutually_exclusive_groups:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1769

><td class="source">            group_actions = mutex_group._group_actions<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1770

><td class="source">            for i, mutex_action in enumerate(mutex_group._group_actions):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1771

><td class="source">                conflicts = action_conflicts.setdefault(mutex_action, [])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1772

><td class="source">                conflicts.extend(group_actions[:i])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1773

><td class="source">                conflicts.extend(group_actions[i + 1:])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1774

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1775

><td class="source">        # find all option indices, and determine the arg_string_pattern<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1776

><td class="source">        # which has an &#39;O&#39; if there is an option at an index,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1777

><td class="source">        # an &#39;A&#39; if there is an argument, or a &#39;-&#39; if there is a &#39;--&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1778

><td class="source">        option_string_indices = {}<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1779

><td class="source">        arg_string_pattern_parts = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1780

><td class="source">        arg_strings_iter = iter(arg_strings)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1781

><td class="source">        for i, arg_string in enumerate(arg_strings_iter):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1782

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1783

><td class="source">            # all args after -- are non-options<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1784

><td class="source">            if arg_string == &#39;--&#39;:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1785

><td class="source">                arg_string_pattern_parts.append(&#39;-&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1786

><td class="source">                for arg_string in arg_strings_iter:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1787

><td class="source">                    arg_string_pattern_parts.append(&#39;A&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1788

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1789

><td class="source">            # otherwise, add the arg to the arg strings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1790

><td class="source">            # and note the index if it was an option<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1791

><td class="source">            else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1792

><td class="source">                option_tuple = self._parse_optional(arg_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1793

><td class="source">                if option_tuple is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1794

><td class="source">                    pattern = &#39;A&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1795

><td class="source">                else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1796

><td class="source">                    option_string_indices[i] = option_tuple<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1797

><td class="source">                    pattern = &#39;O&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1798

><td class="source">                arg_string_pattern_parts.append(pattern)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1799

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1800

><td class="source">        # join the pieces together to form the pattern<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1801

><td class="source">        arg_strings_pattern = &#39;&#39;.join(arg_string_pattern_parts)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1802

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1803

><td class="source">        # converts arg strings to the appropriate and then takes the action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1804

><td class="source">        seen_actions = set()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1805

><td class="source">        seen_non_default_actions = set()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1806

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1807

><td class="source">        def take_action(action, argument_strings, option_string=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1808

><td class="source">            seen_actions.add(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1809

><td class="source">            argument_values = self._get_values(action, argument_strings)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1810

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1811

><td class="source">            # error if this argument is not allowed with other previously<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1812

><td class="source">            # seen arguments, assuming that actions that use the default<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1813

><td class="source">            # value don&#39;t really count as &quot;present&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1814

><td class="source">            if argument_values is not action.default:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1815

><td class="source">                seen_non_default_actions.add(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1816

><td class="source">                for conflict_action in action_conflicts.get(action, []):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1817

><td class="source">                    if conflict_action in seen_non_default_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1818

><td class="source">                        msg = _(&#39;not allowed with argument %s&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1819

><td class="source">                        action_name = _get_action_name(conflict_action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1820

><td class="source">                        raise ArgumentError(action, msg % action_name)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1821

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1822

><td class="source">            # take the action if we didn&#39;t receive a SUPPRESS value<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1823

><td class="source">            # (e.g. from a default)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1824

><td class="source">            if argument_values is not SUPPRESS:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1825

><td class="source">                action(self, namespace, argument_values, option_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1826

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1827

><td class="source">        # function to convert arg_strings into an optional action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1828

><td class="source">        def consume_optional(start_index):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1829

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1830

><td class="source">            # get the optional identified at this index<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1831

><td class="source">            option_tuple = option_string_indices[start_index]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1832

><td class="source">            action, option_string, explicit_arg = option_tuple<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1833

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1834

><td class="source">            # identify additional optionals in the same arg string<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1835

><td class="source">            # (e.g. -xyz is the same as -x -y -z if no args are required)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1836

><td class="source">            match_argument = self._match_argument<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1837

><td class="source">            action_tuples = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1838

><td class="source">            while True:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1839

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1840

><td class="source">                # if we found no optional action, skip it<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1841

><td class="source">                if action is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1842

><td class="source">                    extras.append(arg_strings[start_index])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1843

><td class="source">                    return start_index + 1<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1844

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1845

><td class="source">                # if there is an explicit argument, try to match the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1846

><td class="source">                # optional&#39;s string arguments to only this<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1847

><td class="source">                if explicit_arg is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1848

><td class="source">                    arg_count = match_argument(action, &#39;A&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1849

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1850

><td class="source">                    # if the action is a single-dash option and takes no<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1851

><td class="source">                    # arguments, try to parse more single-dash options out<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1852

><td class="source">                    # of the tail of the option string<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1853

><td class="source">                    chars = self.prefix_chars<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1854

><td class="source">                    if arg_count == 0 and option_string[1] not in chars:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1855

><td class="source">                        action_tuples.append((action, [], option_string))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1856

><td class="source">                        char = option_string[0]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1857

><td class="source">                        option_string = char + explicit_arg[0]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1858

><td class="source">                        new_explicit_arg = explicit_arg[1:] or None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1859

><td class="source">                        optionals_map = self._option_string_actions<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1860

><td class="source">                        if option_string in optionals_map:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1861

><td class="source">                            action = optionals_map[option_string]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1862

><td class="source">                            explicit_arg = new_explicit_arg<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1863

><td class="source">                        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1864

><td class="source">                            msg = _(&#39;ignored explicit argument %r&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1865

><td class="source">                            raise ArgumentError(action, msg % explicit_arg)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1866

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1867

><td class="source">                    # if the action expect exactly one argument, we&#39;ve<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1868

><td class="source">                    # successfully matched the option; exit the loop<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1869

><td class="source">                    elif arg_count == 1:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1870

><td class="source">                        stop = start_index + 1<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1871

><td class="source">                        args = [explicit_arg]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1872

><td class="source">                        action_tuples.append((action, args, option_string))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1873

><td class="source">                        break<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1874

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1875

><td class="source">                    # error if a double-dash option did not use the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1876

><td class="source">                    # explicit argument<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1877

><td class="source">                    else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1878

><td class="source">                        msg = _(&#39;ignored explicit argument %r&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1879

><td class="source">                        raise ArgumentError(action, msg % explicit_arg)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1880

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1881

><td class="source">                # if there is no explicit argument, try to match the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1882

><td class="source">                # optional&#39;s string arguments with the following strings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1883

><td class="source">                # if successful, exit the loop<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1884

><td class="source">                else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1885

><td class="source">                    start = start_index + 1<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1886

><td class="source">                    selected_patterns = arg_strings_pattern[start:]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1887

><td class="source">                    arg_count = match_argument(action, selected_patterns)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1888

><td class="source">                    stop = start + arg_count<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1889

><td class="source">                    args = arg_strings[start:stop]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1890

><td class="source">                    action_tuples.append((action, args, option_string))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1891

><td class="source">                    break<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1892

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1893

><td class="source">            # add the Optional to the list and return the index at which<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1894

><td class="source">            # the Optional&#39;s string args stopped<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1895

><td class="source">            assert action_tuples<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1896

><td class="source">            for action, args, option_string in action_tuples:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1897

><td class="source">                take_action(action, args, option_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1898

><td class="source">            return stop<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1899

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1900

><td class="source">        # the list of Positionals left to be parsed; this is modified<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1901

><td class="source">        # by consume_positionals()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1902

><td class="source">        positionals = self._get_positional_actions()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1903

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1904

><td class="source">        # function to convert arg_strings into positional actions<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1905

><td class="source">        def consume_positionals(start_index):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1906

><td class="source">            # match as many Positionals as possible<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1907

><td class="source">            match_partial = self._match_arguments_partial<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1908

><td class="source">            selected_pattern = arg_strings_pattern[start_index:]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1909

><td class="source">            arg_counts = match_partial(positionals, selected_pattern)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1910

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1911

><td class="source">            # slice off the appropriate arg strings for each Positional<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1912

><td class="source">            # and add the Positional and its args to the list<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1913

><td class="source">            for action, arg_count in zip(positionals, arg_counts):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1914

><td class="source">                args = arg_strings[start_index: start_index + arg_count]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1915

><td class="source">                start_index += arg_count<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1916

><td class="source">                take_action(action, args)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1917

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1918

><td class="source">            # slice off the Positionals that we just parsed and return the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1919

><td class="source">            # index at which the Positionals&#39; string args stopped<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1920

><td class="source">            positionals[:] = positionals[len(arg_counts):]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1921

><td class="source">            return start_index<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1922

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1923

><td class="source">        # consume Positionals and Optionals alternately, until we have<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1924

><td class="source">        # passed the last option string<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1925

><td class="source">        extras = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1926

><td class="source">        start_index = 0<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1927

><td class="source">        if option_string_indices:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1928

><td class="source">            max_option_string_index = max(option_string_indices)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1929

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1930

><td class="source">            max_option_string_index = -1<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1931

><td class="source">        while start_index &lt;= max_option_string_index:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1932

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1933

><td class="source">            # consume any Positionals preceding the next option<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1934

><td class="source">            next_option_string_index = min([<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1935

><td class="source">                index<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1936

><td class="source">                for index in option_string_indices<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1937

><td class="source">                if index &gt;= start_index])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1938

><td class="source">            if start_index != next_option_string_index:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1939

><td class="source">                positionals_end_index = consume_positionals(start_index)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1940

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1941

><td class="source">                # only try to parse the next optional if we didn&#39;t consume<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1942

><td class="source">                # the option string during the positionals parsing<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1943

><td class="source">                if positionals_end_index &gt; start_index:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1944

><td class="source">                    start_index = positionals_end_index<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1945

><td class="source">                    continue<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1946

><td class="source">                else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1947

><td class="source">                    start_index = positionals_end_index<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1948

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1949

><td class="source">            # if we consumed all the positionals we could and we&#39;re not<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1950

><td class="source">            # at the index of an option string, there were extra arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1951

><td class="source">            if start_index not in option_string_indices:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1952

><td class="source">                strings = arg_strings[start_index:next_option_string_index]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1953

><td class="source">                extras.extend(strings)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1954

><td class="source">                start_index = next_option_string_index<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1955

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1956

><td class="source">            # consume the next optional and any arguments for it<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1957

><td class="source">            start_index = consume_optional(start_index)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1958

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1959

><td class="source">        # consume any positionals following the last Optional<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1960

><td class="source">        stop_index = consume_positionals(start_index)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1961

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1962

><td class="source">        # if we didn&#39;t consume all the argument strings, there were extras<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1963

><td class="source">        extras.extend(arg_strings[stop_index:])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1964

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1965

><td class="source">        # if we didn&#39;t use all the Positional objects, there were too few<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1966

><td class="source">        # arg strings supplied.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1967

><td class="source">        if positionals:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1968

><td class="source">            self.error(_(&#39;too few arguments&#39;))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1969

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1970

><td class="source">        # make sure all required actions were present<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1971

><td class="source">        for action in self._actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1972

><td class="source">            if action.required:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1973

><td class="source">                if action not in seen_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1974

><td class="source">                    name = _get_action_name(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1975

><td class="source">                    self.error(_(&#39;argument %s is required&#39;) % name)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1976

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1977

><td class="source">        # make sure all required groups had one option present<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1978

><td class="source">        for group in self._mutually_exclusive_groups:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1979

><td class="source">            if group.required:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1980

><td class="source">                for action in group._group_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1981

><td class="source">                    if action in seen_non_default_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1982

><td class="source">                        break<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1983

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1984

><td class="source">                # if no actions were used, report the error<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1985

><td class="source">                else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1986

><td class="source">                    names = [_get_action_name(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1987

><td class="source">                             for action in group._group_actions<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1988

><td class="source">                             if action.help is not SUPPRESS]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1989

><td class="source">                    msg = _(&#39;one of the arguments %s is required&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1990

><td class="source">                    self.error(msg % &#39; &#39;.join(names))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1991

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1992

><td class="source">        # return the updated namespace and the extra arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1993

><td class="source">        return namespace, extras<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1994

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1995

><td class="source">    def _read_args_from_files(self, arg_strings):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1996

><td class="source">        # expand arguments referencing files<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1997

><td class="source">        new_arg_strings = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1998

><td class="source">        for arg_string in arg_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_1999

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2000

><td class="source">            # for regular arguments, just add them back into the list<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2001

><td class="source">            if arg_string[0] not in self.fromfile_prefix_chars:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2002

><td class="source">                new_arg_strings.append(arg_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2003

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2004

><td class="source">            # replace arguments referencing files with the file content<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2005

><td class="source">            else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2006

><td class="source">                try:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2007

><td class="source">                    args_file = open(arg_string[1:])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2008

><td class="source">                    try:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2009

><td class="source">                        arg_strings = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2010

><td class="source">                        for arg_line in args_file.read().splitlines():<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2011

><td class="source">                            for arg in self.convert_arg_line_to_args(arg_line):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2012

><td class="source">                                arg_strings.append(arg)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2013

><td class="source">                        arg_strings = self._read_args_from_files(arg_strings)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2014

><td class="source">                        new_arg_strings.extend(arg_strings)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2015

><td class="source">                    finally:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2016

><td class="source">                        args_file.close()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2017

><td class="source">                except IOError:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2018

><td class="source">                    err = _sys.exc_info()[1]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2019

><td class="source">                    self.error(str(err))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2020

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2021

><td class="source">        # return the modified argument list<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2022

><td class="source">        return new_arg_strings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2023

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2024

><td class="source">    def convert_arg_line_to_args(self, arg_line):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2025

><td class="source">        return [arg_line]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2026

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2027

><td class="source">    def _match_argument(self, action, arg_strings_pattern):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2028

><td class="source">        # match the pattern for this action to the arg strings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2029

><td class="source">        nargs_pattern = self._get_nargs_pattern(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2030

><td class="source">        match = _re.match(nargs_pattern, arg_strings_pattern)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2031

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2032

><td class="source">        # raise an exception if we weren&#39;t able to find a match<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2033

><td class="source">        if match is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2034

><td class="source">            nargs_errors = {<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2035

><td class="source">                None: _(&#39;expected one argument&#39;),<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2036

><td class="source">                OPTIONAL: _(&#39;expected at most one argument&#39;),<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2037

><td class="source">                ONE_OR_MORE: _(&#39;expected at least one argument&#39;),<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2038

><td class="source">            }<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2039

><td class="source">            default = _(&#39;expected %s argument(s)&#39;) % action.nargs<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2040

><td class="source">            msg = nargs_errors.get(action.nargs, default)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2041

><td class="source">            raise ArgumentError(action, msg)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2042

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2043

><td class="source">        # return the number of arguments matched<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2044

><td class="source">        return len(match.group(1))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2045

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2046

><td class="source">    def _match_arguments_partial(self, actions, arg_strings_pattern):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2047

><td class="source">        # progressively shorten the actions list by slicing off the<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2048

><td class="source">        # final actions until we find a match<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2049

><td class="source">        result = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2050

><td class="source">        for i in range(len(actions), 0, -1):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2051

><td class="source">            actions_slice = actions[:i]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2052

><td class="source">            pattern = &#39;&#39;.join([self._get_nargs_pattern(action)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2053

><td class="source">                               for action in actions_slice])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2054

><td class="source">            match = _re.match(pattern, arg_strings_pattern)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2055

><td class="source">            if match is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2056

><td class="source">                result.extend([len(string) for string in match.groups()])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2057

><td class="source">                break<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2058

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2059

><td class="source">        # return the list of arg string counts<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2060

><td class="source">        return result<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2061

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2062

><td class="source">    def _parse_optional(self, arg_string):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2063

><td class="source">        # if it&#39;s an empty string, it was meant to be a positional<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2064

><td class="source">        if not arg_string:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2065

><td class="source">            return None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2066

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2067

><td class="source">        # if it doesn&#39;t start with a prefix, it was meant to be positional<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2068

><td class="source">        if not arg_string[0] in self.prefix_chars:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2069

><td class="source">            return None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2070

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2071

><td class="source">        # if the option string is present in the parser, return the action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2072

><td class="source">        if arg_string in self._option_string_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2073

><td class="source">            action = self._option_string_actions[arg_string]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2074

><td class="source">            return action, arg_string, None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2075

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2076

><td class="source">        # if it&#39;s just a single character, it was meant to be positional<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2077

><td class="source">        if len(arg_string) == 1:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2078

><td class="source">            return None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2079

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2080

><td class="source">        # if the option string before the &quot;=&quot; is present, return the action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2081

><td class="source">        if &#39;=&#39; in arg_string:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2082

><td class="source">            option_string, explicit_arg = arg_string.split(&#39;=&#39;, 1)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2083

><td class="source">            if option_string in self._option_string_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2084

><td class="source">                action = self._option_string_actions[option_string]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2085

><td class="source">                return action, option_string, explicit_arg<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2086

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2087

><td class="source">        # search through all possible prefixes of the option string<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2088

><td class="source">        # and all actions in the parser for possible interpretations<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2089

><td class="source">        option_tuples = self._get_option_tuples(arg_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2090

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2091

><td class="source">        # if multiple actions match, the option string was ambiguous<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2092

><td class="source">        if len(option_tuples) &gt; 1:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2093

><td class="source">            options = &#39;, &#39;.join([option_string<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2094

><td class="source">                for action, option_string, explicit_arg in option_tuples])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2095

><td class="source">            tup = arg_string, options<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2096

><td class="source">            self.error(_(&#39;ambiguous option: %s could match %s&#39;) % tup)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2097

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2098

><td class="source">        # if exactly one action matched, this segmentation is good,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2099

><td class="source">        # so return the parsed action<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2100

><td class="source">        elif len(option_tuples) == 1:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2101

><td class="source">            option_tuple, = option_tuples<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2102

><td class="source">            return option_tuple<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2103

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2104

><td class="source">        # if it was not found as an option, but it looks like a negative<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2105

><td class="source">        # number, it was meant to be positional<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2106

><td class="source">        # unless there are negative-number-like options<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2107

><td class="source">        if self._negative_number_matcher.match(arg_string):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2108

><td class="source">            if not self._has_negative_number_optionals:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2109

><td class="source">                return None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2110

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2111

><td class="source">        # if it contains a space, it was meant to be a positional<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2112

><td class="source">        if &#39; &#39; in arg_string:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2113

><td class="source">            return None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2114

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2115

><td class="source">        # it was meant to be an optional but there is no such option<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2116

><td class="source">        # in this parser (though it might be a valid option in a subparser)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2117

><td class="source">        return None, arg_string, None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2118

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2119

><td class="source">    def _get_option_tuples(self, option_string):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2120

><td class="source">        result = []<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2121

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2122

><td class="source">        # option strings starting with two prefix characters are only<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2123

><td class="source">        # split at the &#39;=&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2124

><td class="source">        chars = self.prefix_chars<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2125

><td class="source">        if option_string[0] in chars and option_string[1] in chars:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2126

><td class="source">            if &#39;=&#39; in option_string:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2127

><td class="source">                option_prefix, explicit_arg = option_string.split(&#39;=&#39;, 1)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2128

><td class="source">            else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2129

><td class="source">                option_prefix = option_string<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2130

><td class="source">                explicit_arg = None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2131

><td class="source">            for option_string in self._option_string_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2132

><td class="source">                if option_string.startswith(option_prefix):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2133

><td class="source">                    action = self._option_string_actions[option_string]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2134

><td class="source">                    tup = action, option_string, explicit_arg<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2135

><td class="source">                    result.append(tup)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2136

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2137

><td class="source">        # single character options can be concatenated with their arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2138

><td class="source">        # but multiple character options always have to have their argument<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2139

><td class="source">        # separate<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2140

><td class="source">        elif option_string[0] in chars and option_string[1] not in chars:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2141

><td class="source">            option_prefix = option_string<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2142

><td class="source">            explicit_arg = None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2143

><td class="source">            short_option_prefix = option_string[:2]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2144

><td class="source">            short_explicit_arg = option_string[2:]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2145

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2146

><td class="source">            for option_string in self._option_string_actions:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2147

><td class="source">                if option_string == short_option_prefix:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2148

><td class="source">                    action = self._option_string_actions[option_string]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2149

><td class="source">                    tup = action, option_string, short_explicit_arg<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2150

><td class="source">                    result.append(tup)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2151

><td class="source">                elif option_string.startswith(option_prefix):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2152

><td class="source">                    action = self._option_string_actions[option_string]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2153

><td class="source">                    tup = action, option_string, explicit_arg<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2154

><td class="source">                    result.append(tup)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2155

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2156

><td class="source">        # shouldn&#39;t ever get here<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2157

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2158

><td class="source">            self.error(_(&#39;unexpected option string: %s&#39;) % option_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2159

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2160

><td class="source">        # return the collected option tuples<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2161

><td class="source">        return result<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2162

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2163

><td class="source">    def _get_nargs_pattern(self, action):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2164

><td class="source">        # in all examples below, we have to allow for &#39;--&#39; args<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2165

><td class="source">        # which are represented as &#39;-&#39; in the pattern<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2166

><td class="source">        nargs = action.nargs<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2167

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2168

><td class="source">        # the default (None) is assumed to be a single argument<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2169

><td class="source">        if nargs is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2170

><td class="source">            nargs_pattern = &#39;(-*A-*)&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2171

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2172

><td class="source">        # allow zero or one arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2173

><td class="source">        elif nargs == OPTIONAL:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2174

><td class="source">            nargs_pattern = &#39;(-*A?-*)&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2175

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2176

><td class="source">        # allow zero or more arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2177

><td class="source">        elif nargs == ZERO_OR_MORE:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2178

><td class="source">            nargs_pattern = &#39;(-*[A-]*)&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2179

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2180

><td class="source">        # allow one or more arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2181

><td class="source">        elif nargs == ONE_OR_MORE:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2182

><td class="source">            nargs_pattern = &#39;(-*A[A-]*)&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2183

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2184

><td class="source">        # allow any number of options or arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2185

><td class="source">        elif nargs == REMAINDER:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2186

><td class="source">            nargs_pattern = &#39;([-AO]*)&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2187

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2188

><td class="source">        # allow one argument followed by any number of options or arguments<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2189

><td class="source">        elif nargs == PARSER:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2190

><td class="source">            nargs_pattern = &#39;(-*A[-AO]*)&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2191

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2192

><td class="source">        # all others should be integers<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2193

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2194

><td class="source">            nargs_pattern = &#39;(-*%s-*)&#39; % &#39;-*&#39;.join(&#39;A&#39; * nargs)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2195

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2196

><td class="source">        # if this is an optional action, -- is not allowed<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2197

><td class="source">        if action.option_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2198

><td class="source">            nargs_pattern = nargs_pattern.replace(&#39;-*&#39;, &#39;&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2199

><td class="source">            nargs_pattern = nargs_pattern.replace(&#39;-&#39;, &#39;&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2200

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2201

><td class="source">        # return the pattern<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2202

><td class="source">        return nargs_pattern<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2203

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2204

><td class="source">    # ========================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2205

><td class="source">    # Value conversion methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2206

><td class="source">    # ========================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2207

><td class="source">    def _get_values(self, action, arg_strings):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2208

><td class="source">        # for everything but PARSER args, strip out &#39;--&#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2209

><td class="source">        if action.nargs not in [PARSER, REMAINDER]:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2210

><td class="source">            arg_strings = [s for s in arg_strings if s != &#39;--&#39;]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2211

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2212

><td class="source">        # optional argument produces a default when not present<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2213

><td class="source">        if not arg_strings and action.nargs == OPTIONAL:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2214

><td class="source">            if action.option_strings:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2215

><td class="source">                value = action.const<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2216

><td class="source">            else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2217

><td class="source">                value = action.default<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2218

><td class="source">            if isinstance(value, basestring):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2219

><td class="source">                value = self._get_value(action, value)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2220

><td class="source">                self._check_value(action, value)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2221

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2222

><td class="source">        # when nargs=&#39;*&#39; on a positional, if there were no command-line<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2223

><td class="source">        # args, use the default if it is anything other than None<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2224

><td class="source">        elif (not arg_strings and action.nargs == ZERO_OR_MORE and<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2225

><td class="source">              not action.option_strings):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2226

><td class="source">            if action.default is not None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2227

><td class="source">                value = action.default<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2228

><td class="source">            else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2229

><td class="source">                value = arg_strings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2230

><td class="source">            self._check_value(action, value)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2231

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2232

><td class="source">        # single argument or optional argument produces a single value<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2233

><td class="source">        elif len(arg_strings) == 1 and action.nargs in [None, OPTIONAL]:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2234

><td class="source">            arg_string, = arg_strings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2235

><td class="source">            value = self._get_value(action, arg_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2236

><td class="source">            self._check_value(action, value)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2237

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2238

><td class="source">        # REMAINDER arguments convert all values, checking none<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2239

><td class="source">        elif action.nargs == REMAINDER:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2240

><td class="source">            value = [self._get_value(action, v) for v in arg_strings]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2241

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2242

><td class="source">        # PARSER arguments convert all values, but check only the first<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2243

><td class="source">        elif action.nargs == PARSER:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2244

><td class="source">            value = [self._get_value(action, v) for v in arg_strings]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2245

><td class="source">            self._check_value(action, value[0])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2246

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2247

><td class="source">        # all other types of nargs produce a list<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2248

><td class="source">        else:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2249

><td class="source">            value = [self._get_value(action, v) for v in arg_strings]<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2250

><td class="source">            for v in value:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2251

><td class="source">                self._check_value(action, v)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2252

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2253

><td class="source">        # return the converted value<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2254

><td class="source">        return value<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2255

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2256

><td class="source">    def _get_value(self, action, arg_string):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2257

><td class="source">        type_func = self._registry_get(&#39;type&#39;, action.type, action.type)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2258

><td class="source">        if not _callable(type_func):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2259

><td class="source">            msg = _(&#39;%r is not callable&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2260

><td class="source">            raise ArgumentError(action, msg % type_func)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2261

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2262

><td class="source">        # convert the value to the appropriate type<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2263

><td class="source">        try:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2264

><td class="source">            result = type_func(arg_string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2265

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2266

><td class="source">        # ArgumentTypeErrors indicate errors<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2267

><td class="source">        except ArgumentTypeError:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2268

><td class="source">            name = getattr(action.type, &#39;__name__&#39;, repr(action.type))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2269

><td class="source">            msg = str(_sys.exc_info()[1])<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2270

><td class="source">            raise ArgumentError(action, msg)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2271

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2272

><td class="source">        # TypeErrors or ValueErrors also indicate errors<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2273

><td class="source">        except (TypeError, ValueError):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2274

><td class="source">            name = getattr(action.type, &#39;__name__&#39;, repr(action.type))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2275

><td class="source">            msg = _(&#39;invalid %s value: %r&#39;)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2276

><td class="source">            raise ArgumentError(action, msg % (name, arg_string))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2277

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2278

><td class="source">        # return the converted value<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2279

><td class="source">        return result<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2280

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2281

><td class="source">    def _check_value(self, action, value):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2282

><td class="source">        # converted value must be one of the choices (if specified)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2283

><td class="source">        if action.choices is not None and value not in action.choices:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2284

><td class="source">            tup = value, &#39;, &#39;.join(map(repr, action.choices))<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2285

><td class="source">            msg = _(&#39;invalid choice: %r (choose from %s)&#39;) % tup<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2286

><td class="source">            raise ArgumentError(action, msg)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2287

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2288

><td class="source">    # =======================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2289

><td class="source">    # Help-formatting methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2290

><td class="source">    # =======================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2291

><td class="source">    def format_usage(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2292

><td class="source">        formatter = self._get_formatter()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2293

><td class="source">        formatter.add_usage(self.usage, self._actions,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2294

><td class="source">                            self._mutually_exclusive_groups)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2295

><td class="source">        return formatter.format_help()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2296

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2297

><td class="source">    def format_help(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2298

><td class="source">        formatter = self._get_formatter()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2299

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2300

><td class="source">        # usage<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2301

><td class="source">        formatter.add_usage(self.usage, self._actions,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2302

><td class="source">                            self._mutually_exclusive_groups)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2303

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2304

><td class="source">        # description<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2305

><td class="source">        formatter.add_text(self.description)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2306

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2307

><td class="source">        # positionals, optionals and user-defined groups<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2308

><td class="source">        for action_group in self._action_groups:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2309

><td class="source">            formatter.start_section(action_group.title)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2310

><td class="source">            formatter.add_text(action_group.description)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2311

><td class="source">            formatter.add_arguments(action_group._group_actions)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2312

><td class="source">            formatter.end_section()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2313

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2314

><td class="source">        # epilog<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2315

><td class="source">        formatter.add_text(self.epilog)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2316

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2317

><td class="source">        # determine help from format above<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2318

><td class="source">        return formatter.format_help()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2319

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2320

><td class="source">    def format_version(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2321

><td class="source">        import warnings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2322

><td class="source">        warnings.warn(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2323

><td class="source">            &#39;The format_version method is deprecated -- the &quot;version&quot; &#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2324

><td class="source">            &#39;argument to ArgumentParser is no longer supported.&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2325

><td class="source">            DeprecationWarning)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2326

><td class="source">        formatter = self._get_formatter()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2327

><td class="source">        formatter.add_text(self.version)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2328

><td class="source">        return formatter.format_help()<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2329

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2330

><td class="source">    def _get_formatter(self):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2331

><td class="source">        return self.formatter_class(prog=self.prog)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2332

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2333

><td class="source">    # =====================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2334

><td class="source">    # Help-printing methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2335

><td class="source">    # =====================<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2336

><td class="source">    def print_usage(self, file=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2337

><td class="source">        if file is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2338

><td class="source">            file = _sys.stdout<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2339

><td class="source">        self._print_message(self.format_usage(), file)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2340

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2341

><td class="source">    def print_help(self, file=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2342

><td class="source">        if file is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2343

><td class="source">            file = _sys.stdout<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2344

><td class="source">        self._print_message(self.format_help(), file)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2345

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2346

><td class="source">    def print_version(self, file=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2347

><td class="source">        import warnings<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2348

><td class="source">        warnings.warn(<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2349

><td class="source">            &#39;The print_version method is deprecated -- the &quot;version&quot; &#39;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2350

><td class="source">            &#39;argument to ArgumentParser is no longer supported.&#39;,<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2351

><td class="source">            DeprecationWarning)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2352

><td class="source">        self._print_message(self.format_version(), file)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2353

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2354

><td class="source">    def _print_message(self, message, file=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2355

><td class="source">        if message:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2356

><td class="source">            if file is None:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2357

><td class="source">                file = _sys.stderr<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2358

><td class="source">            file.write(message)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2359

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2360

><td class="source">    # ===============<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2361

><td class="source">    # Exiting methods<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2362

><td class="source">    # ===============<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2363

><td class="source">    def exit(self, status=0, message=None):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2364

><td class="source">        if message:<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2365

><td class="source">            self._print_message(message, _sys.stderr)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2366

><td class="source">        _sys.exit(status)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2367

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2368

><td class="source">    def error(self, message):<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2369

><td class="source">        &quot;&quot;&quot;error(message: string)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2370

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2371

><td class="source">        Prints a usage message incorporating the message to stderr and<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2372

><td class="source">        exits.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2373

><td class="source"><br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2374

><td class="source">        If you override this in a subclass, it should not return -- it<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2375

><td class="source">        should either exit or raise an exception.<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2376

><td class="source">        &quot;&quot;&quot;<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2377

><td class="source">        self.print_usage(_sys.stderr)<br></td></tr
><tr
id=sl_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_2378

><td class="source">        self.exit(2, _(&#39;%s: error: %s\n&#39;) % (self.prog, message))<br></td></tr
></table></pre>
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
</td>
</tr></table>

 
<script type="text/javascript">
 var lineNumUnderMouse = -1;
 
 function gutterOver(num) {
 gutterOut();
 var newTR = document.getElementById('gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_' + num);
 if (newTR) {
 newTR.className = 'undermouse';
 }
 lineNumUnderMouse = num;
 }
 function gutterOut() {
 if (lineNumUnderMouse != -1) {
 var oldTR = document.getElementById(
 'gr_svne26233c6cc8f631e27c9ed7fb2bd47b58746c895_' + lineNumUnderMouse);
 if (oldTR) {
 oldTR.className = '';
 }
 lineNumUnderMouse = -1;
 }
 }
 var numsGenState = {table_base_id: 'nums_table_'};
 var srcGenState = {table_base_id: 'src_table_'};
 var alignerRunning = false;
 var startOver = false;
 function setLineNumberHeights() {
 if (alignerRunning) {
 startOver = true;
 return;
 }
 numsGenState.chunk_id = 0;
 numsGenState.table = document.getElementById('nums_table_0');
 numsGenState.row_num = 0;
 if (!numsGenState.table) {
 return; // Silently exit if no file is present.
 }
 srcGenState.chunk_id = 0;
 srcGenState.table = document.getElementById('src_table_0');
 srcGenState.row_num = 0;
 alignerRunning = true;
 continueToSetLineNumberHeights();
 }
 function rowGenerator(genState) {
 if (genState.row_num < genState.table.rows.length) {
 var currentRow = genState.table.rows[genState.row_num];
 genState.row_num++;
 return currentRow;
 }
 var newTable = document.getElementById(
 genState.table_base_id + (genState.chunk_id + 1));
 if (newTable) {
 genState.chunk_id++;
 genState.row_num = 0;
 genState.table = newTable;
 return genState.table.rows[0];
 }
 return null;
 }
 var MAX_ROWS_PER_PASS = 1000;
 function continueToSetLineNumberHeights() {
 var rowsInThisPass = 0;
 var numRow = 1;
 var srcRow = 1;
 while (numRow && srcRow && rowsInThisPass < MAX_ROWS_PER_PASS) {
 numRow = rowGenerator(numsGenState);
 srcRow = rowGenerator(srcGenState);
 rowsInThisPass++;
 if (numRow && srcRow) {
 if (numRow.offsetHeight != srcRow.offsetHeight) {
 numRow.firstChild.style.height = srcRow.offsetHeight + 'px';
 }
 }
 }
 if (rowsInThisPass >= MAX_ROWS_PER_PASS) {
 setTimeout(continueToSetLineNumberHeights, 10);
 } else {
 alignerRunning = false;
 if (startOver) {
 startOver = false;
 setTimeout(setLineNumberHeights, 500);
 }
 }
 }
 function initLineNumberHeights() {
 // Do 2 complete passes, because there can be races
 // between this code and prettify.
 startOver = true;
 setTimeout(setLineNumberHeights, 250);
 window.onresize = setLineNumberHeights;
 }
 initLineNumberHeights();
</script>

 
 
 <div id="log">
 <div style="text-align:right">
 <a class="ifCollapse" href="#" onclick="_toggleMeta(this); return false">Show details</a>
 <a class="ifExpand" href="#" onclick="_toggleMeta(this); return false">Hide details</a>
 </div>
 <div class="ifExpand">
 
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="changelog">
 <p>Change log</p>
 <div>
 <a href="/p/argparse/source/detail?spec=svne26233c6cc8f631e27c9ed7fb2bd47b58746c895&amp;r=2287d776cf60c4b17e6ffcae412c10348fd75bf7">2287d776cf60</a>
 by Thomas Waldmann &lt;tw AT waldmann-edv DOT de&gt;
 on Dec 15, 2014
 &nbsp; <a href="/p/argparse/source/diff?spec=svne26233c6cc8f631e27c9ed7fb2bd47b58746c895&r=2287d776cf60c4b17e6ffcae412c10348fd75bf7&amp;format=side&amp;path=/argparse.py&amp;old_path=/argparse.py&amp;old=8bcccc85a584f5c3790c6cb8f80c7cadc7864049">Diff</a>
 </div>
 <pre>added aliases support, thanks to Roland
Kammerer</pre>
 </div>
 
 
 
 
 
 
 <script type="text/javascript">
 var detail_url = '/p/argparse/source/detail?r=2287d776cf60c4b17e6ffcae412c10348fd75bf7&spec=svne26233c6cc8f631e27c9ed7fb2bd47b58746c895';
 var publish_url = '/p/argparse/source/detail?r=2287d776cf60c4b17e6ffcae412c10348fd75bf7&spec=svne26233c6cc8f631e27c9ed7fb2bd47b58746c895#publish';
 // describe the paths of this revision in javascript.
 var changed_paths = [];
 var changed_urls = [];
 
 changed_paths.push('/argparse.py');
 changed_urls.push('/p/argparse/source/browse/argparse.py?r\x3d2287d776cf60c4b17e6ffcae412c10348fd75bf7\x26spec\x3dsvne26233c6cc8f631e27c9ed7fb2bd47b58746c895');
 
 var selected_path = '/argparse.py';
 
 
 changed_paths.push('/test/test_argparse.py');
 changed_urls.push('/p/argparse/source/browse/test/test_argparse.py?r\x3d2287d776cf60c4b17e6ffcae412c10348fd75bf7\x26spec\x3dsvne26233c6cc8f631e27c9ed7fb2bd47b58746c895');
 
 
 function getCurrentPageIndex() {
 for (var i = 0; i < changed_paths.length; i++) {
 if (selected_path == changed_paths[i]) {
 return i;
 }
 }
 }
 function getNextPage() {
 var i = getCurrentPageIndex();
 if (i < changed_paths.length - 1) {
 return changed_urls[i + 1];
 }
 return null;
 }
 function getPreviousPage() {
 var i = getCurrentPageIndex();
 if (i > 0) {
 return changed_urls[i - 1];
 }
 return null;
 }
 function gotoNextPage() {
 var page = getNextPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoPreviousPage() {
 var page = getPreviousPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoDetailPage() {
 window.location = detail_url;
 }
 function gotoPublishPage() {
 window.location = publish_url;
 }
</script>

 
 <style type="text/css">
 #review_nav {
 border-top: 3px solid white;
 padding-top: 6px;
 margin-top: 1em;
 }
 #review_nav td {
 vertical-align: middle;
 }
 #review_nav select {
 margin: .5em 0;
 }
 </style>
 <div id="review_nav">
 <table><tr><td>Go to:&nbsp;</td><td>
 <select name="files_in_rev" onchange="window.location=this.value">
 
 <option value="/p/argparse/source/browse/argparse.py?r=2287d776cf60c4b17e6ffcae412c10348fd75bf7&amp;spec=svne26233c6cc8f631e27c9ed7fb2bd47b58746c895"
 selected="selected"
 >/argparse.py</option>
 
 <option value="/p/argparse/source/browse/test/test_argparse.py?r=2287d776cf60c4b17e6ffcae412c10348fd75bf7&amp;spec=svne26233c6cc8f631e27c9ed7fb2bd47b58746c895"
 
 >/test/test_argparse.py</option>
 
 </select>
 </td></tr></table>
 
 
 



 <div style="white-space:nowrap">
 Project members,
 <a href="https://www.google.com/accounts/ServiceLogin?service=code&amp;ltmpl=phosting&amp;continue=https%3A%2F%2Fcode.google.com%2Fp%2Fargparse%2Fsource%2Fbrowse%2Fargparse.py&amp;followup=https%3A%2F%2Fcode.google.com%2Fp%2Fargparse%2Fsource%2Fbrowse%2Fargparse.py"
 >sign in</a> to write a code review</div>


 
 </div>
 
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="older_bubble">
 <p>Older revisions</p>
 
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/argparse/source/detail?spec=svne26233c6cc8f631e27c9ed7fb2bd47b58746c895&r=8bcccc85a584f5c3790c6cb8f80c7cadc7864049">8bcccc85a584</a>
 by Thomas Waldmann &lt;tw AT waldmann-edv DOT de&gt;
 on Dec 15, 2014
 &nbsp; <a href="/p/argparse/source/diff?spec=svne26233c6cc8f631e27c9ed7fb2bd47b58746c895&r=8bcccc85a584f5c3790c6cb8f80c7cadc7864049&amp;format=side&amp;path=/argparse.py&amp;old_path=/argparse.py&amp;old=85db5d604421367290e5733f34e6e704b72e68bf">Diff</a>
 <br>
 <pre class="ifOpened">use tox for testing, bump version to
1.3.0, declare support for py 3.3+3.4

also make sure we really test THIS
lib, not the builtin one in stdlib.</pre>
 </div>
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/argparse/source/detail?spec=svne26233c6cc8f631e27c9ed7fb2bd47b58746c895&r=85db5d604421367290e5733f34e6e704b72e68bf">85db5d604421</a>
 by Thomas Waldmann &lt;tw AT waldmann-edv DOT de&gt;
 on Nov 15, 2014
 &nbsp; <a href="/p/argparse/source/diff?spec=svne26233c6cc8f631e27c9ed7fb2bd47b58746c895&r=85db5d604421367290e5733f34e6e704b72e68bf&amp;format=side&amp;path=/argparse.py&amp;old_path=/argparse.py&amp;old=eccaefac6147345ca812f653341b1942a11d9588">Diff</a>
 <br>
 <pre class="ifOpened">add universal wheel support, host
files on pypi</pre>
 </div>
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/argparse/source/detail?spec=svne26233c6cc8f631e27c9ed7fb2bd47b58746c895&r=eccaefac6147345ca812f653341b1942a11d9588">eccaefac6147</a>
 by Thomas Waldmann &lt;tw AT waldmann-edv DOT de&gt;
 on Mar 31, 2011
 &nbsp; <a href="/p/argparse/source/diff?spec=svne26233c6cc8f631e27c9ed7fb2bd47b58746c895&r=eccaefac6147345ca812f653341b1942a11d9588&amp;format=side&amp;path=/argparse.py&amp;old_path=/argparse.py&amp;old=c1c83cae40ebebe8aeb89f212484a33296bc83be">Diff</a>
 <br>
 <pre class="ifOpened">bump version to 1.2.1, add py 3.2 to
the tested list</pre>
 </div>
 
 
 <a href="/p/argparse/source/list?path=/argparse.py&r=2287d776cf60c4b17e6ffcae412c10348fd75bf7">All revisions of this file</a>
 </div>
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="fileinfo_bubble">
 <p>File info</p>
 
 <div>Size: 88400 bytes,
 2378 lines</div>
 
 <div><a href="//argparse.googlecode.com/hg/argparse.py">View raw file</a></div>
 </div>
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 </div>
 </div>


</div>

</div>
</div>

<script src="https://ssl.gstatic.com/codesite/ph/10671232128890609530/js/prettify/prettify.js"></script>
<script type="text/javascript">prettyPrint();</script>


<script src="https://ssl.gstatic.com/codesite/ph/10671232128890609530/js/source_file_scripts.js"></script>

 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/10671232128890609530/js/kibbles.js"></script>
 <script type="text/javascript">
 var lastStop = null;
 var initialized = false;
 
 function updateCursor(next, prev) {
 if (prev && prev.element) {
 prev.element.className = 'cursor_stop cursor_hidden';
 }
 if (next && next.element) {
 next.element.className = 'cursor_stop cursor';
 lastStop = next.index;
 }
 }
 
 function pubRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftDestroyed(data) {
 updateCursorForCell(data.cellId, 'nocursor');
 if (initialized) {
 reloadCursors();
 }
 }
 function reloadCursors() {
 kibbles.skipper.reset();
 loadCursors();
 if (lastStop != null) {
 kibbles.skipper.setCurrentStop(lastStop);
 }
 }
 // possibly the simplest way to insert any newly added comments
 // is to update the class of the corresponding cursor row,
 // then refresh the entire list of rows.
 function updateCursorForCell(cellId, className) {
 var cell = document.getElementById(cellId);
 // we have to go two rows back to find the cursor location
 var row = getPreviousElement(cell.parentNode);
 row.className = className;
 }
 // returns the previous element, ignores text nodes.
 function getPreviousElement(e) {
 var element = e.previousSibling;
 if (element.nodeType == 3) {
 element = element.previousSibling;
 }
 if (element && element.tagName) {
 return element;
 }
 }
 function loadCursors() {
 // register our elements with skipper
 var elements = CR_getElements('*', 'cursor_stop');
 var len = elements.length;
 for (var i = 0; i < len; i++) {
 var element = elements[i]; 
 element.className = 'cursor_stop cursor_hidden';
 kibbles.skipper.append(element);
 }
 }
 function toggleComments() {
 CR_toggleCommentDisplay();
 reloadCursors();
 }
 function keysOnLoadHandler() {
 // setup skipper
 kibbles.skipper.addStopListener(
 kibbles.skipper.LISTENER_TYPE.PRE, updateCursor);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_top', 50);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_bottom', 100);
 // Register our keys
 kibbles.skipper.addFwdKey("n");
 kibbles.skipper.addRevKey("p");
 kibbles.keys.addKeyPressListener(
 'u', function() { window.location = detail_url; });
 kibbles.keys.addKeyPressListener(
 'r', function() { window.location = detail_url + '#publish'; });
 
 kibbles.keys.addKeyPressListener('j', gotoNextPage);
 kibbles.keys.addKeyPressListener('k', gotoPreviousPage);
 
 
 }
 </script>
<script src="https://ssl.gstatic.com/codesite/ph/10671232128890609530/js/code_review_scripts.js"></script>
<script type="text/javascript">
 function showPublishInstructions() {
 var element = document.getElementById('review_instr');
 if (element) {
 element.className = 'opened';
 }
 }
 var codereviews;
 function revsOnLoadHandler() {
 // register our source container with the commenting code
 var paths = {'svne26233c6cc8f631e27c9ed7fb2bd47b58746c895': '/argparse.py'}
 codereviews = CR_controller.setup(
 {"assetVersionPath": "https://ssl.gstatic.com/codesite/ph/10671232128890609530", "projectName": "argparse", "projectHomeUrl": "/p/argparse", "relativeBaseUrl": "", "loggedInUserEmail": null, "profileUrl": null, "token": null, "domainName": null, "assetHostPath": "https://ssl.gstatic.com/codesite/ph"}, '', 'svne26233c6cc8f631e27c9ed7fb2bd47b58746c895', paths,
 CR_BrowseIntegrationFactory);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, showPublishInstructions);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_PUB_PLATE, pubRevealed);
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, draftRevealed);
 codereviews.registerActivityListener(CR_ActivityType.DISCARD_DRAFT_COMMENT, draftDestroyed);
 
 
 
 
 
 
 
 var initialized = true;
 reloadCursors();
 }
 window.onload = function() {keysOnLoadHandler(); revsOnLoadHandler();};

</script>
<script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/10671232128890609530/js/dit_scripts.js"></script>

 
 
 
 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/10671232128890609530/js/ph_core.js"></script>
 
 
 
 
</div> 

<div id="footer" dir="ltr">
 <div class="text">
 <a href="/projecthosting/terms.html">Terms</a> -
 <a href="http://www.google.com/privacy.html">Privacy</a> -
 <a href="/p/support/">Project Hosting Help</a>
 </div>
</div>
 <div class="hostedBy" style="margin-top: -20px;">
 <span style="vertical-align: top;">Powered by <a href="http://code.google.com/projecthosting/">Google Project Hosting</a></span>
 </div>

 
 


 
 </body>
</html>

