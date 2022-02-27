
           Div(
                Div(HTML("<p><strong>Bio"), css_class='bio-label'),
                css_class='form-row bio-label-box'),

            Row(
                Div(Field('bio'), css_class='description-class-bio')),

            Div(
                Div(HTML("<p><strong>Notes"), css_class='bio-label'),
                css_class='form-row bio-label-box'),

            Row(
                Div(Field('notes'), css_class='description-class-notes')),

            Div(
                    Row(
                        Div(HTML('<button type="button" class="btn btn-primary" style="margin-bottom: 50px; padding: 10px 150px 10px 100px; text-align: center; border: 1px solid #D3D3D3; border-radius: 25px 25px 25px 25px; color: white; background-color: #D3D3D3; width: 25px; height: 45px; font-size: 15px;"><strong>Cancel</strong></button>'),
                        css_class = 'cancel'),
                        Div(HTML('<button type="button" class="btn btn-warning ml-4" style="padding: 5px 150px 15px 100px; text-align: center; border: 1px solid #D3D3D3; border-radius: 25px 25px 25px 25px; color: white; ; width: 35px; height: 45px; font-size: 20px; background-color: #00CC33;">Save</button>'),
                        css_class = 'submit'),
                    ),
                css_class = 'btn-row',
                ),
            
        )#end layout