$(function(){
	var index={
		init:function(){
			$("input[type=text]").focus();
			$("#click").click(function(){
				var key=$("input[type=text]").val();
				$.ajax({
					type:'POST',
					url:".",
					dataType:'json',
					data:{key:key},
					success:(function(data){
						$("#result .list-group li:not(:first)").remove();
						$.each(data,function(n,e){
							window.setTimeout(function(){
								$("#result .list-group").append($("<li>").addClass("list-group-item a-fadein").append($("<a>").addClass("item-name").attr("href","list?code="+e.code).attr("target","_blank").text(e.name)).append(
									$("<div>").addClass("item-desc").append($("<span>").text(e.desc[6]))
									).append(
									$("<div>").addClass("item-type").append($("<span>").text(e.desc[4]))
									).append(
									$("<div>").addClass("item-time").append($("<span>").text(e.desc[7]))
									));
							},Math.min(n*100,2000));
							
						});
					})
				});
			});
			$("input[type=text]").keydown(function(e){
				var curKey=e.which;
				if(curKey==13){
					$("#click").trigger("click");
				}
			});
		}
	};
index.init();
});

