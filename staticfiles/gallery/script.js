var req = new XMLHttpRequest();
req.open("GET", "/static/gallery/json/image_list.json");
req.onreadystatechange =function(){
	if( this.readyState ==4){
		//console.log(this.response);
		var data = JSON.parse(this.response);
		for (var i = 0 ; i< data.length;i++){
			var div = document.createElement("div");
			div.setAttribute("class","image");
			div.onclick= function(){
				// if (this.getAttribute("class").indexOf("image-selected")== -1){
				// 	this.setAttribute("class","image image-selected");
				// }
				// else{
				// 	this .setAttribute("class","image")
				// 아래로 바꿀수 있음.
				this.classList.toggle("image-selected")
			}
			div.onmouseover = function(){
				//여기서 this 는 div 그래서 element 를 this 로 저장
				var element = this;
				this.timeId = setTimeout( function(){
					element.classList.add("image-magnified");},1000);
					//여기서 this  div가아님 그래서 this 대신 element씀.
			}
			div.onmouseout = function(){
				clearTimeout(this.timeId);
				this.classList.remove("image-magnified");
			}
			var img = document.createElement("img");
			img.src = data[i];
			div.appendChild(img);
			document.body.appendChild(div);
		}
	}
}
req.send()

function selectAll(btn){
	var images = document.getElementsByClassName("image");
	for (var i =0 ; i< images.length; i++){
		if (btn.value == "Unselect All"){
			images[i].classList.remove("image-selected");}
		else{
			images[i].classList.add("image-selected");
		}
		}
	if (btn.value == "Unselect All"){
		btn.value = "selected All";}
	else{
		btn.value = "Unselect All";
	}

}

function slideshow(btn){
	var images = document.getElementsByClassName("image");
	var index = 0;
	images[index].classList.add("image-magnified");

	var intervalId = setInterval(function(){
		images[index].classList.remove("image-magnified");
		index++
		if(index < images.length){
			images[index].classList.add("image-magnified");}
		else{
			clearInterval(intervalId)}

		},1000);
	}