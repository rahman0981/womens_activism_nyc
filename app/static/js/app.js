window.onload = function() {
    // Functionality for tags
    var selectedTags = [];

    $('.share-tag').click(function () {
        $(this).toggleClass('share-inactive');
        $(this).toggleClass('share-active');
        if ($.inArray(this.childNodes[0].data, selectedTags) > -1) {
            selectedTags.splice($.inArray(this.childNodes[0].data, selectedTags), 1);
        } else {
            selectedTags.push(this.childNodes[0].data);
        }
        $('#hidden-tag-input').val(selectedTags);
    });

    // Share a story - text counter
    $('#her-story-text').keyup(function () {
        $('#story-text-count').text($(this).val().length);
    });

    //Nav active state change
    $(".nav li").removeClass("active");
    $('a[href=".' + this.location.pathname + '"]').parents('li,ul').addClass('active');

    // Scroll fix for Parsley.js
    if (this.location.pathname == '/share') {
      var errorList = [];
      window.Parsley.on('field:error', function() {
        if (!errorList[0]) {
            errorList.push(this.$element);
            $("html, body").animate({
                scrollTop: errorList[0].parent().parent().parent().find('h1').offset().top
            }, 1000, function () {
                errorList = [];
            });
        }
      });
    }
}