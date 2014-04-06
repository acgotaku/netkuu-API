$(function(){
	var list={
		url:"http://movie.zzti.edu.cn/",
		init:function(){
			var str=window.location.search;
			var code=str.match(/code=([a-zA-Z0-9].*[a-zA-Z0-9])/i);
			code=code[1]
			$(".cover").attr("src",this.url+"mov/"+code+"/1.jpg").attr("width","300px").attr("height","400px");
			$.ajax({
					type:'POST',
					url:"/list",
					dataType:'json',
					data:{code:code},
					success:(function(data){
						document.title=data.name;
						$(".item-name").append($("<h2>").text(data.name));
						$(".item-director").append($("<span>").text(data.director));
						$(".item-actor").append($("<span>").text(data.actor));
						$(".item-type").append($("<span>").text(data.type));
						$(".item-region").append($("<span>").text(data.region));
						$(".item-publishTime").append($("<span>").text(data.publishTime));
						$(".item-adddate").append($("<span>").text(data.adddate));
						$(".item-brief").append($("<span>").text(data.brief));
						list.get_item(code);
						})
					
				});
		},
		num:function(code){
			if(code.length>9){
				var tempstr="";
				for(i=0;i<code.length-1;i++){
					tempstr = tempstr+"%"+code.substr(i,2);
					i=i+1;
				}
				var url=decodeURIComponent(tempstr);
			}else{
				return 0;
			}
			num=url.match(/\#\#(\d+)/i);
			if (num){
				return num[1];
			}
			else
				return 0;
		},
		printf:function(num){
			if(num<10){
				return ("00"+num)
			}
			else if(num>=10&&num<100){
				return ("0"+num)
			}
			else if(num>=100){
				return (num)
			}
		},
		get_item:function(code){
			$.ajax({
					type:'POST',
					url:"/list",
					dataType:'json',
					data:{code:code,item:"True"},
					success:(function(data){
						if (data.length==0){
							$(".tiny").append($("<h2>").text("服务器没有资源"));
							return
						}
						var num=list.num(code);
						if (num==0){
							num=1;
						}
						$.each(data.code,function(n,e){
						 	var item=$("<a>").attr("href","item?code="+code+"&num="+n).attr("target","_blank").text(list.printf(parseInt(num)+n));
						 	if (e==""){
						 		item.attr("disabled","disabled");
						 	}
						 	item.click(function(){
						 		header.setCookie("num",$(this).text(),1);
						 		header.setCookie("fname",$(".item-name h2").text(),1);
						 	});
						 	$(".tiny").append(item.clone().addClass("btn btn-default"));
						 	$("<li>").addClass("list-group-item").append($("<i>").addClass("select-box")).append(item.clone().text($(".item-name").text()+"第"+item.clone().text()+"集")).appendTo($(".list .list-group"));
						 	
						 });
						list.select_click();
						})
					
				});
		},
		select_click:function(){
			$("i").click(function(){
				if($(this).attr("data-click")=="all"){
					if($(this).html()==""){
						$("i").append($("<span>").addClass("glyphicon glyphicon-ok"));
						return ;
					}else{
						$("i").empty();
						retuen ;
					}
					
				}
				if($(this).html()==""){
					$(this).append($("<span>").addClass("glyphicon glyphicon-ok"));
				}else{
					$(this).empty();
				}

				
			});
		}
	};
list.init();
});

