$(function(){
	var ahnu={
		init:function(){
			$("#click").click(function(){
				var key=$("input[type=text]").val();
				$.ajax({
					type:'POST',
					url:"http://localhost:8888/",
					dataType:'json',
					data:{key:key},
					success:(function(data){
						$.each(data,function(n,e){
							$(".list-group").append($("<li>").addClass("list-group-item a-fadein").append($("<a>").attr("href","javascript:void(0);").text(e.name)));
						});
					})
				});
			});
		}
	};
ahnu.init();
});

