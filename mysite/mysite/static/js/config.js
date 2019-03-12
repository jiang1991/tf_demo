var vueConfig = new Vue({
  el: '#robot_box',
  data: {
    message: '',
    set_wifi: false,
    robots:[
    ],
    clicked_index: 0,
  },
  methods: {
    cmd_set_wifi: function () {
      this.message = '';
      var self = this;

      var command = {};
      command.cmd = "set_wifi_state";
      command.parameter = {};
      command.parameter.wifi_state = this.set_wifi ? 0 : 1;
      var cmd_json = JSON.stringify(command);

      console.log(cmd_json);

      $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/api/json',
        data: cmd_json,
        success: function (json) {
          
          if (json.return == 1) {
            self.message = "设置wifi成功";
          } else if (json.return == 0) {
            self.message = "设置wifi失败： " + json.error_message;
          }
        },
        dataType: 'json'
      });
    },

    scan_robots: function () {
      this.message = '';
      var self = this;
      self.robots = [];

      var command = {};
      command.cmd = "scan_robot";
      var cmd_json = JSON.stringify(command);

      console.log(cmd_json);

      $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/api/json',
        data: cmd_json,
        success: function (json) {
          console.log(json);
          console.log(typeof(json.robots));

          if (json.robots.length == 0) {
            console.log("no robots");
            self.message = "当前无机器人在线";
          } else {
            console.log(json.robots);
            for (var i=0; i<json.robots.length; i++) {
              // var rb = JSON.parse(robot);
              var rb = json.robots[i];
              console.log(typeof(rb) + rb);
              self.robots.push(rb);
            }
            self.message = "在线机器人数量: " + self.robots.length;
          }
        },
        dataType: 'json'
      });
    },

    set_robots: function () {
      this.message = '';
      var self = this;

      var command = {};
      command.cmd = "set_robots";
      command.robots = [];
      for (var i = 0; i < self.robots.length; i++) {
        command.robots.push(self.robots[i]);
      }

      var cmd_json = JSON.stringify(command);

      console.log(cmd_json);

      $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/api/json',
        data: cmd_json,
        success: function (json) {

          if (json.return == 1) {
            self.message = "批量修改机器人成功";
          } else if (json.return == 0) {
            self.message = "批量修改机器人失败： " + json.error_message;
          }

        },
        dataType: 'json'
      });
    },

    auto_pair: function () {
      this.message = '';
      var self = this;

      var command = {};
      command.cmd = "auto_pairing";
      var cmd_json = JSON.stringify(command);

      console.log(cmd_json);

      $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/api/json',
        data: cmd_json,
        success: function (json) {

          if (json.return == 1) {
            self.message = "自动配对成功";
          } else if (json.return == 0) {
            self.message = "自动配对失败： " + json.error_message;
          }
        },
        dataType: 'json'
      });
    },

    get_robot_info: function (index) {
      console.log(index);

      this.message = '';
      var self = this;

      var command = {};
      command.cmd = "get_robot_info";
      command.parameter = {};
      command.parameter.id = self.robots[index].id;
      command.parameter.ip = self.robots[index].ip;
      var cmd_json = JSON.stringify(command);

      console.log(cmd_json);

      $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/api/json',
        data: cmd_json,
        success: function (json) {

          console.log(json);
          self.message = "获取编号为" + self.robots[index].id + "机器人信息成功";
          self.robots[index] = json;

        },
        dataType: 'json'
      });
    },

    set_robot_info: function (index) {
      console.log(index);

      this.message = '';
      var self = this;

      var command = {};
      command.cmd = "set_robot_info";
      command.parameter = self.robots[index];
      var cmd_json = JSON.stringify(command);

      console.log(cmd_json);

      $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/api/json',
        data: cmd_json,
        success: function (json) {

          if (json.return == 1) {
            console.log(json);
            self.message = "设置编号为" + self.robots[index].id + "机器人信息成功";
          } else if (json.return == 0) {
            self.message = "设置编号为" + self.robots[index].id + "机器人信息失败" + json.error_message;
          }
        },
        dataType: 'json'
      });
    }


  },
})