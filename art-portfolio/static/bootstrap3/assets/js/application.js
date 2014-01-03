// ++++++++++++++++++++++++++++++++++++++++++++++++
// NOTICE!! THIS JAVASCRIPT IS USED JUST FOR DOCS
// YOU MAY NEED SOME CODE FOR YOUR PROJECT
// NOT INCLUDE THIS FILES AS IS
// ++++++++++++++++++++++++++++++++++++++++++++++++

!function ($) {

  $(function(){

    // Disable links in docs
    $('[href=#]').click(function (e) {
      e.preventDefault()
    })

    // tooltip demo
    $("[data-toggle=tooltip]").tooltip();

    // popover demo
    $("[data-toggle=popover]")
      .popover()

    // button state demo
    $('#fat-btn')
      .click(function () {
        var btn = $(this)
        btn.button('loading')
        setTimeout(function () {
          btn.button('reset')
        }, 3000)
      })

    /* Style switcher */
    if ( 'localStorage' in window && window['localStorage'] !== null ) {
      
      var stylesheet = $("#dropper-theme"), stKey = 'dropper-bs3';

      localStorage[stKey] && stylesheet.attr("href", localStorage[stKey]);

      $("#css-switcher a").click(function() { 
          localStorage[stKey] = $(this).attr('rel');
          stylesheet.attr("href", localStorage[stKey]);
          return false;
      });
    }

    // carousel demo
    $('#myCarousel').carousel();
    $('#myFadeCarousel').carousel();


    /////////////////////////////
    // GMAP v3
    /////////////////////////////

    if(typeof google !== 'undefined' && $.fn.gMap )
      $('.gmap').each(function(){
        var d = $(this).data('markers').split(';'),
            m = [];
        for(a in d) { m.push({'address' : d[a]}) }
        $(this).gMap({
          zoom: $(this).data('zoom') || 14,
          markers: m
        });

      })

    /////////////////////////////
    // DATEPICKER
    /////////////////////////////
    
    $('#dp-input1').datepicker();
    $('#dp-input2').datepicker();

    /////////////////////////////
    // COLORPICKER
    /////////////////////////////

    $('#cp1').colorpicker({
      format: 'hex'
    });
    $('#cp2').colorpicker();
    $('#cp3').colorpicker();

    var btnStyle = $('#cp4').length && $('#cp4')[0].style;
    $('#cp4').colorpicker().on('changeColor', function(ev){
        btnStyle.backgroundColor = ev.color.toHex();
    });

  })
}(window.jQuery)
