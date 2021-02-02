var rToLogin = server + 'login/proses';

var loginApp = new Vue({
  el : '#login-app',
  data : {

  },
  methods : {
    loginAtc : function()
    {
      let username = document.querySelector('#txtUsername').value;
      console.log(username);
      let ds = {'username':username}
      axios({
        method : 'post',
        url : rToLogin,
        data : ds,
        headers : {'Content-Type': 'multipart/form-data'}
      }).then(function(res){
        let dr = res.data;
        console.log(dr);
      });
      // axios.post(rToLogin, ds).then(function(res){
      //   let dr = res.data;
      //   console.log(dr);
      // });
    }
  }
});

document.querySelector('#txtUsername').focus();