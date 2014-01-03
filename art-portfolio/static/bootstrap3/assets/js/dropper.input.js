/////////////////////////////////////////////////
// DROPPPER JS for UI ELements
// Include me if you're using the extended ui
//
// author: @geedmo
// website: geedmo.com
// Copyright (c) 2013, Geedmo. All rights reserved.
// Released under CodeCanyon Regular License: http://codecanyon.net/licenses
/////////////////////////////////////////////////

!function ($) {

  $(function(){


    ////////////////////////
    // INPUT APPEND/PREPEND
    ////////////////////////

    $('.input-group input, .input-group input').focusin(function() {
      $(this).parent().addClass('input-focused')
    }).focusout(function() {
      $(this).parent().removeClass('input-focused')
    })

    ////////////////////////
    // CHECKBOX
    ////////////////////////
    var checkboxIconChecked = "fa fa-check"
    $('.checkbox').each(function() {
      var $this = $(this),
          checkbox = $this.find('input:checkbox'),
          label = $this.children('label'),
          overlay = $('<span class="ctrl-overlay"/>').appendTo(label);

      if(checkbox[0].checked) {
        if(!checkbox[0].disabled)
          $this.addClass('checked')
        overlay.addClass(checkboxIconChecked)
      }
    })
    
    $('.checkbox').on('click',function() {
      var $this = $(this),
          input = $this.find('input:checkbox'),
          overlay = $this.find('.ctrl-overlay');
      
      if(input[0].disabled) return;

      $this[input[0].checked ? 'addClass' : 'removeClass']('checked')
      overlay[input[0].checked ? 'addClass' : 'removeClass'](checkboxIconChecked)
      
    })

    ////////////////////////
    // RADIO
    ////////////////////////
    var radioIconChecked = "fa fa-circle-o",
        radioIconUnchecked = "fa fa-circle";
    $('.radio').each(function() {
      var $this = $(this),
          radio = $this.find('input:radio'),
          label = $this.children('label'),
          overlay = $('<span class="ctrl-overlay"/>').appendTo(label);
      
      overlay.addClass('fa fa-circle')

      if(radio[0].checked) {
        if(!radio[0].disabled)
          $this.addClass('checked')
        overlay.addClass(radioIconChecked).removeClass(radioIconUnchecked)
      }
    })
    
    $('.radio').on('click',function() {
      var $this = $(this),
          radio = $this.find('input:radio'),
          overlay = $this.find('.ctrl-overlay');

      if(radio[0].disabled) return;

      $('input:radio[name='+radio.attr('name')+']')
        .not(':disabled')
        .siblings('.ctrl-overlay').removeClass(radioIconChecked).addClass(radioIconUnchecked)
        .parent().parent().removeClass('checked');


      if(radio[0].checked) {
        $this.addClass('checked');
        overlay.removeClass(radioIconUnchecked).addClass(radioIconChecked);
      }

    })

    ////////////////////////
    // INPUT GROUPS
    ////////////////////////

    $('.input-group-addon > input[type=checkbox]').each(function() {
        var checkbox = $(this),
            addon = checkbox.parent()

        addon.addClass('has-checkbox')

        var overlay = $('<span class="ctrl-overlay"/>').appendTo(addon);

        if(checkbox[0].checked) 
          if(!checkbox[0].disabled)
            addon.addClass('checked');
        
        overlay.addClass(checkboxIconChecked)

    }).parent().on('click', function() {
          var checkbox = $(this).find('input:checkbox')
          
          if(checkbox[0].disabled) return;

          checkbox[0].checked = !checkbox[0].checked
          $(this)[checkbox[0].checked ? 'addClass' : 'removeClass']('checked')
        })


    var igRadioIconChecked = "fa fa-circle";
    $('.input-group-addon > input[type=radio]').each(function() {
        var radio = $(this),
            addon = radio.parent()

        addon.addClass('has-radio');

        var overlay = $('<span class="ctrl-overlay"/>').appendTo(addon);

        if(radio[0].checked) 
          if(!radio[0].disabled)
            addon.addClass('checked')
        
        overlay.addClass(igRadioIconChecked)

    }).parent().on('click', function() {
          var $this = $(this),
              radio = $this.find('input:radio'),
              overlay = $this.find('.ctrl-overlay')
          
          if(radio[0].disabled) return;

          $('input:radio[name='+radio.attr('name')+']')
            .not(':disabled')
            .parent().removeClass('checked');

          radio[0].checked = !radio[0].checked
          $this[radio[0].checked ? 'addClass' : 'removeClass']('checked')

        })



    ////////////////////////
    // SELECT TO DROPDOWN
    ////////////////////////

    $('select[data-toggle="dropdown-select"]').each(function() {
      var $this = $(this), $btn, elements, btnStyle = '';
      
      $this.hide();

      // convert options into li
      // saves option value intro a.rel attribute
      elements = $this.find('option').map(function() {
          return $('<li><a href="#" rel="'+$(this).attr('value')+'">' + $(this).text() + '</a></li>').get(0)
      })

      // add buttons styles
      btnStyle += $this.data('size') ? ' btn-' + $this.data('size') : '';
      btnStyle += $this.data('style') ? ' btn-' + $this.data('style') : ' btn-default';

      // build required markup for dropdown buttons
      $btnGroup = $('<div class="btn-group"/>').insertAfter($this).css('display', 'block');
      // the button that replaces the select
      $btn = $('<button/>', {
              'class': 'btn dropdown-toggle dropdown-select' + btnStyle,
              'data-toggle': 'dropdown'
          }).text($this.find('option:first').text())
            .append('<span class="caret"></span>')
            .appendTo($btnGroup)
      // dropdown content based on select options elements
      $btn.after(
        $('<ul class="dropdown-menu"/>').append(elements)
        );

      // bind click event and update text
      $btn.siblings('.dropdown-menu').on('click', 'li > a', function(e) {
          e.preventDefault();
          $btn.contents().filter(function(){ 
            return this.nodeType === 3; 
          })[0].nodeValue = $(this).text() + " ";
          // replicate into select so we can use it later on form submit
          $this.val($(this).attr('rel')).change()
      })

    })

  })

}(window.jQuery)
