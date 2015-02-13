

function highlightDot(idInfo){
    index_viz_data.forEach(function(d) {
        if (true) {
            svg.select('#dot_'+d["guid"])
            .style("fill", function(d) { return d3.rgb(255, 0, 0); })
        } else {
        
        }
    });
}



function showDiv(idInfo) {
    alert(idInfo);
    var sel = document.getElementById('large_wrapper').getElementsByTagName('div');
    for (var i=0; i<sel.length; i++) {sel[i].style.display = 'none'; }
    document.getElementById('large_image_'+idInfo).style.display = 'block';
}


var selNodeY = document.createElement('select');
selNodeY.id = 'y_axis_select'; selNodeY.name = 'y_axis_select'; 
var selNodeX = document.createElement('select');
selNodeX.id = 'x_axis_select'; selNodeX.name = 'x_axis_select'; 

index_viz_meta['plot_keys'].forEach(function(d) {  
    var optionNode = document.createElement("option");
    optionNode.setAttribute("value", d);
    optionNode.innerHTML = d;
    selNodeX.appendChild(optionNode);
    
    var optionNode = document.createElement("option");
    optionNode.setAttribute("value", d);
    optionNode.innerHTML = d;
    selNodeY.appendChild(optionNode);
});

document.getElementById('y_axis_drop_wrapper').appendChild(selNodeY);
document.getElementById('x_axis_drop_wrapper').appendChild(selNodeX);




var wrapNode = document.getElementById('thumb_wrapper');
index_viz_data.forEach(function(d) {
    //Object.keys(index_viz['data']).forEach(function(imgkey, n) {
    //imgdict = index_viz['data'][imgkey];
    //alert(imgdict);
    var anchorNode = document.createElement('a');
    anchorNode.onclick = function(){showDiv(d["guid"])};
    anchorNode.onmouseover = function(){highlightDot(d["guid"])};
    
    var imgNode = document.createElement("img");
    imgNode.src = "../img_1024/"+d['filename_th'];
    imgNode.className = "thumb";
    anchorNode.appendChild(imgNode);
    
    anchorNode.title = "title";
    anchorNode.href = "#";
    wrapNode.appendChild(anchorNode);
});

/*

<select id="y_axis_select" name="y_axis_select">
    <option value ="sepalWidth" selected>s width</option>
    <option value ="sepalLength">s length</option>
    <option value ="petalLength">p length</option>
</select>​


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
    
    