
// if true, will automatically run
// the config below
Dropzone.autoDiscover = true;



Dropzone.options.uploadpieceWidget = {
  paramName: 'file',
  maxFilesize: 2, // MB
  maxFiles: 10,
  thumbnailWidth: 300,
  thumbnailHeight: 300,
  dictDefaultMessage: 'Drag an image here to upload, or click to select one',
  acceptedFiles: 'image/*',
  clickable: true, //if true then dropzone is clickable
  //addRemoveLinks: true, //rmve files//
  createImageThumbnails: true, //show thumbnail//
  previewsContainer: ".dz-preview", //show a preview in another place

  //funtion//
  //init: function() {
    //  this.on("success", function(file) { alert("Success. You did it."); 
    //});
    //}
  //}
}
        // Start of test //

//import * as basicLightbox from 'basiclightbox'

const instance = basicLightbox.create(`
<div class="modal">
    <p>A custom modal that has been styled independently. It's not part of basicLightbox, but perfectly shows its flexibility.</p>
    <input placeholder="Type something">
    <a>Close</a>
</div>
`, {
onShow: (instance) => {
    instance.element().querySelector('').onclick = instance.show()
}
})

instance.show()



// 10/10 //
//Dropzone.autoDiscover = false;
//$("div#dropzone-example").dropzone({ url: "/upload" });


        // End of test //
