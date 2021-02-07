// vue object 
var divMenu = new Vue({
    el : '#divMenu',
    data : {

    },
    methods : {
        berandaAtc : function()
        {
            renderMenu('dashboard/beranda');
        }
    }
});

function renderMenu(halaman){
    progStart();
    $('#divUtama').html("Memuat halaman ..");
    $('#divUtama').load(server+halaman);
    progStop();
}

function progStart()
{
  NProgress.start();
}

function progStop()
{
  NProgress.done();
}