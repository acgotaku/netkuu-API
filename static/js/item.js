$(function(){
	var list={
		url:"http://movie.zzti.edu.cn/",
		init:function(){
			$.ajax({
					type:'POST',
					url:"/item"+window.location.search,
					dataType:'text',
					success:(function(data){
						var server=header.getCookie("server")
						var down_url=data;
						if(server!=""){
							down_url=data.replace(/^http:\/\/.+?\//gi,server);
						}
						var array=data.split(".");
						var file_type=array[array.length-1];
						var num=header.getCookie("num");
						var file_name="视频."+file_type;
						if(num!=""){
							file_name=header.getCookie("fname")+"第"+header.getCookie("num")+"集"+"."+file_type;
						}
						$(".middle a").text(file_name).attr("href",down_url).attr("download",file_name);
						})
					
				});
			setTimeout(function(){
				$(".middle a").trigger("click");
			},3000);
		}
	
	};
list.init();
});

