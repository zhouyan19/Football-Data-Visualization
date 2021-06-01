<template>
  <div class="manage_add">
    <div class="tips"> *Tips: Please Add all the information for the game.</div>
    <el-container class="all_board">
      <el-col class="col_box" :span="24">
        <el-form class="info_form" ref="form" :model="form" :rules="rules" label-width="80px">
          <el-row><el-col>
            <el-form-item id="selectForm" prop="home_name">
              <label slot="label" style="font-size:20px">Home&nbsp;Team</label>
              <el-input class="name_box" v-model="form.home_name"></el-input>
            </el-form-item>
          </el-col></el-row>
          <el-row><el-col>
            <el-form-item id="selectForm" prop="away_name">
              <label slot="label" style="font-size:20px">Away&nbsp;Team</label>
              <el-input class="name_box" v-model="form.away_name"></el-input>
            </el-form-item>
          </el-col></el-row>
          <el-row><el-col>
            <el-form-item id="selectForm" prop="team_type">
              <label slot="label" style="font-size:20px">Team&nbsp;Type</label>
              <el-select class="team_box" v-model="form.team_type" placeholder="Choose the team type">
                <el-option
                  v-for="item in options1"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-col></el-row>
          <el-row><el-col>
            <el-form-item id="selectForm" prop="tournament">
              <label slot="label" style="font-size:20px">Tournament&nbsp;</label>
              <el-cascader
                v-if="form.team_type===0"
                class="type_box"
                v-model="form.tournament"
                :options="options_world"
                placeholder="Choose the tournament">
              </el-cascader>
              <el-cascader
                v-if="form.team_type===1"
                class="type_box"
                v-model="form.tournament"
                :options="options_league"
                placeholder="Choose the tournament">
              </el-cascader>
            </el-form-item>
          </el-col></el-row>
        </el-form>
      </el-col>
      <el-col class="col_box2" :span="24">
        <el-form class="info_form" ref="form" :model="form" :rules="rules" label-width="80px">
          <el-row><el-col>
            <el-form-item id="selectForm" prop="home_score">
              <label slot="label" style="font-size:20px">Home&nbsp;Team&nbsp;Score</label>
              <el-input class="score_box" type="number" v-model.number="form.home_score"></el-input>
            </el-form-item>
          </el-col></el-row>
          <el-row><el-col>
            <el-form-item id="selectForm" prop="away_score">
              <label slot="label" style="font-size:20px">Away&nbsp;Team&nbsp;Score</label>
              <el-input class="score_box" type="number" v-model.number="form.away_score"></el-input>
            </el-form-item>
          </el-col></el-row>
          <el-row><el-col :span="22">
            <el-form-item id="selectForm" prop="date">
              <label slot="label" style="font-size:20px">Competition&nbsp;Date</label>
              <el-date-picker
                class="date_box"
                v-model="form.date"
                type="date"
                placeholder="Choose the date"
              ></el-date-picker>
            </el-form-item>
          </el-col></el-row>
        </el-form>
      </el-col>
    </el-container>
    <el-row class="button_box">
      <el-button
        type="primary"
        @click="submit"
        style="font-size:20px"
      >
        Submit
      </el-button>
    </el-row>
  </div>
</template>

<script>
import {addGame} from '@/utils/communication'
export default {
  name: 'MAdd',
  data () {
    return {
      form: {
        date: new Date(),
        home_name: '',
        away_name: '',
        home_score: 0,
        away_score: 0,
        tournament: '',
        team_type: 0
      },
      rules: {
        home_name: [{required: true, message: 'Please fill in the blank!', trigger: 'blur'}],
        away_name: [{required: true, message: 'Please fill in the blank!', trigger: 'blur'}],
        home_score: [{required: true, message: 'Please fill in the blank!', trigger: 'blur'}],
        away_score: [{required: true, message: 'Please fill in the blank!', trigger: 'blur'}],
        tournament: [{required: true, message: 'Please choose the type!', trigger: 'blur'}],
        team_type: [{required: true, message: 'Please choose the type!', trigger: 'blur'}]
      },
      options_world: [
        {
          value: 'Friendly',
          label: 'Friendly'
        },
        {
          value: 'FIFA',
          label: 'FIFA',
          children: [
            {value: 'FIFA World Cup', label: 'FIFA World Cup'},
            {value: 'FIFA World Cup qualification', label: 'FIFA World Cup qualification'}
          ]
        },
        {
          value: 'UEFA',
          label: 'UEFA',
          children: [
            {value: 'UEFA Euro qualification', label: 'UEFA Euro qualification'},
            {value: 'UEFA Euro championship', label: 'UEFA Euro championship'},
            {value: 'UEFA Nations League', label: 'UEFA Nations League'}
          ]
        },
        {
          value: 'African',
          label: 'African',
          children: [
            {value: 'African Cup of Nations', label: 'African Cup of Nations'},
            {value: 'African Cup of Nations qualification', label: 'African Cup of Nations qualification'},
            {value: 'African Nations Championship', label: 'African Nations Championship'}
          ]
        },
        {
          value: 'CFU',
          label: 'CFU',
          children: [
            {value: 'CFU Caribbean Cup', label: 'CFU Caribbean Cup'},
            {value: 'CFU Caribbean Cup qualification', label: 'CFU Caribbean Cup qualification'}
          ]
        },
        {
          value: 'AFC',
          label: 'AFC',
          children: [
            {value: 'AFC Asian Cup', label: 'AFC Asian Cup'},
            {value: 'AFC Asian Cup qualification', label: 'AFC Asian Cup qualification'},
            {value: 'AFC Challenge Cup qualification', label: 'AFC Challenge Cup qualification'}
          ]
        },
        {
          value: 'Other',
          label: 'Other',
          children: [
            {value: 'International Cup', label: 'International Cup'},
            {value: 'EAFF Championship', label: 'EAFF Championship'},
            {value: 'UAFA Cup', label: 'UAFA Cup'},
            {value: 'UNCAF Cup', label: 'UNCAF Cup'},
            {value: 'UDEAC Cup', label: 'UDEAC Cup'},
            {value: 'CECAFA Cup', label: 'CECAFA Cup'},
            {value: 'CONIFA World Football Cup', label: 'CONIFA World Football Cup'},
            {value: 'Copa América', label: 'Copa América'},
            {value: 'CONCACAF Nations League', label: 'CONCACAF Nations League'},
            {value: 'British Championship', label: 'British Championship'},
            {value: 'CCCF Championship', label: 'CCCF Championship'},
            {value: 'WAFF Championship', label: 'WAFF Championship'}
          ]
        }
      ],
      options_league: [
        {
          value: 'UEFA',
          label: 'UEFA',
          children: [
            {value: 'UEFA EL', label: 'UEFA EL'},
            {value: 'UEFA CL', label: 'UEFA CL'},
            {value: 'UEFA CW', label: 'UEFA CW'},
            {value: 'UEFA SC', label: 'UEFA SC'},
            {value: 'UEFA ITC', label: 'UEFA ITC'}
          ]
        },
        {
          value: 'CAF',
          label: 'CAF',
          children: [
            {value: 'CAF CC', label: 'CAF CC'},
            {value: 'CAF CL', label: 'CAF CL'},
            {value: 'CAF SC', label: 'CAF SC'}
          ]
        },
        {
          value: 'AFC',
          label: 'AFC',
          children: [
            {value: 'AFC CL', label: 'AFC CL'},
            {value: 'AFC Pokal', label: 'AFC Pokal'},
            {value: 'AFC Pres. Cup', label: 'AFC Pres. Cup'}
          ]
        },
        {
          value: 'Copa',
          label: 'Copa',
          children: [
            {value: 'Copa Lib', label: 'Copa Lib'},
            {value: 'Copa Sud', label: 'Copa Sud'}
          ]
        },
        {
          value: 'CONCACAF',
          label: 'CONCACAF',
          children: [
            {value: 'CONCACAF CC', label: 'CONCACAF CC'},
            {value: 'CONCACAF L', label: 'CONCACAF L'}
          ]
        },
        {
          value: 'Other',
          label: 'Other',
          children: [
            {value: 'CFU CC', label: 'CFU CC'},
            {value: 'OFC CC', label: 'OFC CC'},
            {value: 'Recopa', label: 'Recopa'}
          ]
        }
      ],
      options1: [
        {value: 0, label: 'National Team'},
        {value: 1, label: 'League Team'}
      ]
    }
  },
  methods: {
    submit () {
      this.$refs['form'].validate(valid => {
        if (valid) {
          if (this.form.home_score < 0 || this.form.away_score < 0) {
            this.$message({
              type: 'warning',
              message: 'Invalid score！'
            })
            return 'error'
          }
          let d1 = this.form.date
          let t1 = d1
          let mon1 = t1.getMonth() + 1
          let day1 = t1.getDate()
          if (mon1 < 10) {
            mon1 = '0' + String(mon1)
          } else {
            mon1 = String(mon1)
          }
          if (day1 < 10) {
            day1 = '0' + String(day1)
          } else {
            day1 = String(day1)
          }
          d1 = String(t1.getFullYear()) + '-' + mon1 + '-' + day1
          if (this.form.tournament.length === 1) {
            this.form.tournament = this.form.tournament[0]
          } else {
            this.form.tournament = this.form.tournament[1]
          }
          addGame({
            date: d1,
            home_name: this.form.home_name,
            away_name: this.form.away_name,
            home_score: this.form.home_score,
            away_score: this.form.away_score,
            tournament: this.form.tournament,
            league_mark: this.form.team_type
          }).then((successful) => {
            if (successful) {
              this.$message({
                type: 'success',
                message: 'Add successfully！'
              })
            } else {
              this.$message({
                type: 'error',
                message: 'Error！'
              })
            }
          })
        } else {
          this.$message({
            type: 'warning',
            message: 'Please fill in all the blanks!'
          })
        }
      })
    }
  }
}
</script>

<style scoped>
.col_box {
  border: 0px solid rgb(0, 0, 0);
}
.col_box2 {
  border: 0px solid rgb(255, 0, 0);
  margin-left: 40px;
}
.tips {
  font-size: 20px;
  margin-bottom: 50px;
}
.el-form-item {
  margin-bottom: 60px;
}
.name_box {
  margin-left: 80px;
  width: 240px;
}
.type_box {
  margin-left: 80px;
  width: 240px;
}
.team_box {
  margin-left: 80px;
  width: 240px;
}
.score_box {
  margin-left: 140px;
  width: 240px;
}
.date_box {
  margin-left: 140px;
  width: 240px;
}
.button_box {
  margin-top: -40px;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
</style>
