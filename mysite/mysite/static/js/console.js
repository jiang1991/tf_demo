

var vue_config = new Vue({
  el: '#config_box',
  data: {
    message: '',

    errors: [],

    current_mode: '',
    coin_count: 0,
    game_count: 0,
    game_time: 0,
    music_volume: 0,
    sound_volume: 0,
    resolution: '',
    thump_blood: 0,
    tap_blood: 0,
    skill_number: 0,
  },
  methods: {
    read_config: function () {
      this.message = '';
      var self = this;

      var command = {};
      command.cmd = "get_data";
      var cmd_json = JSON.stringify(command);

      $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/api/json',
        data: cmd_json,
        success: function (json) {

          self.message = "读取成功";

          self.current_mode = json.current_mode;
          var mode = json.current_mode;
          if (mode == 'team_mode') {
            self.coin_count = json.team_mode.coin_count;
            self.game_count = json.team_mode.game_count;
            self.game_time = json.team_mode.game_time;
            self.music_volume = json.team_mode.music_volume;
            self.sound_volume = json.team_mode.sound_volume;
            self.resolution = json.team_mode.resolution;
            self.thump_blood = json.team_mode.thump_blood;
            self.tap_blood = json.team_mode.tap_blood;
            self.skill_number = json.team_mode.skill_number;
          } else if (mode == 'melee_mode') {
            self.coin_count = json.melee_mode.coin_count;
            self.game_count = json.melee_mode.game_count;
            self.game_time = json.melee_mode.game_time;
            self.music_volume = json.melee_mode.music_volume;
            self.sound_volume = json.melee_mode.sound_volume;
            self.resolution = json.melee_mode.resolution;
            self.thump_blood = json.melee_mode.thump_blood;
            self.tap_blood = json.melee_mode.tap_blood;
            self.skill_number = json.melee_mode.skill_number;
          } else if (mode == 'football_mode') {
            self.coin_count = json.football_mode.coin_count;
            self.game_count = json.football_mode.game_count;
            self.game_time = json.football_mode.game_time;
            self.music_volume = json.football_mode.music_volume;
            self.sound_volume = json.football_mode.sound_volume;
            self.resolution = json.football_mode.resolution;
            self.thump_blood = json.football_mode.thump_blood;
            self.tap_blood = json.football_mode.tap_blood;
            self.skill_number = json.football_mode.skill_number;
          }


        },
        dataType: 'json'
      });
    },

    write_config: function () {
      this.message = '';
      var self = this;

      this.errors = [];

      if (this.game_time < 10 || this.game_time > 999) {
        this.errors.game_time = true;
      }

      if (this.thump_blood < 20 || this.thump_blood > 50) {
        this.errors.thump_blood = true;
      }

      if (this.tap_blood < 10 || this.tap_blood > 40) {
        this.errors.tap_blood = true;
      }

      if (this.errors.game_time || this.errors.thump_blood || this.errors.tap_blood) {
        console.log("have error");
        return;
      }

      var command = {};
      command.cmd = "modify_data";

      var mode = self.current_mode;

      if (mode == 'team_mode') {
        command.team_mode = {};
        command.team_mode.coin_count = this.coin_count;
        command.team_mode.game_count = this.game_count;
        command.team_mode.game_time = this.game_time;
        command.team_mode.music_volume = this.music_volume;
        command.team_mode.sound_volume = this.sound_volume;
        command.team_mode.resolution = this.resolution;
        command.team_mode.thump_blood = this.thump_blood;
        command.team_mode.tap_blood = this.tap_blood;
        command.team_mode.skill_number = this.skill_number;
      } else if (mode == 'melee_mode') {
        command.melee_mode = {};
        command.melee_mode.coin_count = this.coin_count;
        // command.melee_mode.game_count = this.game_count;
        command.melee_mode.game_count = 0;
        command.melee_mode.game_time = this.game_time;
        command.melee_mode.music_volume = this.music_volume;
        command.melee_mode.sound_volume = this.sound_volume;
        command.melee_mode.resolution = this.resolution;
        command.melee_mode.thump_blood = this.thump_blood;
        command.melee_mode.tap_blood = this.tap_blood;
        command.melee_mode.skill_number = this.skill_number;
      } else if (mode == 'football_mode') {
        command.football_mode = {};
        command.football_mode.coin_count = this.coin_count;
        command.football_mode.game_count = this.game_count;
        command.football_mode.game_time = this.game_time;
        command.football_mode.music_volume = this.music_volume;
        command.football_mode.sound_volume = this.sound_volume;
        command.football_mode.resolution = this.resolution;
      }
      
      var cmd_json = JSON.stringify(command);

      console.log(cmd_json);

      $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/api/json',
        data: cmd_json,
        success: function (json) {

          if (json.return == 1) {
            self.message = "修改成功";
          } else if (json.return == 0) {
            self.message = "修改失败： " + json.error_message;
          }

        },
        dataType: 'json'
      });
    }

  },

})