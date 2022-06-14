$(document).ready(function(){
	$(".hint span").hover(function(){
		$(this).parent().siblings(".hint_message").show();
	}, function(){
		$(this).parent().siblings(".hint_message").hide();
	});
	var number = window.location.href.split("/");
	for(var i=0;i<number[number.length-1];i++){
		$(`#left_nav li:nth-of-type(${i}) .indicator`).addClass("filled");
	}
	console.log($(`#left_nav li:nth-of-type(${number[number.length-1]}) p`).text());
	$(".heading").text($(`#left_nav li:nth-of-type(${number[number.length-1]}) p`).text());
	if(number[number.length-1] == 2){
		$("#id_passive_intensity").parent().hide();
		$("#id_current_smoking_habits").on('change',function(){
			if($(this).val() == "Passive"){
				$("#id_passive_intensity").parent().show();
			}
			else{
				$("#id_passive_intensity").parent().hide();
			}
		})
	}
	if(number[number.length-1] == 6){
		$("#id_bmi").parent().after(`<div class="col-6 align-items-end d-flex">
									 <p class="my-3" role="button" id="calculate_bmi">
									 <u>
									 	Calculate BMI
									 </u>
									 </p></div>`);
		$("#calculate_bmi").click(function(){
				var weight = parseInt($("#id_weight").val());
				var height_squared = Math.pow(parseInt($("#id_height").val())/100,2);
				console.log(weight, height_squared);
				$("#id_bmi").val(parseFloat(weight/height_squared).toFixed(2));
		});
	}
	if(number[number.length-1] == 7){
		$("#id_fatigue1, #id_fatigue2, #id_fatigue3").on('change',function(){
			var fatigues = [$("#id_fatigue1").val(), $("#id_fatigue2").val(), $("#id_fatigue3").val()];
			var f=0;
			for(var i in fatigues){
				if(fatigues[i] == "Yes"){
					f+=1;
				}
			}
			if(f>=2){
				$("#id_fatigue").val("Yes");
			}
			else{
				$("#id_fatigue").val("No");
			}
			console.log($("#id_fatigue").val());
		})
	}
});