
function showDiv(idInfo) {
    alert(idInfo);
    var sel = document.getElementById('large_wrapper').getElementsByTagName('div');
    for (var i=0; i<sel.length; i++) {sel[i].style.display = 'none'; }
    document.getElementById('large_image_'+idInfo).style.display = 'block';
}

var wrapNode = document.getElementById('thumb_wrapper');


img_json_data.forEach(function(d) {
    var anchorNode = document.createElement('a');
    anchorNode.onclick = function(){showDiv("FAKE")};
    
    var imgNode = document.createElement("img");
    imgNode.src = "../img_1024/"+d['filename_th'];
    imgNode.className = "thumb";
    anchorNode.appendChild(imgNode);
    
    anchorNode.title = "title";
    anchorNode.href = "#";
    wrapNode.appendChild(anchorNode);
});

/*
<a href="#" onclick="showDiv('00000');return false">
<img class="thumb" src="img_1024/00000_th.jpg">
</a>
    
<div id="large_image_00000" style="display:none;">
<img class="large_image" src="img_1024/00000.jpg">

<table>
<tr><td></td><td><a class="img_id_link" href="http://iconosquare.com/p/911769247024270180_236415113" target="_blank">00000</a></td></tr><tr><td>keyword</td><td>coffeecup</td></tr><tr><td>retrieved</td><td>Mon, 02 Feb 2015 21:23:04 +0000</td></tr><tr><td>tags</td><td>life, cupoftea, bigalowe, tea, kingandprince, coffeecup, goldenisles, shell, ssi, collection, home, teatime, island, destination, vacation, afternoon</td></tr><tr><td>post-date</td><td>1.09 pm 2/2/2015</td></tr><tr><td>type</td><td>Instagram</td></tr><tr><td>rgb-avg</td><td>[122, 108, 105]</td></tr>
</table>

</div>
    
    */
    
    