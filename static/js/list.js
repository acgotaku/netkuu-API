$(function(){
	var list={
		url:"http://movie.zzti.edu.cn/",
		init:function(){
			var str=window.location.search;
			var code=str.match(/code=([a-zA-Z0-9].*[a-zA-Z0-9])/i);
			code=code[1]
			$(".cover").attr("src",this.url+"mov/"+code+"/1.jpg");
			$.ajax({
					type:'POST',
					url:"/list",
					dataType:'json',
					data:{code:code},
					success:(function(data){
						console.log(data);
						$(".item-name").append($("<h2>").text(data.name));
						$(".item-director").append($("<span>").text(data.director));
						$(".item-actor").append($("<span>").text(data.actor));
						$(".item-type").append($("<span>").text(data.type));
						$(".item-region").append($("<span>").text(data.region));
						$(".item-publishTime").append($("<span>").text(data.publishTime));
						$(".item-adddate").append($("<span>").text(data.adddate));
						$(".item-brief").append($("<span>").text(data.brief));
						})
					
				});
		}
	};
list.init();
});

