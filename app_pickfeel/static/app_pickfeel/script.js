jQuery(function ($) {
        // init the state from the input

        // sync the state to the input
        $(".image-radio").on("click", function (e) {
        		$(".image-radio-checked").each(function(i){
            		$(this).removeClass("image-radio-checked");
            });
						$(this).toggleClass("image-radio-checked");
            e.preventDefault();

        });
    });

