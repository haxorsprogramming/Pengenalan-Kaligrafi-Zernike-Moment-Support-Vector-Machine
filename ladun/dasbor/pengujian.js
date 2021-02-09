var rToProses = server + "dashboard/proses-uji";

var divPengujian = new Vue({
    delimiters: ["[[", "]]"],
    el : '#divPengujian',
    data : {
        titleForm : 'Form pengujian'
    },
    methods : {
        mulaiAnalisaAtc : function()
        {
            let citraData = document.querySelector("#txtPreviewUpload").getAttribute("src");
            let ds = {'citraData':citraData}
            $.post(rToProses, ds, function(data){
                console.log(data);
                $("#divHasilEkstraksi").show();
            });
        }
    }
});

$('#divHasilEkstraksi').hide();

function setImg(){
    var citraInput = document.querySelector('#txtFoto');
    var preview = document.querySelector('#txtPreviewUpload');
    var fileGambar = new FileReader();
    fileGambar.readAsDataURL(citraInput.files[0]);
    fileGambar.onload = function(e){
        let hasil = e.target.result;
        preview.src = hasil;
        divPengujian.titleForm = "Citra berhasil di upload";
    }
    console.log("image ready to upload");
}