	var header={
		init:function(){
			var run=true;
			var schoolName=header.getCookie("name");
			if (schoolName!=""){
				$("#schoolName").text(schoolName);
			}else{
				if(run){
					header.getServerList();
					run=false;
				}
			}
			$(".glyphicon").click(function(){
				if(run){
					header.getServerList();
					run=false;
				}
			});
		},
		getServerList:function(){
			$.ajax({
					type:'POST',
					url:"/server",
					dataType:'json',
					success:(function(data){
						$.each(data,function(n,e){
							$(".modal-body .list-group").append($("<a>").addClass("list-group-item a-fadein").text(e.name).attr("url",e.url).attr("href","javascript:void(0);").click(function(){
								header.setCookie("server",$(this).attr("url"),360);
								$("#schoolName").text($(this).text());
								header.setCookie("name",$(this).text(),360);
								$('#ServerList').modal('hide');
							}));
						});
						})
					
				});
		},
		setCookie:function(name,value,days){
			var d=new Date();
			d.setTime(d.getTime()+(parseInt(days)*60*60*1000));
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

