odoo.define('assignment.recruitment_form_validation', function (require) {
    "use strict";

    var publicWidget = require('web.public.widget');

    publicWidget.registry.RecruitmentFormValidation = publicWidget.Widget.extend({
        selector: '#hr_recruitment_form',  // Form ID
        events: {
            'click .s_website_form_send': '_onClickSendButton',  // <- listen to button click
        },

        _onClickSendButton: function (ev) {
            console.log('Recruitment Send Button clicked');

            var form = this.$el;
            var isValid = true;

            // Clean previous errors
            form.find('.invalid-feedback').remove();
            form.find('.form-control').removeClass('is-invalid');

            // Validate required inputs
            form.find('.s_website_form_input[required]').each(function () {
                var $input = $(this);

                if (!$input.val()) {
                    isValid = false;
                    $input.addClass('is-invalid');

                    $('<div class="invalid-feedback d-block mt-1">This field is required.</div>')
                        .insertAfter($input);
                }
            });

            if (!isValid) {
                ev.preventDefault(); // Stop Odoo's AJAX submit
                console.log('Validation failed: form not submitted.');
            } else {
                console.log('Validation passed: form can submit.');
            }
        },
    });
});

// Update label when a user selects a file
odoo.define('assignment.update_file_input_label', function (require) {
    "use strict";

    $(document).on('change', '.custom-file-input', function (e) {
        let fileName = e.target.files[0] ? e.target.files[0].name : '';
        $(this).next('.custom-file-label').html(fileName);
    });
});
