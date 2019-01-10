$(function () {
  var img_section = (".no_error tbody");
  $("#fileupload").fileupload({
        dataType: 'json',
        async: false,
        done: function (e, data) {
          if (data.result.is_valid) {
            console.log("lk3")
            var url_list=[]
            url_list.push(data.result.url);
            var index = url_list.length-1        
            img_section.eq(index).prepend("<tr><td><a href='" + url_list[index] + "'><img src='"+ url_list[index] +"'></a></td></tr>")
            
            $('.js-upload-photos').attr("style", "visibility: none");
          }
        }
      });
  console.log(img_section.length)  
  $("#ultimate_form").append("<button>ADD pic</button>")
});
