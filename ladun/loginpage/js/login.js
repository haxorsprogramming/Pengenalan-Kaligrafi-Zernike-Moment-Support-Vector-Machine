// Route 
var rToLoginProses = server + "login-proses";

// Vue Object 
var loginApp = new Vue({
  el : '#login-app',
  data : {

  },
  methods : {
    loginAtc : function()
    {
      let username = document.querySelector('#txtUsername').value;
      let password = document.querySelector('#txtPassword').value;
      if(username === ''){
        pesanUmumApp('warning', 'Isi field!!!', 'Harap isi username ...!');
      }
      if(password === ''){
        pesanUmumApp('warning', 'Isi field!!!', 'Harap isi password ...!');
      }
      if(username === '' || password === ''){
      }else{
        let dataSend = {'username':username, 'password':password}
        axios.post(rToLoginProses, dataSend).then(function(res){
          let dr = res.data;
          if(dr.status === 'error_password'){
            pesanUmumApp('warning', 'Error', 'Username / password salah ..');
          }else if(dr.status === 'no_username'){
            pesanUmumApp('warning', 'Error', 'Tidak ada username yg terdaftar, coba cek kembali ..');
          }else{
            console.log("sukses");
          }
        });
      }
    }
  }
});

// Inisialisasi
$.ajaxSetup({
  headers: {
      'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
  }
});
document.querySelector('#txtUsername').focus();

// Function 
function pesanUmumApp(icon, title, text)
{
  Swal.fire({
    icon : icon,
    title : title,
    text : text
  });
}