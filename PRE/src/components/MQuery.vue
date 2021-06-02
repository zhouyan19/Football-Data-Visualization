<template>
  <div class="manage_query">
    <div class="input_box">
      <div class="query_box">
        <el-container class="choose_board">
          <el-col class="col_box1">
            <el-form class="info_form" ref="form" :model="form" label-width="80px">
              <el-row><el-col>
                <el-form-item id="selectForm" prop="name">
                  <label slot="label" style="font-size:14px">Name</label>
                  <el-input class="name_box" v-model="form.name"></el-input>
                </el-form-item>
              </el-col></el-row>
            </el-form>
          </el-col>
          <el-col class="col_box2">
            <el-form class="info_form" ref="form" :model="form" label-width="80px">
              <el-row><el-col>
                <el-form-item id="selectForm" prop="tournament">
                  <label slot="label" style="font-size:14px">Tournament</label>
                  <el-cascader
                    class="tour_box"
                    v-model="form.tournament"
                    :options="options"
                    placeholder="tournament">
                  </el-cascader>
                </el-form-item>
              </el-col></el-row>
            </el-form>
          </el-col>
          <el-col class="col_box3">
            <el-form class="info_form" ref="form" :model="form" label-width="80px">
              <el-row><el-col>
                <el-form-item id="selectForm" prop="result">
                  <label slot="label" style="font-size:14px">Result</label>
                  <el-select class="res_box" v-model="form.result" placeholder="result">
                    <el-option
                      v-for="item in options2"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value">
                    </el-option>
                  </el-select>
                </el-form-item>
              </el-col></el-row>
            </el-form>
          </el-col>
        </el-container>
        <el-container class="choose_board">
          <el-col class="col_box4">
            <el-form class="info_form" ref="form" :model="form" label-width="80px">
              <el-row><el-col>
                <el-form-item id="selectForm" prop="format">
                  <label slot="label" style="font-size:14px">Format</label>
                  <el-select class="format_box" v-model="form.format" placeholder="time format">
                    <el-option
                      v-for="item in options3"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value">
                    </el-option>
                  </el-select>
                </el-form-item>
              </el-col></el-row>
            </el-form>
          </el-col>
          <el-col class="col_box5">
            <el-form class="info_form" ref="form" :model="form" label-width="60px">
              <el-row><el-col>
                <el-form-item id="selectForm" prop="date1">
                  <label slot="label">Start</label>
                  <el-date-picker
                    v-if="form.format==='YYYY'"
                    class="date_box"
                    v-model="form.date1"
                    type="year"
                  ></el-date-picker>
                  <el-date-picker
                    v-else-if="form.format==='YYYY-MM'"
                    class="date_box"
                    v-model="form.date1"
                    type="month"
                  ></el-date-picker>
                  <el-date-picker
                    v-else
                    class="date_box"
                    v-model="form.date1"
                    type="date"
                  ></el-date-picker>
                </el-form-item>
              </el-col></el-row>
            </el-form>
          </el-col>
          <el-col class="col_box6">
            <el-form class="info_form" ref="form" :model="form" label-width="60px">
              <el-row><el-col>
                <el-form-item id="selectForm" prop="date1">
                  <label slot="label">End</label>
                  <el-date-picker
                    v-if="form.format==='YYYY'"
                    class="date_box"
                    v-model="form.date2"
                    type="year"
                  ></el-date-picker>
                  <el-date-picker
                    v-else-if="form.format==='YYYY-MM'"
                    class="date_box"
                    v-model="form.date2"
                    type="month"
                  ></el-date-picker>
                  <el-date-picker
                    v-else
                    class="date_box"
                    v-model="form.date2"
                    type="date"
                  ></el-date-picker>
                </el-form-item>
              </el-col></el-row>
            </el-form>
          </el-col>
        </el-container>
      </div>
      <div class="button_box">
        <el-button
          type="primary"
          icon="el-icon-search"
          @click="submitQuery">
          Query
        </el-button>
      </div>
    </div>
    <div class="display">
      <el-table
        v-loading="loading"
        class="the_table"
        ref="multipleTable"
        stripe
        :data="games.slice((current_page-1)*page_size,current_page*page_size)"
        tooltip-effect="dark"
        empty-text="No Data">
        <el-table-column
          fixed="left"
          label="Date"
          prop="date"
          width="120">
          <template slot-scope="{row}">
            <div>{{ dateParser(row.date) }}</div>
          </template>
        </el-table-column>
        <el-table-column
          class="colomn"
          prop="tournament"
          label="Tournament"
          :show-overflow-tooltip="true"
          width="200">
          <template slot-scope="{row}">
            <div>{{ row.tournament }}</div>
          </template>
        </el-table-column>
        <el-table-column
          class="colomn"
          prop="home_name"
          label="Home Team"
          width="150">
          <template slot-scope="{row}">
            <div>{{ row.home_name }}</div>
          </template>
        </el-table-column>
        <el-table-column
          class="colomn"
          prop="away_name"
          label="Away Team"
          width="150">
          <template slot-scope="{row}">
            <div>{{ row.away_name }}</div>
          </template>
        </el-table-column>
        <el-table-column
          class="colomn"
          prop="score"
          label="Score"
          width="120">
          <template slot-scope="{row}">
            <div>{{ scoreParser(row.home_score, row.away_score) }}</div>
          </template>
        </el-table-column>
        <el-table-column
          class="colomn"
          prop="result"
          label="Result(Home)"
          width="150">
          <template slot-scope="{row}">
            <span style="color:green;" v-if="row.result===1.0">Win</span>
            <span style="color:red;" v-if="row.result===0.0">Lose</span>
            <span style="color:rgba(34, 121, 221);" v-if="row.result===0.5">Draw</span>
          </template>
        </el-table-column>
      </el-table>
      <div class="paginator" align="right">
        <el-pagination
          layout="prev, pager, next"
          :page-size="page_size"
          :pager-count="5"
          :total="count"
          @prev-click="(p) => {
            handleChange(p)
          }"
          @next-click="(p) => {
            handleChange(p)
          }"
          @current-change="(p) => {
            handleChange(p)
          }">
        </el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
import {getGames} from '@/utils/communication'
export default {
  name: 'MQuery',
  data () {
    return {
      loading: false,
      current_page: 1,
      page_size: 10,
      count: 0,
      games: [
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Germany', away_name: 'Brazil', home_score: 9, away_score: 7, result: 1},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Germany', away_name: 'Brazil', home_score: 9, away_score: 7, result: 1},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Germany', away_name: 'Brazil', home_score: 9, away_score: 7, result: 1},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Germany', away_name: 'Brazil', home_score: 9, away_score: 7, result: 1},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Germany', away_name: 'Brazil', home_score: 9, away_score: 7, result: 1},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Germany', away_name: 'Brazil', home_score: 9, away_score: 7, result: 1},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Brazil', away_name: 'Germany', home_score: 1, away_score: 7, result: 0},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Germany', away_name: 'Brazil', home_score: 1, away_score: 1, result: 0.5},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Germany', away_name: 'Brazil', home_score: 1, away_score: 1, result: 0.5},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Germany', away_name: 'Brazil', home_score: 1, away_score: 1, result: 0.5},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Germany', away_name: 'Brazil', home_score: 1, away_score: 0, result: 1},
        // {date: 1464739200000, tournament: 'FIFA World Cup', home_name: 'Germany', away_name: 'Brazil', home_score: 1, away_score: 0, result: 1}
      ],
      form: {
        format: '',
        date1: '',
        date2: '',
        name: '',
        tournament: '',
        result: ''
      },
      options: [
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
            {value: 'UEFA Nations League', label: 'UEFA Nations League'},
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
            {value: 'CFU Caribbean Cup qualification', label: 'CFU Caribbean Cup qualification'},
            {value: 'CFU CC', label: 'CFU CC'}
          ]
        },
        {
          value: 'AFC',
          label: 'AFC',
          children: [
            {value: 'AFC Asian Cup', label: 'AFC Asian Cup'},
            {value: 'AFC Asian Cup qualification', label: 'AFC Asian Cup qualification'},
            {value: 'AFC Challenge Cup qualification', label: 'AFC Challenge Cup qualification'},
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
            {value: 'Copa Sud', label: 'Copa Sud'},
            {value: 'Copa América', label: 'Copa América'}
          ]
        },
        {
          value: 'CONCACAF',
          label: 'CONCACAF',
          children: [
            {value: 'CONCACAF CC', label: 'CONCACAF CC'},
            {value: 'CONCACAF L', label: 'CONCACAF L'},
            {value: 'CONCACAF Nations League', label: 'CONCACAF Nations League'}
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
            {value: 'British Championship', label: 'British Championship'},
            {value: 'CCCF Championship', label: 'CCCF Championship'},
            {value: 'WAFF Championship', label: 'WAFF Championship'},
            {value: 'OFC CC', label: 'OFC CC'},
            {value: 'Recopa', label: 'Recopa'}
          ]
        }
      ],
      options2: [
        {value: 'win', label: 'win'},
        {value: 'lose', label: 'lose'},
        {value: 'draw', label: 'draw'},
        {value: '', label: 'all'}
      ],
      options3: [
        {value: 'YYYY', label: 'YYYY'},
        {value: 'YYYY-MM', label: 'YYYY-MM'},
        {value: 'YYYY-MM-DD', label: 'YYYY-MM-DD'}
      ]
    }
  },
  mounted: function () {
    this.count = this.games.length
    console.log(this.count)
  },
  methods: {
    handleChange (p) {
      this.current_page = p
    },
    submitQuery () {
      this.loading = true
      if (this.form.tournament.length === 1) {
        this.form.tournament = this.form.tournament[0]
      } else {
        this.form.tournament = this.form.tournament[1]
      }
      let t = this.form.tournament
      let n = this.form.name
      let d1 = this.form.date1
      let d2 = this.form.date2
      let r = this.form.result
      if (r === 'win') r = 1.0
      if (r === 'lose') r = 0.0
      if (r === 'draw') r = 0.5
      if (r === '') r = 2.0
      if (this.form.format === 'YYYY') {
        d1 = String(d1.getFullYear())
        d2 = String(d2.getFullYear())
      } else if (this.form.format === 'YYYY-MM') {
        let t1 = d1
        let t2 = d2
        let mon1 = t1.getMonth() + 1
        let mon2 = t2.getMonth() + 1
        if (mon1 < 10) {
          mon1 = '0' + String(mon1)
        } else {
          mon1 = String(mon1)
        }
        if (mon2 < 10) {
          mon2 = '0' + String(mon2)
        } else {
          mon2 = String(mon2)
        }
        d1 = String(t1.getFullYear()) + '-' + mon1
        d2 = String(t2.getFullYear()) + '-' + mon2
      } else if (this.form.format === 'YYYY-MM-DD') {
        let t1 = d1
        let t2 = d2
        let mon1 = t1.getMonth() + 1
        let mon2 = t2.getMonth() + 1
        let day1 = t1.getDate()
        let day2 = t2.getDate()
        if (mon1 < 10) {
          mon1 = '0' + String(mon1)
        } else {
          mon1 = String(mon1)
        }
        if (mon2 < 10) {
          mon2 = '0' + String(mon2)
        } else {
          mon2 = String(mon2)
        }
        if (day1 < 10) {
          day1 = '0' + String(day1)
        } else {
          day1 = String(day1)
        }
        if (day2 < 10) {
          day2 = '0' + String(day2)
        } else {
          day2 = String(day2)
        }
        d1 = String(t1.getFullYear()) + '-' + mon1 + '-' + day1
        d2 = String(t2.getFullYear()) + '-' + mon2 + '-' + day2
      } else {
      }
      // console.log(t, n, d1, d2, r)
      getGames(t, n, d1, d2, r).then((jsonData) => {
        console.log(jsonData)
        console.log('games:', jsonData['games'])
        console.log('count:', jsonData['count'])
        if (jsonData.hasOwnProperty('games')) {
          this.games = jsonData.games
          this.loading = false
          console.log(this.games)
          this.$message({
            type: 'success',
            message: 'Success!'
          })
        }
        if (jsonData.hasOwnProperty('count')) {
          this.count = jsonData.count
        } else {
          this.count = this.games.length
          console.log(this.count)
        }
      }).catch((e) => {
        this.$message({
          type: 'error',
          message: e
        })
        this.games = []
        this.loading = false
      })
    },
    dateParser (d) {
      let t = new Date(d)
      let year = t.getFullYear()
      let month = t.getMonth() + 1
      let day = t.getDate()
      let res = String(year) + '-' + String(month) + '-' + String(day)
      return res
    },
    scoreParser (s1, s2) {
      return String(s1) + ' : ' + String(s2)
    }
  }
}
</script>

<style scoped>
.input_box {
  display: flex;
  justify-content: flex-start;
  align-content: flex-start;
}
.choose_board {
  margin-top: -20px;
  border: 0px solid rgba(131, 131, 131, 0.596);
}
.col_box1 {
  margin-left: -20px;
  height: 75px;
  border: 0px solid rgba(131, 131, 131, 0.596);
}
.col_box2 {
  margin-left: 10px;
  height: 75px;
  border: 0px solid rgba(197, 32, 32, 0.596);
}
.col_box3 {
  margin-left: 10px;
  height: 75px;
  border: 0px solid rgba(34, 121, 221, 0.596);
}
.col_box4 {
  margin-left: -20px;
  height: 65px;
  border: 0px solid rgba(235, 201, 53, 0.596);
}
.col_box5 {
  margin-left: 0px;
  height: 65px;
  border: 0px solid rgba(4, 155, 79, 0.801);
}
.col_box6 {
  margin-left: 10px;
  height: 65px;
  border: 0px solid rgba(158, 14, 151, 0.801);
}
.name_box {
  width: 120px;
}
.tour_box {
  margin-left: 10px;
  width: 120px;
}
.res_box {
  margin-left: 10px;
  width: 120px;
}
.format_box {
  width: 120px;
}
.date_box {
  margin-left: 10px;
  width: 140px;
}
.button_box {
  margin-top: 10px;
  margin-left: 40px;
}
.display {
  margin-top: 20px;
  height: 600px;
}
.the_table {
  max-height: 540px;
}
.paginator {
  margin-top: 10px;
}
</style>
