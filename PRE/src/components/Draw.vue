<template>
  <div class="draw">
    <el-container class="all_board">
      <el-col class="query_board">
        <h1 style="font-size:42px">Query Board</h1>
        <!-- <div class="tips"> *Tips: Choose the country, the event type and the start/end time you want to query.</div> -->
        <el-form class="info_form" ref="form" :model="form" :rules="rules" label-width="80px">
          <el-row><el-col :span="22">
            <el-form-item id="selectForm" prop="event_type">
              <label slot="label">Team&nbsp;Type</label>
              <div class="radio_box">
                <el-radio v-model="form.event_type" label="all" style="zoom: 110%;">All&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</el-radio>
                <el-radio v-model="form.event_type" label="world" style="zoom: 110%;">National Team</el-radio>
                <el-radio v-model="form.event_type" label="league" style="zoom: 110%;">League Team</el-radio>
              </div>
            </el-form-item>
          </el-col></el-row>
          <el-row><el-col :span="18">
            <el-form-item id="selectForm" label="Country " prop="name">
              <el-input class="country_box" v-model="form.name"></el-input>
            </el-form-item>
          </el-col></el-row>
          <el-row><el-col :span="22">
            <el-form-item id="selectForm2" prop="event_type">
              <label slot="label">Time&nbsp;Format</label>
              <div class="radio_box">
                <el-radio v-model="format" label="YYYY" style="zoom: 110%;">YYYY (By Year)</el-radio>
                <el-radio v-model="format" label="YYYY-MM" style="zoom: 110%;">YYYY-MM (By Year+Month)</el-radio>
                <el-radio v-model="format" label="YYYY-MM-DD" style="zoom: 110%;">YYYY-MM-DD (By Specific Date)</el-radio>
              </div>
            </el-form-item>
          </el-col></el-row>
          <el-row><el-col :span="22">
            <el-form-item id="selectForm" prop="name">
              <label slot="label">Start&nbsp;Time</label>
              <el-date-picker
                v-if="format==='YYYY'"
                class="date_box"
                v-model="form.date1"
                type="year"
                placeholder="Choose the start date"
              ></el-date-picker>
              <el-date-picker
                v-else-if="format==='YYYY-MM'"
                class="date_box"
                v-model="form.date1"
                type="month"
                placeholder="Choose the start date"
              ></el-date-picker>
              <el-date-picker
                v-else
                class="date_box"
                v-model="form.date1"
                type="date"
                placeholder="Choose the start date"
              ></el-date-picker>
            </el-form-item>
          </el-col></el-row>
          <el-row><el-col :span="22">
            <el-form-item id="selectForm" prop="name">
              <label slot="label">End&nbsp;Time</label>
              <el-date-picker
                v-if="format==='YYYY'"
                class="date_box"
                v-model="form.date2"
                type="year"
                placeholder="Choose the start date"
              ></el-date-picker>
              <el-date-picker
                v-else-if="format==='YYYY-MM'"
                class="date_box"
                v-model="form.date2"
                type="month"
                placeholder="Choose the start date"
              ></el-date-picker>
              <el-date-picker
                v-else
                class="date_box"
                v-model="form.date2"
                type="date"
                placeholder="Choose the start date"
              ></el-date-picker>
            </el-form-item>
          </el-col></el-row>
        </el-form>
        <el-row class="check_button">
          <el-button
            type="primary"
            :disabled="form.name===''"
            @click="getData"
          >
            CHECK
          </el-button>
        </el-row>
      </el-col>
      <el-col class="result_board">
        <h1 style="font-size:42px">Result</h1>
        <div class="img_box" v-loading="loading">
          <img class="chart" :src="img_url">
        </div>
        <div class="img_buttons">
          <el-button
            icon="el-icon-zoom-in"
            @click="handleImgDesPreview(i)"
            :disabled="img_url===null"
          ></el-button>
        </div>
      </el-col>
    </el-container>
    <el-dialog :visible.sync="dialogVisible" width="80%">
      <img width="100%" :src="dialogImageUrl" alt="">
    </el-dialog>
  </div>
</template>

<script>
import {getInfo} from '@/utils/communication'
export default {
  name: 'Draw',
  data () {
    return {
      format: 'YYYY',
      loading: false,
      form: {
        event_type: 'all',
        name: '',
        date1: new Date(),
        date2: new Date()
      },
      rules: {
        name: [{required: true, message: 'Please fill in the blank!', trigger: 'blur'}]
      },
      dialogImageUrl: '',
      dialogVisible: false,
      img_url: null // return 'https://img.wzf2000.top/image/2021/05/30/pic240e980512942afd.png'
    }
  },
  methods: {
    getData () {
      this.loading = true
      let e = this.form.event_type
      let n = this.form.name
      let d1 = this.form.date1
      let d2 = this.form.date2
      if (this.format === 'YYYY') {
        d1 = String(d1.getFullYear())
        d2 = String(d2.getFullYear())
      } else if (this.format === 'YYYY-MM') {
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
      } else {
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
          day1 = '0' + String(day2)
        } else {
          day2 = String(day2)
        }
        d1 = String(t1.getFullYear()) + '-' + mon1 + '-' + day1
        d2 = String(t2.getFullYear()) + '-' + mon2 + '-' + day2
      }
      console.log(e, n, d1, d2)
      getInfo(e, n, d1, d2).then((jsonData) => {
        if (jsonData.hasOwnProperty('url')) {
          this.img_url = jsonData.url
          this.loading = false
          console.log(this.img_url)
          this.$message({
            type: 'success',
            message: 'Success!'
          })
        }
      }).catch((e) => {
        this.$message({
          type: 'error',
          message: e
        })
        this.img_url = null
        this.loading = false
      })
    },
    handleImgDesPreview (i) {
      this.dialogImageUrl = this.img_url
      this.dialogVisible = true
    }
  }
}
</script>

<style scoped>
.h1 {
  text-align: left;
}
.draw {
  height: 100%;
  box-sizing: border-box;
  border: 0px solid rgba(131, 131, 131, 0.596);
  border-radius: 8px;
  margin-left: 40px;
  margin-top: -20px;
}
.tips {
  margin-bottom: 27px;
}
.radio_box {
  margin-left: 40px;
}
.el-form-item {
  margin-bottom: 20px;
}
#selectForm >>>.el-form-item__label {
  font-size: 20px;
}
#selectForm2 >>>.el-form-item__label {
  font-size: 16px;
}
.country_box {
  margin-left: 40px;
}
.date_box {
  margin-left: 40px;
}
.check_button {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin-top: 5px;
  margin-right: 20px;
}
.result_board {
  margin-left: 20px;
  margin-right: 20px;
}
.img_box {
  height: 400px;
  width: 500px;
  border: 2px solid rgba(107, 160, 189, 0.596);
  border-radius: 10px;
}
.chart {
  display: flex;
  justify-content: center;
  align-content: center;
  max-width: 100%;
  max-height: 100%;
  width: auto;
  height: auto;
}
.img_buttons {
  display: flex;
  justify-content: flex-end;
  margin-top: 25px;
}
</style>
