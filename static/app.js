Dropzone.autoDiscover = false;

function init() {
    const url = "/api/predict";
    let dz = new Dropzone("#dropzone", {
        url: url,
        paramName: "image",
        maxFiles: 1,
        addRemoveLinks: true,
        dictDefaultMessage: "Some Message",
        autoProcessQueue: false
    });

    dz.on("addedfile", function() {
        console.log("added file");
        console.log(dz.files);
        if (dz.files[1]!=null) {
            dz.removeFile(dz.files[0]);
        }
    });

    dz.on("complete", function (file) {
        console.log("on complete");
        if (file.status !== "error") {
            $("#classification-error").hide();
            $("#classification-results").html("this is a cat").show();
            dz.removeFile(file);
        }
    });
    dz.on("error", function(file, error, xhr) {
        $("#classification-error").html(error.detail ? error.detail[0].msg : 'error happened').show();
    })
    dz.on("success", function (file, response) {
        console.log("sucesso");
        // var ficheiro = { nome: file.name, link: response[0] };
        // $scope.$apply($scope.uploadedFiles.push(ficheiro));
    });

    $("#classify-btn").on('click', function (e) {
        dz.processQueue();
        return false;
    });
}

$(document).ready(function() {
    $("#classification-error").hide();
    $("#classification-results").hide();
    init();
});