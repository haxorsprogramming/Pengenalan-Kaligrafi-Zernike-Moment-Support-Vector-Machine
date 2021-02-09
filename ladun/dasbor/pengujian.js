google.charts.load('current', {'packages':['scatter']});
google.charts.setOnLoadCallback(drawChart);

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
                let imgName = data.dataCitra;
                let zernikeValue = data.zernikeValue;
                let imgLocation = server + "ladun/data_zernike/"+imgName;
                document.querySelector('#txtCitraZernike').setAttribute('src', imgLocation);

                var dataChart = new google.visualization.DataTable();
                dataChart.addColumn('number', 'Node');
                dataChart.addColumn('number', 'Values');

                for(i=0; i < 25; i++){
                    let nilaiAwal = zernikeValue[i];
                    let midNilai = nilaiAwal / 2;
                    dataChart.addRows([[nilaiAwal, midNilai]]);

                }
                var options = {
                width: 500,
                height: 400,
                chart: {
                    title: 'Students\' Final Grades',
                    subtitle: 'SVM Height for Kaligrafi'
                },
                axes: {
                    x: {
                    0: {side: 'top'}
                    }
                }
                };

                var chart = new google.charts.Scatter(document.getElementById('scatter_top_x'));
                chart.draw(dataChart, google.charts.Scatter.convertOptions(options));
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

function drawChart () {

    
  }