var rToLogin = server + 'login/proses';

var loginApp = new Vue({
  el : '#login-app',
  data : {

  },
  methods : {
    loginAtc : function()
    {
      let username = document.querySelector('#txtUsername').value;
      let password = document.querySelector('#txtPassword').value;
      let ds = {'username':username, 'password':password}
      $.post(rToLogin, ds, function(data){
        console.log(data);
      });
    }
  }
});
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
$.ajaxSetup({
  headers: {
      'X-CSRF-TOKEN': csrftoken
  }
});
document.querySelector('#txtUsername').focus();