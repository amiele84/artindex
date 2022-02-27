
// if true, will automatically run
// the config below
Dropzone.autoDiscover = true;



Dropzone.options.uploadWidget = {
  paramName: 'file',
  maxFilesize: 2, // MB
  maxFiles: 2,
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
