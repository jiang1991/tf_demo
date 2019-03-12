
var app = new Vue({
    el: '#signin_box',
    data: {
        seen: false,
        password: '',
        err_msg: 'wrong password!'
    },
    methods: {

        sign_in: function () {
            var self = this;

            var post_json = {};
            post_json.password = this.password;
            var send_json = JSON.stringify(post_json);

            console.log(send_json);
//            this.err_msg = this.password;
//            this.seen = true

            $.ajax({
                type: 'POST',
                url: 'http://127.0.0.1:8000/api/login',
                data: send_json,
                success: function(json) {

                    if (json.status == 'ok') {
                        var b64psd = btoa(self.password);
                        document.cookie = "psd=" + b64psd;
                        window.location.href = '/console';
                    } else {
                        self.err_msg = json.error;
                        self.seen = true;
                        console.log(json.status);
                        console.log(self.err_msg)
                    }
                    
                },
                dataType: 'json'
            });
        }
    }
})


