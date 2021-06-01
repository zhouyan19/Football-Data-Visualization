<template>
  <div class="rankings_all">
    <h1 style="font-size:42px">Rankings</h1>
    <el-divider></el-divider>
    <el-container class="all_board">
      <el-col class="query_board">
        <h2 style="font-size:32px">Ranking Type</h2>
        <el-row class="opt_box">
          <el-select v-model="rank_type" placeholder="choose the ranking type">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </el-row>
        <el-row class="check_button">
          <el-button
            type="primary"
            @click="submit">
            Check
          </el-button>
        </el-row>
      </el-col>
      <el-col class="result_board">
        <h2 style="font-size:32px">Result</h2>
        <div class="display">
          <el-table
            v-loading="loading"
            class="the_table"
            ref="multipleTable"
            stripe
            :data="teams.slice((current_page-1)*page_size,current_page*page_size)"
            tooltip-effect="dark"
            empty-text="No Data">
            <el-table-column
              class="colomn"
              prop="rank"
              label="Ranking"
              width="200">
            </el-table-column>
            <el-table-column
              class="colomn"
              prop="name"
              label="Team"
              width="200">
            </el-table-column>
          </el-table>
          <div class="paginator" align="center">
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
      </el-col>
    </el-container>
  </div>
</template>

<script>
import {getRanking} from '@/utils/communication'
export default {
  name: 'Rankings',
  data () {
    return {
      loading: false,
      current_page: 1,
      page_size: 8,
      count: 0,
      rank_type: 'all',
      options: [
        {value: 'all', label: 'All'},
        {value: 'league', label: 'Leagues'},
        {value: 'world', label: 'Nations'},
        {value: 'fifa', label: 'FIFA'},
        {value: 'uefa', label: 'UEFA'}
      ],
      teams: [
        // {'rank': 1, 'name': 'china'},
        // {'rank': 2, 'name': 'germany'},
        // {'rank': 3, 'name': 'spain'},
        // {'rank': 4, 'name': 'brazil'},
        // {'rank': 5, 'name': 'england'},
        // {'rank': 6, 'name': 'scotland'},
        // {'rank': 7, 'name': 'france'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'},
        // {'rank': 1, 'name': 'china'}
      ]
    }
  },
  mounted: function () {
    this.count = this.teams.length
    console.log(this.count)
  },
  methods: {
    handleChange (p) {
      this.current_page = p
    },
    submit () {
      this.loading = true
      getRanking(this.rank_type).then((jsonData) => {
        console.log(jsonData)
        if (jsonData.hasOwnProperty('teams')) {
          this.teams = jsonData.teams
          this.loading = false
          console.log(this.teams)
          this.$message({
            type: 'success',
            message: 'Success!'
          })
        }
        if (jsonData.hasOwnProperty('count')) {
          this.count = jsonData.count
        } else {
          this.count = this.teams.length
          console.log(this.count)
        }
      }).catch((e) => {
        this.$message({
          type: 'error',
          message: e
        })
        this.teams = []
        this.loading = false
      })
    }
  }
}
</script>

<style scoped>
.h1 {
  text-align: left;
}
.rankings_all {
  height: 100%;
  box-sizing: border-box;
  border: 0px solid rgba(131, 131, 131, 0.596);
  border-radius: 8px;
  margin-left: 40px;
  margin-top: -20px;
}
.all_board {
  margin-top: -20px;
}
.result_board {
  margin-left: 20px;
  margin-right: 20px;
}
.check_button {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  margin-right: 0px;
  margin-left: 40px;
}
.display {
  margin-top: 20px;
  height: 500px;
}
.the_table {
  max-height: 450px;
}
.paginator {
  margin-top: 20px;
}
</style>
