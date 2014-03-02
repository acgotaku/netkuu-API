	var header={
		init:function(){
			var schoolName=header.getCookie("name");
			if (schoolName!=""){
				$("#schoolName").text(schoolName);
			}
			$.ajax({
					type:'POST',
					url:"/server",
					dataType:'json',
					success:(function(data){
						$.each(data,function(n,e){
							$(".modal-body .list-group").append($("<a>").addClass("list-group-item a-fadein").text(e.name).attr("url",e.url).attr("href","javascript:void(0);").click(function(){
								header.setCookie("server",$(this).attr("url"));
								$("#schoolName").text($(this).text());
								header.setCookie("name",$(this).text());
								$('#myModal').modal('hide');
							}));
						});
						})
					
				});


		},
		setCookie:function(name,value){
			var d=new Date();
			d.setTime(d.getTime()+(360*24*60*60*1000));
			var expires = "expires="+d.toGMTString();
			value=encodeURIComponent(value)
			document.cookie=name+"="+value+";"+expires;
		},
		getCookie:function(cname){
			var name = cname + "=";
			var ca = document.cookie.split(';');
			for(var i=0; i<ca.length; i++) {

  				var c = ca[i].trim();
  				if (c.indexOf(name)==0) return decodeURIComponent(c.substring(name.length,c.length));
  			}
			return "";
		}
	};
header.init();

